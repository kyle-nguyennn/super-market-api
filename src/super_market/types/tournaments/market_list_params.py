# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MarketListParams"]


class MarketListParams(TypedDict, total=False):
    limit: int
    """Results per page (max 100)."""

    cursor: str
    """Pagination cursor from a previous response."""

    search: str
    """Case-insensitive title search (at most 200 characters)."""

    status: Literal["open", "closed", "settled", "resolved", "any"]
    """Filter by market lifecycle status. `resolved` is a deprecated alias for `settled`."""

    market_group_id: Annotated[str, PropertyInfo(alias="marketGroupId")]
    """Restrict to markets that belong to the given market group. The group must be bound to this tournament; otherwise returns 400."""
