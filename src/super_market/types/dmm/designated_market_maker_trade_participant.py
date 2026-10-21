# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DesignatedMarketMakerTradeParticipant"]


class DesignatedMarketMakerTradeParticipant(BaseModel):
    profile_id: str = FieldInfo(alias="profileId")

    username: Optional[str] = None

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    email: Optional[str] = None
