# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MarketGroupCreateParams"]


class MarketGroupCreateParams(TypedDict, total=False):
    market_group_id: Required[Annotated[str, PropertyInfo(alias="marketGroupId")]]
