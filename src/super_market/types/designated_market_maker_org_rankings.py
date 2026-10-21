# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .designated_market_maker_org_ranking_member import DesignatedMarketMakerOrgRankingMember

__all__ = ["DesignatedMarketMakerOrgRankings"]


class DesignatedMarketMakerOrgRankings(BaseModel):
    organization_id: str = FieldInfo(alias="organizationId")

    organization_slug: Optional[str] = FieldInfo(alias="organizationSlug", default=None)

    organization_name: Optional[str] = FieldInfo(alias="organizationName", default=None)

    market_type: Literal[
        "global",
        "Election Outcome",
        "Financial Product",
        "Freeform",
        "Economic Indicator",
        "Sports Outcome",
        "Corporate Earnings",
        "Imported Market",
    ] = FieldInfo(alias="marketType")
    """Trader-metrics bucket: `global` aggregates across all market types; any other value restricts metrics to that market type. Defaults to `global`."""

    sort_by: Literal[
        "smartScore",
        "smartScoreRaw",
        "roi",
        "sharpe",
        "winRate",
        "realizedPnl",
        "unrealizedPnl",
        "totalStake",
        "trades",
    ] = FieldInfo(alias="sortBy")
    """Column to rank by. `smartScore` is the time-decayed composite; `smartScoreRaw` is the undecayed raw score."""

    order: Literal["asc", "desc"]

    limit: int

    offset: int

    user_group_id: Optional[str] = FieldInfo(alias="userGroupId", default=None)
    """Echo of the `userGroupId` filter; null when unfiltered."""

    market_group_id: Optional[str] = FieldInfo(alias="marketGroupId", default=None)
    """Echo of the `marketGroupId` filter; null when unfiltered."""

    period: Literal["1d", "7d", "30d", "all"]
    """Calendar-aligned period filter (UTC). `1d` = today, `7d` = since most recent Sunday, `30d` = since 1st of the current month, `all` = no time filter. When set to anything other than `all`, metrics are recomputed on-demand and `computed` will be `on-demand`."""

    computed: Literal["snapshot", "on-demand"]
    """`snapshot` = served from the latest persisted trader-metrics snapshot (cheap). `on-demand` = recomputed live with `marketGroupId` / `period` filters applied; somewhat heavier."""

    total: int
    """Total members in the scope (group-filtered when `userGroupId` is set; otherwise the whole organization)."""

    members: List[DesignatedMarketMakerOrgRankingMember]
