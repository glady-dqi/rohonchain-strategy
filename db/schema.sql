-- Core tables for catalog + trades + book snapshots

CREATE TABLE IF NOT EXISTS market_catalog (
  market_id TEXT PRIMARY KEY,
  condition_id TEXT,
  question TEXT,
  outcomes JSONB,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS trades (
  id SERIAL PRIMARY KEY,
  market_id TEXT,
  token_id TEXT,
  price NUMERIC,
  size NUMERIC,
  side TEXT,
  trade_ts TIMESTAMP,
  raw JSONB,
  UNIQUE (market_id, token_id, trade_ts, price, size)
);

CREATE TABLE IF NOT EXISTS book_snapshots (
  id SERIAL PRIMARY KEY,
  token_id TEXT,
  snapshot_ts TIMESTAMP,
  bids JSONB,
  asks JSONB,
  raw JSONB
);
