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
from ....types.dmm.tournaments.user_group_list_response import UserGroupListResponse
from ....types.dmm.tournaments import user_group_list_params, user_group_create_params
from ....types.dmm.tournaments.user_group_create_response import UserGroupCreateResponse
from ....types.dmm.tournaments.user_group_delete_response import UserGroupDeleteResponse

__all__ = ["UserGroupsResource", "AsyncUserGroupsResource"]


class UserGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserGroupsResourceWithRawResponse:
        return UserGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserGroupsResourceWithStreamingResponse:
        return UserGroupsResourceWithStreamingResponse(self)

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
    ) -> UserGroupListResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Lists user groups in the tournament's organization, newest first, flagging which are bound to this tournament and when. Supports opaque cursor pagination.

        Args:
            slug: Tournament slug.
            limit: Page size (default 50, max 200).
            cursor: Opaque pagination cursor from a prior response. It marks the last row served rather than a row offset, so rows added or removed between pages neither repeat a row nor hide an unseen one.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UserGroupListResponse: User groups page with bound flag.

        Example:
            ```python
            user_group = client.dmm.tournaments.user_groups.list(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/dmm/tournaments/{slug}/user-groups", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit, "cursor": cursor}, user_group_list_params.UserGroupListParams),
            ),
            cast_to=UserGroupListResponse,
        )

    def create(
        self,
        slug: str,
        *,
        user_group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserGroupCreateResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Bind a user group to the tournament. Triggers an inngest reconcile that materializes the group's members into `tournament_members` asynchronously.

        Args:
            slug: Tournament slug.
            user_group_id: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UserGroupCreateResponse: Group bound.

        Example:
            ```python
            user_group = client.dmm.tournaments.user_groups.create(
                slug="alpha-tournament",
                user_group_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._post(
            path_template("/dmm/tournaments/{slug}/user-groups", **{"slug": slug}),
            body=maybe_transform(
                {"user_group_id": user_group_id},
                user_group_create_params.UserGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGroupCreateResponse,
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
    ) -> UserGroupDeleteResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Unbind a user group from the tournament. An asynchronous reconciliation then removes every member who loses their last source: members the group supplied who were not added directly and are not supplied by another bound group. Each removed member forfeits as with DELETE /dmm/tournaments/{slug}/members/{profileId}: open orders are cancelled and holdings are deleted with no payout, and removal from an active tournament blocks them from rejoining it.

        Args:
            group_id: Path parameter.
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UserGroupDeleteResponse: Group unbound; member removal is reconciled asynchronously.

        Example:
            ```python
            user_group = client.dmm.tournaments.user_groups.delete(
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
            path_template("/dmm/tournaments/{slug}/user-groups/{groupId}", **{"slug": slug, "groupId": group_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGroupDeleteResponse,
        )


class AsyncUserGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserGroupsResourceWithRawResponse:
        return AsyncUserGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserGroupsResourceWithStreamingResponse:
        return AsyncUserGroupsResourceWithStreamingResponse(self)

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
    ) -> UserGroupListResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Lists user groups in the tournament's organization, newest first, flagging which are bound to this tournament and when. Supports opaque cursor pagination.

        Args:
            slug: Tournament slug.
            limit: Page size (default 50, max 200).
            cursor: Opaque pagination cursor from a prior response. It marks the last row served rather than a row offset, so rows added or removed between pages neither repeat a row nor hide an unseen one.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UserGroupListResponse: User groups page with bound flag.

        Example:
            ```python
            user_group = await client.dmm.tournaments.user_groups.list(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/dmm/tournaments/{slug}/user-groups", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit, "cursor": cursor}, user_group_list_params.UserGroupListParams
                ),
            ),
            cast_to=UserGroupListResponse,
        )

    async def create(
        self,
        slug: str,
        *,
        user_group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserGroupCreateResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Bind a user group to the tournament. Triggers an inngest reconcile that materializes the group's members into `tournament_members` asynchronously.

        Args:
            slug: Tournament slug.
            user_group_id: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UserGroupCreateResponse: Group bound.

        Example:
            ```python
            user_group = await client.dmm.tournaments.user_groups.create(
                slug="alpha-tournament",
                user_group_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._post(
            path_template("/dmm/tournaments/{slug}/user-groups", **{"slug": slug}),
            body=await async_maybe_transform(
                {"user_group_id": user_group_id},
                user_group_create_params.UserGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGroupCreateResponse,
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
    ) -> UserGroupDeleteResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Unbind a user group from the tournament. An asynchronous reconciliation then removes every member who loses their last source: members the group supplied who were not added directly and are not supplied by another bound group. Each removed member forfeits as with DELETE /dmm/tournaments/{slug}/members/{profileId}: open orders are cancelled and holdings are deleted with no payout, and removal from an active tournament blocks them from rejoining it.

        Args:
            group_id: Path parameter.
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UserGroupDeleteResponse: Group unbound; member removal is reconciled asynchronously.

        Example:
            ```python
            user_group = await client.dmm.tournaments.user_groups.delete(
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
            path_template("/dmm/tournaments/{slug}/user-groups/{groupId}", **{"slug": slug, "groupId": group_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGroupDeleteResponse,
        )


class UserGroupsResourceWithRawResponse:
    def __init__(self, user_groups: UserGroupsResource) -> None:
        self._user_groups = user_groups

        self.list = to_raw_response_wrapper(
            user_groups.list,
        )
        self.create = to_raw_response_wrapper(
            user_groups.create,
        )
        self.delete = to_raw_response_wrapper(
            user_groups.delete,
        )


class AsyncUserGroupsResourceWithRawResponse:
    def __init__(self, user_groups: AsyncUserGroupsResource) -> None:
        self._user_groups = user_groups

        self.list = async_to_raw_response_wrapper(
            user_groups.list,
        )
        self.create = async_to_raw_response_wrapper(
            user_groups.create,
        )
        self.delete = async_to_raw_response_wrapper(
            user_groups.delete,
        )


class UserGroupsResourceWithStreamingResponse:
    def __init__(self, user_groups: UserGroupsResource) -> None:
        self._user_groups = user_groups

        self.list = to_streamed_response_wrapper(
            user_groups.list,
        )
        self.create = to_streamed_response_wrapper(
            user_groups.create,
        )
        self.delete = to_streamed_response_wrapper(
            user_groups.delete,
        )


class AsyncUserGroupsResourceWithStreamingResponse:
    def __init__(self, user_groups: AsyncUserGroupsResource) -> None:
        self._user_groups = user_groups

        self.list = async_to_streamed_response_wrapper(
            user_groups.list,
        )
        self.create = async_to_streamed_response_wrapper(
            user_groups.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            user_groups.delete,
        )
