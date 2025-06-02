# analyzer/debt_analysis.py

def analyze_debt(financials: dict):
    try:
        bs = financials['balance_sheet']
        metadata = financials['metadata']
        company = metadata.get("longName", "Unknown Company")

        print(f"\n🏦 Debt & Capital Structure Analysis for {company}")
        print("-" * 40)

        total_debt = bs.loc['Short Long Term Debt'] + bs.loc['Long Term Debt']
        total_assets = bs.loc['Total Assets']
        cash = bs.loc['Cash']
        equity = bs.loc['Total Stockholder Equity']

        print("Year\tTotal Debt\tCash\t\tNet Debt\tDebt/Equity\tDebt/Assets")
        for date in total_debt.index:
            net_debt = total_debt[date] - cash[date]
            d_e = total_debt[date] / equity[date] if equity[date] else 0
            d_a = total_debt[date] / total_assets[date] if total_assets[date] else 0

            print(f"{date.year}\t${total_debt[date]:,.0f}\t${cash[date]:,.0f}"
                  f"\t${net_debt:,.0f}\t{d_e:.2f}\t\t{d_a:.2f}")

    except Exception as e:
        print(f"❌ Error in debt analysis: {e}")
