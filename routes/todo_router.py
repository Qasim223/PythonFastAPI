from fastapi import APIRouter, HTTPException
from models.todos import TodoModel
from config.database import collection
from schema.schema import list_serial
from bson import ObjectId

todo_router = APIRouter(prefix="/todos", tags=["Todo List"])

# GET Request Method
@todo_router.get("")
async def get_todos():
    try:
        todos = list_serial(collection.find())
        return todos
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

# POST Request Method
@todo_router.post("")
async def post_todos(todo:TodoModel):
    collection.insert_one(dict(todo))

#PUT Request Method
@todo_router.put("/{id}")
async def put_todo(id:str, todo:TodoModel):
    collection.find_one_and_update({"_id":ObjectId(id)}, {"$set":dict(todo)})

#DELETE Request Method
@todo_router.delete("/{id}")
async def delete_todo(id:str):
    collection.find_one_and_delete({"_id":ObjectId(id)})