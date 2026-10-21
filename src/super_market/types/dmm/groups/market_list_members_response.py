# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from ...._models import BaseModel

from .market_group_member import MarketGroupMember
from .groups_pagination import GroupsPagination

__all__ = ["MarketListMembersResponse"]


class MarketListMembersResponse(BaseModel):
    data: List[MarketGroupMember]

    pagination: GroupsPagination
