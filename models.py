from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from db import Base

class Movie(Base):

    __tablename__ = "movies"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    image = Column(String)
    labels = Column(String)
    qualities = Column(String)
    imdb = Column(String , unique = True)
    age_res = Column(String)
    download_url = Column(String)
    

