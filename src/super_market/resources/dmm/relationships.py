# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable, Union
from typing_extensions import Literal, overload

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform, strip_not_given, required_args
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.dmm.relationship_create_response import RelationshipCreateResponse
from ...types.dmm import relationship_create_params, relationship_create_reconcile_params
from ...types.dmm.relationship_delete_response import RelationshipDeleteResponse
from ...types.dmm.designated_market_maker_relationship_operation_status import (
    DesignatedMarketMakerRelationshipOperationStatus,
)
from ...types.dmm.relationship_create_reconcile_response import RelationshipCreateReconcileResponse

__all__ = ["RelationshipsResource", "AsyncRelationshipsResource"]


class RelationshipsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RelationshipsResourceWithRawResponse:
        return RelationshipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RelationshipsResourceWithStreamingResponse:
        return RelationshipsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        organization_slug: str | Omit = omit,
        label: str | Omit = omit,
        reason: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        type: Literal["Implication"],
        antecedent: relationship_create_params.VariantAntecedent,
        consequent: relationship_create_params.VariantConsequent,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipCreateResponse: ...

    @overload
    def create(
        self,
        *,
        organization_slug: str | Omit = omit,
        label: str | Omit = omit,
        reason: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        type: Literal["Complementary"],
        exchanges: Iterable[relationship_create_params.Variant2Exchange],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipCreateResponse: ...

    @overload
    def create(
        self,
        *,
        organization_slug: str | Omit = omit,
        label: str | Omit = omit,
        reason: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        type: Literal["MutuallyExclusive"],
        exchanges: Iterable[relationship_create_params.Variant3Exchange],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipCreateResponse: ...

    @required_args(["antecedent", "consequent", "type"], ["exchanges", "type"])
    def create(
        self,
        *,
        organization_slug: str | Omit = omit,
        label: str | Omit = omit,
        reason: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        type: Union[Literal["Implication"], Literal["Complementary"], Literal["MutuallyExclusive"]],
        antecedent: relationship_create_params.VariantAntecedent | Omit = omit,
        consequent: relationship_create_params.VariantConsequent | Omit = omit,
        exchanges: Union[
            Iterable[relationship_create_params.Variant2Exchange], Iterable[relationship_create_params.Variant3Exchange]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipCreateResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Creates and immediately activates one manual canonical ALL relationship. Callers choose markets and outcomes; the API translates them to engine exchanges. Every selected market must belong exclusively to the API key's organization. The optional body `idempotencyKey` identifies the logical mutation for safe retries; omission gives each request a fresh operation identity. A transport-ambiguous outcome returns 202 with an operation ID to poll. Requires an API key with `admin` scope and an organization owner/admin or platform-admin principal.

        The trading engine evaluates at most 12 free variables per connected relationship component: every distinct exchange across the relationships that share exchanges with this one, excluding exchanges a Boolean relationship produces as its output. The limit applies to the whole component the new relationship would join or merge, not to the inputs of this request; a relationship that would push its component past 12 free variables is rejected with 400.

        Args:
            organization_slug: Required for an unbound platform-admin key; omitted for an organization-bound key.
            label: Body parameter.
            reason: Body parameter.
            idempotency_key: Optional in this staged release. Reuse the same key only to retry the same resolved relationship mutation; a completed retry replays and reuse with a different payload returns 409. Omitting the key creates a fresh operation identity for every request.
            type: Body parameter.
            antecedent: Body parameter.
            consequent: Body parameter.
            exchanges: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RelationshipCreateResponse: Relationship established and active.

        Example:
            ```python
            relationship = client.dmm.relationships.create(
                type="Implication",
                antecedent={"market_id": "26", "exchange_id": "36"},
                consequent={"market_id": "26", "exchange_id": "36"},
            )
            ```
        """
        return self._post(
            "/dmm/relationships",
            body=maybe_transform(
                {
                    "organization_slug": organization_slug,
                    "label": label,
                    "reason": reason,
                    "idempotency_key": idempotency_key,
                    "type": type,
                    "antecedent": antecedent,
                    "consequent": consequent,
                    "exchanges": exchanges,
                },
                relationship_create_params.RelationshipCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RelationshipCreateResponse,
        )

    def delete(
        self,
        relationship_id: str,
        *,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipDeleteResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Disables a canonical ALL relationship through the trading engine and never hard-deletes it. The optional `Idempotency-Key` header identifies the logical mutation for safe retries; omission gives each request a fresh operation identity. A transport-ambiguous outcome returns 202 with an operation ID to poll. Organization-bound keys may deactivate a relationship only when every node exchange belongs exclusively to their organization; platform administrators are not organization-scoped. The engine may reject a status change that would make outstanding collateral unsafe. Requires an API key with `admin` scope and an organization owner/admin or platform-admin principal.

        Args:
            relationship_id: Canonical engine relationship UUID.
            idempotency_key: Optional in this staged release. Reuse the same key only to retry disabling the same relationship; a completed retry replays and reuse for a different relationship returns 409. Omitting the header creates a fresh operation identity for every request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RelationshipDeleteResponse: Relationship disabled.

        Example:
            ```python
            relationship = client.dmm.relationships.delete(
                relationship_id="550e8400-e29b-41d4-a716-446655440000",
            )
            ```
        """
        if relationship_id is None or (isinstance(relationship_id, str) and not relationship_id):
            raise ValueError(f"Expected a non-empty value for `relationship_id` but received {relationship_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._delete(
            path_template("/dmm/relationships/{relationshipId}", **{"relationshipId": relationship_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RelationshipDeleteResponse,
        )

    def retrieve_operations(
        self,
        operation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerRelationshipOperationStatus:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Returns durable status for a relationship create or disable operation after a 202 response. Poll until `status` is `succeeded` or `failed`. An organization key can poll only its organization's operations; an operation owned by another organization returns the same 404 as an unknown operation ID. A platform key can poll any organization-owned operation, including those it created on an organization's behalf, plus its own.

        Args:
            operation_id: Operation UUID returned by a 202 relationship mutation response.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerRelationshipOperationStatus: Current durable operation status.

        Example:
            ```python
            relationship = client.dmm.relationships.retrieve_operations(
                operation_id="550e8400-e29b-41d4-a716-446655440000",
            )
            ```
        """
        if operation_id is None or (isinstance(operation_id, str) and not operation_id):
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return self._get(
            path_template("/dmm/relationships/operations/{operationId}", **{"operationId": operation_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignatedMarketMakerRelationshipOperationStatus,
        )

    def create_reconcile(
        self,
        *,
        organization_slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipCreateReconcileResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Derives and reconciles only relationships whose exchanges belong exclusively to one organization. Relationships owned by another organization or spanning organization boundaries are never mutated. Requires an API key with `admin` scope.

        Engine synchronization runs asynchronously and withholds any derived relationship whose connected component would exceed the engine's 12-free-variable limit (the superseded definition it would replace stays in place). Those skips are recorded in server diagnostics, not in this response.

        Args:
            organization_slug: Required for an unbound platform-admin key.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RelationshipCreateReconcileResponse: Diagnostics are computed synchronously while engine synchronization is accepted for asynchronous (debounced) processing.

        Example:
            ```python
            relationship = client.dmm.relationships.create_reconcile()
            ```
        """
        return self._post(
            "/dmm/relationships/reconcile",
            body=maybe_transform(
                {"organization_slug": organization_slug},
                relationship_create_reconcile_params.RelationshipCreateReconcileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RelationshipCreateReconcileResponse,
        )


class AsyncRelationshipsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRelationshipsResourceWithRawResponse:
        return AsyncRelationshipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRelationshipsResourceWithStreamingResponse:
        return AsyncRelationshipsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        organization_slug: str | Omit = omit,
        label: str | Omit = omit,
        reason: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        type: Literal["Implication"],
        antecedent: relationship_create_params.VariantAntecedent,
        consequent: relationship_create_params.VariantConsequent,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipCreateResponse: ...

    @overload
    async def create(
        self,
        *,
        organization_slug: str | Omit = omit,
        label: str | Omit = omit,
        reason: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        type: Literal["Complementary"],
        exchanges: Iterable[relationship_create_params.Variant2Exchange],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipCreateResponse: ...

    @overload
    async def create(
        self,
        *,
        organization_slug: str | Omit = omit,
        label: str | Omit = omit,
        reason: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        type: Literal["MutuallyExclusive"],
        exchanges: Iterable[relationship_create_params.Variant3Exchange],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipCreateResponse: ...

    @required_args(["antecedent", "consequent", "type"], ["exchanges", "type"])
    async def create(
        self,
        *,
        organization_slug: str | Omit = omit,
        label: str | Omit = omit,
        reason: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        type: Union[Literal["Implication"], Literal["Complementary"], Literal["MutuallyExclusive"]],
        antecedent: relationship_create_params.VariantAntecedent | Omit = omit,
        consequent: relationship_create_params.VariantConsequent | Omit = omit,
        exchanges: Union[
            Iterable[relationship_create_params.Variant2Exchange], Iterable[relationship_create_params.Variant3Exchange]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipCreateResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Creates and immediately activates one manual canonical ALL relationship. Callers choose markets and outcomes; the API translates them to engine exchanges. Every selected market must belong exclusively to the API key's organization. The optional body `idempotencyKey` identifies the logical mutation for safe retries; omission gives each request a fresh operation identity. A transport-ambiguous outcome returns 202 with an operation ID to poll. Requires an API key with `admin` scope and an organization owner/admin or platform-admin principal.

        The trading engine evaluates at most 12 free variables per connected relationship component: every distinct exchange across the relationships that share exchanges with this one, excluding exchanges a Boolean relationship produces as its output. The limit applies to the whole component the new relationship would join or merge, not to the inputs of this request; a relationship that would push its component past 12 free variables is rejected with 400.

        Args:
            organization_slug: Required for an unbound platform-admin key; omitted for an organization-bound key.
            label: Body parameter.
            reason: Body parameter.
            idempotency_key: Optional in this staged release. Reuse the same key only to retry the same resolved relationship mutation; a completed retry replays and reuse with a different payload returns 409. Omitting the key creates a fresh operation identity for every request.
            type: Body parameter.
            antecedent: Body parameter.
            consequent: Body parameter.
            exchanges: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RelationshipCreateResponse: Relationship established and active.

        Example:
            ```python
            relationship = await client.dmm.relationships.create(
                type="Implication",
                antecedent={"market_id": "26", "exchange_id": "36"},
                consequent={"market_id": "26", "exchange_id": "36"},
            )
            ```
        """
        return await self._post(
            "/dmm/relationships",
            body=await async_maybe_transform(
                {
                    "organization_slug": organization_slug,
                    "label": label,
                    "reason": reason,
                    "idempotency_key": idempotency_key,
                    "type": type,
                    "antecedent": antecedent,
                    "consequent": consequent,
                    "exchanges": exchanges,
                },
                relationship_create_params.RelationshipCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RelationshipCreateResponse,
        )

    async def delete(
        self,
        relationship_id: str,
        *,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipDeleteResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Disables a canonical ALL relationship through the trading engine and never hard-deletes it. The optional `Idempotency-Key` header identifies the logical mutation for safe retries; omission gives each request a fresh operation identity. A transport-ambiguous outcome returns 202 with an operation ID to poll. Organization-bound keys may deactivate a relationship only when every node exchange belongs exclusively to their organization; platform administrators are not organization-scoped. The engine may reject a status change that would make outstanding collateral unsafe. Requires an API key with `admin` scope and an organization owner/admin or platform-admin principal.

        Args:
            relationship_id: Canonical engine relationship UUID.
            idempotency_key: Optional in this staged release. Reuse the same key only to retry disabling the same relationship; a completed retry replays and reuse for a different relationship returns 409. Omitting the header creates a fresh operation identity for every request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RelationshipDeleteResponse: Relationship disabled.

        Example:
            ```python
            relationship = await client.dmm.relationships.delete(
                relationship_id="550e8400-e29b-41d4-a716-446655440000",
            )
            ```
        """
        if relationship_id is None or (isinstance(relationship_id, str) and not relationship_id):
            raise ValueError(f"Expected a non-empty value for `relationship_id` but received {relationship_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._delete(
            path_template("/dmm/relationships/{relationshipId}", **{"relationshipId": relationship_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RelationshipDeleteResponse,
        )

    async def retrieve_operations(
        self,
        operation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerRelationshipOperationStatus:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Returns durable status for a relationship create or disable operation after a 202 response. Poll until `status` is `succeeded` or `failed`. An organization key can poll only its organization's operations; an operation owned by another organization returns the same 404 as an unknown operation ID. A platform key can poll any organization-owned operation, including those it created on an organization's behalf, plus its own.

        Args:
            operation_id: Operation UUID returned by a 202 relationship mutation response.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerRelationshipOperationStatus: Current durable operation status.

        Example:
            ```python
            relationship = await client.dmm.relationships.retrieve_operations(
                operation_id="550e8400-e29b-41d4-a716-446655440000",
            )
            ```
        """
        if operation_id is None or (isinstance(operation_id, str) and not operation_id):
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return await self._get(
            path_template("/dmm/relationships/operations/{operationId}", **{"operationId": operation_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignatedMarketMakerRelationshipOperationStatus,
        )

    async def create_reconcile(
        self,
        *,
        organization_slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipCreateReconcileResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Derives and reconciles only relationships whose exchanges belong exclusively to one organization. Relationships owned by another organization or spanning organization boundaries are never mutated. Requires an API key with `admin` scope.

        Engine synchronization runs asynchronously and withholds any derived relationship whose connected component would exceed the engine's 12-free-variable limit (the superseded definition it would replace stays in place). Those skips are recorded in server diagnostics, not in this response.

        Args:
            organization_slug: Required for an unbound platform-admin key.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RelationshipCreateReconcileResponse: Diagnostics are computed synchronously while engine synchronization is accepted for asynchronous (debounced) processing.

        Example:
            ```python
            relationship = await client.dmm.relationships.create_reconcile()
            ```
        """
        return await self._post(
            "/dmm/relationships/reconcile",
            body=await async_maybe_transform(
                {"organization_slug": organization_slug},
                relationship_create_reconcile_params.RelationshipCreateReconcileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RelationshipCreateReconcileResponse,
        )


class RelationshipsResourceWithRawResponse:
    def __init__(self, relationships: RelationshipsResource) -> None:
        self._relationships = relationships

        self.create = to_raw_response_wrapper(
            relationships.create,
        )
        self.delete = to_raw_response_wrapper(
            relationships.delete,
        )
        self.retrieve_operations = to_raw_response_wrapper(
            relationships.retrieve_operations,
        )
        self.create_reconcile = to_raw_response_wrapper(
            relationships.create_reconcile,
        )


class AsyncRelationshipsResourceWithRawResponse:
    def __init__(self, relationships: AsyncRelationshipsResource) -> None:
        self._relationships = relationships

        self.create = async_to_raw_response_wrapper(
            relationships.create,
        )
        self.delete = async_to_raw_response_wrapper(
            relationships.delete,
        )
        self.retrieve_operations = async_to_raw_response_wrapper(
            relationships.retrieve_operations,
        )
        self.create_reconcile = async_to_raw_response_wrapper(
            relationships.create_reconcile,
        )


class RelationshipsResourceWithStreamingResponse:
    def __init__(self, relationships: RelationshipsResource) -> None:
        self._relationships = relationships

        self.create = to_streamed_response_wrapper(
            relationships.create,
        )
        self.delete = to_streamed_response_wrapper(
            relationships.delete,
        )
        self.retrieve_operations = to_streamed_response_wrapper(
            relationships.retrieve_operations,
        )
        self.create_reconcile = to_streamed_response_wrapper(
            relationships.create_reconcile,
        )


class AsyncRelationshipsResourceWithStreamingResponse:
    def __init__(self, relationships: AsyncRelationshipsResource) -> None:
        self._relationships = relationships

        self.create = async_to_streamed_response_wrapper(
            relationships.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            relationships.delete,
        )
        self.retrieve_operations = async_to_streamed_response_wrapper(
            relationships.retrieve_operations,
        )
        self.create_reconcile = async_to_streamed_response_wrapper(
            relationships.create_reconcile,
        )
