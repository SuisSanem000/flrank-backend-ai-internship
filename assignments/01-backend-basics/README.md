# Assignment 01: Backend Basics

## Overview
This is the smallest possible backend implemented in Python as part of the FlyRank AI Internship. It features a simple server with two JSON endpoints that allow testing the request-response loop using both `curl` and a web browser.

## Technologies Used
- **Python 3**: The core programming language used.
- **FastAPI**: A modern, fast web framework for building APIs with Python, chosen for its simplicity and out-of-the-box JSON validation.
- **Uvicorn**: An ASGI web server implementation for Python used to run the FastAPI application.

## Approach
The goal was to build a backend in around 20 lines of code. By leveraging `FastAPI`, I was able to define two endpoints effortlessly:
1. `GET /health` - A simple endpoint returning a static JSON response `{"status": "ok"}` to check if the server is running.
2. `POST /echo` - An endpoint that accepts a JSON payload with a `message` field and returns it back to the client.

## Running Locally

### 1. Install Dependencies
Ensure you have Python installed, then install the required packages:
```bash
pip install -r requirements.txt
```
*(Alternatively, you can just run `pip install fastapi uvicorn pydantic`)*

### 2. Start the Server
Run the application using Python:
```bash
python main.py
```
The server will start at `http://127.0.0.1:8000`.

### 3. Test the Endpoints

**Test the `/health` Endpoint (GET request via Browser)**
Navigate to: [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)

**Test the `/echo` Endpoint (POST request via Terminal)**
Open another terminal window and run:
**For Mac/Linux (Bash):**
```bash
curl -X POST "http://127.0.0.1:8000/echo" -H "Content-Type: application/json" -d '{"message": "Hello from curl!"}'
```

**For Windows (PowerShell):**
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/echo" -Method Post -Headers @{"Content-Type"="application/json"} -Body '{"message": "Hello from PowerShell!"}'
```
You should receive a JSON response with your message!

## Package Explanations

Here is a breakdown of the core Python packages used in this project:

- **`fastapi`**: The web framework that handles the core logic of the backend. It provides the application instance and decorators (like `@app.get` and `@app.post`) that map URLs to Python functions. It is responsible for automatically converting Python dictionaries into JSON responses.
- **`uvicorn`**: The ASGI web server that actually runs the FastAPI application. While FastAPI defines the rules and logic, Uvicorn listens on port 8000, accepts incoming HTTP requests, passes them to FastAPI to be processed, and sends the responses back to the client.
- **`pydantic`**: A data validation library used by FastAPI under the hood. It ensures incoming JSON data matches expected formats (like the `Message` class). If the data is incorrect or missing fields, Pydantic automatically rejects the request with a helpful error before the Python function even executes.
