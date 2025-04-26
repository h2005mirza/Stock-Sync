import urllib.request, urllib.error
import json
import time



def get_stock_data(ticker, api_key):

    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/prev?adjusted=true&apiKey={api_key}"

    try:
        response = urllib.request.urlopen(url)
        data = response.read().decode()
        json_data = json.loads(data)
        return json_data

    except urllib.error.URLError as e:
        print(f"A URL error occurred: {e.reason}")
    except Exception as e:
        print("An error occurred: ", str(e))

if __name__ == "__main__":
    api_key = "YOUR-API-KEY"
    tickers = [
        "AAPL",  # Apple (Tech)
        "MSFT",  # Microsoft (Tech)
        "GOOGL",  # Alphabet (Google) (Tech)
        "AMZN",  # Amazon (E-commerce)
        "TSLA",  # Tesla (Automotive)
        "META",  # Meta (Facebook) (Tech)
        "NVDA",  # Nvidia (Semiconductors)
        "V",  # Visa (Finance)
        "PYPL",  # PayPal (Finance)
        "DIS",  # Disney (Entertainment)
        "NFLX",  # Netflix (Streaming)
        "INTC",  # Intel (Semiconductors)
        "AMD",  # AMD (Semiconductors)
        "BA",  # Boeing (Aerospace & Defense)
        "BABA",  # Alibaba (E-commerce)
        "LMT",  # Lockheed Martin (Defense)
        "RTX",  # Raytheon Technologies (Defense)
        "GD",  # General Dynamics (Defense)
        "NOC",  # Northrop Grumman (Defense)
        "HII",  # Huntington Ingalls Industries (Defense)
        "SPY",  # SPDR S&P 500 ETF (Index Fund)
        "GM",  # General Motors (Automotive)
        "FORD",  # Ford (Automotive)
        "UBER",  # Uber (Transport)
        "LYFT",  # Lyft (Transport)
        "ZM",  # Zoom (Tech)
        "CSCO",  # Cisco (Networking)
        "NVDA",  # Nvidia (Semiconductors)
        "CRM",  # Salesforce (Tech)
        "SQ",  # Square (Finance)
        "INTU",  # Intuit (Tech/Finance)
        "ORCL",  # Oracle (Tech)
        "SHOP",  # Shopify (E-commerce)
        "T",  # AT&T (Telecom)
        "VZ",  # Verizon (Telecom)
        "XOM",  # ExxonMobil (Energy)
        "CVX",  # Chevron (Energy)
        "KO",  # Coca-Cola (Consumer Goods)
        "PEP",  # PepsiCo (Consumer Goods)
        "PG",  # Procter & Gamble (Consumer Goods)
        "WMT",  # Walmart (Retail)
        "HD",  # Home Depot (Retail)
        "MCD",  # McDonald's (Food/Restaurant)
        "NKE",  # Nike (Apparel)
        "MS",  # Morgan Stanley (Banking)
        "GS",  # Goldman Sachs (Banking)
        "JPM",  # JPMorgan Chase (Banking)
        "C",  # Citigroup (Banking)
        "BAC",  # Bank of America (Banking)
        "AXP",  # American Express (Finance)
        "UNH",  # UnitedHealth Group (Healthcare)
        "PFE",  # Pfizer (Healthcare)
        "MRK",  # Merck (Healthcare)
        "JNJ",  # Johnson & Johnson (Healthcare)
        "LLY"  # Eli Lilly (Healthcare)
    ]

    for ticker in tickers:
        fetched_data = get_stock_data(ticker, api_key)
        print("\n---TICKER---")
        print(f"{'-' * 40}")
        print(json.dumps(fetched_data, indent=4))
        time.sleep(12)



