# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR usr/src/app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
#COPY . .
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

# Expose the port your application will run on
EXPOSE 80

# Run the Flask application
CMD ["python", "app.py"]
