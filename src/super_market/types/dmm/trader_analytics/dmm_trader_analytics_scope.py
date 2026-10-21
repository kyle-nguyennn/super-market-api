# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DmmTraderAnalyticsScope"]


class DmmTraderAnalyticsScope(BaseModel):
    market_type: str = FieldInfo(alias="marketType")

    organization_id: str = FieldInfo(alias="organizationId")

    organization_slug: Optional[str] = FieldInfo(alias="organizationSlug", default=None)

    tournament_id: Optional[str] = FieldInfo(alias="tournamentId", default=None)
    """Tournament id when the request was scoped to a tournament; null otherwise."""

    tournament_slug: Optional[str] = FieldInfo(alias="tournamentSlug", default=None)

    user_group_id: Optional[str] = FieldInfo(alias="userGroupId", default=None)

    market_group_id: Optional[str] = FieldInfo(alias="marketGroupId", default=None)

    period: Literal["day", "week", "month", "quarter", "all"]
    """Calendar-aligned period (UTC). `day` = today, `week` = since the most recent Sunday, `month` = since the 1st of the current month, `quarter` = since the 1st of the current calendar quarter, `all` = no time filter."""

    period_start: Optional[str] = FieldInfo(alias="periodStart", default=None)
    """Resolved window start used to recompute metrics: the custom `periodStart` when one was sent (including with `period=all`), otherwise the start of the calendar `period`; null when no start applies."""

    period_end: Optional[str] = FieldInfo(alias="periodEnd", default=None)
    """Echo of the custom `periodEnd` the metrics were computed as of; null when none was sent and metrics run up to the time of the request."""
