# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional, Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .leaderboard_entry import LeaderboardEntry
from .archived_leaderboard_entry import ArchivedLeaderboardEntry
from .season_descriptor import SeasonDescriptor
from .bound_group import BoundGroup

__all__ = ["TournamentListLeaderboardResponse", "Leaderboard"]

Leaderboard: TypeAlias = Union[LeaderboardEntry, ArchivedLeaderboardEntry]


class TournamentListLeaderboardResponse(BaseModel):
    leaderboard: List[Leaderboard]

    total: int

    period: str

    limit: int

    offset: int

    sort: Optional[Literal["pnl", "roi", "winRate", "volume", "trades"]] = None
    """Echo of the applied sort. Omitted for archived seasons."""

    my_rank: Optional[int] = FieldInfo(alias="myRank", default=None)
    """Caller's competition rank under the selected sort within the same `period` as the leaderboard rows; ties share a rank and subsequent positions skip by the tie size. Null if the caller has not traded in the period (unranked)."""

    season: Optional[SeasonDescriptor] = None
    """Season descriptor for Ongoing Play tournaments; null for other tournaments."""

    bound_groups: List[BoundGroup] = FieldInfo(alias="boundGroups")
    """User groups bound to this tournament. Empty when no groups are bound."""

    active_group_id: Optional[str] = FieldInfo(alias="activeGroupId", default=None)
    """Echo of the `groupId` filter; null when unfiltered."""
