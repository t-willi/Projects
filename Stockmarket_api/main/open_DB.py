from pymysql import connect
import pandas as pd
import matplotlib.pyplot as plt
data_base = connect(host = "localhost",
                    user = "root",
                    passwd = "tobias",
                    database= "sakila")
cur = data_base.cursor()
#query = "show databases"
query = "show tables"
cur.execute(query)

#data_bases = cur.fetchall()
data = cur.fetchall()
print(data)

query = "select * from payment"
cur.execute(query)
df=pd.read_sql(query,data_base)
print(df)
