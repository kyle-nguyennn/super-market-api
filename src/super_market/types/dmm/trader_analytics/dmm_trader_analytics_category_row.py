# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DmmTraderAnalyticsCategoryRow"]


class DmmTraderAnalyticsCategoryRow(BaseModel):
    market_type: str = FieldInfo(alias="marketType")

    calculation_as_of: str = FieldInfo(alias="calculationAsOf")

    total_trades: int = FieldInfo(alias="totalTrades")

    markets_traded: int = FieldInfo(alias="marketsTraded")

    realized_pnl: float = FieldInfo(alias="realizedPnl")

    unrealized_pnl: float = FieldInfo(alias="unrealizedPnl")

    total_pnl: float = FieldInfo(alias="totalPnl")

    total_stake: float = FieldInfo(alias="totalStake")

    win_rate: float = FieldInfo(alias="winRate")

    roi: float

    sharpe_scaled: float = FieldInfo(alias="sharpeScaled")

    smart_score: float = FieldInfo(alias="smartScore")

    smart_score_decayed: float = FieldInfo(alias="smartScoreDecayed")
