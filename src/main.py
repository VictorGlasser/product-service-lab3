# ChatGPT was used to convert this from Rust to Python
import os
from dotenv import load_dotenv  # Loads environment variables from .env
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Load environment variables from .env if it exists
load_dotenv()

# Create the FastAPI app
app = FastAPI()

# Read the port from environment variables or use 3030 as default
PORT = int(os.getenv("PORT", 3030))

# Configure CORS (allow all origins and GET requests only)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all domains
    allow_methods=["GET"],  # Only GET allowed
    allow_headers=["*"],  # Allow all headers
)

# Define the /products endpoint
@app.get("/products")
async def get_products():
    return [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ]

# Run the server (equivalent to warp::serve)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)

'''
install dependencies (if not already):

pip install fastapi uvicorn python-dotenv


Create a .env file (optional):

PORT=8080


Run the server:

python main.py


Open your browser or use curl:

http://localhost:8080/products
'''