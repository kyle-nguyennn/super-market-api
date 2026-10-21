# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .designated_market_maker_failed_settlement_row import DesignatedMarketMakerFailedSettlementRow

__all__ = ["DesignatedMarketMakerFailedSettlementList", "Pagination"]


class Pagination(BaseModel):
    limit: int

    offset: int

    total: int

    has_more: bool = FieldInfo(alias="hasMore")


class DesignatedMarketMakerFailedSettlementList(BaseModel):
    data: List[DesignatedMarketMakerFailedSettlementRow]

    pagination: Pagination
