# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["UserGroupCreateResponse"]


class UserGroupCreateResponse(BaseModel):
    user_group_id: str = FieldInfo(alias="userGroupId")

    name: str
