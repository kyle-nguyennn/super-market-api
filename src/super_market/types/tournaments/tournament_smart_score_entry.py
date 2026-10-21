# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TournamentSmartScoreEntry"]


class TournamentSmartScoreEntry(BaseModel):
    market_type: str = FieldInfo(alias="marketType")
    """Bucket the score was computed for (e.g. `global`, `sports`, `politics`)."""

    smart_score: float = FieldInfo(alias="smartScore")
    """Raw composite score from the trader-scoring pipeline."""

    smart_score_decayed: float = FieldInfo(alias="smartScoreDecayed")
    """Time-decayed composite score used for ranking."""

    is_elite: bool = FieldInfo(alias="isElite")
    """True when the caller is in the latest elite cut for this marketType."""

    selected_via: Optional[Literal["percentile", "threshold"]] = FieldInfo(alias="selectedVia", default=None)

    rank: int

    total_traders: int = FieldInfo(alias="totalTraders")

    minimum_elite_score: float = FieldInfo(alias="minimumEliteScore")

    calculation_as_of: str = FieldInfo(alias="calculationAsOf")
