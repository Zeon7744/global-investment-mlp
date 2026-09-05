# CONTRIBUTING

感谢你对 global-investment-mlp 的关注！以下是参与贡献的指南。

## 如何贡献

1. Fork 本仓库
2. 创建特性分支: `git checkout -b feature/your-feature`
3. 提交更改: `git commit -m 'Add your feature'`
4. 推送分支: `git push origin feature/your-feature`
5. 提交 Pull Request

## 因子开发

- 新因子需在 `factors/` 目录实现
- 每个因子需包含回测验证脚本
- 提交前确保 Sharpe Ratio 符合预期

## 市场适配

当前支持：
- 美股 (S&P 500, Nasdaq)
- 港股 (恒生指数成分)
- 加密货币 (BTC, ETH, ALT)

新增市场请在 `markets/` 目录添加配置。

## 报告问题

请在 [Issues](https://github.com/Zeon7744/global-investment-mlp/issues) 中报告。

## 赞助支持

如果框架对你有帮助：
- [爱发电](https://afdian.com/@Zeon7744)
- [GitHub Sponsors](https://github.com/sponsors/Zeon7744)
