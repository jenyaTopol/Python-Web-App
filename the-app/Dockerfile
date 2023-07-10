# created by `jenyaTopolnitski'
FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# Set environment variables
ENV MYSQL_USER=admin
ENV MYSQL_PASSWORD=password
ENV MYSQL_HOST=mysql
ENV MYSQL_PORT=3306
ENV MYSQL_DB=mydatabase

# Start the application
CMD ["python", "app.py"]
