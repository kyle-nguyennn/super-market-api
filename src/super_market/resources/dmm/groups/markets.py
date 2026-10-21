# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable, Optional, Union

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
from ....types.dmm.groups.market_list_response import MarketListResponse
from ....types.dmm.groups import (
    market_list_params,
    market_create_params,
    market_update_params,
    market_list_members_params,
    market_create_members_params,
    market_delete_members_params,
)
from ....types.dmm.groups.group import Group
from ....types.dmm.groups.market_delete_response import MarketDeleteResponse
from ....types.dmm.groups.market_list_members_response import MarketListMembersResponse
from ....types.dmm.groups.market_group_member_add_result import MarketGroupMemberAddResult
from ....types.dmm.groups.market_group_member_remove_result import MarketGroupMemberRemoveResult

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
        *,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        search: str | Omit = omit,
        organization_slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketListResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Lists market groups in the caller's organization. Admin-scoped. Cursor-paginated (offset).

        Args:
            limit: Query parameter.
            cursor: Query parameter.
            search: Case-insensitive match on name or slug (at most 200 characters).
            organization_slug: Platform-admin only; restrict to a specific org. Org-admin callers always see their own org.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketListResponse: Paginated list of market groups.

        Example:
            ```python
            market = client.dmm.groups.markets.list(
                limit=25,
            )
            ```
        """
        return self._get(
            "/dmm/groups/markets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit, "cursor": cursor, "search": search, "organization_slug": organization_slug},
                    market_list_params.MarketListParams,
                ),
            ),
            cast_to=MarketListResponse,
        )

    def create(
        self,
        *,
        name: str,
        slug: str | Omit = omit,
        description: Optional[str] | Omit = omit,
        organization_slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Creates a market group. Slug auto-generated from name when omitted. Platform-admin callers must include `organizationSlug`.

        Args:
            name: Body parameter.
            slug: 1-100 lowercase letters, digits, and hyphens, with no leading or trailing hyphen. Auto-generated from `name` when omitted.
            description: Body parameter.
            organization_slug: Required for platform-admin callers. Org-admin callers may omit it (their own org is used).
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Group: Market group created.

        Example:
            ```python
            market = client.dmm.groups.markets.create(
                name="Earnings Markets",
            )
            ```
        """
        return self._post(
            "/dmm/groups/markets",
            body=maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "description": description,
                    "organization_slug": organization_slug,
                },
                market_create_params.MarketCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Group,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Reads a single market group by ID.

        Args:
            id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Group: Market group detail.

        Example:
            ```python
            market = client.dmm.groups.markets.retrieve(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/dmm/groups/markets/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Group,
        )

    def update(
        self,
        id: str,
        *,
        name: str | Omit = omit,
        slug: str | Omit = omit,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Updates a market group's name, slug, or description. Each field is optional, but the body must contain at least one of them.

        Args:
            id: Path parameter.
            name: Body parameter.
            slug: 1-100 lowercase letters, digits, and hyphens, with no leading or trailing hyphen.
            description: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Group: Updated group.

        Example:
            ```python
            market = client.dmm.groups.markets.update(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/dmm/groups/markets/{id}", **{"id": id}),
            body=maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "description": description,
                },
                market_update_params.MarketUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Group,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketDeleteResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Deletes a market group and its membership rows. In tournaments the group is bound to that have ended, the markets it supplied are kept as direct assignments so the historical record stays intact. In bound tournaments that have not ended (archived tournaments are left unchanged), the markets that lose their last source are removed by asynchronous reconciliation, which cancels their open orders and pays holders out at the tournament's valuation price. Because of that payout, the delete is refused with 409 while any of the group's exchanges with holdings in such a tournament has no tournament valuation price (`details.tournamentId`, `details.missingValuations`).

        Args:
            id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketDeleteResponse: Deleted.

        Example:
            ```python
            market = client.dmm.groups.markets.delete(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/dmm/groups/markets/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketDeleteResponse,
        )

    def list_members(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketListMembersResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Lists the markets in a market group. Admin-scoped. Cursor-paginated (offset).

        Args:
            id: Path parameter.
            limit: Query parameter.
            cursor: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketListMembersResponse: Paginated list of markets.

        Example:
            ```python
            market = client.dmm.groups.markets.list_members(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=25,
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/dmm/groups/markets/{id}/members", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit, "cursor": cursor}, market_list_members_params.MarketListMembersParams
                ),
            ),
            cast_to=MarketListMembersResponse,
        )

    def create_members(
        self,
        id: str,
        *,
        market_ids: Iterable[Union[str, float]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketGroupMemberAddResult:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Bulk-adds markets to a market group (up to 500 per call). Ids that are malformed, unknown, or not visible to your organization are reported in `notFound` rather than failing the call. Additions propagate to every bound tournament that has not ended.

        Args:
            id: Path parameter.
            market_ids: Market ids, as strings or numbers. Numbers must be safe integers (below 2^53); a larger id is rounded by JSON parsing before it reaches us, so send it as a string. Ids that cannot be parsed are reported in notFound.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketGroupMemberAddResult: Batch result.

        Example:
            ```python
            market = client.dmm.groups.markets.create_members(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                market_ids=["1042", "1043"],
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/dmm/groups/markets/{id}/members", **{"id": id}),
            body=maybe_transform(
                {"market_ids": market_ids},
                market_create_members_params.MarketCreateMembersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketGroupMemberAddResult,
        )

    def delete_members(
        self,
        id: str,
        *,
        market_ids: Iterable[Union[str, float]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketGroupMemberRemoveResult:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Removes markets from a market group (up to 500 per call). Requires a request body; pass a one-element array to remove a single market. Removal settles positions held in bound tournaments, so any market whose exchanges still have holdings but no tournament valuation price is left in place and reported in `blocked`; the rest of the batch proceeds. Markets sourced into an *ended* tournament are pinned in place first.

        Args:
            id: Path parameter.
            market_ids: Market ids, as strings or numbers. Numbers must be safe integers (below 2^53); a larger id is rounded by JSON parsing before it reaches us, so send it as a string. Ids that cannot be parsed are reported in notFound.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketGroupMemberRemoveResult: Batch result.

        Example:
            ```python
            market = client.dmm.groups.markets.delete_members(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                market_ids=["1042", "1043"],
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/dmm/groups/markets/{id}/members", **{"id": id}),
            body=maybe_transform(
                {"market_ids": market_ids},
                market_delete_members_params.MarketDeleteMembersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketGroupMemberRemoveResult,
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
        *,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        search: str | Omit = omit,
        organization_slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketListResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Lists market groups in the caller's organization. Admin-scoped. Cursor-paginated (offset).

        Args:
            limit: Query parameter.
            cursor: Query parameter.
            search: Case-insensitive match on name or slug (at most 200 characters).
            organization_slug: Platform-admin only; restrict to a specific org. Org-admin callers always see their own org.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketListResponse: Paginated list of market groups.

        Example:
            ```python
            market = await client.dmm.groups.markets.list(
                limit=25,
            )
            ```
        """
        return await self._get(
            "/dmm/groups/markets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit, "cursor": cursor, "search": search, "organization_slug": organization_slug},
                    market_list_params.MarketListParams,
                ),
            ),
            cast_to=MarketListResponse,
        )

    async def create(
        self,
        *,
        name: str,
        slug: str | Omit = omit,
        description: Optional[str] | Omit = omit,
        organization_slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Creates a market group. Slug auto-generated from name when omitted. Platform-admin callers must include `organizationSlug`.

        Args:
            name: Body parameter.
            slug: 1-100 lowercase letters, digits, and hyphens, with no leading or trailing hyphen. Auto-generated from `name` when omitted.
            description: Body parameter.
            organization_slug: Required for platform-admin callers. Org-admin callers may omit it (their own org is used).
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Group: Market group created.

        Example:
            ```python
            market = await client.dmm.groups.markets.create(
                name="Earnings Markets",
            )
            ```
        """
        return await self._post(
            "/dmm/groups/markets",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "description": description,
                    "organization_slug": organization_slug,
                },
                market_create_params.MarketCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Group,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Reads a single market group by ID.

        Args:
            id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Group: Market group detail.

        Example:
            ```python
            market = await client.dmm.groups.markets.retrieve(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/dmm/groups/markets/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Group,
        )

    async def update(
        self,
        id: str,
        *,
        name: str | Omit = omit,
        slug: str | Omit = omit,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Updates a market group's name, slug, or description. Each field is optional, but the body must contain at least one of them.

        Args:
            id: Path parameter.
            name: Body parameter.
            slug: 1-100 lowercase letters, digits, and hyphens, with no leading or trailing hyphen.
            description: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Group: Updated group.

        Example:
            ```python
            market = await client.dmm.groups.markets.update(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/dmm/groups/markets/{id}", **{"id": id}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "description": description,
                },
                market_update_params.MarketUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Group,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketDeleteResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Deletes a market group and its membership rows. In tournaments the group is bound to that have ended, the markets it supplied are kept as direct assignments so the historical record stays intact. In bound tournaments that have not ended (archived tournaments are left unchanged), the markets that lose their last source are removed by asynchronous reconciliation, which cancels their open orders and pays holders out at the tournament's valuation price. Because of that payout, the delete is refused with 409 while any of the group's exchanges with holdings in such a tournament has no tournament valuation price (`details.tournamentId`, `details.missingValuations`).

        Args:
            id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketDeleteResponse: Deleted.

        Example:
            ```python
            market = await client.dmm.groups.markets.delete(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/dmm/groups/markets/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketDeleteResponse,
        )

    async def list_members(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketListMembersResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Lists the markets in a market group. Admin-scoped. Cursor-paginated (offset).

        Args:
            id: Path parameter.
            limit: Query parameter.
            cursor: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketListMembersResponse: Paginated list of markets.

        Example:
            ```python
            market = await client.dmm.groups.markets.list_members(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=25,
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/dmm/groups/markets/{id}/members", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit, "cursor": cursor}, market_list_members_params.MarketListMembersParams
                ),
            ),
            cast_to=MarketListMembersResponse,
        )

    async def create_members(
        self,
        id: str,
        *,
        market_ids: Iterable[Union[str, float]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketGroupMemberAddResult:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Bulk-adds markets to a market group (up to 500 per call). Ids that are malformed, unknown, or not visible to your organization are reported in `notFound` rather than failing the call. Additions propagate to every bound tournament that has not ended.

        Args:
            id: Path parameter.
            market_ids: Market ids, as strings or numbers. Numbers must be safe integers (below 2^53); a larger id is rounded by JSON parsing before it reaches us, so send it as a string. Ids that cannot be parsed are reported in notFound.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketGroupMemberAddResult: Batch result.

        Example:
            ```python
            market = await client.dmm.groups.markets.create_members(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                market_ids=["1042", "1043"],
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/dmm/groups/markets/{id}/members", **{"id": id}),
            body=await async_maybe_transform(
                {"market_ids": market_ids},
                market_create_members_params.MarketCreateMembersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketGroupMemberAddResult,
        )

    async def delete_members(
        self,
        id: str,
        *,
        market_ids: Iterable[Union[str, float]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketGroupMemberRemoveResult:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Removes markets from a market group (up to 500 per call). Requires a request body; pass a one-element array to remove a single market. Removal settles positions held in bound tournaments, so any market whose exchanges still have holdings but no tournament valuation price is left in place and reported in `blocked`; the rest of the batch proceeds. Markets sourced into an *ended* tournament are pinned in place first.

        Args:
            id: Path parameter.
            market_ids: Market ids, as strings or numbers. Numbers must be safe integers (below 2^53); a larger id is rounded by JSON parsing before it reaches us, so send it as a string. Ids that cannot be parsed are reported in notFound.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketGroupMemberRemoveResult: Batch result.

        Example:
            ```python
            market = await client.dmm.groups.markets.delete_members(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                market_ids=["1042", "1043"],
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/dmm/groups/markets/{id}/members", **{"id": id}),
            body=await async_maybe_transform(
                {"market_ids": market_ids},
                market_delete_members_params.MarketDeleteMembersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketGroupMemberRemoveResult,
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
        self.retrieve = to_raw_response_wrapper(
            markets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            markets.update,
        )
        self.delete = to_raw_response_wrapper(
            markets.delete,
        )
        self.list_members = to_raw_response_wrapper(
            markets.list_members,
        )
        self.create_members = to_raw_response_wrapper(
            markets.create_members,
        )
        self.delete_members = to_raw_response_wrapper(
            markets.delete_members,
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
        self.retrieve = async_to_raw_response_wrapper(
            markets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            markets.update,
        )
        self.delete = async_to_raw_response_wrapper(
            markets.delete,
        )
        self.list_members = async_to_raw_response_wrapper(
            markets.list_members,
        )
        self.create_members = async_to_raw_response_wrapper(
            markets.create_members,
        )
        self.delete_members = async_to_raw_response_wrapper(
            markets.delete_members,
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
        self.retrieve = to_streamed_response_wrapper(
            markets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            markets.update,
        )
        self.delete = to_streamed_response_wrapper(
            markets.delete,
        )
        self.list_members = to_streamed_response_wrapper(
            markets.list_members,
        )
        self.create_members = to_streamed_response_wrapper(
            markets.create_members,
        )
        self.delete_members = to_streamed_response_wrapper(
            markets.delete_members,
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
        self.retrieve = async_to_streamed_response_wrapper(
            markets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            markets.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            markets.delete,
        )
        self.list_members = async_to_streamed_response_wrapper(
            markets.list_members,
        )
        self.create_members = async_to_streamed_response_wrapper(
            markets.create_members,
        )
        self.delete_members = async_to_streamed_response_wrapper(
            markets.delete_members,
        )
