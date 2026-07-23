# 📘 Assignment: Consuming APIs with Python Requests

## 🎯 Objective

Learn how to make HTTP requests in Python, parse JSON responses, and display useful information from a public API.

## 📝 Tasks

### 🛠️ Fetch Data from an API

#### Description
Use the Python `requests` library to call a public API and print the response data.

#### Requirements
Completed program should:

- Import the `requests` library.
- Send a GET request to a public API endpoint.
- Print the response body or a selected piece of data.

### 🛠️ Work with JSON Responses

#### Description
Parse the JSON response and display it in a student-friendly format.

#### Requirements
Completed program should:

- Convert the response into Python data using `.json()`.
- Access at least one field such as `title`, `name`, or `id`.
- Print a readable message using that data.

### 🛠️ Handle Errors Gracefully

#### Description
Add simple error handling so the program responds nicely when a request fails.

#### Requirements
Completed program should:

- Check the HTTP status code.
- Handle request errors with a clear message.
- Exit cleanly if the API cannot be reached.
