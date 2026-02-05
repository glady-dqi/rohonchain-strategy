"""Snapshot orderbooks for a sample of markets (proxy backtest)."""
import json
from ..data.db import get_conn
from ..data.clob_api import get_book


def run(limit=20):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT market_id, clob_token_ids FROM market_catalog WHERE clob_token_ids IS NOT NULL AND active = TRUE AND closed = FALSE LIMIT %s",
                (limit,),
            )
            rows = cur.fetchall()

    snaps = 0
    with get_conn() as conn:
        with conn.cursor() as cur:
            for market_id, token_ids in rows:
                try:
                    tokens = json.loads(token_ids) if isinstance(token_ids, str) else token_ids
                except Exception:
                    tokens = token_ids
                if not tokens:
                    continue
                for tid in tokens:
                    book = get_book(tid)
                    cur.execute(
                        """
                        INSERT INTO book_snapshots (token_id, snapshot_ts, bids, asks, raw)
                        VALUES (%s, NOW(), %s, %s, %s)
                        """,
                        (tid, json.dumps(book.get("bids")), json.dumps(book.get("asks")), json.dumps(book))
                    )
                    snaps += 1
        conn.commit()
    return snaps

if __name__ == "__main__":
    n = run()
    print("snapshots", n)
