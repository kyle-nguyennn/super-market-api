# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PortfolioListPnlParams"]


class PortfolioListPnlParams(TypedDict, total=False):
    period: Literal["day", "week", "month", "quarter", "year", "all"]
    """Rolling lookback window for period P&L and Sharpe, measured back from the request time: `day` 1, `week` 7, `month` 30, `quarter` 90, `year` 365 days; `all` is unbounded. Unlike leaderboard periods, these are not calendar-aligned."""
