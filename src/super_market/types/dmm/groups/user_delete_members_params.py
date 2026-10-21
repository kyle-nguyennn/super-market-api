# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict
from ...._types import SequenceNotStr

from ...._utils import PropertyInfo

__all__ = ["UserDeleteMembersParams"]


class UserDeleteMembersParams(TypedDict, total=False):
    profile_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="profileIds")]]
