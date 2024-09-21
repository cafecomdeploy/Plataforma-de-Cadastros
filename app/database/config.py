from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

TEST_MODE = config('TEST_MODE', default=False, cast=bool)
DB_URL = config('DATABASE_URL') if TEST_MODE else config('DATABASE_URL')

engine = create_engine(DB_URL, pool_pre_ping=True)
Session = sessionmaker(bind=engine)