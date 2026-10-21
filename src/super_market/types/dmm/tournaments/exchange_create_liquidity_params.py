# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Union
from typing_extensions import Annotated, Literal, Required, TypeAlias, TypedDict

from ...._utils import PropertyInfo

from .designated_market_maker_liquidity_level_param import DesignatedMarketMakerLiquidityLevelParam

__all__ = ["ExchangeCreateLiquidityParams", "Variant", "Variant2"]


class Variant2(TypedDict, total=False):
    mode: Required[Literal["replace"]]

    operation_key: Required[Annotated[str, PropertyInfo(alias="operationKey")]]
    """Required client-supplied idempotency key for replace retries on both engine and legacy paths. An identical payload replays the stored status and body of the completed request, including a stored 400, 404, or 409 error; after fixing the cause, retry with a new key. A changed payload returns 409. Replace and append use independent key namespaces, so the same key may be used once for each mode."""

    bids: Iterable[DesignatedMarketMakerLiquidityLevelParam]
    """Outcome-perspective bid levels. Prices must be unique. Executed from highest price to lowest price."""

    asks: Iterable[DesignatedMarketMakerLiquidityLevelParam]
    """Outcome-perspective ask levels. Prices must be unique. Executed from lowest price to highest price."""


class Variant(TypedDict, total=False):
    mode: Required[Literal["append"]]

    operation_key: Required[Annotated[str, PropertyInfo(alias="operationKey")]]
    """Required client-supplied idempotency key for append retries on both engine and legacy paths. An identical payload replays the stored status and body of the completed request, including a stored 400, 404, or 409 error; after fixing the cause, retry with a new key. A changed payload returns 409. Append and replace use independent key namespaces, so the same key may be used once for each mode."""

    bids: Iterable[DesignatedMarketMakerLiquidityLevelParam]
    """Outcome-perspective bid levels. Prices must be unique. Executed from highest price to lowest price."""

    asks: Iterable[DesignatedMarketMakerLiquidityLevelParam]
    """Outcome-perspective ask levels. Prices must be unique. Executed from lowest price to highest price."""


ExchangeCreateLiquidityParams: TypeAlias = Union[Variant, Variant2]
