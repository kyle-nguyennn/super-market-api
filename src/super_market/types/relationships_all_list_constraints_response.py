# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .all_relationship_constraint import AllRelationshipConstraint

__all__ = ["RelationshipsAllListConstraintsResponse"]


class RelationshipsAllListConstraintsResponse(BaseModel):
    data: List[AllRelationshipConstraint]

    violations_count: int = FieldInfo(alias="violationsCount")

    computed_at: datetime = FieldInfo(alias="computedAt")
