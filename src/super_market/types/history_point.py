# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["HistoryPoint"]


class HistoryPoint(BaseModel):
    time: str

    total_value: float = FieldInfo(alias="totalValue")

    holdings_value: Optional[float] = FieldInfo(alias="holdingsValue", default=None)

    cash_value: Optional[float] = FieldInfo(alias="cashValue", default=None)

    interpolated: bool
    """True for sub-daily (1h/6h) points that are linearly interpolated between the selected stored history points rather than directly valued at that timestamp."""
