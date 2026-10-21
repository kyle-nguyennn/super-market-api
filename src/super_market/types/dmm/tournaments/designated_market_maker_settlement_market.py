# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

from .designated_market_maker_settlement_exchange import DesignatedMarketMakerSettlementExchange

__all__ = ["DesignatedMarketMakerSettlementMarket"]


class DesignatedMarketMakerSettlementMarket(BaseModel):
    market_id: str = FieldInfo(alias="marketId")

    title: str

    exchanges: List[DesignatedMarketMakerSettlementExchange]
