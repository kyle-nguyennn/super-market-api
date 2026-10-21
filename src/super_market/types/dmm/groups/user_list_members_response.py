# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from ...._models import BaseModel

from .user_group_member import UserGroupMember
from .groups_pagination import GroupsPagination

__all__ = ["UserListMembersResponse"]


class UserListMembersResponse(BaseModel):
    data: List[UserGroupMember]

    pagination: GroupsPagination
