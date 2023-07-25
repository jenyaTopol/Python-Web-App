# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install MySQL client
RUN apt-get update && apt-get install -y default-mysql-client

# Expose the port the Flask app will be listening on
EXPOSE 5000

# Start the MySQL service
CMD ["service", "mysql", "start"]

# Wait for MySQL to start (You can adjust this wait time based on your setup)
CMD ["sleep", "10"]

# Initialize the database using the init.sql script
RUN mysql -h mysql_host -u username -ppassword < ../db/init.sql

# Start the Flask application
CMD ["python", "app.py"]
