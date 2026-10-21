# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["MarketGroupMember"]


class MarketGroupMember(BaseModel):
    market_id: str = FieldInfo(alias="marketId")
    """Market id (bigint serialized as a string)."""

    title: str

    status: Literal["open", "closed", "settled"]

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    added_at: Optional[str] = FieldInfo(alias="addedAt", default=None)
    """When the market was added to this group."""
