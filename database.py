import sqlite3
import pandas as pd

connection = sqlite3.connect("wildlife.db")

cursor = connection.cursor()

sanctuaries = pd.read_csv("data/sanctuaries.csv")
conservations = pd.read_csv("data/conservations.csv")

sanctuaries.to_sql(
    "sanctuaries",
    connection,
    if_exists="replace",
    index=False
)

conservations.to_sql(
    "conservations",
    connection,
    if_exists="replace",
    index=False
)

print("Database created successfully!")

connection.close()