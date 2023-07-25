#created by Jenya

FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y default-mysql-client

EXPOSE 5000

# Start the MySQL service
CMD ["service", "mysql", "start"]

# Wait for MySQL to start (You can adjust this wait time based on your setup)
CMD ["sleep", "10"]

# Initialize the database using the init.sql script
RUN mysql -h mysql_host -u username -ppassword < ../db/init.sql

# Start the Flask application
CMD ["python", "app.py"]
