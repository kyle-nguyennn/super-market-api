# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AllRelationshipDirection"]


class AllRelationshipDirection(BaseModel):
    kind: Literal[
        "antecedent_to_consequent",
        "condition_consequence_to_output",
        "inputs_to_output",
        "symmetric",
        "ordered_members",
    ]

    from_exchange_ids: List[str] = FieldInfo(alias="fromExchangeIds")

    to_exchange_ids: List[str] = FieldInfo(alias="toExchangeIds")

    description: str
