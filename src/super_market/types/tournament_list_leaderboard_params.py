# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["TournamentListLeaderboardParams"]


class TournamentListLeaderboardParams(TypedDict, total=False):
    period: Literal["1d", "7d", "30d", "all"]
    """Calendar-aligned period (UTC). `1d` = today, `7d` = this week (Sunday-anchored), `30d` = this month, `all` = all-time."""

    limit: int
    """Results per page (max 100)."""

    offset: Optional[int]
    """Offset for pagination."""

    group_id: Annotated[str, PropertyInfo(alias="groupId")]
    """Optional user-group filter. Must be a group bound to the tournament (see `boundGroups` in the response)."""

    season: str
    """Ongoing Play tournaments only. Archived season key (e.g. `2026-Q1`) or `current`. An archived key requires `period=all`."""

    sort: Literal["pnl", "roi", "winRate", "volume", "trades"]
    """Ranking key for `rank` and `myRank`. Ignored for archived seasons."""
