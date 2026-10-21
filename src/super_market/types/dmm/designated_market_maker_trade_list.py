# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from .designated_market_maker_trade import DesignatedMarketMakerTrade

__all__ = ["DesignatedMarketMakerTradeList"]


class DesignatedMarketMakerTradeList(BaseModel):
    data: List[DesignatedMarketMakerTrade]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
