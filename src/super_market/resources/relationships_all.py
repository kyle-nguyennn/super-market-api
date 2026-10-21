# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional
from typing_extensions import Literal

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.relationships_all_list_relationships_response import RelationshipsAllListRelationshipsResponse
from ..types.dmm.all_relationship_type import AllRelationshipType
from ..types import (
    relationships_all_list_relationships_params,
    relationships_all_list_graph_params,
    relationships_all_list_constraints_params,
)
from ..types.relationships_all_list_graph_response import RelationshipsAllListGraphResponse
from ..types.relationships_all_list_constraints_response import RelationshipsAllListConstraintsResponse

__all__ = ["RelationshipsAllResource", "AsyncRelationshipsAllResource"]


class RelationshipsAllResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RelationshipsAllResourceWithRawResponse:
        return RelationshipsAllResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RelationshipsAllResourceWithStreamingResponse:
        return RelationshipsAllResourceWithStreamingResponse(self)

    def list_relationships(
        self,
        *,
        market_id: str | Omit = omit,
        exchange_id: str | Omit = omit,
        type: AllRelationshipType | Omit = omit,
        depth: int | Omit = omit,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipsAllListRelationshipsResponse:
        """
        Returns active canonical ALL relationships from the trading engine, enriched with market titles and outcome labels. Filter by a market to fetch every relationship touching any exchange in that market, or by one exchange. `marketId` and `exchangeId` are mutually exclusive.

        Args:
            market_id: Return relationships touching any exchange in this accessible market.
            exchange_id: Return relationships touching this accessible exchange.
            type: Query parameter.
            depth: Query parameter.
            limit: Query parameter.
            cursor: Query parameter.
            tournament_id: Evaluate or read relationships in one accessible tournament context. Omit for the API key's default context: the public context for an unbound key, or the organization's default tournament for an organization-bound key.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RelationshipsAllListRelationshipsResponse: Paginated canonical relationships.

        Example:
            ```python
            relationships_all = client.relationships_all.list_relationships(
                depth=1,
                limit=100,
            )
            ```
        """
        return self._get(
            "/relationships",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "market_id": market_id,
                        "exchange_id": exchange_id,
                        "type": type,
                        "depth": depth,
                        "limit": limit,
                        "cursor": cursor,
                        "tournament_id": tournament_id,
                    },
                    relationships_all_list_relationships_params.RelationshipsAllListRelationshipsParams,
                ),
            ),
            cast_to=RelationshipsAllListRelationshipsResponse,
        )

    def list_graph(
        self,
        *,
        market_id: str,
        depth: int | Omit = omit,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipsAllListGraphResponse:
        """
        Traverses the canonical engine-owned ALL graph outward from every exchange in one accessible market and returns deduplicated relationships plus their labeled exchange nodes.

        Args:
            market_id: Accessible market whose exchanges seed the graph traversal.
            depth: Query parameter.
            tournament_id: Evaluate or read relationships in one accessible tournament context. Omit for the API key's default context: the public context for an unbound key, or the organization's default tournament for an organization-bound key.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RelationshipsAllListGraphResponse: Canonical relationship subgraph.

        Example:
            ```python
            relationships_all = client.relationships_all.list_graph(
                market_id="36",
                depth=2,
            )
            ```
        """
        return self._get(
            "/relationships/graph",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"market_id": market_id, "depth": depth, "tournament_id": tournament_id},
                    relationships_all_list_graph_params.RelationshipsAllListGraphParams,
                ),
            ),
            cast_to=RelationshipsAllListGraphResponse,
        )

    def list_constraints(
        self,
        *,
        market_id: str | Omit = omit,
        relationship_id: str | Omit = omit,
        violations_only: Literal["true", "false"] | Omit = omit,
        min_violation: Optional[float] | Omit = omit,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipsAllListConstraintsResponse:
        """
        Returns engine-computed price-constraint evaluations. This endpoint reports satisfied, violated, and unevaluable states; Next.js does not recompute or reinterpret the engine's result.

        Args:
            market_id: Optionally restrict evaluations to relationships touching this accessible market.
            relationship_id: Return the engine evaluation for one accessible canonical relationship.
            violations_only: Query parameter.
            min_violation: Query parameter.
            tournament_id: Evaluate or read relationships in one accessible tournament context. Omit for the API key's default context: the public context for an unbound key, or the organization's default tournament for an organization-bound key.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RelationshipsAllListConstraintsResponse: Current engine-computed evaluations.

        Example:
            ```python
            relationships_all = client.relationships_all.list_constraints(
                violations_only="false",
                min_violation=0.01,
            )
            ```
        """
        return self._get(
            "/relationships/constraints",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "market_id": market_id,
                        "relationship_id": relationship_id,
                        "violations_only": violations_only,
                        "min_violation": min_violation,
                        "tournament_id": tournament_id,
                    },
                    relationships_all_list_constraints_params.RelationshipsAllListConstraintsParams,
                ),
            ),
            cast_to=RelationshipsAllListConstraintsResponse,
        )


class AsyncRelationshipsAllResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRelationshipsAllResourceWithRawResponse:
        return AsyncRelationshipsAllResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRelationshipsAllResourceWithStreamingResponse:
        return AsyncRelationshipsAllResourceWithStreamingResponse(self)

    async def list_relationships(
        self,
        *,
        market_id: str | Omit = omit,
        exchange_id: str | Omit = omit,
        type: AllRelationshipType | Omit = omit,
        depth: int | Omit = omit,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipsAllListRelationshipsResponse:
        """
        Returns active canonical ALL relationships from the trading engine, enriched with market titles and outcome labels. Filter by a market to fetch every relationship touching any exchange in that market, or by one exchange. `marketId` and `exchangeId` are mutually exclusive.

        Args:
            market_id: Return relationships touching any exchange in this accessible market.
            exchange_id: Return relationships touching this accessible exchange.
            type: Query parameter.
            depth: Query parameter.
            limit: Query parameter.
            cursor: Query parameter.
            tournament_id: Evaluate or read relationships in one accessible tournament context. Omit for the API key's default context: the public context for an unbound key, or the organization's default tournament for an organization-bound key.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RelationshipsAllListRelationshipsResponse: Paginated canonical relationships.

        Example:
            ```python
            relationships_all = await client.relationships_all.list_relationships(
                depth=1,
                limit=100,
            )
            ```
        """
        return await self._get(
            "/relationships",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "market_id": market_id,
                        "exchange_id": exchange_id,
                        "type": type,
                        "depth": depth,
                        "limit": limit,
                        "cursor": cursor,
                        "tournament_id": tournament_id,
                    },
                    relationships_all_list_relationships_params.RelationshipsAllListRelationshipsParams,
                ),
            ),
            cast_to=RelationshipsAllListRelationshipsResponse,
        )

    async def list_graph(
        self,
        *,
        market_id: str,
        depth: int | Omit = omit,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipsAllListGraphResponse:
        """
        Traverses the canonical engine-owned ALL graph outward from every exchange in one accessible market and returns deduplicated relationships plus their labeled exchange nodes.

        Args:
            market_id: Accessible market whose exchanges seed the graph traversal.
            depth: Query parameter.
            tournament_id: Evaluate or read relationships in one accessible tournament context. Omit for the API key's default context: the public context for an unbound key, or the organization's default tournament for an organization-bound key.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RelationshipsAllListGraphResponse: Canonical relationship subgraph.

        Example:
            ```python
            relationships_all = await client.relationships_all.list_graph(
                market_id="36",
                depth=2,
            )
            ```
        """
        return await self._get(
            "/relationships/graph",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"market_id": market_id, "depth": depth, "tournament_id": tournament_id},
                    relationships_all_list_graph_params.RelationshipsAllListGraphParams,
                ),
            ),
            cast_to=RelationshipsAllListGraphResponse,
        )

    async def list_constraints(
        self,
        *,
        market_id: str | Omit = omit,
        relationship_id: str | Omit = omit,
        violations_only: Literal["true", "false"] | Omit = omit,
        min_violation: Optional[float] | Omit = omit,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipsAllListConstraintsResponse:
        """
        Returns engine-computed price-constraint evaluations. This endpoint reports satisfied, violated, and unevaluable states; Next.js does not recompute or reinterpret the engine's result.

        Args:
            market_id: Optionally restrict evaluations to relationships touching this accessible market.
            relationship_id: Return the engine evaluation for one accessible canonical relationship.
            violations_only: Query parameter.
            min_violation: Query parameter.
            tournament_id: Evaluate or read relationships in one accessible tournament context. Omit for the API key's default context: the public context for an unbound key, or the organization's default tournament for an organization-bound key.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RelationshipsAllListConstraintsResponse: Current engine-computed evaluations.

        Example:
            ```python
            relationships_all = await client.relationships_all.list_constraints(
                violations_only="false",
                min_violation=0.01,
            )
            ```
        """
        return await self._get(
            "/relationships/constraints",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "market_id": market_id,
                        "relationship_id": relationship_id,
                        "violations_only": violations_only,
                        "min_violation": min_violation,
                        "tournament_id": tournament_id,
                    },
                    relationships_all_list_constraints_params.RelationshipsAllListConstraintsParams,
                ),
            ),
            cast_to=RelationshipsAllListConstraintsResponse,
        )


class RelationshipsAllResourceWithRawResponse:
    def __init__(self, relationships_all: RelationshipsAllResource) -> None:
        self._relationships_all = relationships_all

        self.list_relationships = to_raw_response_wrapper(
            relationships_all.list_relationships,
        )
        self.list_graph = to_raw_response_wrapper(
            relationships_all.list_graph,
        )
        self.list_constraints = to_raw_response_wrapper(
            relationships_all.list_constraints,
        )


class AsyncRelationshipsAllResourceWithRawResponse:
    def __init__(self, relationships_all: AsyncRelationshipsAllResource) -> None:
        self._relationships_all = relationships_all

        self.list_relationships = async_to_raw_response_wrapper(
            relationships_all.list_relationships,
        )
        self.list_graph = async_to_raw_response_wrapper(
            relationships_all.list_graph,
        )
        self.list_constraints = async_to_raw_response_wrapper(
            relationships_all.list_constraints,
        )


class RelationshipsAllResourceWithStreamingResponse:
    def __init__(self, relationships_all: RelationshipsAllResource) -> None:
        self._relationships_all = relationships_all

        self.list_relationships = to_streamed_response_wrapper(
            relationships_all.list_relationships,
        )
        self.list_graph = to_streamed_response_wrapper(
            relationships_all.list_graph,
        )
        self.list_constraints = to_streamed_response_wrapper(
            relationships_all.list_constraints,
        )


class AsyncRelationshipsAllResourceWithStreamingResponse:
    def __init__(self, relationships_all: AsyncRelationshipsAllResource) -> None:
        self._relationships_all = relationships_all

        self.list_relationships = async_to_streamed_response_wrapper(
            relationships_all.list_relationships,
        )
        self.list_graph = async_to_streamed_response_wrapper(
            relationships_all.list_graph,
        )
        self.list_constraints = async_to_streamed_response_wrapper(
            relationships_all.list_constraints,
        )
