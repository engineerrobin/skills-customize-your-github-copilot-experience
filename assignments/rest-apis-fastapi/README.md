# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a fully functional REST API using the FastAPI framework in Python, learning how to define routes, handle HTTP methods, validate request data, and return structured JSON responses.

## 📝 Tasks

### 🛠️ Set Up a FastAPI Application

#### Description
Install FastAPI and create the entry point for your API. Define the app instance and run a basic server to confirm everything is working.

#### Requirements
Completed program should:

- Install `fastapi` and `uvicorn` using pip
- Create a `main.py` file that initializes a `FastAPI()` app instance
- Define a root route `GET /` that returns a welcome message as JSON
- Run the server with `uvicorn main:app --reload` and confirm it responds in the browser

Example output:

```json
{ "message": "Welcome to my FastAPI app!" }
```

### 🛠️ Build a CRUD API for a Resource

#### Description
Choose a simple resource (e.g. books, tasks, or students) and implement full Create, Read, Update, and Delete (CRUD) endpoints for it.

#### Requirements
Completed program should:

- Define a Pydantic model for the resource with at least 3 fields
- Implement the following routes:
  - `GET /items` — return a list of all items
  - `GET /items/{id}` — return a single item by ID
  - `POST /items` — create a new item from a JSON request body
  - `PUT /items/{id}` — update an existing item by ID
  - `DELETE /items/{id}` — delete an item by ID
- Return appropriate HTTP status codes (e.g. `404` when item is not found)
- Store items in an in-memory dictionary (no database required)

### 🛠️ Test Your API with the Interactive Docs

#### Description
Use FastAPI's built-in interactive documentation to manually test all your endpoints and verify they behave correctly.

#### Requirements
Completed program should:

- Access the auto-generated Swagger UI at `http://127.0.0.1:8000/docs`
- Successfully test each endpoint (GET, POST, PUT, DELETE) using the Swagger UI
- Handle edge cases: requesting a non-existent ID returns a `404` response with a helpful error message

Example error response:

```json
{ "detail": "Item not found" }
```
