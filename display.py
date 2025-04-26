import sqlite3
from tabulate import tabulate # for displaying data in a structured format

conn = sqlite3.connect('stockmarket.db')
cur = conn.cursor()

cur.execute('SELECT *FROM Stock_Info')
rows = cur.fetchall()

headers = ['Ticker', 'Volume', 'Vol Weighted Avg Price', 'Open Price', 'Close Price',
           'High Price', 'Low Price', 'Timestamp', 'Total Transactions'] # defining headers
print("---STOCKS DATA---")
print(tabulate(rows, headers=headers, tablefmt='fancy_grid')) # functions of tabulate library

conn.close()
