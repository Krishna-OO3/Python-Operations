import pandas as pd
import pyodbc
# import mysql.connector

data = pd.read_csv("2021-08-17commerce_event-443804504849141782.csv")
df = pd.DataFrame(data, columns=['id' , 'name' , 'timestamp_iso' , 'user_data_geo_country_code' , 'user_data_model' , 'user_data_brand' , 'user_data_developer_id' , 'event_data_revenue_in_usd' , 'last_attributed_touch_data_tilde_feature'])

# driver = 'SQL Server'
# server = '127.0.0.1'
# db = 'krishna'
# tcon = 'yes'
# uname = 'root'
# pword = 'Sairam99'

conn = pyodbc.connect( Driver = '{SQL Driver}', host='127.0.0.1', User='root', Password='Sairam99', Database='Commerce', use_pure=False)

cursor = conn.cursor()

cursor.execute('CREATE TABLE Commerce_Info (id int(500), name varchar(100), timestamp_iso datetime , user_data_geo_country_code varchar(50), user_data_model varchar(25), user_data_brand varchar(20), user_data_developer_id varchar(50), event_data_revenue_in_usd float(25), lat_attributed_touch_data_tilde_feature varchar(20))')

for row in df.itertuples():
    cursor.execute
    ('''INSERT INTO krishna.dbo.Commerce_Info (id, name, timestamp_iso, user_data_geo_country_code, user_data_model, user_data_brand, user_data_developer_id, event_data_revenue_in_usd, last_attribute_touch_data_tilde_feature) VALUES (?,?,?,?,?,?,?,?,?)''',
    row.id,
    row.name,
    row.timestamp_iso,
    row.user_data_geo_country_code,
    row.user_data_model,
    row.user_data_brand,
    row.user_data_developer_id,
    row.event_data_revenue_in_usd,
    row.last_attributed_touch_data_tilde_feature
    )

conn.commit()
