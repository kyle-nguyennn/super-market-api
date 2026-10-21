# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

from .blocked_market_removal import BlockedMarketRemoval

__all__ = ["MarketGroupMemberRemoveResult"]


class MarketGroupMemberRemoveResult(BaseModel):
    removed: int

    removed_market_ids: List[str] = FieldInfo(alias="removedMarketIds")

    not_found: List[str] = FieldInfo(alias="notFound")

    blocked: List[BlockedMarketRemoval]
    """Markets left in place because removing them would settle held positions on an exchange with no tournament valuation price. The rest of the batch still proceeds."""
