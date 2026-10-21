# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["TournamentListParams"]


class TournamentListParams(TypedDict, total=False):
    status: Literal["draft", "active", "ended", "any"]
    """Filter by tournament status. Omit or pass `any` for all statuses."""

    limit: int
    """Results per page (max 100)."""

    offset: Optional[int]
    """Number of records to skip."""

    market_id: Annotated[int, PropertyInfo(alias="marketId")]
    """Restrict results to tournaments containing this market."""
