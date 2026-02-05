"""Trade ingest (placeholder). Attach to Data API when endpoint finalized."""
from ..data.db import get_conn


def run(trades):
    with get_conn() as conn:
        with conn.cursor() as cur:
            for t in trades:
                cur.execute(
                    """
                    INSERT INTO trades (market_id, token_id, price, size, side, trade_ts, raw)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT DO NOTHING
                    """,
                    (
                        t.get("market_id"), t.get("token_id"), t.get("price"), t.get("size"),
                        t.get("side"), t.get("trade_ts"), t
                    )
                )
        conn.commit()
