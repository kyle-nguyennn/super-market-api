# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from .all_relationship_type import AllRelationshipType
from .all_relationship_direction import AllRelationshipDirection
from .all_relationship_constraint_semantics import AllRelationshipConstraintSemantics

__all__ = ["AllRelationship"]


class AllRelationship(BaseModel):
    id: str

    type: AllRelationshipType

    source: Literal["auto_derived", "admin_tagged"]

    status: Literal["active", "stale", "disabled", "settled", "deleted"]

    label: Optional[str] = None

    reason: Optional[str] = None

    is_exhaustive: bool = FieldInfo(alias="isExhaustive")
    """Whether the relationship members exhaust every valid outcome in their logical component."""

    expression: Optional["AllRelationshipExpression"] = None
    """Canonical AST for `boolean_expression`; null for relationship types without an expression payload."""

    nodes: List["AllRelationshipNode"]

    direction: AllRelationshipDirection

    constraint: AllRelationshipConstraintSemantics

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    version: int


from ..all_relationship_node import AllRelationshipNode
from .all_relationship_expression import AllRelationshipExpression
