import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime

Base = declarative_base()



class Parameters(Base):
    __tablename__ = 'parameters'
    id = Column(Integer, primary_key=True)
    Frequency = Column(String(), nullable=False)
    Power = Column(String(), nullable=False)
    date = Column(String(), nullable=True)



