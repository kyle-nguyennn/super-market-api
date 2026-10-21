# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional
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
from .markets import (
    MarketsResource,
    AsyncMarketsResource,
    MarketsResourceWithRawResponse,
    AsyncMarketsResourceWithRawResponse,
    MarketsResourceWithStreamingResponse,
    AsyncMarketsResourceWithStreamingResponse,
)
from .portfolio import (
    PortfolioResource,
    AsyncPortfolioResource,
    PortfolioResourceWithRawResponse,
    AsyncPortfolioResourceWithRawResponse,
    PortfolioResourceWithStreamingResponse,
    AsyncPortfolioResourceWithStreamingResponse,
)
from .me import (
    MeResource,
    AsyncMeResource,
    MeResourceWithRawResponse,
    AsyncMeResourceWithRawResponse,
    MeResourceWithStreamingResponse,
    AsyncMeResourceWithStreamingResponse,
)
from ...types.tournament_list_response import TournamentListResponse
from ...types import tournament_list_params, tournament_list_leaderboard_params
from ...types.tournament_retrieve_response import TournamentRetrieveResponse
from ...types.tournament_list_leaderboard_response import TournamentListLeaderboardResponse
from ...types.tournament_list_seasons_response import TournamentListSeasonsResponse

__all__ = ["TournamentsResource", "AsyncTournamentsResource"]


