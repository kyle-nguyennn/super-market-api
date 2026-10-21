# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DmmTournamentMemberAdd"]


class DmmTournamentMemberAdd(BaseModel):
    profile_id: str = FieldInfo(alias="profileId")

    username: Optional[str] = None
