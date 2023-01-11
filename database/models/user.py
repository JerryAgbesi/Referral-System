import datetime
from sqlalchemy import String,Integer,Column,TIMESTAMP,Text,Boolean,ForeignKey
from database.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True,index=True)
    firstname = Column(String(200))
    lastname = Column(String(200))
    email = Column(String(200),unique=True)
    phone = Column(String(200))
    token = Column(String(400),unique=True)
    referral_code = relationship('Referral',uselist=False,back_populates='user') 
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True))

class Referral(Base):
    __tablename__ = 'referral'
    
    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(ForeignKey('user.id'))
    referral_code = Column(String(300),unique=True)
    is_active = Column(Boolean)
    user = relationship('User',back_populates='referral_code')
    created_at =  Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
