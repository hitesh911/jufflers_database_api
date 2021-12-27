from pydantic import BaseModel


class Create_parameters_model(BaseModel):
    name : str = "test_name"
    image : str = "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_960_720.jpg"
    labels : str = "Action , Adventure , Comedy"
    qualities : str = "480 , 720"
    imdb : str = "tt6320628"
    age_res : str = "R"
    download_url : str = "https://jufflersbot.herokuapp.com/downloadyt?urlyt=https://youtu.be/K7MfUDxzAzE"
    trailer_url : str = "https://www.youtube.com/embed/2QKg5SZ_35I"

class Update_parameters_model(BaseModel):
    name : str = "NULL"
    image : str = "NULL"
    labels : str = "NULL"
    qualities : str = "NULL"
    imdb : str = "NULL"
    age_res : str = "NULL"
    download_url : str ="NULL"
    trailer_url : str = "NULL"
