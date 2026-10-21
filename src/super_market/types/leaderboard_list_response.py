# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from .._models import BaseModel

from .leaderboard_entry import LeaderboardEntry

__all__ = ["LeaderboardListResponse"]


class LeaderboardListResponse(BaseModel):
    leaderboard: List[LeaderboardEntry]

    total: int

    period: str

    limit: int

    offset: int
