# from hashlib import new
# import pwd
# from signal import raise_signal
# from typing import List
# from urllib import response 
# ###############import the stautus, Response
# from fastapi import FastAPI, Depends, status, Response, HTTPException

# ########### import the schemas########## import the models#########hashing for password
# from . import schemas, models

# ###########import the database #########
# from .database import engine, get_db

# #############define the session #############
# from sqlalchemy.orm import Session

# ##########password increpted using this one##########
# #from passlib.context import CryptContext

# #######import the hash###########
# # from .hashing import Hash

# ###########import the router the blog###########3
# from .routers import blog







# app = FastAPI()

# # ############pydintic model############
# # class Blog(BaseModel):
# #     title: str
# #     body: str

# ########to create and used the engine ##############33
# models.Base.metadata.create_all(engine)

# app.include_router(blog.router)



# ######### get_db function get the data ##################33
# # def get_db():
# #     db = SessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()



# ############api###############################
# # @app.post('/blog')
# # def create(title, body):
# #     return {'title':title, 'body':body}

# ##############using the pydantic model############ add the schemas in the base model
# # @app.post('/blog')
# # def create(request: schemas.Blog):
# #     return request





# ############################# use the tags in the saperate the blogs or defult###########
#                     ########    #######
#                     ########    ######
#                     ########    #######
#                     ########    ######
#                     ########    #######
#                     ########    ######                   
#                     ########    ######                    
#                     ########    ######                    
#                     ########    ######                    
#                     ########    ######                    
#                     ########    ######
#                       ####       ####     
#                         ##       ##   
#                           #     #    

#             #########  (tags=['blogs']) #########









# ############## define into the db ############## add the status code in place of the crate#######declar the status the number place
# # @app.post('/blog' , status_code=status.HTTP_201_CREATED, tags=['blogs'])
# # def create(request: schemas.Blog, db:Session = Depends(get_db)):
# #     new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
# #     db.add(new_blog)
# #     db.commit()
# #     db.refresh(new_blog)
# #     return new_blog

# ############### delete the blogs ###################
# # @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
# # def destroy(id,db: Session = Depends(get_db)):
# #     db.query(models.Blog).filter(models.Blog.id == id)
# #     if not blog.first():
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {id} not found")
# #     blog.delete(synchronize_session=False)
    
# #     db.commit()
# #     return 'done'

# #########update the blogs ################
# # @app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
# # def update(id,request: schemas.Blog, db:Session = Depends(get_db)):
# #     blog = db.query(models.Blog).filter(models.Blog.id == id)
    
# #     if not blog.first():
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
# #     blog.update(request)
# #     db.commit()
# #     return 'updated'
    

# ############### get method of the blogs #############list of the blogs
# # @app.get('/blog', response_model=List[schemas.ShowBlog],tags=['blogs'])
# # def all(db: Session = Depends(get_db)):
# #     blogs = db.query(models.Blog).all()
# #     return blogs



# ##################filter the db data ############ add the reponse
# # @app.get('/blog/{id}')
# # def all(id,db: Session = Depends(get_db)):
# #     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
# #     return blog


# ############respone##########
# # @app.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog,tags=['blogs'])
# # def show(id, response: Response, db: Session = Depends(get_db)):
# #     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
# #     if not blog:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
# #                             detail=f'Blog with the id{id} is not available')
    
# #     return blog

# ##############password hashing the password##########
# #pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ###############create the user in base model ##########
# ######show user######@app.post('/user')##==> @app.post('/user',response_model=schemas.ShowUser)####show user
# # @app.post('/user', response_model=schemas.ShowUser,tags=['users'])
# # def create_user(request: schemas.User,db: Session = Depends(get_db)):
# #     ###########password hashed###########
# #     #hashedPassword = pwd_cxt.hash(request.password)
# #     #############password hashed##############password=request.password##==>password=hashedPassword
# #     new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
# #     db.add(new_user)
# #     db.commit()
# #     db.refresh(new_user)
# #     return new_user

# # @app.get('/user/{id}',response_model=schemas.ShowUser,tags=['users'])
# # def get_user(id:int,db:Session = Depends(get_db)):
# #     user = db.query(models.User).filter(models.User.id == id).first()
# #     if not user:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id {id} is not available")
# #     return user




from fastapi import FastAPI
from blog import  models
from blog.database import engine
from blog.routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router) 