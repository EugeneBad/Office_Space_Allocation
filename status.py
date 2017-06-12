from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Binary, Integer


engine = create_engine('sqlite:///database/interactive_status.db', echo=False)
Base = declarative_base()


class State(Base):
    __tablename__ = 'state'

    id = Column(Integer, primary_key=True)
    state_name = Column(String)
    state_file = Column(Binary)
Base.metadata.create_all(engine)
