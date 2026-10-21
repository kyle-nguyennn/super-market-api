# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DesignatedMarketMakerSettlementActor"]


class DesignatedMarketMakerSettlementActor(BaseModel):
    type: Literal["platform_admin", "dmm_operator"]

    profile_id: Optional[str] = FieldInfo(alias="profileId", default=None)
    """Null in DMM status responses when the actor is a platform admin."""

    organization_id: Optional[str] = FieldInfo(alias="organizationId", default=None)

    api_key_id: Optional[str] = FieldInfo(alias="apiKeyId", default=None)
    """Redacted from DMM status responses and currently null in DMM queue-command responses."""
