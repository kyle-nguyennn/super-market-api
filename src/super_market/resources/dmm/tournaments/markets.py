# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.dmm.tournaments.market_list_response import MarketListResponse
from ....types.dmm.tournaments import market_list_params, market_create_params
from ....types.dmm.tournaments.market_create_response import MarketCreateResponse
from ....types.dmm.tournaments.market_delete_response import MarketDeleteResponse

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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketListResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Deprecated compatibility alias for `GET /dmm/tournaments/{slug}/market-assignments`. It returns assignment metadata, not exchange IDs or tournament pricing. Every response carries `Deprecation: true` and a `Link` header naming the successor endpoint. New integrations should use the successor endpoint.

        Args:
            slug: Tournament slug.
            limit: Page size (default 50, max 200).
            cursor: Opaque pagination cursor from a prior response. It marks the last row served rather than a row offset, so rows added or removed between pages neither repeat a row nor hide an unseen one.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketListResponse: Tournament markets page.

        Example:
            ```python
            market = client.dmm.tournaments.markets.list(
                slug="alpha-tournament",
            )
            ```

        Deprecated: this method is deprecated.
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/dmm/tournaments/{slug}/markets", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit, "cursor": cursor}, market_list_params.MarketListParams),
            ),
            cast_to=MarketListResponse,
        )

    def create(
        self,
        slug: str,
        *,
        market_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketCreateResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Attach a market to this tournament directly. Seeds tournament-scoped exchange state and CFMM orderbook (when applicable). Rejects ended and archived tournaments and markets attached to another organization.

        If the market is already in the tournament only because a bound market group supplies it, the same request promotes it to a direct assignment and returns 200 with the same body; nothing is re-seeded, and unbinding the group no longer removes it.

        Args:
            slug: Tournament slug.
            market_id: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketCreateResponse: A group-supplied market was promoted to a direct assignment.

        Example:
            ```python
            market = client.dmm.tournaments.markets.create(
                slug="alpha-tournament",
                market_id="26",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._post(
            path_template("/dmm/tournaments/{slug}/markets", **{"slug": slug}),
            body=maybe_transform(
                {"market_id": market_id},
                market_create_params.MarketCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketCreateResponse,
        )

    def delete(
        self,
        market_id: str,
        *,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketDeleteResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Removes a directly assigned market. When the market is assigned only directly, this cancels open orders, pays holders out at the tournament's `valuation_price`, and deletes tournament-scoped exchange state; the response reports `exchangesCleared` and `paidOutHoldings`.

        When a bound market group also supplies the market, nothing is removed: the assignment is demoted to group-sourced and the response is `{ success: true, demoted: true }`. The market then leaves the tournament only when its last group source goes. A market supplied only by a group cannot be removed here (409); remove it from the group or unbind the group instead.

        Args:
            market_id: Path parameter.
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketDeleteResponse: Market removed, or demoted to group-sourced when a bound group still supplies it.

        Example:
            ```python
            market = client.dmm.tournaments.markets.delete(
                slug="slug",
                market_id="marketId",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if market_id is None or (isinstance(market_id, str) and not market_id):
            raise ValueError(f"Expected a non-empty value for `market_id` but received {market_id!r}")
        return self._delete(
            path_template("/dmm/tournaments/{slug}/markets/{marketId}", **{"slug": slug, "marketId": market_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketDeleteResponse,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketListResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Deprecated compatibility alias for `GET /dmm/tournaments/{slug}/market-assignments`. It returns assignment metadata, not exchange IDs or tournament pricing. Every response carries `Deprecation: true` and a `Link` header naming the successor endpoint. New integrations should use the successor endpoint.

        Args:
            slug: Tournament slug.
            limit: Page size (default 50, max 200).
            cursor: Opaque pagination cursor from a prior response. It marks the last row served rather than a row offset, so rows added or removed between pages neither repeat a row nor hide an unseen one.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketListResponse: Tournament markets page.

        Example:
            ```python
            market = await client.dmm.tournaments.markets.list(
                slug="alpha-tournament",
            )
            ```

        Deprecated: this method is deprecated.
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/dmm/tournaments/{slug}/markets", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit, "cursor": cursor}, market_list_params.MarketListParams
                ),
            ),
            cast_to=MarketListResponse,
        )

    async def create(
        self,
        slug: str,
        *,
        market_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketCreateResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Attach a market to this tournament directly. Seeds tournament-scoped exchange state and CFMM orderbook (when applicable). Rejects ended and archived tournaments and markets attached to another organization.

        If the market is already in the tournament only because a bound market group supplies it, the same request promotes it to a direct assignment and returns 200 with the same body; nothing is re-seeded, and unbinding the group no longer removes it.

        Args:
            slug: Tournament slug.
            market_id: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketCreateResponse: A group-supplied market was promoted to a direct assignment.

        Example:
            ```python
            market = await client.dmm.tournaments.markets.create(
                slug="alpha-tournament",
                market_id="26",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._post(
            path_template("/dmm/tournaments/{slug}/markets", **{"slug": slug}),
            body=await async_maybe_transform(
                {"market_id": market_id},
                market_create_params.MarketCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketCreateResponse,
        )

    async def delete(
        self,
        market_id: str,
        *,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketDeleteResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Removes a directly assigned market. When the market is assigned only directly, this cancels open orders, pays holders out at the tournament's `valuation_price`, and deletes tournament-scoped exchange state; the response reports `exchangesCleared` and `paidOutHoldings`.

        When a bound market group also supplies the market, nothing is removed: the assignment is demoted to group-sourced and the response is `{ success: true, demoted: true }`. The market then leaves the tournament only when its last group source goes. A market supplied only by a group cannot be removed here (409); remove it from the group or unbind the group instead.

        Args:
            market_id: Path parameter.
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketDeleteResponse: Market removed, or demoted to group-sourced when a bound group still supplies it.

        Example:
            ```python
            market = await client.dmm.tournaments.markets.delete(
                slug="slug",
                market_id="marketId",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if market_id is None or (isinstance(market_id, str) and not market_id):
            raise ValueError(f"Expected a non-empty value for `market_id` but received {market_id!r}")
        return await self._delete(
            path_template("/dmm/tournaments/{slug}/markets/{marketId}", **{"slug": slug, "marketId": market_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketDeleteResponse,
        )


class MarketsResourceWithRawResponse:
    def __init__(self, markets: MarketsResource) -> None:
        self._markets = markets

        self.list = to_raw_response_wrapper(
            markets.list,
        )
        self.create = to_raw_response_wrapper(
            markets.create,
        )
        self.delete = to_raw_response_wrapper(
            markets.delete,
        )


class AsyncMarketsResourceWithRawResponse:
    def __init__(self, markets: AsyncMarketsResource) -> None:
        self._markets = markets

        self.list = async_to_raw_response_wrapper(
            markets.list,
        )
        self.create = async_to_raw_response_wrapper(
            markets.create,
        )
        self.delete = async_to_raw_response_wrapper(
            markets.delete,
        )


class MarketsResourceWithStreamingResponse:
    def __init__(self, markets: MarketsResource) -> None:
        self._markets = markets

        self.list = to_streamed_response_wrapper(
            markets.list,
        )
        self.create = to_streamed_response_wrapper(
            markets.create,
        )
        self.delete = to_streamed_response_wrapper(
            markets.delete,
        )


class AsyncMarketsResourceWithStreamingResponse:
    def __init__(self, markets: AsyncMarketsResource) -> None:
        self._markets = markets

        self.list = async_to_streamed_response_wrapper(
            markets.list,
        )
        self.create = async_to_streamed_response_wrapper(
            markets.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            markets.delete,
        )
