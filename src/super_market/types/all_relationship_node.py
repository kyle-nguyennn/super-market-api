# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AllRelationshipNode"]


class AllRelationshipNode(BaseModel):
    exchange_id: str = FieldInfo(alias="exchangeId")
    """Positive numeric ID encoded as a string."""

    market_id: Optional[str] = FieldInfo(alias="marketId", default=None)
    """Positive numeric ID encoded as a string."""

    market_title: Optional[str] = FieldInfo(alias="marketTitle", default=None)

    outcome: Optional[str] = None

    current_price: Optional[float] = FieldInfo(alias="currentPrice", default=None)
    """Latest available price for this exchange in the returned context."""

    role: Literal["member", "antecedent", "consequent", "output", "input"]
    """The exchange's logical role within the relationship."""

    contract_id: Optional[str] = FieldInfo(alias="contractId", default=None)
