from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import bcrypt
import setup
from emailInterfacing import generate_reservation

app = FastAPI()

# Enable CORS for all routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database setup
def connect_to_database():
    login_details = setup.getDatabaseLogin()
    db_name, host, user, password, port = login_details
    conn = psycopg2.connect(database=db_name, host=host, user=user, password=password, port=port)
    return conn

@app.post('/api/login')
async def login(request: Request):
    data = await request.json()
    email = data.get('email')
    password = data.get('password')

    conn = connect_to_database()
    cursor = conn.cursor()

    query = "SELECT password FROM Users WHERE email=%s;"
    cursor.execute(query, (email,))
    stored_hashed_pw = cursor.fetchone()

    if stored_hashed_pw and bcrypt.checkpw(password.encode('utf-8'), stored_hashed_pw[0].encode('utf-8')):
        return {'status': 'success'}
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

    conn = connect_to_database()
    cursor = conn.cursor()

    # Hash the password and decode it to a string
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    query = "INSERT INTO Users(first_name, last_name, email, password, phone_number, location) VALUES(%s, %s, %s, %s, %s, %s);"
    try:
        cursor.execute(query, (first_name, last_name, email, hashed_pw, phone_number, location))
        conn.commit()
    except psycopg2.DatabaseError as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

    return {'status': 'success'}

@app.post('/api/get_calendar_invite')
async def getCalendarInvite(request: Request):
    return generate_reservation

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=5000)
