# RohOnChain Strategy Implementation (Polymarket Arbitrage Framework)

This repo implements a **research-grade** framework described in the provided thread:
- Arbitrage detection via **linear constraints / integer programming**
- Arbitrage removal via **Bregman projection** (LMSR / KL divergence)
- **Frank–Wolfe** with an **integer-programming oracle**
- Execution modeling with **VWAP**, liquidity constraints, and non‑atomic risk

> ⚠️ This is a *research/engineering framework*. It does **not** place live trades by default.

## Architecture
```
rohonchain-strategy/
├─ README.md
├─ pyproject.toml
├─ src/
│  ├─ data/
│  │  ├─ polygon_events.py
│  │  └─ polymarket_clob.py
│  ├─ arbitrage/
│  │  ├─ constraints.py
│  │  ├─ ip_oracle.py
│  │  └─ detect.py
│  ├─ projection/
│  │  ├─ bregman.py
│  │  ├─ frank_wolfe.py
│  │  └─ barrier_fw.py
│  ├─ execution/
│  │  ├─ vwap.py
│  │  ├─ non_atomic.py
│  │  └─ sizing.py
│  └─ pipeline/
│     ├─ realtime.py
│     └─ backtest.py
├─ notebooks/
│  └─ demo.ipynb
└─ tests/
   └─ test_constraints.py
```

## Quick Start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Notes
- IP solver default: **PuLP** (CBC). Replace with **Gurobi** if available.
- LMSR/KL projection is implemented with configurable epsilon contraction.
- Execution layer is modeled; no live trading without explicit enablement.

## References
- "Unravelling the Probabilistic Forest: Arbitrage in Prediction Markets" (arXiv:2508.03474v1)
- "Arbitrage-Free Combinatorial Market Making via Integer Programming" (arXiv:1606.02825v2)
