# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set environment variables
ENV USERNAME=admin
ENV PASSWORD=password

# Expose port
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
