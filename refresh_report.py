"""global-investment-mlp 数据刷新：yfinance 拉全球行情 → 写 reports/。CI/本地可跑。
国内访问 yfinance 受限，回退占位；有代理/有网环境自动填真实数据。"""
import os
import json
import datetime


def fetch_yfinance():
    try:
        import yfinance as yf
        tks = yf.Tickers("^GSPC ^HSI BTC-USD")
        out = {}
        for t in tks.tickers:
            h = tks.tickers[t].history(period="1d")
            if len(h):
                out[t] = {"price": float(h["Close"].iloc[-1])}
        return out or None
    except Exception as e:
        print("[warn] yfinance 拉取失败，回退占位：", e)
        return None


def main():
    os.makedirs("reports", exist_ok=True)
    day = datetime.date.today().isoformat()
    data = fetch_yfinance()
    if data:
        payload = {"date": day, "source": "yfinance", "quotes": data, "signals": []}
    else:
        payload = {"date": day, "source": "placeholder", "signals": [],
                   "note": "yfinance 不可用/国内受限，占位；有网环境自动填充"}
    open(f"reports/{day}.json", "w", encoding="utf-8").write(json.dumps(payload, ensure_ascii=False, indent=2))
    open("reports/latest.json", "w", encoding="utf-8").write(json.dumps(payload, ensure_ascii=False, indent=2))
    print("report @", day, "source=", payload["source"])


if __name__ == "__main__":
    main()
