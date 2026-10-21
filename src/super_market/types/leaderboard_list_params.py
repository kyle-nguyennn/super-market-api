# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["LeaderboardListParams"]


class LeaderboardListParams(TypedDict, total=False):
    tournament_slug: Annotated[str, PropertyInfo(alias="tournamentSlug")]
    """Optional tournament/global tournament slug to scope to. When omitted, organization-bound keys use the organization's default tournament and unbound keys use the global leaderboard."""

    group_id: Annotated[str, PropertyInfo(alias="groupId")]
    """Optional user-group filter. Requires an explicit tournament slug or an organization-bound key; the group must be bound to the resolved tournament."""

    period: Literal["1d", "7d", "30d", "quarter", "all"]
    """Calendar-aligned period (UTC)."""

    sort: Literal["pnl", "roi", "winRate", "volume", "trades"]
    """Sort key. Honored for explicit or organization-defaulted tournament leaderboards; defaults to `pnl`."""

    limit: int
    """Results per page (max 100)."""

    offset: Optional[int]
    """Offset for pagination."""
