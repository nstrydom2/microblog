from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, TIMESTAMP, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


db_engine = create_engine('sqlite:///blog.sqlite3')
Base = declarative_base()

class Entry(Base):
    __tablename__ = 'entry'

    id = Column(Integer, primary_key=True)
    timestamp = Column(TIMESTAMP)
    content = Column(String)

    def __init__(self, timestamp, content):
        self.timestamp = timestamp
        self.content = content

# Create all tables
Base.metadata.create_all(db_engine)

