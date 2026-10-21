# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from ...._models import BaseModel

from .group import Group
from .groups_pagination import GroupsPagination

__all__ = ["MarketListResponse"]


class MarketListResponse(BaseModel):
    data: List[Group]

    pagination: GroupsPagination
