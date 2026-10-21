# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional, Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "AllRelationshipExpression",
    "AllRelationshipExpression2",
    "AllRelationshipExpression3",
    "AllRelationshipExpression4",
    "AllRelationshipExpression5",
    "AllRelationshipExpression6",
]


class AllRelationshipExpression6(BaseModel):
    kind: Literal["cond"]

    condition: Optional[
        Union[
            AllRelationshipExpression2,
            AllRelationshipExpression3,
            AllRelationshipExpression4,
            AllRelationshipExpression5,
            AllRelationshipExpression6,
        ]
    ] = None
    """Canonical AST for `boolean_expression`; null for relationship types without an expression payload."""

    consequence: Optional[
        Union[
            AllRelationshipExpression2,
            AllRelationshipExpression3,
            AllRelationshipExpression4,
            AllRelationshipExpression5,
            AllRelationshipExpression6,
        ]
    ] = None
    """Canonical AST for `boolean_expression`; null for relationship types without an expression payload."""


class AllRelationshipExpression5(BaseModel):
    kind: Literal["not"]

    child: Optional[
        Union[
            AllRelationshipExpression2,
            AllRelationshipExpression3,
            AllRelationshipExpression4,
            AllRelationshipExpression5,
            AllRelationshipExpression6,
        ]
    ] = None
    """Canonical AST for `boolean_expression`; null for relationship types without an expression payload."""


class AllRelationshipExpression4(BaseModel):
    kind: Literal["or"]

    children: List[
        Optional[
            Union[
                AllRelationshipExpression2,
                AllRelationshipExpression3,
                AllRelationshipExpression4,
                AllRelationshipExpression5,
                AllRelationshipExpression6,
            ]
        ]
    ]


class AllRelationshipExpression3(BaseModel):
    kind: Literal["and"]

    children: List[
        Optional[
            Union[
                AllRelationshipExpression2,
                AllRelationshipExpression3,
                AllRelationshipExpression4,
                AllRelationshipExpression5,
                AllRelationshipExpression6,
            ]
        ]
    ]


class AllRelationshipExpression2(BaseModel):
    kind: Literal["leaf"]

    exchangeId: int


AllRelationshipExpression: TypeAlias = Optional[
    Union[
        AllRelationshipExpression2,
        AllRelationshipExpression3,
        AllRelationshipExpression4,
        AllRelationshipExpression5,
        AllRelationshipExpression6,
    ]
]
