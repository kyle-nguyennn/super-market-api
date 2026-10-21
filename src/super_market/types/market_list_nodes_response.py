# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from .._models import BaseModel

from .market_tree_node import MarketTreeNode
from .market_read_context_descriptor import MarketReadContextDescriptor

__all__ = ["MarketListNodesResponse"]


class MarketListNodesResponse(BaseModel):
    market_id: str

    root: MarketTreeNode
    """Market node returned by `GET /markets/{id}/nodes`: an operator node or a contract (leaf) node, discriminated by `node_type`."""

    contexts: List[MarketReadContextDescriptor]
