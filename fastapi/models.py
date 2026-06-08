from sqlalchemy import Column, Integer, String, Boolean
from database import Base
#models.py is where we will define our database models. We will create a model for our todo items.
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    completed = Column(Boolean, default=False)