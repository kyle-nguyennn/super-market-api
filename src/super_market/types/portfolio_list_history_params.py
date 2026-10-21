# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["PortfolioListHistoryParams"]


class PortfolioListHistoryParams(TypedDict, total=False):
    interval: Literal["1h", "6h", "1d", "1w", "all"]
    """`1h` and `6h` are linearly interpolated after selecting the stitched history points (flagged with `interpolated: true`). `all` returns the selected stored points without weekly downsampling."""

    from_: Annotated[str, PropertyInfo(alias="from")]
    """ISO-8601 start date (inclusive). Must not be after `to`. Defaults to 1 year before `to`, or to the interval's maximum span where that is shorter (`1h` → 31 days)."""

    to: str
    """ISO-8601 end date (inclusive). Defaults to now."""
