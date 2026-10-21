# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DesignatedMarketMakerTournamentCreate"]


class DesignatedMarketMakerTournamentCreate(BaseModel):
    id: str

    slug: str

    name: str

    description: Optional[str] = None

    invite_code: str = FieldInfo(alias="inviteCode")

    start_date: Optional[str] = FieldInfo(alias="startDate", default=None)

    end_date: Optional[str] = FieldInfo(alias="endDate", default=None)

    initial_balance: float = FieldInfo(alias="initialBalance")

    auto_enroll_on_signup: bool = FieldInfo(alias="autoEnrollOnSignup")
    """Enroll future organization registrations while this tournament is open, scheduled and not archived or ended. Does not backfill participants or open trading early."""

    currency_name: str = FieldInfo(alias="currencyName")

    organization_id: Optional[str] = FieldInfo(alias="organizationId", default=None)

    organization_slug: Optional[str] = FieldInfo(alias="organizationSlug", default=None)

    mode: Literal["cfmm", "p2p"]
    """Active trading mode for the tournament."""

    visibility: Literal["private", "open"]
    """Access model for the tournament."""

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)

    banner_url: Optional[str] = FieldInfo(alias="bannerUrl", default=None)

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)
    """When this tournament was archived, or null while it is active."""

    created_at: str = FieldInfo(alias="createdAt")

    market_group_ids: List[str] = FieldInfo(alias="marketGroupIds")
    """Market groups bound at creation (deduplicated); empty when none were sent."""

    user_group_ids: List[str] = FieldInfo(alias="userGroupIds")
    """User groups bound at creation (deduplicated); empty when none were sent."""
