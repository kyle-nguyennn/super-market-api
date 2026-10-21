# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DesignatedMarketMakerSettlementExchange"]


class DesignatedMarketMakerSettlementExchange(BaseModel):
    exchange_id: str = FieldInfo(alias="exchangeId")

    settlement_option: str = FieldInfo(alias="settlementOption")

    proposed_price: Optional[float] = FieldInfo(alias="proposedPrice", default=None)
    """Manipulation-resistant proposed settlement price (5h VWAP). `null` if no valuation is available."""

    proposed_price_source: Literal[
        "vwap", "cfmm_pool", "seed", "backfilled", "admin_override", "dmm_submission", "missing"
    ] = FieldInfo(alias="proposedPriceSource")

    needs_submitted_price: bool = FieldInfo(alias="needsSubmittedPrice")
    """True when the tournament scope has engine trading activity or nonzero app holdings and no valuation price is available — POST must include a submittedPrices entry for this exchangeId."""

    last_trade_price: Optional[float] = FieldInfo(alias="lastTradePrice", default=None)
