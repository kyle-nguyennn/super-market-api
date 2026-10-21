# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["UserGroupMemberRemoveResult"]


class UserGroupMemberRemoveResult(BaseModel):
    removed: int

    removed_profile_ids: List[str] = FieldInfo(alias="removedProfileIds")

    not_found: List[str] = FieldInfo(alias="notFound")
    """Requested ids that held no membership row in this group."""
