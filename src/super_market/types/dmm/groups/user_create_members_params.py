# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict
from ...._types import SequenceNotStr

from ...._utils import PropertyInfo

__all__ = ["UserCreateMembersParams"]


class UserCreateMembersParams(TypedDict, total=False):
    profile_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="profileIds")]
    """Profile UUIDs to add."""

    identifiers: SequenceNotStr[str]
    """Emails or usernames, matched case-insensitively. Usernames matching no profile and malformed emails come back in `unmatched`; other emails that are not organization members are invited."""
