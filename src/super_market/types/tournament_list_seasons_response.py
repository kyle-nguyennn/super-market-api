# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TournamentListSeasonsResponse", "Current", "Archived"]


class Archived(BaseModel):
    season_key: str

    starts_at: str

    ends_at: str

    total_members: int

    archived: Literal[True]


class Current(BaseModel):
    season_key: str

    starts_at: str

    ends_at: str

    archived: Literal[False]


class TournamentListSeasonsResponse(BaseModel):
    current: Current

    archived: List[Archived]
