import datetime
from sqlalchemy import String,Integer,Column,TIMESTAMP,text
from database.database import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True,index=True)
    firstname = Column(String(200))
    lastname = Column(String(200))
    email = Column(String(200),unique=True)
    phone = Column(String(200))
    token = Column(String(400),unique=True)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True))

