# REST APIs with FastAPI
# Build a simple REST API using the FastAPI framework.
# Follow the TODO comments below to complete each task.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# TODO: Step 1 - Define a Pydantic model for your resource
# Choose a resource (e.g. Book, Task, Student) and add at least 3 fields.
# Example:
# class Book(BaseModel):
#     title: str
#     author: str
#     year: int


# TODO: Step 2 - Create an in-memory "database" (a dictionary)
# This will store your items with an integer ID as the key.
# Example: items = {}
# Also create a counter to track the next available ID.
# Example: next_id = 1


# TODO: Step 3 - Define the root route
# Create a GET endpoint at "/" that returns a welcome message.
@app.get("/")
def read_root():
    pass  # Replace with: return {"message": "Welcome to my FastAPI app!"}


# TODO: Step 4 - GET /items — return all items
# Return a list of all items in the in-memory dictionary.
@app.get("/items")
def get_items():
    pass


# TODO: Step 5 - GET /items/{item_id} — return a single item
# Return the item with the given ID, or raise a 404 error if not found.
@app.get("/items/{item_id}")
def get_item(item_id: int):
    pass
    # Hint: if item_id not in items: raise HTTPException(status_code=404, detail="Item not found")


# TODO: Step 6 - POST /items — create a new item
# Accept a request body matching your Pydantic model, store it, and return the created item.
@app.post("/items", status_code=201)
def create_item(item):  # Replace `item` type hint with your model class
    pass


# TODO: Step 7 - PUT /items/{item_id} — update an existing item
# Replace the item at the given ID with the new data, or raise 404 if not found.
@app.put("/items/{item_id}")
def update_item(item_id: int, item):  # Replace `item` type hint with your model class
    pass


# TODO: Step 8 - DELETE /items/{item_id} — delete an item
# Remove the item with the given ID and return a confirmation message, or raise 404.
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    pass


# To run the server, open a terminal and run:
#   uvicorn main:app --reload
# Then open http://127.0.0.1:8000/docs to test your API.
