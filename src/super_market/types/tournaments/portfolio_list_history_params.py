# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PortfolioListHistoryParams"]


class PortfolioListHistoryParams(TypedDict, total=False):
    interval: Literal["1h", "6h", "1d", "1w", "all"]
    """`1h` and `6h` linearly interpolate between selected tournament history points; `all` returns selected stored points without weekly downsampling."""

    from_: Annotated[str, PropertyInfo(alias="from")]
    """ISO-8601 start date (inclusive). Must not be after `to`."""

    to: str
    """ISO-8601 end date (inclusive). Defaults to now."""
