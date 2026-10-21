# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["MarketDeleteResponse", "Removed", "Demoted"]


class Demoted(BaseModel):
    success: Literal[True]

    demoted: Literal[True]


class Removed(BaseModel):
    success: Literal[True]

    exchanges_cleared: int = FieldInfo(alias="exchangesCleared")

    paid_out_holdings: int = FieldInfo(alias="paidOutHoldings")


MarketDeleteResponse: TypeAlias = Union[Removed, Demoted]
