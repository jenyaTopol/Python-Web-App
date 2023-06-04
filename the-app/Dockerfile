# Use the official Python base image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application files
COPY . .

# Expose the port your application runs on
EXPOSE 80

# Set environment variables
ENV USERNAME=admin
ENV PASSWORD=password

# Start the Flask application
CMD ["python", "app.py"]
