from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo

# App object
app = FastAPI()

from database import (
    fetch_all_todos,
    fetch_one_todo,
    create_todo,
    remove_todo,
    update_todo
)

origins = ['http://localhost:3000', 'https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_root():
    return {"Ping": "Pong"}

#CRUD

@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response

@app.get("/api/todo{title}", response_model=Todo)
async def get_todo_by_id(title):
    response = await fetch_one_todo(title)
    if response:
        return response

    raise  HTTPException(404, f"there is no TODO item with this title: {title}")

@app.post("/api/todo", response_model=Todo)
async def post_todo(todo:Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    
    raise HTTPException(400, f"Something went wrong / Bad Request")

@app.put("/api/todo{title}/", response_model=Todo)
async def put_todo(title:str,description:str):
    response = await post_todo(title, description)
    if response:
        return response
    
    raise HTTPException(400, f"there is no TODO item with this title: {title}")

@app.delete("/api/todo{title}")
async def delete_todo(title):
    response = await remove_todo(title)

    if response:
        return "Successfully deleted todo item !"
    
    raise HTTPException(400, f"there is no TODO item with this title: {title}")
    return 1