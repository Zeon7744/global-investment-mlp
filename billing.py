"""
global-investment-mlp 收款层 — 爱发电 afdian 网关

定价锚点（与 README 对齐）：
  免费: ¥0 — 每日报告 3 份/月
  Pro:  ¥199/月 — 全市场信号 + 风控模型 + 压力测试
  企业:  ¥1999/月 — 私有 ML 部署 + 定制因子 + API
"""
import os
import time
import uuid
import json
import urllib.request

PAYWALL_RULES = {
    "free":       {"daily_limit": 1, "monthly_limit": 3, "label": "免费版（3 份/月）"},
    "pro":        {"daily_limit": -1, "label": "Pro ¥199/月"},
    "enterprise": {"daily_limit": -1, "label": "企业 ¥1999/月"},
}

_STATE = {"date": "", "count": 0, "month": "", "monthly_count": 0}

def _today():
    return time.strftime("%Y-%m-%d")

def _this_month():
    return time.strftime("%Y-%m")

def check_access(plan: str = "free", action: str = "report") -> dict:
    """门控：免费版 3 份/月，Pro/企业不限次。"""
    rules = PAYWALL_RULES.get(plan, PAYWALL_RULES["free"])
    limit = rules["daily_limit"]

    if limit == -1:
        return {"allowed": True, "remaining": -1, "reason": ""}

    # 月度限额
    if _STATE["month"] != _this_month():
        _STATE["month"] = _this_month()
        _STATE["monthly_count"] = 0
    if _STATE["monthly_count"] >= rules.get("monthly_limit", 999):
        return {
            "allowed": False,
            "remaining": 0,
            "reason": "免费版 3 份/月已用完，升级 Pro 解锁全市场信号",
            "upgrade_url": "https://afdian.com/@Zeon7744",
            "http_status": 402,
        }

    _STATE["monthly_count"] += 1
    return {
        "allowed": True,
        "remaining": rules.get("monthly_limit", 999) - _STATE["monthly_count"],
        "reason": "",
    }

def get_pricing() -> list[dict]:
    return [
        {"plan": "free", "price": 0, "price_label": "¥0",
         "features": ["每日多因子报告", "3 份/月", "基础风控"]},
        {"plan": "pro", "price": 199, "price_label": "¥199/月",
         "features": ["全市场信号", "风控模型", "压力测试", "组合管理"]},
        {"plan": "enterprise", "price": 1999, "price_label": "¥1999/月",
         "features": ["私有 ML 部署", "定制因子", "API 接入"]},
    ]

class NoopGateway:
    name = "noop"
    def create_order(self, tenant_id, amount_cents, product, plan, order_meta=None):
        return {"order_id": "noop_" + str(uuid.uuid4())[:12], "status": "created", "gateway": "noop"}
    def query_callback(self, order_id):
        return {"order_id": order_id, "status": "unpaid", "paid": False}
    def refund(self, order_id, amount_cents, reason=""):
        return {"order_id": order_id, "ok": True}

class AfdianGateway:
    name = "afdian"
    DEFAULT_BASE = "https://afdian.com/api"
    def __init__(self):
        self.user_id = os.environ.get("JZ_AFDIAN_USER", "")
        self.token = os.environ.get("JZ_AFDIAN_TOKEN", "")
        self.base = os.environ.get("JZ_AFDIAN_BASE", self.DEFAULT_BASE)

    def _post(self, path, payload):
        body = dict(payload)
        if self.token:
            body["token"] = self.token
        req = urllib.request.Request(f"{self.base}{path}",
            data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))

    def create_order(self, tenant_id, amount_cents, product, plan, order_meta=None):
        if not self.user_id or not self.token:
            return {"order_id": "pending", "status": "created_pending_key",
                    "needs_secret": ["JZ_AFDIAN_USER", "JZ_AFDIAN_TOKEN"]}
        price = round(amount_cents / 100.0, 2)
        out_trade_no = "inv_" + str(uuid.uuid4())[:16]
        payload = {"user_id": self.user_id, "price": str(price),
                   "name": f"global-investment({plan})"[:42], "out_trade_no": out_trade_no}
        try:
            result = self._post("/payment/create", payload)
            if result.get("code") != 0:
                return {"order_id": out_trade_no, "status": "gateway_rejected"}
            return {"order_id": out_trade_no, "status": "created",
                    "pay_url": result.get("data", {}).get("url", ""), "gateway": "afdian"}
        except Exception as e:
            return {"order_id": out_trade_no, "status": "gateway_error", "error": str(e)}

    def query_callback(self, order_id):
        if not self.user_id or not self.token:
            return {"order_id": order_id, "status": "pending_key", "paid": False}
        payload = {"user_id": self.user_id, "out_trade_no": order_id}
        try:
            result = self._post("/payment/query", payload)
            return {"order_id": order_id, "paid": result.get("data", {}).get("status") in ("paid", "success")}
        except Exception as e:
            return {"order_id": order_id, "paid": False, "error": str(e)}

    def refund(self, order_id, amount_cents, reason=""):
        if not self.user_id or not self.token:
            return {"order_id": order_id, "ok": False}
        price = round(amount_cents / 100.0, 2)
        try:
            self._post("/payment/refund", {"user_id": self.user_id, "out_trade_no": order_id, "price": str(price)})
            return {"order_id": order_id, "ok": True}
        except Exception as e:
            return {"order_id": order_id, "ok": False, "error": str(e)}

_REGISTRY = {"noop": NoopGateway, "afdian": AfdianGateway}
def get_gateway(name=None):
    return _REGISTRY.get(name or os.environ.get("BILLING_GATEWAY", "noop"), NoopGateway)()

def create_order_for_plan(tenant_id, plan, product="global-investment"):
    g = get_gateway()
    prices = {p["plan"]: p["price"] for p in get_pricing()}
    return g.create_order(tenant_id, int(prices.get(plan, 0) * 100), product, plan)
