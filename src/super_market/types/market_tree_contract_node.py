# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MarketTreeContractNode"]


class MarketTreeContractNode(BaseModel):
    node_id: str

    node_type: Literal["contract"]

    contract_id: str
    """Same value as `node_id`."""

    contract_type: Optional[str] = None

    title: Optional[str] = None

    settlement_date: Optional[datetime] = None

    settled_with: Optional[str] = None
    """Outcome this contract settled with; null while unsettled."""

    contract_details: Optional[Dict[str, object]] = None
    """Contract-type-specific data passed through as stored, or null. Its shape varies by `contract_type`."""
