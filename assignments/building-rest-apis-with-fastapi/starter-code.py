from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

# TODO: Add endpoints for listing books, getting a single book, and creating a new book.
