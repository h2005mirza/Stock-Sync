import sqlite3
import time
from api_handler import get_stock_data

# Create table if not exists
def create_table():
    conn = sqlite3.connect('stockmarket.db')
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Stock_Info(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT,
            volume INTEGER,
            volume_weighted_average_price REAL,
            open_price REAL,
            close_price REAL,
            high_price REAL,
            low_price REAL,
            timestamp REAL,
            number_of_transactions INTEGER,
            UNIQUE (ticker, timestamp)
        )
    ''')

    conn.commit()
    conn.close()

def insert_stock_data(api_key, tickers):
    conn = sqlite3.connect('stockmarket.db')
    cur = conn.cursor()

    for i, ticker in enumerate(tickers):
        print(f"Fetching Data: {ticker}")
        data = get_stock_data(ticker, api_key)

        if data and 'results' in data and data['results']:
            result = data['results'][0]
            cur.execute('''
                INSERT OR REPLACE INTO Stock_Info(
                    ticker, volume, volume_weighted_average_price, open_price, close_price,
                    high_price, low_price, timestamp, number_of_transactions
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                result.get('T'),
                result.get('v'),
                result.get('vw'),
                result.get('o'),
                result.get('c'),
                result.get('h'),
                result.get('l'),
                result.get('t'),
                result.get('n')
            ))

            conn.commit()
            print(f"Data {ticker} inserted successfully!")
        else:
            print(f"No data for: {ticker}")

        time.sleep(12)  # Respect API rate limits

    conn.close()
    print("Data Updated Successfully!")

# Auto run when file is executed
if __name__ == "__main__":
    api_key = "LBYggJ93PZ2KPU68NV5nhTBUTapRRpp1"
    tickers = [
        "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA",
        "V", "PYPL", "DIS", "NFLX", "INTC", "AMD", "BA", "BABA",
        "LMT", "RTX", "GD", "NOC", "HII", "SPY", "GM", "FORD",
        "UBER", "LYFT", "ZM", "CSCO", "CRM", "SQ", "INTU", "ORCL",
        "SHOP", "T", "VZ", "XOM", "CVX", "KO", "PEP", "PG", "WMT",
        "HD", "MCD", "NKE", "MS", "GS", "JPM", "C", "BAC", "AXP",
        "UNH", "PFE", "MRK", "JNJ", "LLY"
    ]

    create_table()
    insert_stock_data(api_key, tickers)
