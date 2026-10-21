# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .tournament_summary import TournamentSummary

__all__ = ["TournamentListResponse", "Pagination"]


class Pagination(BaseModel):
    limit: int

    offset: int

    has_more: bool = FieldInfo(alias="hasMore")

    total: int
    """Exact number of matching tournaments before pagination."""


class TournamentListResponse(BaseModel):
    data: List[TournamentSummary]

    pagination: Pagination
