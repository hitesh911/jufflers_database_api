from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker



SQLALCHEMY_DATABASE_URL = "postgresql://uzqembaougkjbd:fcc4f8eb2fcb83d6d39621c12f0a836c8f73284ddfee4494bd88b40a15e51420@ec2-3-211-228-251.compute-1.amazonaws.com:5432/d2md93msn8sj3j"

engine = create_engine(SQLALCHEMY_DATABASE_URL , use_native_hstore = False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
