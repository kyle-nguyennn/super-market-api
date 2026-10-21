# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PortfolioListPnlParams"]


class PortfolioListPnlParams(TypedDict, total=False):
    period: Literal["day", "week", "month", "quarter", "year", "all"]
    """Rolling lookback window measured back from the request time; `all` is unbounded."""
