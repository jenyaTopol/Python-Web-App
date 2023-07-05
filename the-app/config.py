class Config:
   # MySQL config
    MYSQL_USER = 'myuser'
    MYSQL_PASSWORD = 'mypassword'
    MYSQL_HOST = 'myhost'
    MYSQL_PORT = 3306
    MYSQL_DB = 'mydb'

   
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
