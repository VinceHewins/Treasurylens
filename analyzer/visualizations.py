import matplotlib.pyplot as plt
import os

def plot_cash_flows(cf, ticker):
    years = cf.columns.astype(str)
    op_cash = cf.loc.get("Operating Cash Flow", None)
    capex = cf.loc.get("Capital Expenditure", None)

    if op_cash is None or capex is None:
        print("⚠️  Not enough data to plot cash flows.")
        return

    fcf = op_cash + capex  # CapEx is negative

    plt.figure(figsize=(10, 6))
    plt.plot(years, op_cash / 1e9, label='Operating Cash Flow', marker='o')
    plt.plot(years, capex / 1e9, label='Capital Expenditure', marker='o')
    plt.plot(years, fcf / 1e9, label='Free Cash Flow', marker='o')
    plt.title(f"{ticker.upper()} - Cash Flows Over Time")
    plt.ylabel("Billions USD")
    plt.xlabel("Year")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    path = f"output/{ticker.upper()}_cash_flows.png"
    plt.savefig(path)
    plt.close()
    print(f"📈 Saved cash flow plot: {path}")

def plot_debt_vs_equity(bs, ticker):
    years = bs.columns.astype(str)
    debt = bs.loc.get("Long Term Debt", None)
    equity = bs.loc.get("Total Stockholder Equity", None)

    if debt is None or equity is None:
        print("⚠️  Not enough data to plot debt vs equity.")
        return

    plt.figure(figsize=(10, 6))
    plt.plot(years, debt / 1e9, label='Long Term Debt', marker='o')
    plt.plot(years, equity / 1e9, label='Stockholder Equity', marker='o')
    plt.title(f"{ticker.upper()} - Capital Structure")
    plt.ylabel("Billions USD")
    plt.xlabel("Year")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    path = f"output/{ticker.upper()}_debt_equity.png"
    plt.savefig(path)
    plt.close()
    print(f"📉 Saved debt vs equity plot: {path}")

def plot_peer_comparison(peers_data, main_ticker):
    if not peers_data:
        print("⚠️  No peer data available to plot.")
        return

    tickers = [t for t, _ in peers_data]
    pe_ratios = [p for _, p in peers_data]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(tickers, pe_ratios, color=['green' if t == main_ticker.upper() else 'gray' for t in tickers])
    plt.title(f"{main_ticker.upper()} vs Peers - P/E Ratio")
    plt.ylabel("P/E Ratio")
    plt.tight_layout()

    path = f"output/{main_ticker.upper()}_peer_pe_comparison.png"
    plt.savefig(path)
    plt.close()
    print(f"📊 Saved peer comparison chart: {path}")
