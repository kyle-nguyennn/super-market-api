# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, Optional, TYPE_CHECKING

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AllRelationshipCorrectiveTrade"]


class AllRelationshipCorrectiveTrade(BaseModel):
    exchange_id: str = FieldInfo(alias="exchangeId")
    """Positive numeric ID encoded as a string."""

    outcome_side: str = FieldInfo(alias="outcomeSide")

    action: str

    rationale: str

    market_id: Optional[str] = FieldInfo(alias="marketId", default=None)
    """Positive numeric ID encoded as a string."""

    market_title: Optional[str] = FieldInfo(alias="marketTitle", default=None)

    outcome: Optional[str] = None

    current_price: Optional[float] = FieldInfo(alias="currentPrice", default=None)

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...

    else:
        __pydantic_extra__: Dict[str, object]
