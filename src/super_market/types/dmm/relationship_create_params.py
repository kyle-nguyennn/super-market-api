# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Union
from typing_extensions import Annotated, Literal, Required, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "RelationshipCreateParams",
    "Variant",
    "VariantAntecedent",
    "VariantConsequent",
    "Variant2",
    "Variant2Exchange",
    "Variant3",
    "Variant3Exchange",
]


class Variant3Exchange(TypedDict, total=False):
    market_id: Required[Annotated[str, PropertyInfo(alias="marketId")]]

    exchange_id: Required[Annotated[str, PropertyInfo(alias="exchangeId")]]


class Variant3(TypedDict, total=False):
    organization_slug: Annotated[str, PropertyInfo(alias="organizationSlug")]
    """Required for an unbound platform-admin key; omitted for an organization-bound key."""

    label: str

    reason: str

    idempotency_key: Annotated[str, PropertyInfo(alias="idempotencyKey")]
    """Optional in this staged release. Reuse the same key only to retry the same resolved relationship mutation; a completed retry replays and reuse with a different payload returns 409. Omitting the key creates a fresh operation identity for every request."""

    type: Required[Literal["MutuallyExclusive"]]

    exchanges: Required[Iterable[Variant3Exchange]]


class Variant2Exchange(TypedDict, total=False):
    market_id: Required[Annotated[str, PropertyInfo(alias="marketId")]]

    exchange_id: Required[Annotated[str, PropertyInfo(alias="exchangeId")]]


class Variant2(TypedDict, total=False):
    organization_slug: Annotated[str, PropertyInfo(alias="organizationSlug")]
    """Required for an unbound platform-admin key; omitted for an organization-bound key."""

    label: str

    reason: str

    idempotency_key: Annotated[str, PropertyInfo(alias="idempotencyKey")]
    """Optional in this staged release. Reuse the same key only to retry the same resolved relationship mutation; a completed retry replays and reuse with a different payload returns 409. Omitting the key creates a fresh operation identity for every request."""

    type: Required[Literal["Complementary"]]

    exchanges: Required[Iterable[Variant2Exchange]]


class VariantConsequent(TypedDict, total=False):
    market_id: Required[Annotated[str, PropertyInfo(alias="marketId")]]

    exchange_id: Required[Annotated[str, PropertyInfo(alias="exchangeId")]]


class VariantAntecedent(TypedDict, total=False):
    market_id: Required[Annotated[str, PropertyInfo(alias="marketId")]]

    exchange_id: Required[Annotated[str, PropertyInfo(alias="exchangeId")]]


class Variant(TypedDict, total=False):
    organization_slug: Annotated[str, PropertyInfo(alias="organizationSlug")]
    """Required for an unbound platform-admin key; omitted for an organization-bound key."""

    label: str

    reason: str

    idempotency_key: Annotated[str, PropertyInfo(alias="idempotencyKey")]
    """Optional in this staged release. Reuse the same key only to retry the same resolved relationship mutation; a completed retry replays and reuse with a different payload returns 409. Omitting the key creates a fresh operation identity for every request."""

    type: Required[Literal["Implication"]]

    antecedent: Required[VariantAntecedent]

    consequent: Required[VariantConsequent]


RelationshipCreateParams: TypeAlias = Union[Variant, Variant2, Variant3]
