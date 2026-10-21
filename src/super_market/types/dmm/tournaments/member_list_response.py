# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from ...._models import BaseModel

from .dmm_tournament_member_entry import DmmTournamentMemberEntry

__all__ = ["MemberListResponse"]


class MemberListResponse(BaseModel):
    data: List[DmmTournamentMemberEntry]
