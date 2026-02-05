"""Subgraph client (historicals)."""
import os
from graphqlclient import GraphQLClient

SUBGRAPH = os.getenv("SUBGRAPH_URL")


def query(q: str, variables=None):
    if not SUBGRAPH:
        raise RuntimeError("SUBGRAPH_URL not set")
    client = GraphQLClient(SUBGRAPH)
    return client.execute(query=q, variables=variables or {})

# Example query template
# q = """
# query($first:Int){ markets(first:$first){ id question } }
# """
# print(query(q, {"first": 5}))
