# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .market_tree_operator_node import MarketTreeOperatorNode
from .market_tree_contract_node import MarketTreeContractNode

__all__ = ["MarketTreeNode"]

MarketTreeNode: TypeAlias = Union[MarketTreeOperatorNode, MarketTreeContractNode]
