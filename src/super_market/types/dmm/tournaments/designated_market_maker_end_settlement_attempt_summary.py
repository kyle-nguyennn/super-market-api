# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

from .designated_market_maker_submitted_settlement_price import DesignatedMarketMakerSubmittedSettlementPrice
from .designated_market_maker_settlement_error_summary import DesignatedMarketMakerSettlementErrorSummary

__all__ = ["DesignatedMarketMakerEndSettlementAttemptSummary"]


class DesignatedMarketMakerEndSettlementAttemptSummary(BaseModel):
    id: str

    status: Literal["queued", "running", "succeeded", "failed", "skipped_stale", "skipped_not_ended"]

    trigger: Optional[Literal["automation", "platform_admin", "dmm_operator"]] = None

    submitted_prices: Optional[List[DesignatedMarketMakerSubmittedSettlementPrice]] = FieldInfo(
        alias="submittedPrices", default=None
    )

    error: Optional[DesignatedMarketMakerSettlementErrorSummary] = None
