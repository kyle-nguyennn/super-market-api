# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DmmTraderAnalyticsHistoryPoint"]


class DmmTraderAnalyticsHistoryPoint(BaseModel):
    as_of: str = FieldInfo(alias="asOf")

    smart_score: float = FieldInfo(alias="smartScore")

    smart_score_decayed: float = FieldInfo(alias="smartScoreDecayed")

    total_trades: int = FieldInfo(alias="totalTrades")
