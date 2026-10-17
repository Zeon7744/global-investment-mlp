"""global-investment-mlp 数据刷新：多源拉全球行情 → 写 reports/。CI/本地可跑。

数据源优先级（fallback 链）：
  1. yfinance（真实行情，国内受限需代理）
  2. 占位兜底（保证 pipeline 不挂，标注 source=placeholder）

健壮性增强（本次迭代）：
  - 修复 yfinance 传参 bug：旧版 yf.Tickers(...) 误用，改为逐个 Ticker
  - 限流/网络异常指数退避重试（最多 3 次）
  - 写 health.json 供 CI 读取判断数据源状态
  - 幂等：无变化不产生空 commit
"""
import os
import json
import time
import datetime

INDEXES = ["^GSPC", "^HSI", "BTC-USD"]


def _retry(fn, attempts=3, base_delay=2.0):
    """指数退避重试。"""
    last = None
    for i in range(attempts):
        try:
            return fn()
        except Exception as e:  # noqa: BLE001
            last = e
            if i < attempts - 1:
                time.sleep(base_delay * (2 ** i))
    raise last


def fetch_yfinance():
    try:
        import yfinance as yf

        def do():
            out = {}
            for t in INDEXES:
                h = yf.Ticker(t).history(period="1d")
                if len(h):
                    out[t] = {"price": float(h["Close"].iloc[-1])}
            return out or None

        return _retry(do, attempts=3, base_delay=2.0)
    except Exception as e:  # noqa: BLE001
        print(f"[warn] yfinance 拉取失败（已重试3次），回退占位：{e}")
        return None


def main():
    os.makedirs("reports", exist_ok=True)
    day = datetime.date.today().isoformat()
    data = fetch_yfinance()
    if data:
        payload = {"date": day, "source": "yfinance", "quotes": data, "signals": []}
    else:
        payload = {"date": day, "source": "placeholder", "quotes": {},
                   "signals": [],
                   "note": "yfinance 不可用/国内受限，占位；有网或配代理后自动填充真实行情"}
    # 写健康度文件，供 CI / 管理后台读取
    health = {"date": day, "source": payload["source"],
              "quotes_count": len(payload.get("quotes", {})),
              "ok": payload["source"] != "placeholder"}
    open(f"reports/{day}.json", "w", encoding="utf-8").write(
        json.dumps(payload, ensure_ascii=False, indent=2))
    open("reports/latest.json", "w", encoding="utf-8").write(
        json.dumps(payload, ensure_ascii=False, indent=2))
    open("reports/health.json", "w", encoding="utf-8").write(
        json.dumps(health, ensure_ascii=False, indent=2))
    print("report @", day, "source=", payload["source"], "quotes=", health["quotes_count"])


if __name__ == "__main__":
    main()
