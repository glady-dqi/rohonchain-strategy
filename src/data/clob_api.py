"""CLOB REST client (public endpoints)."""
import os
import requests

BASE = os.getenv("CLOB_API", "https://clob.polymarket.com")


def get_price(token_id: str):
    r = requests.get(f"{BASE}/price", params={"token_id": token_id}, timeout=30)
    r.raise_for_status()
    return r.json()


def get_book(token_id: str):
    r = requests.get(f"{BASE}/book", params={"token_id": token_id}, timeout=30)
    r.raise_for_status()
    return r.json()


def get_midpoint(token_id: str):
    r = requests.get(f"{BASE}/midpoint", params={"token_id": token_id}, timeout=30)
    r.raise_for_status()
    return r.json()
