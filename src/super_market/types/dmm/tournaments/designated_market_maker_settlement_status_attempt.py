# File generated from our OpenAPI spec by Scalar. See README.md for details.
# pyright: reportIncompatibleVariableOverride=false

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .designated_market_maker_end_settlement_attempt_summary import DesignatedMarketMakerEndSettlementAttemptSummary
from .designated_market_maker_submitted_settlement_price import DesignatedMarketMakerSubmittedSettlementPrice
from .designated_market_maker_settlement_error_summary import DesignatedMarketMakerSettlementErrorSummary
from .designated_market_maker_settlement_result_summary import DesignatedMarketMakerSettlementResultSummary

__all__ = ["DesignatedMarketMakerSettlementStatusAttempt"]


class DesignatedMarketMakerSettlementStatusAttempt(DesignatedMarketMakerEndSettlementAttemptSummary):
    trigger: Literal["automation", "platform_admin", "dmm_operator"]

    submitted_prices: List[DesignatedMarketMakerSubmittedSettlementPrice] = FieldInfo(alias="submittedPrices")

    error: Optional[DesignatedMarketMakerSettlementErrorSummary] = None

    created_at: str = FieldInfo(alias="createdAt")

    started_at: Optional[str] = FieldInfo(alias="startedAt", default=None)

    finished_at: Optional[str] = FieldInfo(alias="finishedAt", default=None)

    result: Optional[DesignatedMarketMakerSettlementResultSummary] = None
