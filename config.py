import os

ENV = "dev"

DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB", "babyfoot"),
    "user": os.getenv("USER", "postgres"),
    "password": os.getenv("PWD"),
}
