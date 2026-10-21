# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from .designated_market_maker_order import DesignatedMarketMakerOrder

__all__ = ["DesignatedMarketMakerOrderList"]


class DesignatedMarketMakerOrderList(BaseModel):
    data: List[DesignatedMarketMakerOrder]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
