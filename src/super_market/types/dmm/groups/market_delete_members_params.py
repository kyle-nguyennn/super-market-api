# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Union
from typing_extensions import Annotated, Required, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MarketDeleteMembersParams"]


class MarketDeleteMembersParams(TypedDict, total=False):
    market_ids: Required[Annotated[Iterable[Union[str, float]], PropertyInfo(alias="marketIds")]]
    """Market ids, as strings or numbers. Numbers must be safe integers (below 2^53); a larger id is rounded by JSON parsing before it reaches us, so send it as a string. Ids that cannot be parsed are reported in notFound."""
