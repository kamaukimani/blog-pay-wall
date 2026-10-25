from flask_sqlalchemy import SQLAlchemy  
from flask_migrate import Migrate 
from sqlalchemy.orm import DeclarativeBase
from flask_bcrypt import Bcrypt

class Base(DeclarativeBase):
    pass 

db=SQLAlchemy(model_class=Base)
migrate=Migrate()
bcrypt=Bcrypt()