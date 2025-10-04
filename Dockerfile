# Use Python 3.11 slim as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app
COPY app.py .

# Expose port 5000
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
