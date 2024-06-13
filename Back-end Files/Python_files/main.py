from fastapi import FastAPI, HTTPException, Depends, Request, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2
import bcrypt
import uuid
import setup
import emailInterfacing
from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional
from HAAK import HAAKChatbot
from fastapi.security import OAuth2PasswordBearer


SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

chatbot_states = {}
class TokenData(BaseModel):
    email: Optional[str] = None

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/login")

class ChatRequest(BaseModel):
    message: str
    session_id: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResetRequest(BaseModel):
    session_id: str



def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def fetch_user_details(email: str):
    conn = setup.connect_to_database()
    cursor = conn.cursor()
    query = "SELECT first_name, location FROM Users WHERE email=%s;"
    cursor.execute(query, (email,))
    result = cursor.fetchone()
    conn.close()

    if result:
        user_name, user_location = result[0], result[1]
        return user_name, user_location
    return None, None

def format_phone_number(phone_number):
    # Ensure the phone number is in the correct format (10 digits)
    if phone_number.isdigit():
        return f"({phone_number[:3]})-{phone_number[3:6]}-{phone_number[6:]}"
    else:
        return "Invalid phone number"



def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    return token_data.email

@app.post('/api/login')
async def login(request: Request):
    data = await request.json()
    email = data.get('email')
    password = data.get('password')

    conn = setup.connect_to_database()
    cursor = conn.cursor()

    query = "SELECT password FROM Users WHERE email=%s;"
    cursor.execute(query, (email,))
    stored_hashed_pw = cursor.fetchone()

    if stored_hashed_pw and bcrypt.checkpw(password.encode('utf-8'), stored_hashed_pw[0].encode('utf-8')):
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": email}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail='Incorrect email or password')


@app.post('/api/signup')
async def signup(request: Request):
    data = await request.json()
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    phone_number = data.get('phone_number', None)
    location = data.get('location', None)

    conn = setup.connect_to_database()
    cursor = conn.cursor()

    # Hash the password and decode it to a string
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    query = "INSERT INTO Users(first_name, last_name, email, password, phone_number, location) VALUES(%s, %s, %s, %s, %s, %s);"
    cursor.execute(query, (first_name, last_name, email, hashed_pw, phone_number, location))
    conn.commit()
    conn.close()
    body =  """
Dear recipient,

Thank you so much for being a part of the launch of HAAK! We are so excited to have you on board and we hope you enjoy your experience with us. We are a small team of students who are passionate about food and we hope that our service will help you find the best restaurants in your area.

In celebration of our launch we are giving you recommendations for if you are ever in the area where our team is located in Downtown Brooklyn, New York. We hope you enjoy!

    1. KUUN
    2. The Alcove
    3. The Long Island Bar
    4. The River Cafe
    5. The Osprey

Consider checking these out if you are ever in the area and we are extremely happy to have you on board!

Best regards,
HAAK Team
    """
    emailInterfacing.sendPromotionalEmail(receiver_email=email, subject="Thank you for using HAAK!", body=body)
    return {'status': 'success'}


@app.post("/reset/")
async def reset(request: ResetRequest):
    session_id = request.session_id
    if session_id in chatbot_states:
        chatbot_states[session_id].reset_state()
    return {"message": "Chat reset successfully"}


@app.post("/chat/")
async def chat(request: ChatRequest, token: Optional[str] = Depends(oauth2_scheme, use_cache=False)):
    user_email, user_name, user_location = None, None, None
    if token:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_email = payload.get("sub")
            user_name, user_location = fetch_user_details(user_email)  # Function to fetch additional details
        except JWTError:
            pass

    session_id = request.session_id
    if session_id not in chatbot_states:
        chatbot_states[session_id] = HAAKChatbot(user_email=user_email, user_name=user_name, user_location=user_location)

    chatbot = chatbot_states[session_id]
    response = chatbot.handle_interaction(request.message)
    return {"response": response}


@app.get('/api/user_data')
async def get_user_data(email: str = Depends(get_current_user)):
    conn = setup.connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT first_name, last_name, location, phone_number FROM Users WHERE email=%s;", (email,))
    user_data = cursor.fetchone()
    conn.close()
    if user_data:
        if user_data[3] != None:
            phone = format_phone_number(user_data[3])
        else:
            phone = user_data[3]
        return {"first_name": user_data[0], "last_name": user_data[1], "location": user_data[2], "phone": phone, "email": email}
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.put('/api/update_user_data')
async def update_user_data(request: Request, email: str = Depends(get_current_user)):
    data = await request.json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    phone = data.get('phone')
    location = data.get('location')
    # ... handle other fields ...

    conn = setup.connect_to_database()
    cursor = conn.cursor()
    cursor.execute("UPDATE Users SET first_name=%s, last_name=%s, location=%s, phone_number=%s WHERE email=%s;", (first_name, last_name, location, phone, email))
    conn.commit()
    conn.close()
    return {"status": "success"}

@app.put('/api/update_credentials')
async def update_credentials(request: Request, email: str = Depends(get_current_user)):
    data = await request.json()
    new_email = data.get('email')
    new_password = data.get('password')

    conn = setup.connect_to_database()
    cursor = conn.cursor()
    try:
        hashed_pw = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        cursor.execute("UPDATE Users SET email=%s, password=%s WHERE email=%s;", (new_email, hashed_pw, email))
        conn.commit()
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        conn.close()



