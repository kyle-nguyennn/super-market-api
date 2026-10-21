# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MarketTournamentContext"]


class MarketTournamentContext(BaseModel):
    """Tournament metadata, or null for the public global context."""

    id: str

    slug: str

    name: str

    currency_name: str = FieldInfo(alias="currencyName")

    is_ongoing_play: bool = FieldInfo(alias="isOngoingPlay")
    """True for the organization's permanent Ongoing Play tournament."""
