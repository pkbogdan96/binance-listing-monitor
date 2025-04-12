# 🚀 Binance Listing Monitor (Python Bot)

A real-time tool to detect new crypto listings on Binance using Python, the Binance API, and web scraping. Ideal for crypto traders, automation builders, or devs seeking alpha signals.

---

## 🔧 Features

- 📡 **Live Binance API monitoring** for new trading pairs  
- 📰 **Scraping official Binance announcements** for early listing alerts  
- ✅ Clean & modular Python code  
- 🔐 Secure API key handling using `.env`  
- 📈 Ready for Telegram/Email/Discord integrations  

---

## 📁 Project Structure

📂 binance-listing-monitor/ ├── binance_monitor.py # Main Python script ├── .env.example # API key format (do not commit real keys!) ├── requirements.txt # Python dependencies └── README.md # You’re reading it



---

## 🚀 Setup Instructions

1. **Clone the repo**  

git clone https://github.com/pkbogdan96/binance-listing-monitor.git
cd binance-listing-monitor
Install dependencies


pip install -r requirements.txt
Add your Binance API keys
Create a .env file based on .env.example:



BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
Run the bot


python binance_monitor.py
💡 How it works
The bot checks Binance exchange info every 10 seconds for new trading pairs

It also scrapes the official Binance Announcements Page
for upcoming listings by searching for “will list” headlines

🤖 Ideal for:
Crypto scalpers & swing traders

Telegram alert bots

Portfolio auto-updaters

Web3 data scrapers

📬 Contact
Made by Bogdan Pavelescu
📩 Need a custom crypto bot? Hire me on Upwork or DM on GitHub!
