from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker



SQLALCHEMY_DATABASE_URL = "postgresql://sbcsiztwxpcgnm:5a9f3c448edccb6d80a261b5a588be799040abf86dd5a1af8ea0ba0ef224b484@ec2-54-204-99-176.compute-1.amazonaws.com:5432/d97pjqqubil7om"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
