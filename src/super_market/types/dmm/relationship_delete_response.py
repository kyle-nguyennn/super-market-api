# File generated from our OpenAPI spec by Scalar. See README.md for details.

from ..._models import BaseModel

from .all_relationship import AllRelationship

__all__ = ["RelationshipDeleteResponse"]


class RelationshipDeleteResponse(BaseModel):
    data: AllRelationship
