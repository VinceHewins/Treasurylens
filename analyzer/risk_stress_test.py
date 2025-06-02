# analyzer/risk_stress_test.py

def run_stress_test(cash_flow, balance_sheet, ticker):
    print(f"\n🔍 Running stress test for {ticker}...")

    try:
        op_cash = cash_flow.loc.get("Operating Cash Flow")
        debt = balance_sheet.loc.get("Long Term Debt")

        if op_cash is None or debt is None:
            print("❌ Missing data for stress testing.")
            return

        # Use most recent year (leftmost column)
        latest_cash = op_cash.iloc[0]
        latest_debt = debt.iloc[0] if debt.iloc[0] != 0 else 1

        liquidity_ratio = latest_cash / latest_debt

        print(f"🧪 Liquidity Ratio: {liquidity_ratio:.2f}")

        if liquidity_ratio < 0.5:
            print("⚠️  Company may struggle to cover debt with operations.")
        elif liquidity_ratio < 1.0:
            print("🟡 Caution: Moderate financial pressure.")
        else:
            print("✅ Resilient: Operating cash flow covers long-term debt.")

    except Exception as e:
        print(f"❌ Error during stress test: {e}")
