# analyzer/cash_flow_analysis.py

import pandas as pd

def analyze_cash_flows(financials: dict):
    """
    Analyze cash flow health and trends.
    Outputs free cash flow, reinvestment ratio, and key observations.
    """
    try:
        cf = financials['cash_flow']
        metadata = financials['metadata']
        company_name = metadata.get("longName", "Unknown Company")

        print(f"\n💵 Cash Flow Analysis for {company_name}")
        print("-" * 40)

        # Rename for easier access
        op_cash = cf.loc['Total Cash From Operating Activities']
        capex = cf.loc['Capital Expenditures']

        fcf = op_cash + capex  # CapEx is negative
        fcf_margin = fcf / op_cash.replace(0, 1)  # Avoid div by zero

        print("Year\tOp. Cash Flow\tCapEx\t\tFree Cash Flow\tFCF Margin")
        for date in op_cash.index:
            print(f"{date.year}\t${op_cash[date]:,.0f}\t${capex[date]:,.0f}\t"
                  f"${fcf[date]:,.0f}\t{fcf_margin[date]*100:.1f}%")

        # Reinvestment ratio
        reinvestment_ratio = -capex / op_cash.replace(0, 1)
        print("\n🛠 Reinvestment Ratio (CapEx / OpCF):")
        for date in reinvestment_ratio.index:
            print(f"{date.year}: {reinvestment_ratio[date]*100:.1f}%")

        # Simple heuristics
        fcf_growth = (fcf.iloc[0] - fcf.iloc[-1]) / abs(fcf.iloc[-1] if fcf.iloc[-1] != 0 else 1)
        print("\n📈 FCF Growth (Oldest to Newest): {:.2f}%".format(fcf_growth * 100))

        if fcf_growth > 0.1:
            print("✅ Strong free cash flow growth.")
        elif fcf_growth < -0.1:
            print("⚠️ Declining free cash flow. Investigate further.")
        else:
            print("ℹ️ Relatively flat FCF over time.")

    except Exception as e:
        print(f"❌ Error analyzing cash flow: {e}")
