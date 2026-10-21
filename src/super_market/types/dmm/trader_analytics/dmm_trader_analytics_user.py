# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

from .dmm_trader_analytics_scope import DmmTraderAnalyticsScope

__all__ = ["DmmTraderAnalyticsUser"]


class DmmTraderAnalyticsUser(BaseModel):
    profile_id: str = FieldInfo(alias="profileId")

    username: Optional[str] = None

    email: Optional[str] = None

    smart_score: float = FieldInfo(alias="smartScore")

    smart_score_decayed: float = FieldInfo(alias="smartScoreDecayed")

    is_elite: bool = FieldInfo(alias="isElite")

    sharpe_scaled: float = FieldInfo(alias="sharpeScaled")
    """Sharpe scaled to 0–100 by the trader-scoring pipeline."""

    roi: float

    win_rate: float = FieldInfo(alias="winRate")
    """Resolved-only win rate as a percentage (0–100)."""

    realized_pnl: float = FieldInfo(alias="realizedPnl")

    unrealized_pnl: float = FieldInfo(alias="unrealizedPnl")

    total_pnl: float = FieldInfo(alias="totalPnl")
    """realizedPnl + unrealizedPnl."""

    total_trades: int = FieldInfo(alias="totalTrades")

    total_stake: float = FieldInfo(alias="totalStake")

    markets_traded: int = FieldInfo(alias="marketsTraded")

    normalized_pnl: float = FieldInfo(alias="normalizedPnl")

    last_trade_at: Optional[str] = FieldInfo(alias="lastTradeAt", default=None)

    scope: DmmTraderAnalyticsScope
