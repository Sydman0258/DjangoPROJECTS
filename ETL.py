import pandas as pd
from sqlalchemy import create_engine


world_cup=pd.read_csv('world_cup_last_50_years.csv')

world_cup.drop_duplicates(inplace=True)
world_cup=world_cup[world_cup['winner'] !='Draw']
world_cup=world_cup[world_cup['stage']=='Final']

engine=create_engine("sqlite:///football.db")
world_cup.to_sql("match_result", engine,if_exists='append',index=False)

print("Data Loaded Successfully 👍👍👍")