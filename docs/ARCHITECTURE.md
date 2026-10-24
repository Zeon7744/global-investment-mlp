# global-investment-mlp 模块结构

## 目录
```
global-investment-mlp/
├── main.py            # 入口：完整投资分析管线
├── data_fetcher.py    # 数据获取
├── multi_factor_model.py / core_analyzer.py   # 多因子 + 热点
├── risk_analytics.py  # 风控
├── report_generator.py / refresh_report.py    # 报告
├── billing.py         # 收款层：NoopGateway + MbdGateway + PAYWALL_RULES + check_access
├── test_all.py        # 全量测试
└── docs/
```

## 数据流
1. `main.py` argparse → 数据获取 → 热点检测 → 多因子 → 风控 → 配置建议 → 报告生成
2. 每份报告前走 `billing.check_access('free','report')` 门控（3 份/月）
3. 超限 402 + 升级链接（面包多 Pay https://mbd.com/@Zeon7744）

## 门控模型
- `PAYWALL_RULES`: free=3 份/月, pro=不限, enterprise=不限
