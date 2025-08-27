import os
from dotenv import load_dotenv

load_dotenv()

ENV = "dev"

DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB", "babyfoot"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PWD"),
}
