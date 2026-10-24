from sqlalchemy.orm import Mapped,mapped_column,relationship 
from from typing import List 
from  sqlalchemy_serializer import SerializerMixin 
from app.db import db 

class User(db.Model,SerializerMixin):
    __tablename__="users"

    serialize_rules=("-articles.user",)

    id:Mapped[int]=mapped_column(primary_key=True)
    username:Mapped[str]
    email:Mapped[str]=mapped_column(unique=True)
    password:Mapped[str]

    articles:Mapped[List["Article"]]=relationship(back_populates="user",cascade="all,delete-orphan")

    def __repr__(self):
        return f"<User {self.id} Name: {self.username}>"