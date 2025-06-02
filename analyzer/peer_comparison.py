# analyzer/peer_comparison.py

import yfinance as yf

# Sample peer map (you can customize this later)
PEER_GROUPS = {
    "AAPL": ["AAPL", "MSFT", "GOOGL", "AMZN"],
    "MSFT": ["MSFT", "AAPL", "ORCL", "IBM"],
    "JPM":  ["JPM", "BAC", "C", "WFC"],
    "TSLA": ["TSLA", "GM", "F", "NIO"],
    "NVDA": ["NVDA", "AMD", "INTC", "AVGO"],
}


def compare_peers(ticker):
    peers = PEER_GROUPS.get(ticker.upper(), [ticker.upper()])

    print(f"\n🔎 Peer Comparison for {ticker.upper()}")
    print(f"Comparing with: {', '.join(peers)}")

    results = []

    for peer in peers:
        try:
            stock = yf.Ticker(peer)
            pe_ratio = stock.info.get("trailingPE", None)

            if pe_ratio is None:
                print(f"⚠️  No P/E data for {peer}")
                continue

            results.append((peer, pe_ratio))
            print(f"{peer}: P/E Ratio = {pe_ratio:.2f}")
        except Exception as e:
            print(f"❌ Error fetching data for {peer}: {e}")

    return results
