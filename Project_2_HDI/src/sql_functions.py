
from sqlalchemy import create_engine

# Test Connection
 #use your own user_name and password
host_name='localhost'
user_name='hdi' 
user_password='hdi'
data_base_name='sustainable_development'
def get_connection():
    connection = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=host_name,db=data_base_name, user=user_name, pw=user_password))
    return connection
    
def create_database():
    connection= get_connection()
    create_query =f'CREATE DATABASE IF NOT EXISTS {data_base_name};'
    connection.execute(create_query)

