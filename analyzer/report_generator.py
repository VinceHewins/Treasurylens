# analyzer/report_generator.py

import os
from datetime import datetime

def generate_report(ticker, financials):
    os.makedirs("output", exist_ok=True)

    filename = f"output/{ticker.upper()}_report.txt"
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    try:
        with open(filename, "w") as f:
            f.write(f"TreasuryLens Report for {ticker.upper()}\n")
            f.write(f"Generated on {now}\n")
            f.write("=" * 50 + "\n\n")

            f.write("💵 Income Statement Snapshot:\n")
            f.write(financials["income_statement"].to_string())
            f.write("\n\n")

            f.write("🏦 Balance Sheet Snapshot:\n")
            f.write(financials["balance_sheet"].to_string())
            f.write("\n\n")

            f.write("💧 Cash Flow Snapshot:\n")
            f.write(financials["cash_flow"].to_string())
            f.write("\n")

        print(f"✅ Report saved to '{filename}'")

    except Exception as e:
        print(f"❌ Failed to generate report: {e}")
