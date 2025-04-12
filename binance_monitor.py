
import os
import time
import requests
from bs4 import BeautifulSoup
from binance.client import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")

client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

def get_binance_symbols():
    """Fetch all trading symbols from Binance."""
    exchange_info = client.get_exchange_info()
    return {symbol['symbol'] for symbol in exchange_info['symbols']}

def monitor_binance(interval=10):
    """Monitor Binance for new trading pairs."""
    known_symbols = get_binance_symbols()
    print("[INFO] Monitoring Binance for new listings...")
    while True:
        time.sleep(interval)
        new_symbols = get_binance_symbols()
        added = new_symbols - known_symbols
        if added:
            print(f"[ALERT] New coin listed: {added}")
            known_symbols = new_symbols

def check_binance_announcements():
    """Scrape Binance announcements for listing news."""
    url = "https://www.binance.com/en/support/announcement"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print("[INFO] Checking Binance announcements...")
    for link in soup.find_all("a", href=True):
        if "will list" in link.text.lower():
            print(f"[NEWS] Potential new listing: {link.text.strip()} - https://www.binance.com{link['href']}")

if __name__ == "__main__":
    check_binance_announcements()
    monitor_binance()
