from fastapi import FastAPI
from routes.todo_router import todo_router
app = FastAPI()

app.include_router(todo_router)