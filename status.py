from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Binary, Integer

engine = create_engine('sqlite:///:memory:', echo=False)
Base = declarative_base()

