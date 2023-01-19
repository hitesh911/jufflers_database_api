from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker



SQLALCHEMY_DATABASE_URL = "your_database_uri"

engine = create_engine(SQLALCHEMY_DATABASE_URL , use_native_hstore = False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
