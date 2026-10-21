# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["MarketGroupMemberAddResult"]


class MarketGroupMemberAddResult(BaseModel):
    added: int

    skipped: int
    """Eligible markets that were already in the group."""

    not_found: List[str] = FieldInfo(alias="notFound")
    """Ids that are malformed, unknown, or not visible to this organization."""
