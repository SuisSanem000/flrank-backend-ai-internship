# Import the FastAPI class to create the application instance
from fastapi import FastAPI

# Import BaseModel from pydantic to define the data structure for incoming JSON payloads
from pydantic import BaseModel

# Create a FastAPI application instance called 'app'
app = FastAPI()

# Define a data model called Message that inherits from BaseModel
class Message(BaseModel):
    # Specify that the expected JSON payload should have a 'message' field of type string
    message: str

# Create a route that listens for HTTP GET requests at the "/health" endpoint
@app.get("/health")

# Define an asynchronous function that handles the request to the "/health" endpoint
async def health():
    # Return a simple dictionary, which FastAPI automatically converts to a JSON response
    return {"status": "ok"}

# Create a route that listens for HTTP POST requests at the "/echo" endpoint
@app.post("/echo")

# Define an asynchronous function that expects a JSON payload matching the Message model
async def echo(msg: Message):
    # Return a dictionary containing the original message text, which becomes the JSON response
    return {"echo": msg.message}

# Check if this script is being run directly (not imported as a module in another script)
if __name__ == "__main__":
    
    # Import uvicorn, which is the ASGI server that will run the FastAPI app
    import uvicorn
    
    # Start the server, pointing it to 'app' in 'main.py', listening on all network interfaces at port 8000, with auto-reload enabled
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
