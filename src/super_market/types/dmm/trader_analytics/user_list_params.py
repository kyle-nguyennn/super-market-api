# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, TypedDict

from ...._utils import PropertyInfo

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    tournament_id: Annotated[str, PropertyInfo(alias="tournamentId")]
    """Tournament id (must belong to your organization)."""

    group_id: Annotated[str, PropertyInfo(alias="groupId")]
    """User-group id (must belong to your organization)."""

    market_group_id: Annotated[str, PropertyInfo(alias="marketGroupId")]
    """Market-group id (must belong to your organization)."""

    market_type: Annotated[str, PropertyInfo(alias="marketType")]
    """Trader-metrics bucket. Defaults to `global`."""

    period: Literal["day", "week", "month", "quarter", "all"]
    """Calendar-aligned period (UTC). `day` = today, `week` = since the most recent Sunday, `month` = since the 1st of the current month, `quarter` = since the 1st of the current calendar quarter, `all` = no time filter."""

    period_start: Annotated[Union[str, datetime], PropertyInfo(alias="periodStart", format="iso8601")]
    """Custom window start (ISO 8601). Mutually exclusive with `period` when `period != all`."""

    period_end: Annotated[Union[str, datetime], PropertyInfo(alias="periodEnd", format="iso8601")]
    """Custom window end (ISO 8601). Metrics are computed as of this instant, with open positions marked at prices as of `periodEnd`. Requires `period` to be omitted or `all`, and must be after `periodStart` when both are sent."""

    min_smart_score: Annotated[Optional[float], PropertyInfo(alias="minSmartScore")]

    min_trades: Annotated[Optional[int], PropertyInfo(alias="minTrades")]

    elite_only: Annotated[Literal["true", "false"], PropertyInfo(alias="eliteOnly")]

    sort: Literal["smart_score_desc", "profit_desc", "roi_desc", "sharpe_desc", "win_rate_desc", "trades_desc"]

    limit: int

    cursor: str
    """Opaque pagination cursor from a prior response."""

    organization_slug: Annotated[str, PropertyInfo(alias="organizationSlug")]
    """Required for platform administrators when `tournamentId` is omitted."""
