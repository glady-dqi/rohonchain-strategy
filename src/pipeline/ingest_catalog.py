"""Ingest MarketCatalog into Postgres."""
from .catalog import build_catalog
from ..data.db import get_conn


def run(limit=1000):
    rows = build_catalog(limit=limit)
    with get_conn() as conn:
        with conn.cursor() as cur:
            for r in rows:
                cur.execute(
                    """
                    INSERT INTO market_catalog (market_id, condition_id, question, outcomes)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (market_id) DO UPDATE
                    SET condition_id = EXCLUDED.condition_id,
                        question = EXCLUDED.question,
                        outcomes = EXCLUDED.outcomes
                    """,
                    (r.get("marketId"), r.get("conditionId"), r.get("question"), r.get("outcomes"))
                )
        conn.commit()

if __name__ == "__main__":
    run()
