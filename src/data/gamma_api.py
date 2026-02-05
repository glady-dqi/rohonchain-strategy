"""Gamma API client (market/event discovery)."""
import os
import requests

BASE = os.getenv("GAMMA_API", "https://gamma-api.polymarket.com")


def list_events(limit=100, offset=0, status=None):
    params = {"limit": limit, "offset": offset}
    if status:
        params["status"] = status
    r = requests.get(f"{BASE}/events", params=params, timeout=30)
    r.raise_for_status()
    return r.json()


def list_markets(limit=100, offset=0, status=None, active=None, closed=None):
    params = {"limit": limit, "offset": offset}
    if status:
        params["status"] = status
    if active is not None:
        params["active"] = str(active).lower()
    if closed is not None:
        params["closed"] = str(closed).lower()
    r = requests.get(f"{BASE}/markets", params=params, timeout=30)
    r.raise_for_status()
    return r.json()
