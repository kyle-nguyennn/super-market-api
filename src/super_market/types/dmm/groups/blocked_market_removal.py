# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["BlockedMarketRemoval", "MissingValuation"]


class MissingValuation(BaseModel):
    exchange_id: str = FieldInfo(alias="exchangeId")

    market_id: str = FieldInfo(alias="marketId")

    market_title: str = FieldInfo(alias="marketTitle")

    settlement_option: Optional[str] = FieldInfo(alias="settlementOption", default=None)


class BlockedMarketRemoval(BaseModel):
    market_id: str = FieldInfo(alias="marketId")

    reason: Literal["MISSING_TOURNAMENT_VALUATION"]

    tournament_id: str = FieldInfo(alias="tournamentId")

    missing_valuations: List[MissingValuation] = FieldInfo(alias="missingValuations")