class TournamentsResource(SyncAPIResource):
    @cached_property
    def markets(self) -> MarketsResource:
        return MarketsResource(self._client)

    @cached_property
    def portfolio(self) -> PortfolioResource:
        return PortfolioResource(self._client)

    @cached_property
    def me(self) -> MeResource:
        return MeResource(self._client)

    @cached_property
    def with_raw_response(self) -> TournamentsResourceWithRawResponse:
        return TournamentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TournamentsResourceWithStreamingResponse:
        return TournamentsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        status: Literal["draft", "active", "ended", "any"] | Omit = omit,
        limit: int | Omit = omit,
        offset: Optional[int] | Omit = omit,
        market_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TournamentListResponse:
        """
        Returns all tournaments the authenticated user can access, including open organization tournaments before first-action enrolment. Owners and admins of an organization also see every private tournament of that organization before they join.

        Args:
            status: Filter by tournament status. Omit or pass `any` for all statuses.
            limit: Results per page (max 100).
            offset: Number of records to skip.
            market_id: Restrict results to tournaments containing this market.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TournamentListResponse: List of tournaments the caller can access.

        Example:
            ```python
            tournament = client.tournaments.list(
                status="any",
                limit=50,
                offset=0,
            )
            ```
        """
        return self._get(
            "/tournaments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"status": status, "limit": limit, "offset": offset, "market_id": market_id},
                    tournament_list_params.TournamentListParams,
                ),
            ),
            cast_to=TournamentListResponse,
        )

    def retrieve(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TournamentRetrieveResponse:
        """
        Returns metadata and the authenticated member's current virtual balance for the tournament. The response `id` is the tournament UUID to pass as `tournamentId` on exchange price/orderbook and trading requests; the path itself uses the stable slug. Returns 403 if the caller is not a member, unless the tournament is open or the caller owns or administers the tournament's organization.

        Args:
            slug: Tournament slug.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TournamentRetrieveResponse: Tournament info.

        Example:
            ```python
            tournament = client.tournaments.retrieve(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/tournaments/{slug}", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TournamentRetrieveResponse,
        )

    def list_leaderboard(
        self,
        slug: str,
        *,
        period: Literal["1d", "7d", "30d", "all"] | Omit = omit,
        limit: int | Omit = omit,
        offset: Optional[int] | Omit = omit,
        group_id: str | Omit = omit,
        season: str | Omit = omit,
        sort: Literal["pnl", "roi", "winRate", "volume", "trades"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TournamentListLeaderboardResponse:
        """
        Returns members ranked within the tournament by the selected `sort` (P&L by default). `rank` and `myRank` follow the selected sort, and `myRank` is computed against the **same period** as the rankings list. `null` if the caller has not traded in the period (unranked). Ranks use standard competition ranking: tied entries share a rank and the positions that follow skip by the size of the tie (1-1-3).

        **Period semantics (calendar-aligned, UTC):**
        - `1d` — Today (since 00:00 UTC today)
        - `7d` — This Week (since 00:00 UTC on the most recent Sunday)
        - `30d` — This Month (since 00:00 UTC on the 1st of the current month)
        - `all` — All-time

        Baselines come from the daily tournament-portfolio snapshot taken at 00:00 UTC.

        On **Ongoing Play** tournaments, rankings never cross a season reset: `all` covers the current season, and `1d`/`7d`/`30d` start no earlier than the last reset.

        `groupId` filters to members of a user group bound to the tournament. Ongoing Play tournaments additionally support `season` (archived snapshots). An archived `season` key requires `period=all`; its entries use the archived shape (`finalTotalValue` / `finalBalance` instead of `pnl`), and the response omits `sort`.

        Args:
            slug: Tournament slug.
            period: Calendar-aligned period (UTC). `1d` = today, `7d` = this week (Sunday-anchored), `30d` = this month, `all` = all-time.
            limit: Results per page (max 100).
            offset: Offset for pagination.
            group_id: Optional user-group filter. Must be a group bound to the tournament (see `boundGroups` in the response).
            season: Ongoing Play tournaments only. Archived season key (e.g. `2026-Q1`) or `current`. An archived key requires `period=all`.
            sort: Ranking key for `rank` and `myRank`. Ignored for archived seasons.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TournamentListLeaderboardResponse: Tournament leaderboard.

        Example:
            ```python
            tournament = client.tournaments.list_leaderboard(
                slug="alpha-tournament",
                period="all",
                limit=50,
                offset=0,
                sort="pnl",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/tournaments/{slug}/leaderboard", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "period": period,
                        "limit": limit,
                        "offset": offset,
                        "group_id": group_id,
                        "season": season,
                        "sort": sort,
                    },
                    tournament_list_leaderboard_params.TournamentListLeaderboardParams,
                ),
            ),
            cast_to=TournamentListLeaderboardResponse,
        )

    def list_seasons(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TournamentListSeasonsResponse:
        """
        Lists the current season + archived snapshots for an **Ongoing Play** tournament. Returns 404 for other tournaments, which have no seasons.

        Args:
            slug: Tournament slug.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TournamentListSeasonsResponse: Current season + archived seasons (newest first).

        Example:
            ```python
            tournament = client.tournaments.list_seasons(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/tournaments/{slug}/seasons", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TournamentListSeasonsResponse,
        )


class AsyncTournamentsResource(AsyncAPIResource):
    @cached_property
    def markets(self) -> AsyncMarketsResource:
        return AsyncMarketsResource(self._client)

    @cached_property
    def portfolio(self) -> AsyncPortfolioResource:
        return AsyncPortfolioResource(self._client)

    @cached_property
    def me(self) -> AsyncMeResource:
        return AsyncMeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTournamentsResourceWithRawResponse:
        return AsyncTournamentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTournamentsResourceWithStreamingResponse:
        return AsyncTournamentsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        status: Literal["draft", "active", "ended", "any"] | Omit = omit,
        limit: int | Omit = omit,
        offset: Optional[int] | Omit = omit,
        market_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TournamentListResponse:
        """
        Returns all tournaments the authenticated user can access, including open organization tournaments before first-action enrolment. Owners and admins of an organization also see every private tournament of that organization before they join.

        Args:
            status: Filter by tournament status. Omit or pass `any` for all statuses.
            limit: Results per page (max 100).
            offset: Number of records to skip.
            market_id: Restrict results to tournaments containing this market.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TournamentListResponse: List of tournaments the caller can access.

        Example:
            ```python
            tournament = await client.tournaments.list(
                status="any",
                limit=50,
                offset=0,
            )
            ```
        """
        return await self._get(
            "/tournaments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"status": status, "limit": limit, "offset": offset, "market_id": market_id},
                    tournament_list_params.TournamentListParams,
                ),
            ),
            cast_to=TournamentListResponse,
        )

    async def retrieve(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TournamentRetrieveResponse:
        """
        Returns metadata and the authenticated member's current virtual balance for the tournament. The response `id` is the tournament UUID to pass as `tournamentId` on exchange price/orderbook and trading requests; the path itself uses the stable slug. Returns 403 if the caller is not a member, unless the tournament is open or the caller owns or administers the tournament's organization.

        Args:
            slug: Tournament slug.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TournamentRetrieveResponse: Tournament info.

        Example:
            ```python
            tournament = await client.tournaments.retrieve(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/tournaments/{slug}", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TournamentRetrieveResponse,
        )

    async def list_leaderboard(
        self,
        slug: str,
        *,
        period: Literal["1d", "7d", "30d", "all"] | Omit = omit,
        limit: int | Omit = omit,
        offset: Optional[int] | Omit = omit,
        group_id: str | Omit = omit,
        season: str | Omit = omit,
        sort: Literal["pnl", "roi", "winRate", "volume", "trades"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TournamentListLeaderboardResponse:
        """
        Returns members ranked within the tournament by the selected `sort` (P&L by default). `rank` and `myRank` follow the selected sort, and `myRank` is computed against the **same period** as the rankings list. `null` if the caller has not traded in the period (unranked). Ranks use standard competition ranking: tied entries share a rank and the positions that follow skip by the size of the tie (1-1-3).

        **Period semantics (calendar-aligned, UTC):**
        - `1d` — Today (since 00:00 UTC today)
        - `7d` — This Week (since 00:00 UTC on the most recent Sunday)
        - `30d` — This Month (since 00:00 UTC on the 1st of the current month)
        - `all` — All-time

        Baselines come from the daily tournament-portfolio snapshot taken at 00:00 UTC.

        On **Ongoing Play** tournaments, rankings never cross a season reset: `all` covers the current season, and `1d`/`7d`/`30d` start no earlier than the last reset.

        `groupId` filters to members of a user group bound to the tournament. Ongoing Play tournaments additionally support `season` (archived snapshots). An archived `season` key requires `period=all`; its entries use the archived shape (`finalTotalValue` / `finalBalance` instead of `pnl`), and the response omits `sort`.

        Args:
            slug: Tournament slug.
            period: Calendar-aligned period (UTC). `1d` = today, `7d` = this week (Sunday-anchored), `30d` = this month, `all` = all-time.
            limit: Results per page (max 100).
            offset: Offset for pagination.
            group_id: Optional user-group filter. Must be a group bound to the tournament (see `boundGroups` in the response).
            season: Ongoing Play tournaments only. Archived season key (e.g. `2026-Q1`) or `current`. An archived key requires `period=all`.
            sort: Ranking key for `rank` and `myRank`. Ignored for archived seasons.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TournamentListLeaderboardResponse: Tournament leaderboard.

        Example:
            ```python
            tournament = await client.tournaments.list_leaderboard(
                slug="alpha-tournament",
                period="all",
                limit=50,
                offset=0,
                sort="pnl",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/tournaments/{slug}/leaderboard", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "period": period,
                        "limit": limit,
                        "offset": offset,
                        "group_id": group_id,
                        "season": season,
                        "sort": sort,
                    },
                    tournament_list_leaderboard_params.TournamentListLeaderboardParams,
                ),
            ),
            cast_to=TournamentListLeaderboardResponse,
        )

    async def list_seasons(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TournamentListSeasonsResponse:
        """
        Lists the current season + archived snapshots for an **Ongoing Play** tournament. Returns 404 for other tournaments, which have no seasons.

        Args:
            slug: Tournament slug.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TournamentListSeasonsResponse: Current season + archived seasons (newest first).

        Example:
            ```python
            tournament = await client.tournaments.list_seasons(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/tournaments/{slug}/seasons", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TournamentListSeasonsResponse,
        )


class TournamentsResourceWithRawResponse:
    def __init__(self, tournaments: TournamentsResource) -> None:
        self._tournaments = tournaments

        self.list = to_raw_response_wrapper(
            tournaments.list,
        )
        self.retrieve = to_raw_response_wrapper(
            tournaments.retrieve,
        )
        self.list_leaderboard = to_raw_response_wrapper(
            tournaments.list_leaderboard,
        )
        self.list_seasons = to_raw_response_wrapper(
            tournaments.list_seasons,
        )

    @cached_property
    def markets(self) -> MarketsResourceWithRawResponse:
        return MarketsResourceWithRawResponse(self._tournaments.markets)

    @cached_property
    def portfolio(self) -> PortfolioResourceWithRawResponse:
        return PortfolioResourceWithRawResponse(self._tournaments.portfolio)

    @cached_property
    def me(self) -> MeResourceWithRawResponse:
        return MeResourceWithRawResponse(self._tournaments.me)


class AsyncTournamentsResourceWithRawResponse:
    def __init__(self, tournaments: AsyncTournamentsResource) -> None:
        self._tournaments = tournaments

        self.list = async_to_raw_response_wrapper(
            tournaments.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tournaments.retrieve,
        )
        self.list_leaderboard = async_to_raw_response_wrapper(
            tournaments.list_leaderboard,
        )
        self.list_seasons = async_to_raw_response_wrapper(
            tournaments.list_seasons,
        )

    @cached_property
    def markets(self) -> AsyncMarketsResourceWithRawResponse:
        return AsyncMarketsResourceWithRawResponse(self._tournaments.markets)

    @cached_property
    def portfolio(self) -> AsyncPortfolioResourceWithRawResponse:
        return AsyncPortfolioResourceWithRawResponse(self._tournaments.portfolio)

    @cached_property
    def me(self) -> AsyncMeResourceWithRawResponse:
        return AsyncMeResourceWithRawResponse(self._tournaments.me)


class TournamentsResourceWithStreamingResponse:
    def __init__(self, tournaments: TournamentsResource) -> None:
        self._tournaments = tournaments

        self.list = to_streamed_response_wrapper(
            tournaments.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            tournaments.retrieve,
        )
        self.list_leaderboard = to_streamed_response_wrapper(
            tournaments.list_leaderboard,
        )
        self.list_seasons = to_streamed_response_wrapper(
            tournaments.list_seasons,
        )

    @cached_property
    def markets(self) -> MarketsResourceWithStreamingResponse:
        return MarketsResourceWithStreamingResponse(self._tournaments.markets)

    @cached_property
    def portfolio(self) -> PortfolioResourceWithStreamingResponse:
        return PortfolioResourceWithStreamingResponse(self._tournaments.portfolio)

    @cached_property
    def me(self) -> MeResourceWithStreamingResponse:
        return MeResourceWithStreamingResponse(self._tournaments.me)


class AsyncTournamentsResourceWithStreamingResponse:
    def __init__(self, tournaments: AsyncTournamentsResource) -> None:
        self._tournaments = tournaments

        self.list = async_to_streamed_response_wrapper(
            tournaments.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tournaments.retrieve,
        )
        self.list_leaderboard = async_to_streamed_response_wrapper(
            tournaments.list_leaderboard,
        )
        self.list_seasons = async_to_streamed_response_wrapper(
            tournaments.list_seasons,
        )

    @cached_property
    def markets(self) -> AsyncMarketsResourceWithStreamingResponse:
        return AsyncMarketsResourceWithStreamingResponse(self._tournaments.markets)

    @cached_property
    def portfolio(self) -> AsyncPortfolioResourceWithStreamingResponse:
        return AsyncPortfolioResourceWithStreamingResponse(self._tournaments.portfolio)

    @cached_property
    def me(self) -> AsyncMeResourceWithStreamingResponse:
        return AsyncMeResourceWithStreamingResponse(self._tournaments.me)
