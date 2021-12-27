from fastapi import FastAPI , Depends
from schemas import Create_parameters_model , Update_parameters_model
from sqlalchemy.orm import Session
import models 
from db import SessionLocal, engine
password_key = "JUFFLER_GEEKS"
app = FastAPI()
# connection to the database 
models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()

@app.post("/create" )
async def create(key :str , parameter_schema : Create_parameters_model , db: Session = Depends(get_db)):
    if key == password_key:
        movie_object = db.query(models.Movie).filter(models.Movie.imdb == parameter_schema.imdb)
        if movie_object.count() == 0:
            new_movie = models.Movie(
                name = parameter_schema.name,
                image = parameter_schema.image,
                labels = parameter_schema.labels,
                qualities = parameter_schema.qualities,
                imdb = parameter_schema.imdb,
                age_res = parameter_schema.age_res,
                download_url = parameter_schema.download_url,
            )
            db.add(new_movie)
            db.commit()
            db.refresh(new_movie)
            response = {"Post successed with imdb id  ": parameter_schema.imdb}
        else:
            response = {"post exists with imdb id": parameter_schema.imdb}
    else:
        return {"Wrong key" , key}


    return response
@app.get("/read")
async def read(key : str , db: Session = Depends(get_db)):
    # intitilizing movies list 
    movies = []
    if key == password_key:
        try :
            movies = db.query(models.Movie).all()
        except:
            movies = []
    return movies

    
@app.delete("/delete/{imdb}")
async def delete(imdb : str , key : str , db: Session = Depends(get_db)):
    if key == password_key:
        movie_object = db.query(models.Movie).filter(models.Movie.imdb == imdb)
        if movie_object.count() != 0:
            movie_name = movie_object.first().name
            movie_to_delete = movie_object.delete(synchronize_session=False)
            db.commit()
        else:
            movie_to_delete = 0
            movie_name = None
        

        if movie_to_delete:
            return {"Movie deleted successfully ": movie_name }
        else:
            return {"Movie not found with id : ": imdb }
    else:
        return {"Wrong key ":key}
    
@app.put("/update" )
async def update(key :str ,imdb: str, parameter_schema : Update_parameters_model , db: Session = Depends(get_db)):
    # initilizing response 
    response = {}
    if key == password_key:
        movie_object = db.query(models.Movie).filter(models.Movie.imdb == imdb)
        if movie_object.first():
            if parameter_schema.name != "NULL":
                response["name"] = [movie_object.first().name , parameter_schema.name]
                movie_object.update( {"name" : parameter_schema.name} , synchronize_session=False)
                db.commit()
            if parameter_schema.image != "NULL":
                response["image"] = [movie_object.first().image , parameter_schema.image]
                movie_object.update( {"image" : parameter_schema.image} , synchronize_session=False)
                db.commit()
            if parameter_schema.labels != "NULL":
                response["labels"] = [movie_object.first().labels, parameter_schema.labels]
                movie_object.update( {"labels" : parameter_schema.labels} , synchronize_session=False)
                db.commit()
            if parameter_schema.qualities != "NULL":
                response["qualities"] = [movie_object.first().qualities, parameter_schema.qualities]
                movie_object.update( {"qualities" : parameter_schema.qualities} , synchronize_session=False)
                db.commit()
            if parameter_schema.age_res != "NULL":
                response["age_res "] = [movie_object.first().age_res , parameter_schema.age_res ]
                movie_object.update( {"age_res" : parameter_schema.age_res} , synchronize_session=False)
                db.commit()
            if parameter_schema.download_url != "NULL":
                response["download_url"] = [movie_object.first().download_url , parameter_schema.download_url ]
                movie_object.update( {"download_url" : parameter_schema.download_url} , synchronize_session=False)
                db.commit()
            if parameter_schema.imdb != "NULL":
                response["imdb"] = [movie_object.first().imdb , parameter_schema.imdb ]
                movie_object.update( {"imdb" : parameter_schema.imdb} , synchronize_session=False)
                db.commit()
            else : 
                response["No change found"] = "nothing"
            return response
        else:
            return {"No movie found with imdb id": imdb}
    else:
        return {"wrong key ": key}





