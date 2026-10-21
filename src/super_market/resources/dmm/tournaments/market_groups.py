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
from ....types.dmm.tournaments.market_group_list_response import MarketGroupListResponse
from ....types.dmm.tournaments import market_group_list_params, market_group_create_params
from ....types.dmm.tournaments.market_group_create_response import MarketGroupCreateResponse
from ....types.dmm.tournaments.market_group_delete_response import MarketGroupDeleteResponse

__all__ = ["MarketGroupsResource", "AsyncMarketGroupsResource"]


class MarketGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MarketGroupsResourceWithRawResponse:
        return MarketGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketGroupsResourceWithStreamingResponse:
        return MarketGroupsResourceWithStreamingResponse(self)

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
    ) -> MarketGroupListResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Lists market groups in the tournament's organization, newest first, flagging which are bound to this tournament and when. Supports opaque cursor pagination.

        Args:
            slug: Tournament slug.
            limit: Page size (default 50, max 200).
            cursor: Opaque pagination cursor from a prior response. It marks the last row served rather than a row offset, so rows added or removed between pages neither repeat a row nor hide an unseen one.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketGroupListResponse: Market groups page with bound flag.

        Example:
            ```python
            market_group = client.dmm.tournaments.market_groups.list(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/dmm/tournaments/{slug}/market-groups", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit, "cursor": cursor}, market_group_list_params.MarketGroupListParams
                ),
            ),
            cast_to=MarketGroupListResponse,
        )

    def create(
        self,
        slug: str,
        *,
        market_group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketGroupCreateResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Bind a market group to the tournament. Group must belong to the tournament's organization. Triggers an inngest reconcile that materializes the group's markets into `tournament_markets` asynchronously.

        Args:
            slug: Tournament slug.
            market_group_id: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketGroupCreateResponse: Group bound.

        Example:
            ```python
            market_group = client.dmm.tournaments.market_groups.create(
                slug="alpha-tournament",
                market_group_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._post(
            path_template("/dmm/tournaments/{slug}/market-groups", **{"slug": slug}),
            body=maybe_transform(
                {"market_group_id": market_group_id},
                market_group_create_params.MarketGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketGroupCreateResponse,
        )

    def delete(
        self,
        group_id: str,
        *,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketGroupDeleteResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Unbind a market group from the tournament. An asynchronous reconciliation then removes every market that loses its last source: markets the group supplied that are not directly assigned and not supplied by another bound group. Each removed market has its open orders cancelled and its holders paid out at the tournament's valuation price, as with DELETE /dmm/tournaments/{slug}/markets/{marketId}.

        Because removal settles held positions, the unbind is refused with 409 while any of the group's exchanges with holdings has no tournament valuation price (`details.missingValuations`).

        Args:
            group_id: Path parameter.
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketGroupDeleteResponse: Group unbound; market removal is reconciled asynchronously.

        Example:
            ```python
            market_group = client.dmm.tournaments.market_groups.delete(
                slug="slug",
                group_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if group_id is None or (isinstance(group_id, str) and not group_id):
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._delete(
            path_template("/dmm/tournaments/{slug}/market-groups/{groupId}", **{"slug": slug, "groupId": group_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketGroupDeleteResponse,
        )


class AsyncMarketGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMarketGroupsResourceWithRawResponse:
        return AsyncMarketGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketGroupsResourceWithStreamingResponse:
        return AsyncMarketGroupsResourceWithStreamingResponse(self)

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
    ) -> MarketGroupListResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Lists market groups in the tournament's organization, newest first, flagging which are bound to this tournament and when. Supports opaque cursor pagination.

        Args:
            slug: Tournament slug.
            limit: Page size (default 50, max 200).
            cursor: Opaque pagination cursor from a prior response. It marks the last row served rather than a row offset, so rows added or removed between pages neither repeat a row nor hide an unseen one.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketGroupListResponse: Market groups page with bound flag.

        Example:
            ```python
            market_group = await client.dmm.tournaments.market_groups.list(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/dmm/tournaments/{slug}/market-groups", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit, "cursor": cursor}, market_group_list_params.MarketGroupListParams
                ),
            ),
            cast_to=MarketGroupListResponse,
        )

    async def create(
        self,
        slug: str,
        *,
        market_group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketGroupCreateResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Bind a market group to the tournament. Group must belong to the tournament's organization. Triggers an inngest reconcile that materializes the group's markets into `tournament_markets` asynchronously.

        Args:
            slug: Tournament slug.
            market_group_id: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketGroupCreateResponse: Group bound.

        Example:
            ```python
            market_group = await client.dmm.tournaments.market_groups.create(
                slug="alpha-tournament",
                market_group_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._post(
            path_template("/dmm/tournaments/{slug}/market-groups", **{"slug": slug}),
            body=await async_maybe_transform(
                {"market_group_id": market_group_id},
                market_group_create_params.MarketGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketGroupCreateResponse,
        )

    async def delete(
        self,
        group_id: str,
        *,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketGroupDeleteResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Unbind a market group from the tournament. An asynchronous reconciliation then removes every market that loses its last source: markets the group supplied that are not directly assigned and not supplied by another bound group. Each removed market has its open orders cancelled and its holders paid out at the tournament's valuation price, as with DELETE /dmm/tournaments/{slug}/markets/{marketId}.

        Because removal settles held positions, the unbind is refused with 409 while any of the group's exchanges with holdings has no tournament valuation price (`details.missingValuations`).

        Args:
            group_id: Path parameter.
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketGroupDeleteResponse: Group unbound; market removal is reconciled asynchronously.

        Example:
            ```python
            market_group = await client.dmm.tournaments.market_groups.delete(
                slug="slug",
                group_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if group_id is None or (isinstance(group_id, str) and not group_id):
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._delete(
            path_template("/dmm/tournaments/{slug}/market-groups/{groupId}", **{"slug": slug, "groupId": group_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketGroupDeleteResponse,
        )


class MarketGroupsResourceWithRawResponse:
    def __init__(self, market_groups: MarketGroupsResource) -> None:
        self._market_groups = market_groups

        self.list = to_raw_response_wrapper(
            market_groups.list,
        )
        self.create = to_raw_response_wrapper(
            market_groups.create,
        )
        self.delete = to_raw_response_wrapper(
            market_groups.delete,
        )


class AsyncMarketGroupsResourceWithRawResponse:
    def __init__(self, market_groups: AsyncMarketGroupsResource) -> None:
        self._market_groups = market_groups

        self.list = async_to_raw_response_wrapper(
            market_groups.list,
        )
        self.create = async_to_raw_response_wrapper(
            market_groups.create,
        )
        self.delete = async_to_raw_response_wrapper(
            market_groups.delete,
        )


class MarketGroupsResourceWithStreamingResponse:
    def __init__(self, market_groups: MarketGroupsResource) -> None:
        self._market_groups = market_groups

        self.list = to_streamed_response_wrapper(
            market_groups.list,
        )
        self.create = to_streamed_response_wrapper(
            market_groups.create,
        )
        self.delete = to_streamed_response_wrapper(
            market_groups.delete,
        )


class AsyncMarketGroupsResourceWithStreamingResponse:
    def __init__(self, market_groups: AsyncMarketGroupsResource) -> None:
        self._market_groups = market_groups

        self.list = async_to_streamed_response_wrapper(
            market_groups.list,
        )
        self.create = async_to_streamed_response_wrapper(
            market_groups.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            market_groups.delete,
        )
