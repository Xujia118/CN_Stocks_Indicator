import sqlalchemy
import pandas as pd

engine = sqlalchemy.create_engine('sqlite:///CSI_300.db')
df = pd.read_sql('600519.ss', engine)

print(df.head())
