# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["MemberDeleteResponse", "Removed", "Demoted"]


class Demoted(BaseModel):
    success: Literal[True]

    demoted: Literal[True]


class Removed(BaseModel):
    success: Literal[True]

    rejoin_blocked: bool = FieldInfo(alias="rejoinBlocked")


MemberDeleteResponse: TypeAlias = Union[Removed, Demoted]
