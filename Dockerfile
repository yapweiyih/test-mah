# Use the official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY main.py .

# Expose the port that the app runs on (Cloud Run uses PORT env variable)
EXPOSE 8080

# Command to run the application
CMD ["python", "main.py"]
