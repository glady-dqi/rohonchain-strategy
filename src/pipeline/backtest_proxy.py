"""Proxy backtest using CLOB orderbook snapshots (no historical trades)."""
import json
from statistics import mean
from ..data.db import get_conn


def vwap_from_book(side_levels, size):
    # side_levels: list of {"price": str, "size": str}
    remaining = size
    cost = 0.0
    filled = 0.0
    for lvl in side_levels:
        p = float(lvl.get("price"))
        q = float(lvl.get("size"))
        take = min(q, remaining)
        cost += p * take
        filled += take
        remaining -= take
        if remaining <= 0:
            break
    if filled == 0:
        return None
    return cost / filled


def run(sample=200, size=10.0):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT token_id, bids, asks
                FROM book_snapshots
                ORDER BY id DESC
                LIMIT %s
                """,
                (sample,),
            )
            rows = cur.fetchall()

    spreads = []
    vwap_spreads = []
    for token_id, bids, asks in rows:
        bids = json.loads(bids) if isinstance(bids, str) else (bids or [])
        asks = json.loads(asks) if isinstance(asks, str) else (asks or [])
        if not bids or not asks:
            continue
        best_bid = float(bids[0]["price"])
        best_ask = float(asks[0]["price"])
        spreads.append(best_ask - best_bid)

        buy_vwap = vwap_from_book(asks, size)
        sell_vwap = vwap_from_book(bids, size)
        if buy_vwap is not None and sell_vwap is not None:
            vwap_spreads.append(buy_vwap - sell_vwap)

    return {
        "samples": len(rows),
        "spreads_n": len(spreads),
        "avg_spread": mean(spreads) if spreads else None,
        "avg_vwap_spread": mean(vwap_spreads) if vwap_spreads else None,
    }

if __name__ == "__main__":
    print(run())
