"""CLOB trades endpoint (authenticated)."""
import os
import requests

BASE = os.getenv("CLOB_API", "https://clob.polymarket.com")
API_KEY = os.getenv("CLOB_API_KEY")  # if required by your setup


def get_trades(params: dict):
    headers = {}
    if API_KEY:
        headers["Authorization"] = API_KEY
    r = requests.get(f"{BASE}/data/trades", params=params, headers=headers, timeout=30)
    r.raise_for_status()
    return r.json()
