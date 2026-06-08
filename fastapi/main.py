from fastapi import FastAPI, Depends
from schemas import Todo as TodoSchema
from sqlalchemy.orm import Session
from models import Todo 

app = FastAPI()
#Dependency for DB section
def get_db():
    db = SectionLocal()
    try:
        yield db
    finally: 
        db.close()
#past todo
@app.post("/todos", response_model=TodoSchema)
def create(todo: TodoSchema, db: Session = Depends(get_db)):
    db_todo = Todo(**todo.dict())