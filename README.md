# global-investment-mlp

## 💰 价值主张 & 定价
> **能卖什么**：多资产配置投资模型 — 四因子量化信号 + VaR/CVaR 压力测试，美股/港股/加密货币一键切换，每日多因子 HTML 报告。
>
> **定价**：免费（每日报告 3 份/月）/ **Pro 授权 ¥99/次**（完整源码 + 全市场信号 + 风控模型）/ **企业 ¥1999/月**（私有 ML 部署 + 定制因子 + API）。付费渠道：[爱发电 @Zeon7744](https://afdian.net/@Zeon7744)。⚠️ 本工具不构成投资建议，仅供研究学习。


> 多因子量化投资框架 — 四因子模型 · VaR/压力测试 · HTML报告

[![GitHub Stars](https://img.shields.io/github/stars/Zeon7744/global-investment-mlp?style=social)](https://github.com/Zeon7744/global-investment-mlp)
[![Gitee stars](https://gitee.com/Zeon7744/global-investment-mlp/badge/star.svg?theme=gvp)](https://gitee.com/Zeon7744/global-investment-mlp)
[![GitCode stars](https://gitcode.com/Zeon7744/global-investment-mlp/stars/badge)](https://gitcode.com/Zeon7744/global-investment-mlp)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-v0.1.0-blue)](https://github.com/Zeon7744/global-investment-mlp/releases/tag/v0.1.0)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)]()

## 在线演示

- [GitHub Pages](https://zeon7744.github.io/global-investment-mlp/)

## 简介

**多因子量化投资框架**，适用于美股、港股、加密货币市场。提供风险调整后的选股模型和压力测试能力。

## 核心特性

- **四类因子**: 动量(Momentum)、价值(Value)、质量(Quality)、波动(Volatility)
- **风险调整选股模型**: Sharpe Ratio 优化
- **压力测试与情景分析**: VaR / CVaR / 极端市场环境模拟
- **多市场适配**: 美股/港股/加密货币一键切换
- **HTML 报告生成**: 自动输出投资分析报告

## 支持市场

| 市场 | 标的 |
|------|------|
| 美股 | S&P 500, Nasdaq 100 |
| 港股 | 恒生指数成分 |
| 加密货币 | BTC, ETH, ALT |

## 快速开始

```bash
git clone https://github.com/Zeon7744/global-investment-mlp.git
cd global-investment-mlp
pip install -r requirements.txt
python main.py --market us --factor momentum
```

## 文档

- [CHANGELOG.md](CHANGELOG.md) — 版本历史

## 多平台镜像

| 平台 | 链接 |
|------|------|
| GitHub (主仓库) | [GitHub](https://github.com/Zeon7744/global-investment-mlp) |
| Gitee | [Gitee](https://gitee.com/Zeon7744/global-investment-mlp) |
| GitCode | [GitCode](https://gitcode.com/Zeon7744/global-investment-mlp) |

## 赞助与支持

| 平台 | 链接 | 支付方式 |
|------|------|----------|
| ☕ **爱发电** | [afdian.com/@Zeon7744](https://afdian.com/@Zeon7744) | 支付宝 / 微信支付 |
| 🌍 **GitHub Sponsors** | [github.com/sponsors/Zeon7744](https://github.com/sponsors/Zeon7744) | PayPal / Stripe |

### 赞助档位

| 档位 | 价格 | 权益 |
|------|------|------|
| ☕ 请喝咖啡 | ¥18/月 | 感谢支持 |
| 🍺 请喝啤酒 | ¥58/月 | 优先回复 Issue |
| 🎁 项目赞助 | ¥188/月 | 定制功能需求 |

## 相关项目

- [baibai](https://github.com/Zeon7744/baibai) — MCP 工具库
- [crypto-mlp-high-confidence](https://github.com/Zeon7744/crypto-mlp-high-confidence) — 加密货币预测
- [dev-artifacts](https://github.com/Zeon7744/dev-artifacts) — 开发工具箱

## 贡献

欢迎提交 Issue 和 Pull Request！详见 [CONTRIBUTING.md](CONTRIBUTING.md)

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

---

*由 [Zeon7744](https://github.com/Zeon7744) 维护 · 量化投资 · 三平台同步*

---

## 🚀 免费 → Pro → 企业（变现入口）

免费=每日多因子报告；Pro=¥199/月（全市场信号+风控）；企业=¥1999/月（私有 ML 部署）

- **免费**：立即 [安装/克隆] 使用，命中配额即可升级。
- **Pro（¥199/月）**：[爱发电订阅](https://afdian.net/@Zeon7744) 解锁高级能力。
- **企业（¥1999/月）**：私有部署 / 定制需求 → [联系商务](https://afdian.net/@Zeon7744)。

> 详细定价见 [pricing.md](pricing.md) | 🎁 crypto+global 套餐 ¥299/月

---

## 快速上手
依赖安装：
```bash
python3 -m pip install -r requirements.txt
```

## 变现路径
研究仓，变现路径=开源背书→量化内容输出→咨询/课程（非代码直接售卖）。
> 定价：见 [pricing.md](pricing.md) | 订阅：[爱发电 @Zeon7744](https://afdian.net/@Zeon7744)

---


---

## ⚖️ 商用与合规

### 开源范围
- 代码（多因子模型、回测框架、报告生成器）以 MIT License 开放，可自由使用、修改与商用。
- 以下部分不属于开源范围：Pro/企业档位的托管服务（全市场信号、私有 ML 部署、定制因子）。

### 付费功能边界
- 免费（¥0）：每日多因子报告、基础回测、HTML 报告生成
- Pro（¥199/月）：全市场信号 + 风控模型 + 组合回测
- 企业（¥1999/月）：私有 ML 部署 + 定制因子 + SLA 保障

### 内容版权
- 基金/指数数据来自公开行情与模拟数据，不构成投资建议
- 开源代码：MIT 适用范围为全部 Python 代码、测试、文档
- 历史回测指标基于公开数据，不代表未来收益

### 合规免责
- 本项目是研究与教学用途的全球资产配置与基金回测工具，**不构成任何投资建议、证券研究意见或投资顾问服务**
- 使用本工具产生的任何投资/交易决策由使用者自行承担，本项目作者不对任何交易结果、亏损或合规责任负责
- 涉及跨境投资/基金/外汇时，请自行遵守所在地及相关市场监管法规
- 实盘交易请遵守当地证券/外汇监管法规；本项目不托管真实资金

---

## ⚖️ 法控声明（Non-investment-advice disclaimer）

- **非投资建议 / 非投资顾问**：本项目是研究与教学用途的全球资产配置与基金回测工具，**不构成任何投资建议、证券研究意见或投资顾问服务**。组合回测的超额收益、信息比率、再平衡对比等指标均基于历史/模拟数据，**不代表未来收益**，不构成买卖依据。
- **合规免责**：使用本工具产生的任何投资/交易决策由使用者自行承担，本项目作者不对任何交易结果、亏损或合规责任负责。涉及跨境投资/基金/外汇时，请自行遵守所在地及相关市场监管法规。
- **数据脱敏**：基金/指数数据来自公开行情与模拟数据，不涉任何真实个人账户或持仓；若接入真实数据源，仅读取公开行情，**不采集、不存储任何用户私人信息或交易账户凭据**。
- **使用边界**：仅可用于研究与学习，不得用于违反当地金融监管法规的用途。

> 发布产物 / 付费门 / 法控总览：见 `DISTRIBUTION.md`


---

## 💰 订阅支持

| 档位 | 价格 | 核心权益 |
|------|------|----------|
| 免费 | ¥0 | 每日多因子报告 |
| Pro | ¥199/月 | 全市场信号 + 风控模型 |
| 企业 | ¥1999/月 | 私有 ML 部署 + 定制因子 |

🎁 **量化套餐**：crypto-mlp Pro + global-investment Pro = **¥299/月**（省 ¥89）

👉 **[立即订阅 — 爱发电](https://afdian.net/@Zeon7744)**（支付宝 / 微信支付）

> 详细定价见 [pricing.md](pricing.md)
