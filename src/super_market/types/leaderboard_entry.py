# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LeaderboardEntry"]


class LeaderboardEntry(BaseModel):
    rank: int
    """Placement rank. Tied entries share a rank, and subsequent positions skip by the size of the tie (1-1-3)."""

    profile_id: str = FieldInfo(alias="profileId")

    username: Optional[str] = None

    pnl: float

    trades_count: int = FieldInfo(alias="tradesCount")

    volume: float
    """Bid+ask notional volume in the period, using non-tournament trades globally or trades in the selected tournament."""

    win_rate: Optional[float] = FieldInfo(alias="winRate", default=None)
    """Lifetime resolved-only win rate (0-100) from the latest trader-scoring snapshot for the leaderboard scope (global or selected tournament). Null when no snapshot or resolved history exists."""

    roi: float
    """Period PnL divided by period volume × 100, rounded to 2 decimals and clamped to ±500 (0 when volume is 0)."""
