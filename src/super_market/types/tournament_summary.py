# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TournamentSummary"]


class TournamentSummary(BaseModel):
    id: str

    slug: str

    name: str

    description: Optional[str] = None

    status: str

    start_date: Optional[str] = FieldInfo(alias="startDate", default=None)

    end_date: Optional[str] = FieldInfo(alias="endDate", default=None)

    initial_balance: float = FieldInfo(alias="initialBalance")

    currency_name: str = FieldInfo(alias="currencyName")

    my_balance: float = FieldInfo(alias="myBalance")
    """Caller's cash balance in this tournament, rounded to 2 decimals; the seed balance before their first trade. Resting orders do not reserve any of it: cash moves only when orders fill. See `POST /orders` for how buys are admitted against it."""

    joined_at: Optional[str] = FieldInfo(alias="joinedAt", default=None)

    is_pending_enrolment: bool = FieldInfo(alias="isPendingEnrolment")
    """True when the caller can access an open tournament, or a private tournament of an organization they own or administer, but has not yet been enrolled."""
