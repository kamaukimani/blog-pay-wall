from sqlalchemy.orm import Mapped,mapped_column,relationship
from  sqlalchemy_serializer import SerializerMixin 
from app.db import db 
from datetime import datetime 
from sqlalchemy import ForeignKey,func 

class Article(db.Model,SerializerMixin):
    __tablename__="articles"

    serialize_rules=("-user.articles",)

    id:Mapped[int]=mapped_column(primary_key=True)
    author:Mapped[str]
    title:Mapped[str]
    content:Mapped[str]
    preview:Mapped[str]
    minutes_to_read:Mapped[int]
    created_at:Mapped[datetime]=mapped_column(server_default=func.now())
    is_member_only:Mapped[bool]=mapped_column(default=False)

    user_id:Mapped[int]=mapped_column(ForeignKey("users.id"))

    user:Mapped["User"]=relationship(back_populates="articles")

    def __repr__(self):
        return f"<Article {self.id} Title:{self.title}>"
        
