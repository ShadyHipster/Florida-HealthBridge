import logging
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.debug("Loading ORM models.")

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=True)
    role = Column(String, nullable=False)  # "guest", "patient", "admin"
    # Log instance creation in __init__ if desired (optional)

class Resource(Base):
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String, nullable=False)
    location = Column(String, nullable=False)
    
logger.info("ORM models loaded successfully.")
