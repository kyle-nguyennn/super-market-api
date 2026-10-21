# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .exchange_list_item import ExchangeListItem

__all__ = ["ExchangeListResponse", "Pagination"]


class Pagination(BaseModel):
    limit: int

    has_more: bool = FieldInfo(alias="hasMore")

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)


class ExchangeListResponse(BaseModel):
    data: List[ExchangeListItem]

    pagination: Pagination
