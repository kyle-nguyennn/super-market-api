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
from ....types.dmm.tournaments.member_list_response import MemberListResponse
from ....types.dmm.tournaments.dmm_tournament_member_add import DmmTournamentMemberAdd
from ....types.dmm.tournaments import member_create_params
from ....types.dmm.tournaments.member_delete_response import MemberDeleteResponse

__all__ = ["MembersResource", "AsyncMembersResource"]


class MembersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MembersResourceWithRawResponse:
        return MembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MembersResourceWithStreamingResponse:
        return MembersResourceWithStreamingResponse(self)

    def list(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberListResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>



        Args:
            slug: Tournament slug.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MemberListResponse: Tournament members.

        Example:
            ```python
            member = client.dmm.tournaments.members.list(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/dmm/tournaments/{slug}/members", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberListResponse,
        )

    def create(
        self,
        slug: str,
        *,
        username: str | Omit = omit,
        email: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmmTournamentMemberAdd:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Add a member by username or email. The user must already belong to the tournament's organization. Idempotent: re-adding flags the row as `added_directly`.

        Args:
            slug: Tournament slug.
            username: Body parameter.
            email: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DmmTournamentMemberAdd: Member already belongs to the tournament.

        Example:
            ```python
            member = client.dmm.tournaments.members.create(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._post(
            path_template("/dmm/tournaments/{slug}/members", **{"slug": slug}),
            body=maybe_transform(
                {
                    "username": username,
                    "email": email,
                },
                member_create_params.MemberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DmmTournamentMemberAdd,
        )

    def delete(
        self,
        profile_id: str,
        *,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberDeleteResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Removes a directly added member. The member's open tournament orders are cancelled and their tournament holdings, position lots, and membership are deleted with no payout; the forfeit is then applied in the trading engine asynchronously. Removing a member from an active tournament records an exit that blocks them from rejoining it (`rejoinBlocked: true`); removal from a tournament that has not started does not.

        When a bound user group also supplies the member, nothing is removed: the membership is demoted to group-sourced and the response is `{ success: true, demoted: true }`. A member supplied only by a group cannot be removed here (409); remove them from the group or unbind the group instead.

        Args:
            profile_id: Path parameter.
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MemberDeleteResponse: Member removed, or demoted to group-sourced when a bound group still supplies them.

        Example:
            ```python
            member = client.dmm.tournaments.members.delete(
                slug="slug",
                profile_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if profile_id is None or (isinstance(profile_id, str) and not profile_id):
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._delete(
            path_template("/dmm/tournaments/{slug}/members/{profileId}", **{"slug": slug, "profileId": profile_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberDeleteResponse,
        )


class AsyncMembersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMembersResourceWithRawResponse:
        return AsyncMembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMembersResourceWithStreamingResponse:
        return AsyncMembersResourceWithStreamingResponse(self)

    async def list(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberListResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>



        Args:
            slug: Tournament slug.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MemberListResponse: Tournament members.

        Example:
            ```python
            member = await client.dmm.tournaments.members.list(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/dmm/tournaments/{slug}/members", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberListResponse,
        )

    async def create(
        self,
        slug: str,
        *,
        username: str | Omit = omit,
        email: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmmTournamentMemberAdd:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Add a member by username or email. The user must already belong to the tournament's organization. Idempotent: re-adding flags the row as `added_directly`.

        Args:
            slug: Tournament slug.
            username: Body parameter.
            email: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DmmTournamentMemberAdd: Member already belongs to the tournament.

        Example:
            ```python
            member = await client.dmm.tournaments.members.create(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._post(
            path_template("/dmm/tournaments/{slug}/members", **{"slug": slug}),
            body=await async_maybe_transform(
                {
                    "username": username,
                    "email": email,
                },
                member_create_params.MemberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DmmTournamentMemberAdd,
        )

    async def delete(
        self,
        profile_id: str,
        *,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberDeleteResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Removes a directly added member. The member's open tournament orders are cancelled and their tournament holdings, position lots, and membership are deleted with no payout; the forfeit is then applied in the trading engine asynchronously. Removing a member from an active tournament records an exit that blocks them from rejoining it (`rejoinBlocked: true`); removal from a tournament that has not started does not.

        When a bound user group also supplies the member, nothing is removed: the membership is demoted to group-sourced and the response is `{ success: true, demoted: true }`. A member supplied only by a group cannot be removed here (409); remove them from the group or unbind the group instead.

        Args:
            profile_id: Path parameter.
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MemberDeleteResponse: Member removed, or demoted to group-sourced when a bound group still supplies them.

        Example:
            ```python
            member = await client.dmm.tournaments.members.delete(
                slug="slug",
                profile_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if profile_id is None or (isinstance(profile_id, str) and not profile_id):
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._delete(
            path_template("/dmm/tournaments/{slug}/members/{profileId}", **{"slug": slug, "profileId": profile_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberDeleteResponse,
        )


class MembersResourceWithRawResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.list = to_raw_response_wrapper(
            members.list,
        )
        self.create = to_raw_response_wrapper(
            members.create,
        )
        self.delete = to_raw_response_wrapper(
            members.delete,
        )


class AsyncMembersResourceWithRawResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.list = async_to_raw_response_wrapper(
            members.list,
        )
        self.create = async_to_raw_response_wrapper(
            members.create,
        )
        self.delete = async_to_raw_response_wrapper(
            members.delete,
        )


class MembersResourceWithStreamingResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.list = to_streamed_response_wrapper(
            members.list,
        )
        self.create = to_streamed_response_wrapper(
            members.create,
        )
        self.delete = to_streamed_response_wrapper(
            members.delete,
        )


class AsyncMembersResourceWithStreamingResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.list = async_to_streamed_response_wrapper(
            members.list,
        )
        self.create = async_to_streamed_response_wrapper(
            members.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            members.delete,
        )
