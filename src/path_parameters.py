from fastapi import FastAPI

myapp = FastAPI()

@myapp.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id":item_id}