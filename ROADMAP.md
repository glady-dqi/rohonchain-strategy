# Roadmap (Production-Ready)

## Phase 0 — Catalog & identifiers (NOW)
- [ ] Build MarketCatalog from Gamma API (eventId, marketId, conditionId, tokenYes/No)
- [ ] Daily sync job + snapshot persistence

## Phase 1 — Historical ingest (NOW)
- [ ] Data API / CLOB trade history ingest (normalized fills)
- [ ] Subgraph backfill for positions + liquidity

## Phase 2 — Real-time stream
- [ ] CLOB WS MARKET channel (asset_ids)
- [ ] Orderbook reconstruction + snapshotting

## Phase 3 — On-chain verifier (optional, later)
- [ ] Index Polygon logs (CTFExchange + ERC1155 transfers)
- [ ] Join on-chain settlement with off-chain fills

## Phase 4 — Backtest engine
- [ ] Event-driven simulator
- [ ] Execution models: top-of-book + VWAP
- [ ] Fees + latency modeling

## Engineering
- [ ] Postgres schema + migrations
- [ ] Config + secrets
- [ ] Tests (parsers + golden files)
- [ ] Docker + CI
