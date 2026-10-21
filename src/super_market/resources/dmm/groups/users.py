# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional
from ...._types import SequenceNotStr

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
from ....types.dmm.groups.user_list_response import UserListResponse
from ....types.dmm.groups import (
    user_list_params,
    user_create_params,
    user_update_params,
    user_list_members_params,
    user_create_members_params,
    user_delete_members_params,
)
from ....types.dmm.groups.group import Group
from ....types.dmm.groups.user_delete_response import UserDeleteResponse
from ....types.dmm.groups.user_list_members_response import UserListMembersResponse
from ....types.dmm.groups.user_group_member_add_result import UserGroupMemberAddResult
from ....types.dmm.groups.user_group_member_remove_result import UserGroupMemberRemoveResult

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self)

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
    ) -> UserListResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Lists user groups in the caller's organization. Admin-scoped. Cursor-paginated (offset).

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
            UserListResponse: Paginated list of user groups.

        Example:
            ```python
            user = client.dmm.groups.users.list(
                limit=25,
            )
            ```
        """
        return self._get(
            "/dmm/groups/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit, "cursor": cursor, "search": search, "organization_slug": organization_slug},
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserListResponse,
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

        Creates a user group. Slug auto-generated from name when omitted. Platform-admin callers must include `organizationSlug`.

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
            Group: User group created.

        Example:
            ```python
            user = client.dmm.groups.users.create(
                name="Earnings Markets",
            )
            ```
        """
        return self._post(
            "/dmm/groups/users",
            body=maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "description": description,
                    "organization_slug": organization_slug,
                },
                user_create_params.UserCreateParams,
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

        Reads a single user group by ID.

        Args:
            id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Group: User group detail.

        Example:
            ```python
            user = client.dmm.groups.users.retrieve(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/dmm/groups/users/{id}", **{"id": id}),
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

        Updates a user group's name, slug, or description. Each field is optional, but the body must contain at least one of them.

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
            user = client.dmm.groups.users.update(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/dmm/groups/users/{id}", **{"id": id}),
            body=maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "description": description,
                },
                user_update_params.UserUpdateParams,
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
    ) -> UserDeleteResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Deletes a user group and its membership rows. In tournaments the group is bound to that have ended, the members it supplied are kept as direct members so the historical record stays intact. In bound tournaments that have not ended (archived tournaments are left unchanged), the members who lose their last source are removed by asynchronous reconciliation: their open orders are cancelled and holdings deleted with no payout, and removal from an active tournament blocks them from rejoining it.

        Args:
            id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UserDeleteResponse: Deleted.

        Example:
            ```python
            user = client.dmm.groups.users.delete(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/dmm/groups/users/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserDeleteResponse,
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
    ) -> UserListMembersResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Lists the profiles in a user group. Admin-scoped. Cursor-paginated (offset).

        Args:
            id: Path parameter.
            limit: Query parameter.
            cursor: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UserListMembersResponse: Paginated list of profiles.

        Example:
            ```python
            user = client.dmm.groups.users.list_members(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=25,
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/dmm/groups/users/{id}/members", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit, "cursor": cursor}, user_list_members_params.UserListMembersParams
                ),
            ),
            cast_to=UserListMembersResponse,
        )

    def create_members(
        self,
        id: str,
        *,
        profile_ids: SequenceNotStr[str] | Omit = omit,
        identifiers: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserGroupMemberAddResult:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Bulk-adds profiles to a user group (up to 500 per call). Only profiles already in the group's organization are added directly. Anyone else is emailed an organization invitation (reported in `invited`) and joins the group when they sign in on the organization's site; an admin never enrols anyone in an organization. Profiles already in a different organization are reported in `rejected` and not added. Additions propagate to every bound tournament that has not ended.

        Args:
            id: Path parameter.
            profile_ids: Profile UUIDs to add.
            identifiers: Emails or usernames, matched case-insensitively. Usernames matching no profile and malformed emails come back in `unmatched`; other emails that are not organization members are invited.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UserGroupMemberAddResult: Batch result.

        Example:
            ```python
            user = client.dmm.groups.users.create_members(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/dmm/groups/users/{id}/members", **{"id": id}),
            body=maybe_transform(
                {
                    "profile_ids": profile_ids,
                    "identifiers": identifiers,
                },
                user_create_members_params.UserCreateMembersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGroupMemberAddResult,
        )

    def delete_members(
        self,
        id: str,
        *,
        profile_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserGroupMemberRemoveResult:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Removes profiles from a user group (up to 500 per call). Requires a request body; pass a one-element array to remove a single member. Ids holding no membership row are reported in `notFound`. Members this group sourced into an *ended* tournament are pinned in place first — ended tournaments are frozen historical records.

        Args:
            id: Path parameter.
            profile_ids: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UserGroupMemberRemoveResult: Batch result.

        Example:
            ```python
            user = client.dmm.groups.users.delete_members(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                profile_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/dmm/groups/users/{id}/members", **{"id": id}),
            body=maybe_transform(
                {"profile_ids": profile_ids},
                user_delete_members_params.UserDeleteMembersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGroupMemberRemoveResult,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self)

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
    ) -> UserListResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Lists user groups in the caller's organization. Admin-scoped. Cursor-paginated (offset).

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
            UserListResponse: Paginated list of user groups.

        Example:
            ```python
            user = await client.dmm.groups.users.list(
                limit=25,
            )
            ```
        """
        return await self._get(
            "/dmm/groups/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit, "cursor": cursor, "search": search, "organization_slug": organization_slug},
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserListResponse,
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

        Creates a user group. Slug auto-generated from name when omitted. Platform-admin callers must include `organizationSlug`.

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
            Group: User group created.

        Example:
            ```python
            user = await client.dmm.groups.users.create(
                name="Earnings Markets",
            )
            ```
        """
        return await self._post(
            "/dmm/groups/users",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "description": description,
                    "organization_slug": organization_slug,
                },
                user_create_params.UserCreateParams,
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

        Reads a single user group by ID.

        Args:
            id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Group: User group detail.

        Example:
            ```python
            user = await client.dmm.groups.users.retrieve(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/dmm/groups/users/{id}", **{"id": id}),
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

        Updates a user group's name, slug, or description. Each field is optional, but the body must contain at least one of them.

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
            user = await client.dmm.groups.users.update(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/dmm/groups/users/{id}", **{"id": id}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "description": description,
                },
                user_update_params.UserUpdateParams,
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
    ) -> UserDeleteResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Deletes a user group and its membership rows. In tournaments the group is bound to that have ended, the members it supplied are kept as direct members so the historical record stays intact. In bound tournaments that have not ended (archived tournaments are left unchanged), the members who lose their last source are removed by asynchronous reconciliation: their open orders are cancelled and holdings deleted with no payout, and removal from an active tournament blocks them from rejoining it.

        Args:
            id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UserDeleteResponse: Deleted.

        Example:
            ```python
            user = await client.dmm.groups.users.delete(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/dmm/groups/users/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserDeleteResponse,
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
    ) -> UserListMembersResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Lists the profiles in a user group. Admin-scoped. Cursor-paginated (offset).

        Args:
            id: Path parameter.
            limit: Query parameter.
            cursor: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UserListMembersResponse: Paginated list of profiles.

        Example:
            ```python
            user = await client.dmm.groups.users.list_members(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=25,
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/dmm/groups/users/{id}/members", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit, "cursor": cursor}, user_list_members_params.UserListMembersParams
                ),
            ),
            cast_to=UserListMembersResponse,
        )

    async def create_members(
        self,
        id: str,
        *,
        profile_ids: SequenceNotStr[str] | Omit = omit,
        identifiers: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserGroupMemberAddResult:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Bulk-adds profiles to a user group (up to 500 per call). Only profiles already in the group's organization are added directly. Anyone else is emailed an organization invitation (reported in `invited`) and joins the group when they sign in on the organization's site; an admin never enrols anyone in an organization. Profiles already in a different organization are reported in `rejected` and not added. Additions propagate to every bound tournament that has not ended.

        Args:
            id: Path parameter.
            profile_ids: Profile UUIDs to add.
            identifiers: Emails or usernames, matched case-insensitively. Usernames matching no profile and malformed emails come back in `unmatched`; other emails that are not organization members are invited.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UserGroupMemberAddResult: Batch result.

        Example:
            ```python
            user = await client.dmm.groups.users.create_members(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/dmm/groups/users/{id}/members", **{"id": id}),
            body=await async_maybe_transform(
                {
                    "profile_ids": profile_ids,
                    "identifiers": identifiers,
                },
                user_create_members_params.UserCreateMembersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGroupMemberAddResult,
        )

    async def delete_members(
        self,
        id: str,
        *,
        profile_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserGroupMemberRemoveResult:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Removes profiles from a user group (up to 500 per call). Requires a request body; pass a one-element array to remove a single member. Ids holding no membership row are reported in `notFound`. Members this group sourced into an *ended* tournament are pinned in place first — ended tournaments are frozen historical records.

        Args:
            id: Path parameter.
            profile_ids: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UserGroupMemberRemoveResult: Batch result.

        Example:
            ```python
            user = await client.dmm.groups.users.delete_members(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                profile_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/dmm/groups/users/{id}/members", **{"id": id}),
            body=await async_maybe_transform(
                {"profile_ids": profile_ids},
                user_delete_members_params.UserDeleteMembersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGroupMemberRemoveResult,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.create = to_raw_response_wrapper(
            users.create,
        )
        self.retrieve = to_raw_response_wrapper(
            users.retrieve,
        )
        self.update = to_raw_response_wrapper(
            users.update,
        )
        self.delete = to_raw_response_wrapper(
            users.delete,
        )
        self.list_members = to_raw_response_wrapper(
            users.list_members,
        )
        self.create_members = to_raw_response_wrapper(
            users.create_members,
        )
        self.delete_members = to_raw_response_wrapper(
            users.delete_members,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.create = async_to_raw_response_wrapper(
            users.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            users.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            users.update,
        )
        self.delete = async_to_raw_response_wrapper(
            users.delete,
        )
        self.list_members = async_to_raw_response_wrapper(
            users.list_members,
        )
        self.create_members = async_to_raw_response_wrapper(
            users.create_members,
        )
        self.delete_members = async_to_raw_response_wrapper(
            users.delete_members,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.create = to_streamed_response_wrapper(
            users.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            users.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            users.update,
        )
        self.delete = to_streamed_response_wrapper(
            users.delete,
        )
        self.list_members = to_streamed_response_wrapper(
            users.list_members,
        )
        self.create_members = to_streamed_response_wrapper(
            users.create_members,
        )
        self.delete_members = to_streamed_response_wrapper(
            users.delete_members,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.create = async_to_streamed_response_wrapper(
            users.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            users.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            users.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            users.delete,
        )
        self.list_members = async_to_streamed_response_wrapper(
            users.list_members,
        )
        self.create_members = async_to_streamed_response_wrapper(
            users.create_members,
        )
        self.delete_members = async_to_streamed_response_wrapper(
            users.delete_members,
        )
