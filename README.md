
# Binance Listing Monitor (Python Project)

This Python-based tool detects new coin listings on Binance using two approaches:

1. **Binance API Monitoring**: Detects newly added trading pairs in real-time.
2. **Web Scraping**: Scrapes Binance's announcements page for upcoming listings.

## Features

- ✅ Real-time tracking of new coins
- ✅ Scrapes official Binance announcements
- ✅ Easy to use and customize
- ✅ Ideal for crypto traders and bot builders

## Requirements

- Python 3.x
- Binance API Key & Secret
- `python-binance`, `requests`, `beautifulsoup4`, `python-dotenv`

## Setup

1. Clone this repo or copy the files.
2. Create a `.env` file and add your Binance keys:
```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Run the script:
```
python binance_monitor.py
```

## Disclaimer

This tool is for educational purposes only. Always trade responsibly.

---

Created by Bogdan – Crypto Automation Specialist
