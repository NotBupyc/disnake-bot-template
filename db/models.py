# Imports

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Guild(Base):
    __tablename__ = "guilds"

    id = Column(Integer(), primary_key=True)
    guild_id = Column(Integer(), nullable=False)

    
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer(), primary_key=True)

    user_id = Column(Integer(), nullable=False)


    

    
    



