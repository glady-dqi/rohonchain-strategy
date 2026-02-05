"""Ingest trades from CLOB /data/trades (authenticated)."""
from ..data.clob_trades import get_trades
from ..data.db import get_conn


def run(market=None, after=None, before=None):
    params = {}
    if market:
        params["market"] = market  # conditionId
    if after:
        params["after"] = after
    if before:
        params["before"] = before
    trades = get_trades(params)

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
                        t.get("market"), t.get("asset_id"), t.get("price"), t.get("size"),
                        t.get("side"), t.get("match_time"), t
                    )
                )
        conn.commit()

if __name__ == "__main__":
    run()
