#SHIFT + Z TO EXECUTE

#from turtle import clear
from sqlalchemy import create_engine
import pandas as pd
#import matplotlib as plt
#import seaborn as sns

host="sql4.freemysqlhosting.net"
database="sql4475967"
user="sql4475967"
password="wyqTTgFxLS"
port = 3306

def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )

£
sql = '''

SELECT * FROM guests
WHERE id<=50
AND id >=3;

'''

#add your SQL heare
df = pd.read_sql(sql, get_connection())
print (df)
