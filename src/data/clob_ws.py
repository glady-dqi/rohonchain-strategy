"""CLOB WebSocket skeleton for MARKET channel subscriptions."""
import os
import json
import asyncio
import websockets

WS_URL = os.getenv("CLOB_WS", "wss://ws-subscriptions-clob.polymarket.com/ws/")

async def subscribe_market(asset_ids):
    async with websockets.connect(WS_URL) as ws:
        msg = {
            "type": "MARKET",
            "asset_ids": asset_ids,
            "custom_feature_enabled": False
        }
        await ws.send(json.dumps(msg))
        async for raw in ws:
            yield json.loads(raw)

# Example usage:
# async for m in subscribe_market(["token_id"]):
#     print(m)
