# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from .._models import BaseModel

from .dmm.all_relationship import AllRelationship
from .all_relationship_node import AllRelationshipNode

__all__ = ["RelationshipsAllListGraphResponse"]


class RelationshipsAllListGraphResponse(BaseModel):
    relationships: List[AllRelationship]

    nodes: List[AllRelationshipNode]
