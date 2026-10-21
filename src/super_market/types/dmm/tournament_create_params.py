# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, Required, TypedDict
from ..._types import SequenceNotStr

from ..._utils import PropertyInfo

__all__ = ["TournamentCreateParams"]


class TournamentCreateParams(TypedDict, total=False):
    name: Required[str]

    description: Optional[str]

    start_date: Annotated[Union[str, datetime], PropertyInfo(alias="startDate", format="iso8601")]
    """Tournament start. Defaults to the time of the request when omitted. When supplied, it must not be more than 60 seconds in the past (400), and `endDate` must be after it (400)."""

    end_date: Required[Annotated[Union[str, datetime], PropertyInfo(alias="endDate", format="iso8601")]]

    initial_virtual_balance: Annotated[float, PropertyInfo(alias="initialVirtualBalance")]

    auto_enroll_on_signup: Annotated[bool, PropertyInfo(alias="autoEnrollOnSignup")]
    """Defaults false. Enable only for open, scheduled organization tournaments. Applies to future registrations only; default-tournament selection is independent."""

    currency_name: Annotated[str, PropertyInfo(alias="currencyName")]
    """Display name for the tournament's virtual currency. When the owning organization locks its currency name, this must match that name exactly — any other value is rejected with 400. Omit it to inherit the organization's name."""

    organization_slug: Required[Annotated[str, PropertyInfo(alias="organizationSlug")]]
    """Slug of the organization that will own this tournament. Org slugs are immutable."""

    mode: Literal["cfmm", "p2p"]
    """Trading mode. `p2p` = peer-to-peer orderbook seeded with maker quotes (default). `cfmm` = constant-function market maker (automatic price curve)."""

    visibility: Literal["private", "open"]
    """`private` requires tournament membership, except for owners and admins of the organization, who can browse every organization tournament and are enrolled on first action. `open` allows organization members to browse and be enrolled on first action."""

    logo_url: Annotated[Optional[str], PropertyInfo(alias="logoUrl")]

    banner_url: Annotated[Optional[str], PropertyInfo(alias="bannerUrl")]

    market_group_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="marketGroupIds")]
    """Existing market groups of the tournament's organization to bind at creation (duplicates are ignored). Their markets are attached asynchronously, as with POST /dmm/tournaments/{slug}/market-groups. An unknown id returns 404; a group from another organization, or one containing a market already attached to another organization's tournament, returns 400."""

    user_group_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="userGroupIds")]
    """Existing user groups of the tournament's organization to bind at creation (duplicates are ignored). Their members are enrolled asynchronously, as with POST /dmm/tournaments/{slug}/user-groups. An unknown id returns 404; a group from another organization returns 400."""
