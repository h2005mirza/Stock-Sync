import time
import schedule
import pytz
from datetime import datetime
from database import create_table, insert_stock_data

# defining the timezone
ny_timezone = pytz.timezone('America/New_York')
pk_timezone = pytz.timezone('Asia/Karachi')

# defining the NYSE market hours
market_open = datetime.strptime("09:30", "%H:%M").time()  # PKT 6:30 PM
market_close = datetime.strptime("10:00", "%H:%M").time()  # PKT 7:00 PM

# API key and ticker list
api_key = "YOUR-API-KEY"
ticker_symbol = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "V", "PYPL", "DIS",
    "NFLX", "INTC", "AMD", "BA", "BABA", "LMT", "RTX", "GD", "NOC", "HII", "SPY",
    "GM", "FORD", "UBER", "LYFT", "ZM", "CSCO", "CRM", "SQ", "INTU", "ORCL",
    "SHOP", "T", "VZ", "XOM", "CVX", "KO", "PEP", "PG", "WMT", "HD", "MCD", "NKE",
    "MS", "GS", "JPM", "C", "BAC", "AXP", "UNH", "PFE", "MRK", "JNJ", "LLY"
]


def fetch_stock_market_data():

    # defining current timezone
    current_ny_time = datetime.now(ny_timezone).time()
    current_pk_time = datetime.now(pk_timezone).strftime("%Y-%m-%d %H:%M:%S")

    if market_open <= current_ny_time <= market_close:
        print(f"[{current_pk_time}] Market is open. Fetching Data....")
        insert_stock_data(api_key, ticker_symbol)
    else:
        print(f"[{current_pk_time}] Market closed. Stopping the scheduler.")
        exit()

create_table()

schedule.every(15).minutes.do(fetch_stock_market_data())  # every 15 minutes
print("NYSE TIME SCHEDULER HAS BEEN INITIATED...\n")

# creating loop to make sure that the program doesn't run infinitely
while True:
    schedule.run_pending()
    time.sleep(1) # prohibiting max CPU usage
