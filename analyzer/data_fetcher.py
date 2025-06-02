# analyzer/data_fetcher.py

import yfinance as yf
import pandas as pd

def fetch_financial_data(ticker: str) -> dict:
    """
    Fetch financial statements and key metrics using yfinance.
    Returns a dictionary of dataframes and metadata.
    """
    try:
        stock = yf.Ticker(ticker)

        info = stock.info
        financials = {
            "income_statement": stock.financials.T,
            "balance_sheet": stock.balance_sheet.T,
            "cash_flow": stock.cashflow.T,
            "quarterly_cashflow": stock.quarterly_cashflow.T,
            "metadata": {
                "longName": info.get("longName"),
                "sector": info.get("sector"),
                "industry": info.get("industry"),
                "marketCap": info.get("marketCap"),
                "beta": info.get("beta"),
                "dividendYield": info.get("dividendYield"),
                "country": info.get("country")
            }
        }

        print(f"\n📊 Fetched financial data for {financials['metadata']['longName']}")
        return financials

    except Exception as e:
        print(f"❌ Error fetching data for {ticker}: {e}")
        return {}

