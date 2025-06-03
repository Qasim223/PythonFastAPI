from pydantic import BaseModel

class TodoModel(BaseModel):
    name: str
    description: str
    completed: bool

    