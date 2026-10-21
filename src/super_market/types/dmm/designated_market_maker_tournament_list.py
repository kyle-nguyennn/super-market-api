# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from .designated_market_maker_tournament_list_item import DesignatedMarketMakerTournamentListItem

__all__ = ["DesignatedMarketMakerTournamentList", "Pagination"]


class Pagination(BaseModel):
    limit: int

    has_more: bool = FieldInfo(alias="hasMore")

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)


class DesignatedMarketMakerTournamentList(BaseModel):
    data: List[DesignatedMarketMakerTournamentListItem]

    pagination: Pagination
