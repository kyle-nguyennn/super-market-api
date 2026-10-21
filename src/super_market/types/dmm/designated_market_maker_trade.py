# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from .designated_market_maker_trade_participant import DesignatedMarketMakerTradeParticipant

__all__ = ["DesignatedMarketMakerTrade"]


class DesignatedMarketMakerTrade(BaseModel):
    id: int

    created_at: str = FieldInfo(alias="createdAt")

    market_id: str = FieldInfo(alias="marketId")

    market_title: str = FieldInfo(alias="marketTitle")

    settlement_option: str = FieldInfo(alias="settlementOption")

    price: float

    quantity: int

    volume: float

    bid_order_id: Optional[int] = FieldInfo(alias="bidOrderId", default=None)

    ask_order_id: Optional[int] = FieldInfo(alias="askOrderId", default=None)

    bid: Optional[DesignatedMarketMakerTradeParticipant] = None

    ask: Optional[DesignatedMarketMakerTradeParticipant] = None
