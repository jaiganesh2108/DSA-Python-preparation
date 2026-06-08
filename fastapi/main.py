from fastapi import FastAPI
from schemas import Todo as TodoSchema
app = FastAPI()

#past todo
@app.post("/todos", response_model=TodoSchema)