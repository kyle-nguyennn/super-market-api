# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from ..fill import Fill
from .tournament_pagination import TournamentPagination

__all__ = ["PortfolioListFillsResponse", "Coverage"]


class Coverage(BaseModel):
    complete: Literal[True]
    """Always true because cursor pagination exposes the complete portfolio fill history."""

    projected_through_sequence: Optional[int] = FieldInfo(alias="projectedThroughSequence", default=None)
    """Latest trading-engine sequence reflected by the reporting projection, or null when no checkpoint exists."""


class PortfolioListFillsResponse(BaseModel):
    data: List[Fill]

    pagination: TournamentPagination

    coverage: Coverage
    """Reporting projection coverage metadata. Always present."""
