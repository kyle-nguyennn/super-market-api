# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TournamentUpdateParams"]


class TournamentUpdateParams(TypedDict, total=False):
    name: str

    description: Optional[str]

    start_date: Annotated[Union[str, datetime], PropertyInfo(alias="startDate", format="iso8601")]
    """New start date. When supplied, it must not be more than 60 seconds in the past (400) — even if it equals the stored value — so omit it unless you are changing it. Changing it is allowed only while the tournament is a draft (409 otherwise)."""

    initial_virtual_balance: Annotated[float, PropertyInfo(alias="initialVirtualBalance")]

    auto_enroll_on_signup: Annotated[bool, PropertyInfo(alias="autoEnrollOnSignup")]
    """Defaults false. Enable only for open, scheduled organization tournaments. Applies to future registrations only; default-tournament selection is independent."""

    currency_name: Annotated[str, PropertyInfo(alias="currencyName")]
    """Display name for the tournament's virtual currency. When the owning organization locks its currency name, this must match that name exactly — any other value is rejected with 400. Omit it to inherit the organization's name."""

    visibility: Literal["private", "open"]
    """`private` requires tournament membership, except for owners and admins of the organization, who can browse every organization tournament and are enrolled on first action. `open` allows organization members to browse and be enrolled on first action."""

    logo_url: Annotated[Optional[str], PropertyInfo(alias="logoUrl")]

    banner_url: Annotated[Optional[str], PropertyInfo(alias="bannerUrl")]

    end_date: Annotated[Union[str, datetime], PropertyInfo(alias="endDate", format="iso8601")]
