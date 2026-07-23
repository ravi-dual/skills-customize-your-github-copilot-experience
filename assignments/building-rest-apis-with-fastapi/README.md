# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to create a simple REST API with FastAPI by building endpoints for a small collection of books and validating incoming data with Pydantic.

## 📝 Tasks

### 🛠️ Create a FastAPI App

#### Description
Set up a FastAPI application and create a basic health check endpoint.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance.
- Add a `/health` endpoint that returns a JSON response.
- Run the app locally with Uvicorn.

### 🛠️ Build Book Endpoints

#### Description
Implement endpoints to list books and retrieve a single book by ID.

#### Requirements
Completed program should:

- Add a `GET /books` endpoint that returns all books.
- Add a `GET /books/{book_id}` endpoint that returns one matching book.
- Return a helpful response for missing books.

### 🛠️ Accept and Validate New Books

#### Description
Add support for creating new books through a POST request.

#### Requirements
Completed program should:

- Define a Pydantic model for book data.
- Add a `POST /books` endpoint that accepts a title and author.
- Store the new book in memory and return the created record.
