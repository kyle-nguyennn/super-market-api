# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DesignatedMarketMakerSubmittedSettlementPrice"]


class DesignatedMarketMakerSubmittedSettlementPrice(BaseModel):
    exchange_id: str = FieldInfo(alias="exchangeId")

    price: float

    source: Optional[Literal["admin_override", "dmm_submission", "automation"]] = None
    """Context for who supplied the price; admin overrides remain distinguishable from DMM-submitted prices."""
