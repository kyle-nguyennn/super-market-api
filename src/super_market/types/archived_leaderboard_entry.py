# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ArchivedLeaderboardEntry"]


class ArchivedLeaderboardEntry(BaseModel):
    rank: int
    """Placement rank. Tied entries share a rank, and subsequent positions skip by the size of the tie (1-1-3)."""

    profile_id: str = FieldInfo(alias="profileId")

    username: Optional[str] = None

    final_total_value: float = FieldInfo(alias="finalTotalValue")
    """Frozen total portfolio value at season close."""

    final_balance: float = FieldInfo(alias="finalBalance")
    """Frozen virtual-cash balance at season close."""

    trades_count: int = FieldInfo(alias="tradesCount")
