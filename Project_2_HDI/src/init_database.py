import pandas as pd
import sql_functions as hdi_sql_functions




def init_data_base():
    hdi_sql_functions.create_database()
    con = hdi_sql_functions.get_connection()
    countries_file_path = '..//data/hdi_revised.csv'
    others_file_path = '..//data/others.csv'
    entity_file_path = '..//data/entity.csv'

    countries_data = pd.read_csv(countries_file_path,delimiter=';') 
    others_data = pd.read_csv(others_file_path,delimiter=';') 
    entity_data = pd.read_csv(entity_file_path,delimiter=';') 

    input_data= countries_data.append(others_data)
    input_data.to_sql(con=con, name='inputs', if_exists='replace', index=False)
    entity_data.to_sql(con=con, name='entity', if_exists='replace', index=False)