import yfinance as yf
import pandas as pd

def analyze_cement_stocks():
    # NSE Tickers for UltraTech, Ambuja, and ACC
    tickers = ["ULTRACEMCO.NS", "AMBUJACEM.NS", "ACC.NS"]
    results = []

    for symbol in tickers:
        stock = yf.Ticker(symbol)
        info = stock.info
        
        # Calculating/Extracting the required assignment metrics
        metrics = {
            "Company": info.get("shortName"),
            "P/E Ratio": round(info.get("trailingPE", 0), 2),
            "P/B Ratio": round(info.get("priceToBook", 0), 2),
            "ROE (%)": round(info.get("returnOnEquity", 0) * 100, 2),
            "Op. Margin (%)": round(info.get("operatingMargins", 0) * 100, 2),
            "Debt-to-Equity": info.get("debtToEquity", 0)
        }
        results.append(metrics)

    # Create DataFrame and Export
    df = pd.DataFrame(results)
    df.to_excel("Cement_Sector_Analysis.xlsx", index=False)
    print("Analysis Complete. File saved as Cement_Sector_Analysis.xlsx")
    return df

if __name__ == "__main__":
    analyze_cement_stocks()