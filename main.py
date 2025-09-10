import os

import uvicorn
from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI(title="Hello World API")


@app.get("/")
async def root():
    """Root endpoint that returns Hello World"""
    return {"message": "Hello World"}


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    # Get port from environment variable or default to 8080
    port = int(os.environ.get("PORT", 8080))

    # Run the application
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
