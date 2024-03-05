import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# bot token
TOKEN = os.getenv("TOKEN")

# api tmdb key
API_KEY = os.getenv("API_KEY")  # v3

# Postgres
PGHOST = os.getenv("PGHOST")
PG_USER = os.getenv("PG_USER")
PG_PASS = os.getenv("PG_PASS")
DB_NAME = os.getenv("DB_NAME")


# mysql
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASS = os.getenv("MYSQL_PASS")
DB_NAME2 = os.getenv("DB_NAME2")

# For the FUTURE
I18N_DOMAIN = "MovieBuddyBot"
BASE_DIR = Path(__file__).parent
LOCALES_DIR = BASE_DIR / "locales"

# ADMIN
ADMIN_ID = int(os.getenv("ADMIN_ID"))
