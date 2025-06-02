# analyzer/portfolio_tracker.py

import yfinance as yf
from datetime import datetime

def track_portfolio(tickers):
    print(f"\n📊 Portfolio Tracker — {datetime.today().strftime('%Y-%m-%d')}")

    print(f"{'Ticker':<10} {'Price':>10} {'% Change (1D)':>15}")
    print("-" * 40)

    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="2d")

            if len(hist) < 2:
                print(f"{ticker:<10} Data unavailable")
                continue

            latest_close = hist["Close"].iloc[-1]
            previous_close = hist["Close"].iloc[-2]
            percent_change = ((latest_close - previous_close) / previous_close) * 100

            print(f"{ticker:<10} ${latest_close:>9.2f} {percent_change:>14.2f}%")
        except Exception as e:
            print(f"❌ Error fetching data for {ticker}: {e}")
