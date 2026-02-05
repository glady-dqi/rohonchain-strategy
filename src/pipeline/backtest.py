"""Backtest skeleton using stored trades and simple execution model."""
from ..data.db import get_conn


def run():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT market_id, token_id, price, size, trade_ts FROM trades ORDER BY trade_ts ASC")
            rows = cur.fetchall()
    # TODO: event-driven simulation
    return rows
