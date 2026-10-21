# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing_extensions import Literal

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.tournaments.market_list_response import MarketListResponse
from ...types.tournaments import market_list_params
from ...types.tournaments.market_retrieve_response import MarketRetrieveResponse

__all__ = ["MarketsResource", "AsyncMarketsResource"]


class MarketsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MarketsResourceWithRawResponse:
        return MarketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketsResourceWithStreamingResponse:
        return MarketsResourceWithStreamingResponse(self)

    def list(
        self,
        slug: str,
        *,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        search: str | Omit = omit,
        status: Literal["open", "closed", "settled", "resolved", "any"] | Omit = omit,
        market_group_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketListResponse:
        """
        Equivalent explicit tournament-scoped view of `GET /markets?tournamentId={id}`, addressed by slug. Returns exchange IDs and tournament-specific prices. Use the tournament UUID from `GET /tournaments/{slug}` as `tournamentId` on downstream exchange price/orderbook and trading requests so every call resolves the same isolated context. Only accessible to authorized organization/tournament members and to owners or admins of the tournament's organization.

        Args:
            slug: Tournament slug.
            limit: Results per page (max 100).
            cursor: Pagination cursor from a previous response.
            search: Case-insensitive title search (at most 200 characters).
            status: Filter by market lifecycle status. `resolved` is a deprecated alias for `settled`.
            market_group_id: Restrict to markets that belong to the given market group. The group must be bound to this tournament; otherwise returns 400.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketListResponse: Paginated list of tournament markets.

        Example:
            ```python
            market = client.tournaments.markets.list(
                slug="alpha-tournament",
                limit=20,
                status="any",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/tournaments/{slug}/markets", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "cursor": cursor,
                        "search": search,
                        "status": status,
                        "market_group_id": market_group_id,
                    },
                    market_list_params.MarketListParams,
                ),
            ),
            cast_to=MarketListResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketRetrieveResponse:
        """
        Returns a single market's detail with tournament-specific prices and the tournament-scoped orderbook embedded per exchange. Each exchange's embedded book carries `asOf`, the engine version it was read at, `{ sequence, at }`, the same version realtime `books` carry (compare by `sequence`, then `at`); it is null when the book is served without an engine version. `latestPrice` is null when no tournament trade has established a price, even when bids or asks are resting, and never falls back to the global exchange price. Returns 404 if the market is not assigned to this tournament.

        Args:
            id: Market ID.
            slug: Tournament slug.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketRetrieveResponse: Tournament market detail with embedded orderbook.

        Example:
            ```python
            market = client.tournaments.markets.retrieve(
                slug="alpha-tournament",
                id="26",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/tournaments/{slug}/markets/{id}", **{"slug": slug, "id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketRetrieveResponse,
        )


class AsyncMarketsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMarketsResourceWithRawResponse:
        return AsyncMarketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketsResourceWithStreamingResponse:
        return AsyncMarketsResourceWithStreamingResponse(self)

    async def list(
        self,
        slug: str,
        *,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        search: str | Omit = omit,
        status: Literal["open", "closed", "settled", "resolved", "any"] | Omit = omit,
        market_group_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketListResponse:
        """
        Equivalent explicit tournament-scoped view of `GET /markets?tournamentId={id}`, addressed by slug. Returns exchange IDs and tournament-specific prices. Use the tournament UUID from `GET /tournaments/{slug}` as `tournamentId` on downstream exchange price/orderbook and trading requests so every call resolves the same isolated context. Only accessible to authorized organization/tournament members and to owners or admins of the tournament's organization.

        Args:
            slug: Tournament slug.
            limit: Results per page (max 100).
            cursor: Pagination cursor from a previous response.
            search: Case-insensitive title search (at most 200 characters).
            status: Filter by market lifecycle status. `resolved` is a deprecated alias for `settled`.
            market_group_id: Restrict to markets that belong to the given market group. The group must be bound to this tournament; otherwise returns 400.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketListResponse: Paginated list of tournament markets.

        Example:
            ```python
            market = await client.tournaments.markets.list(
                slug="alpha-tournament",
                limit=20,
                status="any",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/tournaments/{slug}/markets", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "cursor": cursor,
                        "search": search,
                        "status": status,
                        "market_group_id": market_group_id,
                    },
                    market_list_params.MarketListParams,
                ),
            ),
            cast_to=MarketListResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketRetrieveResponse:
        """
        Returns a single market's detail with tournament-specific prices and the tournament-scoped orderbook embedded per exchange. Each exchange's embedded book carries `asOf`, the engine version it was read at, `{ sequence, at }`, the same version realtime `books` carry (compare by `sequence`, then `at`); it is null when the book is served without an engine version. `latestPrice` is null when no tournament trade has established a price, even when bids or asks are resting, and never falls back to the global exchange price. Returns 404 if the market is not assigned to this tournament.

        Args:
            id: Market ID.
            slug: Tournament slug.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketRetrieveResponse: Tournament market detail with embedded orderbook.

        Example:
            ```python
            market = await client.tournaments.markets.retrieve(
                slug="alpha-tournament",
                id="26",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/tournaments/{slug}/markets/{id}", **{"slug": slug, "id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketRetrieveResponse,
        )


class MarketsResourceWithRawResponse:
    def __init__(self, markets: MarketsResource) -> None:
        self._markets = markets

        self.list = to_raw_response_wrapper(
            markets.list,
        )
        self.retrieve = to_raw_response_wrapper(
            markets.retrieve,
        )


class AsyncMarketsResourceWithRawResponse:
    def __init__(self, markets: AsyncMarketsResource) -> None:
        self._markets = markets

        self.list = async_to_raw_response_wrapper(
            markets.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            markets.retrieve,
        )


class MarketsResourceWithStreamingResponse:
    def __init__(self, markets: MarketsResource) -> None:
        self._markets = markets

        self.list = to_streamed_response_wrapper(
            markets.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            markets.retrieve,
        )


class AsyncMarketsResourceWithStreamingResponse:
    def __init__(self, markets: AsyncMarketsResource) -> None:
        self._markets = markets

        self.list = async_to_streamed_response_wrapper(
            markets.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            markets.retrieve,
        )
