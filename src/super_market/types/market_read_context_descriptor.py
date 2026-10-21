# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

from .market_tournament_context import MarketTournamentContext

__all__ = ["MarketReadContextDescriptor"]


class MarketReadContextDescriptor(BaseModel):
    type: Literal["public", "tournament"]

    tournament: Optional[MarketTournamentContext] = None
    """Tournament metadata, or null for the public global context."""
