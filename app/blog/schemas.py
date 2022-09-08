# #############import the List#########
# from typing import List


# from pydantic import BaseModel






# ############pydintic model###past thou the main.py#########
# class BlogBase(BaseModel):
#     title: str
#     body: str

# class Blog(BlogBase):
#     class Config():
#         orm_mode = True
    

        
# ########create the  user of the basemodel############         
# class User(BaseModel):
#     name:str
#     email:str
#     password:str
    

# ###########show User ############################
# class ShowUser(BaseModel):
#     name:str
#     email:str
#     blogs: List[Blog] = []
#     class Config():
#         orm_mode = True
        
        
# ################relationships
# class ShowBlog(BaseModel):
#     title: str
#     body: str
#     creator: ShowUser
#     class Config():
#         orm_mode = True
        
        
# class Login(BaseModel):
#     username:str
#     password:str
    
    
    
# class Token(BaseModel):
#     access_token: str
#     token_type: str


# class TokenData(BaseModel):
#     username: Opational[str] = None





from typing import List, Optional
from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    blogs : List[Blog] =[]
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body:str
    creator: ShowUser

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None