import yelpapi as yelp # Yelp API
import psycopg2 as postgres # Postgresql
import os
import psycopg2

def getYelpToken() -> str:
    # Get Yelp API token
    # Contains: Yelp Fusion API token
    #if os.environ['YELP_TOKEN']:
    #    return os.environ['YELP_TOKEN']
    with open("../text_files/yelp_token.txt", "r") as file:
        api_key = file.read()
    file.close()
    return api_key

def getOpenCageToken() -> str:
    #if os.environ['OPENCAGE_TOKEN']:
    #    return os.environ['OPENCAGE_TOKEN']
    with open("../text_files/opencage_token.txt", "r") as file:
        api_key = file.readline()
    file.close()
    return api_key

def getDatabaseLogin() -> list:
    # Get database login information
    # Contains: database name, port, username, password, host
    #if os.environ['POSTGRES_DATABASE'] and os.environ['POSTGRES_HOST'] and os.environ['POSTGRES_USERNAME'] and os.environ['POSTGRES_PASSWORD'] and os.environ['POSTGRES_PORT']:
    #    return [os.environ['POSTGRES_DATABASE'], os.environ['POSTGRES_HOST'], os.environ['POSTGRES_USERNAME'], os.environ['POSTGRES_PASSWORD'], os.environ['POSTGRES_PORT']]
    with open("../text_files/postgres_login.txt", "r") as file:
        postgres_login = list(file.readline().split(" "))
    file.close()
    return postgres_login

def connect_to_database():
    login_details = getDatabaseLogin()
    db_name, host, user, password, port = login_details
    conn = psycopg2.connect(database=db_name, host=host, user=user, password=password, port=port)
    return conn

def initializeDatabase(postgres_database, postgres_host, postgres_user, postgres_password, postgres_port) -> None:
    try: # Attempt to connect to database
        global db_connection 
        db_connection = postgres.connect(database=postgres_database, host=postgres_host, user = postgres_user, password=postgres_password, port=postgres_port)
        print("Successfully connected to PostgreSQL")
    except (Exception, postgres.Error) as error: # Print Error if doesn't connect
        print("Error while connecting to PostgreSQL:\n", error)
    
def closeDatabase() -> None:
    try: # Close the database connection
        global db_connection
        db_connection.close()
        print("Database connection closed successfully.")
    except (Exception, postgres.Error) as error: # Print Error if doesn't close
        print("Error while closing PostgreSQL connection:\n", error)
