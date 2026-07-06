import sqlite3
import pandas as pd

connection = sqlite3.connect("wildlife.db")

query = "SELECT * FROM sanctuaries"

data = pd.read_sql(query, connection)

print(data)

connection.close()