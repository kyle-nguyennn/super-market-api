# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

from .dmm_trader_analytics_user import DmmTraderAnalyticsUser
from .dmm_trader_analytics_scope import DmmTraderAnalyticsScope

__all__ = ["DmmTraderAnalyticsUsersList"]


class DmmTraderAnalyticsUsersList(BaseModel):
    users: List[DmmTraderAnalyticsUser]

    computed_as_of: str = FieldInfo(alias="computedAsOf")

    sort: Literal["smart_score_desc", "profit_desc", "roi_desc", "sharpe_desc", "win_rate_desc", "trades_desc"]

    limit: int

    total: int

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)

    scope: DmmTraderAnalyticsScope
