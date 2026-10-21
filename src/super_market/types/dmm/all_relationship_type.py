# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["AllRelationshipType"]

AllRelationshipType: TypeAlias = Literal[
    "monotonic",
    "complementary",
    "mutually_exclusive",
    "implication",
    "boolean_and",
    "boolean_or",
    "boolean_not",
    "conditional_if",
    "boolean_expression",
]
