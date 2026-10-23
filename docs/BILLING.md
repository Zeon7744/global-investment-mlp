# global-investment-mlp 收款与门控（爱发电 afdian）

## 定价档位（与 billing.py 对齐）
| 档位 | 价格 | 限制 |
|---|---|---|
| Free | ¥0 | 3 份/月报告 |
| Pro | ¥199/月 | 全市场信号+风控+压力测试 |
| 企业 | ¥1999/月 | 私有 ML+定制因子+API |

## 收款流程（先体验后付费）
1. 免费 3 份/月，超限 402 + 升级链接（爱发电 https://afdian.com/@Zeon7744）
2. 付款 → `billing.AfdianGateway.query_callback` 核验 → 本地提权
3. 无 key 走 `noop` 安全降级

## 环境变量
`JZ_AFDIAN_USER` / `JZ_AFDIAN_TOKEN` / `BILLING_GATEWAY`（noop|afdian）
