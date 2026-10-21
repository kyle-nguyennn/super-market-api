# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

from .designated_market_maker_settlement_market import DesignatedMarketMakerSettlementMarket

__all__ = ["DesignatedMarketMakerEndSettlementPreview"]


class DesignatedMarketMakerEndSettlementPreview(BaseModel):
    tournament_id: str = FieldInfo(alias="tournamentId")

    slug: str

    markets: List[DesignatedMarketMakerSettlementMarket]

    open_orders_count: int = FieldInfo(alias="openOrdersCount")
