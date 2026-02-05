"""Build MarketCatalog by joining Gamma markets/events to token IDs."""
from ..data.gamma_api import list_markets


def build_catalog(limit=1000):
    # Placeholder: paginate and normalize into a catalog table
    offset = 0
    rows = []
    while True:
        data = list_markets(limit=100, offset=offset)
        items = data.get("markets", data) if isinstance(data, dict) else data
        if not items:
            break
        for m in items:
            rows.append({
                "marketId": m.get("id"),
                "conditionId": m.get("conditionId"),
                "question": m.get("question"),
                "outcomes": m.get("outcomes"),
            })
        offset += 100
        if offset >= limit:
            break
    return rows
