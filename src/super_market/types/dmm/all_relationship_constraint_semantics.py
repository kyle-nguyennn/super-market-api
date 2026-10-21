# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AllRelationshipConstraintSemantics"]


class AllRelationshipConstraintSemantics(BaseModel):
    description: str

    price_rule: str = FieldInfo(alias="priceRule")

    bound_semantics: str = FieldInfo(alias="boundSemantics")

    evaluation_endpoint: str = FieldInfo(alias="evaluationEndpoint")
