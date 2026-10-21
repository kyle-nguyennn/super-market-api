# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from ...._models import BaseModel

from .designated_market_maker_liquidity_level import DesignatedMarketMakerLiquidityLevel

__all__ = ["DesignatedMarketMakerLiquidityBook"]


class DesignatedMarketMakerLiquidityBook(BaseModel):
    bids: List[DesignatedMarketMakerLiquidityLevel]

    asks: List[DesignatedMarketMakerLiquidityLevel]
