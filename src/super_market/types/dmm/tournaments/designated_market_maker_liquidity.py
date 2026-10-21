# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

from .designated_market_maker_liquidity_book import DesignatedMarketMakerLiquidityBook

__all__ = ["DesignatedMarketMakerLiquidity"]


class DesignatedMarketMakerLiquidity(BaseModel):
    mode: Literal["replace", "append"]

    exchange_id: str = FieldInfo(alias="exchangeId")

    trades_executed: int = FieldInfo(alias="tradesExecuted")

    quantity_matched: float = FieldInfo(alias="quantityMatched")

    resting_orders_created: int = FieldInfo(alias="restingOrdersCreated")

    swept_orders: int = FieldInfo(alias="sweptOrders")
    """Number of existing managed orders actually cancelled. Retained unchanged rungs do not count; an identical `replace` returns 0."""

    latest_price: Optional[float] = FieldInfo(alias="latestPrice", default=None)

    book: DesignatedMarketMakerLiquidityBook
