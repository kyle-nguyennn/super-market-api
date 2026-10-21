# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["DmmListRankingsParams"]


class DmmListRankingsParams(TypedDict, total=False):
    organization_slug: Annotated[str, PropertyInfo(alias="organizationSlug")]
    """Slug of the organization to read rankings for. Organization-bound keys may only name their own organization (defaults to it when omitted; another organization's slug returns 403, an unknown slug 404). Required for platform administrators."""

    market_type: Annotated[
        Literal[
            "global",
            "Election Outcome",
            "Financial Product",
            "Freeform",
            "Economic Indicator",
            "Sports Outcome",
            "Corporate Earnings",
            "Imported Market",
        ],
        PropertyInfo(alias="marketType"),
    ]
    """Trader-metrics bucket: `global` aggregates across all market types; any other value restricts metrics to that market type. Defaults to `global`."""

    sort_by: Annotated[
        Literal[
            "smartScore",
            "smartScoreRaw",
            "roi",
            "sharpe",
            "winRate",
            "realizedPnl",
            "unrealizedPnl",
            "totalStake",
            "trades",
        ],
        PropertyInfo(alias="sortBy"),
    ]
    """Column to rank by. `smartScore` is the time-decayed composite; `smartScoreRaw` is the undecayed raw score."""

    order: Literal["asc", "desc"]

    limit: int

    offset: Optional[int]

    user_group_id: Annotated[str, PropertyInfo(alias="userGroupId")]
    """Optional user-group filter. Must be a `user_group` belonging to the target organization; otherwise the request is rejected with a validation error. Ranks are recomputed within the filtered set."""

    market_group_id: Annotated[str, PropertyInfo(alias="marketGroupId")]
    """Optional market-group filter. Must be a `market_group` belonging to the target organization; otherwise the request is rejected with a validation error. Switches the response to on-demand metrics scoped to trades within the group."""

    period: Literal["1d", "7d", "30d", "all"]
    """Calendar-aligned period filter (UTC). `1d` = today, `7d` = since most recent Sunday, `30d` = since 1st of the current month, `all` = no time filter. When set to anything other than `all`, metrics are recomputed on-demand and `computed` will be `on-demand`."""
