# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["UserGroupMemberAddResult"]


class UserGroupMemberAddResult(BaseModel):
    added: int
    """Membership rows created."""

    skipped: int
    """Organization members that were already in the group."""

    invited: List[str]
    """Supplied profile ids or identifiers that are not yet in the organization. Each was emailed an organization invitation and joins the group when they sign in on the organization's site. Every well-formed email identifier that is not already a member is listed here, whether or not an account exists for it."""

    rejected: List[str]
    """Supplied profile ids or usernames belonging to a different organization (one org per profile) or with no email address to invite, and integration-account emails."""

    unmatched: List[str]
    """Username identifiers that matched no profile, and malformed email identifiers."""

    not_found: List[str] = FieldInfo(alias="notFound")
    """Supplied profile ids that reference no profile."""
