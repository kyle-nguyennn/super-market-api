# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MarketTreeOperatorNode"]


class MarketTreeOperatorNode(BaseModel):
    node_id: str

    node_type: Literal["operator"]

    operator: Literal["AND", "OR", "NOT", "IF"]

    children: List["MarketTreeNode"]


from .market_tree_node import MarketTreeNode
