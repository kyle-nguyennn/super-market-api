# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional, Union
from datetime import datetime
from typing_extensions import Literal
from ...._types import SequenceNotStr

from ...._types import Body, Omit, Query, Headers, NotGiven, NoneType, omit, not_given
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
from .end_settlement import (
    EndSettlementResource,
    AsyncEndSettlementResource,
    EndSettlementResourceWithRawResponse,
    AsyncEndSettlementResourceWithRawResponse,
    EndSettlementResourceWithStreamingResponse,
    AsyncEndSettlementResourceWithStreamingResponse,
)
from .settlement_overrides import (
    SettlementOverridesResource,
    AsyncSettlementOverridesResource,
    SettlementOverridesResourceWithRawResponse,
    AsyncSettlementOverridesResourceWithRawResponse,
    SettlementOverridesResourceWithStreamingResponse,
    AsyncSettlementOverridesResourceWithStreamingResponse,
)
from .markets import (
    MarketsResource,
    AsyncMarketsResource,
    MarketsResourceWithRawResponse,
    AsyncMarketsResourceWithRawResponse,
    MarketsResourceWithStreamingResponse,
    AsyncMarketsResourceWithStreamingResponse,
)
from .members import (
    MembersResource,
    AsyncMembersResource,
    MembersResourceWithRawResponse,
    AsyncMembersResourceWithRawResponse,
    MembersResourceWithStreamingResponse,
    AsyncMembersResourceWithStreamingResponse,
)
from .market_groups import (
    MarketGroupsResource,
    AsyncMarketGroupsResource,
    MarketGroupsResourceWithRawResponse,
    AsyncMarketGroupsResourceWithRawResponse,
    MarketGroupsResourceWithStreamingResponse,
    AsyncMarketGroupsResourceWithStreamingResponse,
)
from .user_groups import (
    UserGroupsResource,
    AsyncUserGroupsResource,
    UserGroupsResourceWithRawResponse,
    AsyncUserGroupsResourceWithRawResponse,
    UserGroupsResourceWithStreamingResponse,
    AsyncUserGroupsResourceWithStreamingResponse,
)
from .exchanges import (
    ExchangesResource,
    AsyncExchangesResource,
    ExchangesResourceWithRawResponse,
    AsyncExchangesResourceWithRawResponse,
    ExchangesResourceWithStreamingResponse,
    AsyncExchangesResourceWithStreamingResponse,
)
from ....types.dmm.designated_market_maker_tournament_list import DesignatedMarketMakerTournamentList
from ....types.dmm import (
    tournament_list_params,
    tournament_create_params,
    tournament_update_params,
    tournament_create_reset_balances_params,
    tournament_list_rankings_params,
    tournament_list_market_assignments_params,
    tournament_list_trades_params,
    tournament_list_orders_params,
    tournament_list_transactions_params,
    tournament_list_inventory_params,
)
from ....types.dmm.designated_market_maker_tournament_create import DesignatedMarketMakerTournamentCreate
from ....types.dmm.designated_market_maker_tournament import DesignatedMarketMakerTournament
from ....types.dmm.designated_market_maker_reset_balances import DesignatedMarketMakerResetBalances
from ....types.dmm.designated_market_maker_tournament_rankings import DesignatedMarketMakerTournamentRankings
from ....types.dmm.tournament_list_market_assignments_response import TournamentListMarketAssignmentsResponse
from ....types.dmm.designated_market_maker_trade_list import DesignatedMarketMakerTradeList
from ....types.dmm.designated_market_maker_order_list import DesignatedMarketMakerOrderList
from ....types.dmm.designated_market_maker_transaction_list import DesignatedMarketMakerTransactionList
from ....types.dmm.dmm_inventory import DmmInventory

__all__ = ["TournamentsResource", "AsyncTournamentsResource"]


class TournamentsResource(SyncAPIResource):
    @cached_property
    def end_settlement(self) -> EndSettlementResource:
        return EndSettlementResource(self._client)

    @cached_property
    def settlement_overrides(self) -> SettlementOverridesResource:
        return SettlementOverridesResource(self._client)

    @cached_property
    def markets(self) -> MarketsResource:
        return MarketsResource(self._client)

    @cached_property
    def members(self) -> MembersResource:
        return MembersResource(self._client)

    @cached_property
    def market_groups(self) -> MarketGroupsResource:
        return MarketGroupsResource(self._client)

    @cached_property
    def user_groups(self) -> UserGroupsResource:
        return UserGroupsResource(self._client)

    @cached_property
    def exchanges(self) -> ExchangesResource:
        return ExchangesResource(self._client)

    @cached_property
    def with_raw_response(self) -> TournamentsResourceWithRawResponse:
        return TournamentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TournamentsResourceWithStreamingResponse:
        return TournamentsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        organization_slug: str | Omit = omit,
        archived: Literal["active", "archived", "all"] | Omit = omit,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerTournamentList:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Admin-only endpoint that lists tournaments, optionally scoped to a single organization. Requires an API key with the `admin` scope.

        Args:
            organization_slug: Filter to a single organization's tournaments.
            archived: Select active tournaments (default), archived tournaments, or all tournaments.
            limit: Query parameter.
            cursor: Opaque pagination cursor from a prior response.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerTournamentList: Tournaments page.

        Example:
            ```python
            tournament = client.dmm.tournaments.list()
            ```
        """
        return self._get(
            "/dmm/tournaments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_slug": organization_slug, "archived": archived, "limit": limit, "cursor": cursor},
                    tournament_list_params.TournamentListParams,
                ),
            ),
            cast_to=DesignatedMarketMakerTournamentList,
        )

    def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        start_date: Union[str, datetime] | Omit = omit,
        end_date: Union[str, datetime],
        initial_virtual_balance: float | Omit = omit,
        auto_enroll_on_signup: bool | Omit = omit,
        currency_name: str | Omit = omit,
        organization_slug: str,
        mode: Literal["cfmm", "p2p"] | Omit = omit,
        visibility: Literal["private", "open"] | Omit = omit,
        logo_url: Optional[str] | Omit = omit,
        banner_url: Optional[str] | Omit = omit,
        market_group_ids: SequenceNotStr[str] | Omit = omit,
        user_group_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerTournamentCreate:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Admin-only designated-market-maker endpoint for creating an organization-scoped tournament. Requires an API key with the `admin` scope and an admin role on the caller's account.

        Optional `marketGroupIds` / `userGroupIds` bind existing groups of the tournament's organization in the same transaction as the tournament row; the response echoes the bound ids. The groups' markets and members are then materialized asynchronously, exactly as when a group is bound later.

        Args:
            name: Body parameter.
            description: Body parameter.
            start_date: Tournament start. Defaults to the time of the request when omitted. When supplied, it must not be more than 60 seconds in the past (400), and `endDate` must be after it (400).
            end_date: Body parameter.
            initial_virtual_balance: Body parameter.
            auto_enroll_on_signup: Defaults false. Enable only for open, scheduled organization tournaments. Applies to future registrations only; default-tournament selection is independent.
            currency_name: Display name for the tournament's virtual currency. When the owning organization locks its currency name, this must match that name exactly — any other value is rejected with 400. Omit it to inherit the organization's name.
            organization_slug: Slug of the organization that will own this tournament. Org slugs are immutable.
            mode: Trading mode. `p2p` = peer-to-peer orderbook seeded with maker quotes (default). `cfmm` = constant-function market maker (automatic price curve).
            visibility: `private` requires tournament membership, except for owners and admins of the organization, who can browse every organization tournament and are enrolled on first action. `open` allows organization members to browse and be enrolled on first action.
            logo_url: Body parameter.
            banner_url: Body parameter.
            market_group_ids: Existing market groups of the tournament's organization to bind at creation (duplicates are ignored). Their markets are attached asynchronously, as with POST /dmm/tournaments/{slug}/market-groups. An unknown id returns 404; a group from another organization, or one containing a market already attached to another organization's tournament, returns 400.
            user_group_ids: Existing user groups of the tournament's organization to bind at creation (duplicates are ignored). Their members are enrolled asynchronously, as with POST /dmm/tournaments/{slug}/user-groups. An unknown id returns 404; a group from another organization returns 400.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerTournamentCreate: Tournament created, with any groups bound.

        Example:
            ```python
            tournament = client.dmm.tournaments.create(
                name="Alpha Tournament",
                end_date="2026-07-01T00:00:00.000Z",
                organization_slug="acme-corp",
            )
            ```
        """
        return self._post(
            "/dmm/tournaments",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "start_date": start_date,
                    "end_date": end_date,
                    "initial_virtual_balance": initial_virtual_balance,
                    "auto_enroll_on_signup": auto_enroll_on_signup,
                    "currency_name": currency_name,
                    "organization_slug": organization_slug,
                    "mode": mode,
                    "visibility": visibility,
                    "logo_url": logo_url,
                    "banner_url": banner_url,
                    "market_group_ids": market_group_ids,
                    "user_group_ids": user_group_ids,
                },
                tournament_create_params.TournamentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignatedMarketMakerTournamentCreate,
        )

    def update(
        self,
        slug: str,
        *,
        name: str | Omit = omit,
        description: Optional[str] | Omit = omit,
        start_date: Union[str, datetime] | Omit = omit,
        initial_virtual_balance: float | Omit = omit,
        auto_enroll_on_signup: bool | Omit = omit,
        currency_name: str | Omit = omit,
        visibility: Literal["private", "open"] | Omit = omit,
        logo_url: Optional[str] | Omit = omit,
        banner_url: Optional[str] | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerTournament:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Admin-only designated-market-maker endpoint for updating tournament settings. Requires an API key with the `admin` scope and an admin role on the caller's account. The body must contain at least one field, and unknown fields are rejected.

        - Ended tournaments cannot be modified (409).
        - `startDate` must not be more than 60 seconds in the past whenever it is supplied (400), even when it equals the stored start, so omit it unless you are changing it. Changing it is allowed only while the tournament is a draft (not yet started); otherwise 409.
        - `initialVirtualBalance` can change only while the tournament is a draft; otherwise 409. Sending the current value is accepted. Changing it on a draft resets every existing member's balance to the new amount.
        - `endDate` must be after the start date (400), and an active tournament cannot be given an `endDate` in the past (409).
        - Currency name changes are rejected after the tournament's first trade (409); sending the current currency name remains valid. A name that diverges from a locked organization currency name returns 400.
        - The organization's default tournament cannot be made `private` (409). The visibility of Ongoing Play cannot be changed (400), and a tournament without an organization cannot be made `open` (400).
        - `autoEnrollOnSignup: true` requires an open, scheduled organization tournament (400 otherwise).
        - While another tournament operation (such as a balance reset) is in progress, the update returns 409; retry after it completes.

        Args:
            slug: Tournament slug.
            name: Body parameter.
            description: Body parameter.
            start_date: New start date. When supplied, it must not be more than 60 seconds in the past (400) — even if it equals the stored value — so omit it unless you are changing it. Changing it is allowed only while the tournament is a draft (409 otherwise).
            initial_virtual_balance: Body parameter.
            auto_enroll_on_signup: Defaults false. Enable only for open, scheduled organization tournaments. Applies to future registrations only; default-tournament selection is independent.
            currency_name: Display name for the tournament's virtual currency. When the owning organization locks its currency name, this must match that name exactly — any other value is rejected with 400. Omit it to inherit the organization's name.
            visibility: `private` requires tournament membership, except for owners and admins of the organization, who can browse every organization tournament and are enrolled on first action. `open` allows organization members to browse and be enrolled on first action.
            logo_url: Body parameter.
            banner_url: Body parameter.
            end_date: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerTournament: Tournament updated.

        Example:
            ```python
            tournament = client.dmm.tournaments.update(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._patch(
            path_template("/dmm/tournaments/{slug}", **{"slug": slug}),
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "start_date": start_date,
                    "initial_virtual_balance": initial_virtual_balance,
                    "auto_enroll_on_signup": auto_enroll_on_signup,
                    "currency_name": currency_name,
                    "visibility": visibility,
                    "logo_url": logo_url,
                    "banner_url": banner_url,
                    "end_date": end_date,
                },
                tournament_update_params.TournamentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignatedMarketMakerTournament,
        )

    def delete(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Admin-only designated-market-maker endpoint for deleting a draft tournament. Active and ended tournaments cannot be deleted, nor can the organization's default tournament or a tournament with an attached market already settled for its organization. The API key's owner must have an email address, which is recorded in the deletion audit.

        Args:
            slug: Tournament slug.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Tournament deleted.

        Example:
            ```python
            client.dmm.tournaments.delete(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/dmm/tournaments/{slug}", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_reset_balances(
        self,
        slug: str,
        *,
        confirm: str,
        reset_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerResetBalances:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Admin-only endpoint that cancels open tournament orders, deletes tournament-scoped holdings, position lots, portfolio snapshots, and the tournament's super-signal data (market signals, signal elites, signal trader metrics, and cohort cuts), and resets every member balance to the tournament's initial virtual balance. Each affected member gets a `BALANCE_RESET` ledger transaction for the difference. Past trades and transactions remain for audit. Ended tournaments cannot be reset. The API key's owner must have an email address, which is recorded in the admin audit.

        **Destructive.** Body must contain `{ "confirm": "<slug>", "resetKey": "<stable-key>" }`; `confirm` must match the path slug. The client-supplied `resetKey` is required so timeouts and lost responses can be retried safely. A committed attempt replays its stored response without repeating the destructive DB or engine phases; an interrupted attempt is resumed. Treat `503 TX_CONFLICT` as transient and retry with backoff using the same key.

        Args:
            slug: Tournament slug.
            confirm: Must match the path `slug` exactly. Guards against accidental destructive calls.
            reset_key: Required stable client retry key. Reuse the same value after a timeout or `503 TX_CONFLICT`; a committed reset is replayed and an interrupted reset is resumed.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerResetBalances: Tournament live state reset.

        Example:
            ```python
            tournament = client.dmm.tournaments.create_reset_balances(
                slug="alpha-tournament",
                confirm="alpha-tournament",
                reset_key="quarterly-reset-2026-q3",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._post(
            path_template("/dmm/tournaments/{slug}/reset-balances", **{"slug": slug}),
            body=maybe_transform(
                {
                    "confirm": confirm,
                    "reset_key": reset_key,
                },
                tournament_create_reset_balances_params.TournamentCreateResetBalancesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignatedMarketMakerResetBalances,
        )

    def list_rankings(
        self,
        slug: str,
        *,
        market_type: Literal[
            "global",
            "Election Outcome",
            "Financial Product",
            "Freeform",
            "Economic Indicator",
            "Sports Outcome",
            "Corporate Earnings",
            "Imported Market",
        ]
        | Omit = omit,
        sort_by: Literal[
            "smartScore",
            "smartScoreRaw",
            "roi",
            "sharpe",
            "winRate",
            "realizedPnl",
            "unrealizedPnl",
            "totalStake",
            "trades",
            "balance",
        ]
        | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        limit: int | Omit = omit,
        offset: Optional[int] | Omit = omit,
        user_group_id: str | Omit = omit,
        market_group_id: str | Omit = omit,
        period: Literal["1d", "7d", "30d", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerTournamentRankings:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Per-tournament user rankings. Requires owner/admin role in the tournament's organization. Reads from the latest `tournament_trader_metrics` snapshot for the requested `marketType` by default, joined with `tournament_members` so members without a snapshot still appear (with zeroed metric fields). Adds the current authoritative engine balance and exposes it as a sortable column.

        Pass `userGroupId` to restrict rows to members of a user group bound to this tournament; ranks are recomputed within the filtered set.

        Pass `marketGroupId` and/or `period` to switch to an on-demand recompute that scopes trader metrics to trades inside that market group and/or within the calendar-aligned window. The response `computed` field indicates which path served the request. Ranks use standard competition ranking: tied entries share a rank and the positions that follow skip by the size of the tie (1-1-3).

        Args:
            slug: Tournament slug.
            market_type: Trader-metrics bucket: `global` aggregates across all market types; any other value restricts metrics to that market type. Defaults to `global`.
            sort_by: Column to rank by. `balance` is the member's current virtual-cash balance; everything else comes from the latest trader-metrics snapshot.
            order: Query parameter.
            limit: Query parameter.
            offset: Query parameter.
            user_group_id: Optional user-group filter. Must be a group bound to the tournament via `tournament_user_groups`; otherwise the request is rejected with a validation error. Ranks are recomputed within the filtered set.
            market_group_id: Optional market-group filter. Must be a `market_group` belonging to the tournament's organization; otherwise the request is rejected with a validation error. Switches the response to on-demand metrics scoped to trades within the group.
            period: Calendar-aligned period filter (UTC). `1d` = today, `7d` = since most recent Sunday, `30d` = since 1st of the current month, `all` = no time filter. When set to anything other than `all`, metrics are recomputed on-demand and `computed` will be `on-demand`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerTournamentRankings: Tournament rankings page.

        Example:
            ```python
            tournament = client.dmm.tournaments.list_rankings(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/dmm/tournaments/{slug}/rankings", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "market_type": market_type,
                        "sort_by": sort_by,
                        "order": order,
                        "limit": limit,
                        "offset": offset,
                        "user_group_id": user_group_id,
                        "market_group_id": market_group_id,
                        "period": period,
                    },
                    tournament_list_rankings_params.TournamentListRankingsParams,
                ),
            ),
            cast_to=DesignatedMarketMakerTournamentRankings,
        )

    def list_market_assignments(
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
    ) -> TournamentListMarketAssignmentsResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Returns administrative assignment metadata for markets attached directly or supplied by bound market groups, newest first, with opaque cursor pagination. This is not a market-data feed: use `/markets` with the appropriate API-key scope or `tournamentId` for exchange IDs and prices.

        Args:
            slug: Tournament slug.
            limit: Page size (default 50, max 200).
            cursor: Opaque pagination cursor from a prior response. It marks the last row served rather than a row offset, so rows added or removed between pages neither repeat a row nor hide an unseen one.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TournamentListMarketAssignmentsResponse: Tournament market assignments page.

        Example:
            ```python
            tournament = client.dmm.tournaments.list_market_assignments(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/dmm/tournaments/{slug}/market-assignments", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit, "cursor": cursor},
                    tournament_list_market_assignments_params.TournamentListMarketAssignmentsParams,
                ),
            ),
            cast_to=TournamentListMarketAssignmentsResponse,
        )

    def list_trades(
        self,
        slug: str,
        *,
        from_: Union[str, datetime] | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerTradeList:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Returns executed trades for the league, newest first, with both sides' identity fields. Org-scoped: an org API key may only read its own organization's tournaments. Supports `from`/`to` windowing and opaque cursor pagination.

        Args:
            slug: Tournament slug.
            from_: Inclusive lower bound on the row timestamp (ISO-8601 UTC).
            to: Inclusive upper bound on the row timestamp (ISO-8601 UTC).
            limit: Query parameter.
            cursor: Opaque time cursor returned as `nextCursor` by a prior page.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerTradeList: Trades page.

        Example:
            ```python
            designated_market_maker_trades = client.dmm.tournaments.list_trades(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/dmm/tournaments/{slug}/trades", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"from_": from_, "to": to, "limit": limit, "cursor": cursor},
                    tournament_list_trades_params.TournamentListTradesParams,
                ),
            ),
            cast_to=DesignatedMarketMakerTradeList,
        )

    def list_orders(
        self,
        slug: str,
        *,
        from_: Union[str, datetime] | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerOrderList:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Returns orders placed in the league, newest first, with the placing trader's identity fields. Org-scoped. Supports `from`/`to` windowing and opaque cursor pagination.

        Args:
            slug: Tournament slug.
            from_: Inclusive lower bound on the row timestamp (ISO-8601 UTC).
            to: Inclusive upper bound on the row timestamp (ISO-8601 UTC).
            limit: Query parameter.
            cursor: Opaque time cursor returned as `nextCursor` by a prior page.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerOrderList: Orders page.

        Example:
            ```python
            designated_market_maker_orders = client.dmm.tournaments.list_orders(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/dmm/tournaments/{slug}/orders", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"from_": from_, "to": to, "limit": limit, "cursor": cursor},
                    tournament_list_orders_params.TournamentListOrdersParams,
                ),
            ),
            cast_to=DesignatedMarketMakerOrderList,
        )

    def list_transactions(
        self,
        slug: str,
        *,
        from_: Union[str, datetime] | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerTransactionList:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Returns the league's virtual-balance ledger (opening balances, nominal trade cost/proceeds, separate ALL collateral advances/repayments/releases, settlement payouts/refunds/corrections, and balance resets), newest first, with the affected trader's identity fields. The nominal execution price is never rewritten: a collateral entry records the capital-efficiency adjustment atomically alongside its trade or lifecycle command. Tournaments run on virtual currency, so there are no real-money deposits, withdrawals, or fees. Org-scoped. Supports `from`/`to` windowing and opaque cursor pagination.

        Args:
            slug: Tournament slug.
            from_: Inclusive lower bound on the row timestamp (ISO-8601 UTC).
            to: Inclusive upper bound on the row timestamp (ISO-8601 UTC).
            limit: Query parameter.
            cursor: Opaque time cursor returned as `nextCursor` by a prior page.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerTransactionList: Transactions page.

        Example:
            ```python
            designated_market_maker_transactions = client.dmm.tournaments.list_transactions(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/dmm/tournaments/{slug}/transactions", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"from_": from_, "to": to, "limit": limit, "cursor": cursor},
                    tournament_list_transactions_params.TournamentListTransactionsParams,
                ),
            ),
            cast_to=DesignatedMarketMakerTransactionList,
        )

    def list_inventory(
        self,
        slug: str,
        *,
        market: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmmInventory:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Read-only snapshot of the managed `market_maker`'s inventory and risk across one P2P tournament. The maker's position is synthetic (it holds no `holdings` rows), so net inventory and net cash are reconstructed from its filled trades. Returns one row per outcome that the maker either holds inventory on or is quoting on (fully-closed, unquoted outcomes are omitted), grouped by market with a tournament-level rollup. Each row reports net inventory + net cash, mark-to-market value + unrealized PnL (via the tournament valuation price), resting bid/ask exposure, and worst-case settlement loss. Same admin / org-ownership gates as the liquidity endpoints.

        Args:
            slug: Tournament slug.
            market: Optional market id. When provided, the snapshot is scoped to that single market instead of every market the maker has exposure on, and the `summary` totals reflect only that market. The market must belong to the tournament (otherwise 404). Omit to list all markets.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DmmInventory: Inventory and exposure snapshot.

        Example:
            ```python
            tournament = client.dmm.tournaments.list_inventory(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/dmm/tournaments/{slug}/inventory", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"market": market}, tournament_list_inventory_params.TournamentListInventoryParams
                ),
            ),
            cast_to=DmmInventory,
        )


class AsyncTournamentsResource(AsyncAPIResource):
    @cached_property
    def end_settlement(self) -> AsyncEndSettlementResource:
        return AsyncEndSettlementResource(self._client)

    @cached_property
    def settlement_overrides(self) -> AsyncSettlementOverridesResource:
        return AsyncSettlementOverridesResource(self._client)

    @cached_property
    def markets(self) -> AsyncMarketsResource:
        return AsyncMarketsResource(self._client)

    @cached_property
    def members(self) -> AsyncMembersResource:
        return AsyncMembersResource(self._client)

    @cached_property
    def market_groups(self) -> AsyncMarketGroupsResource:
        return AsyncMarketGroupsResource(self._client)

    @cached_property
    def user_groups(self) -> AsyncUserGroupsResource:
        return AsyncUserGroupsResource(self._client)

    @cached_property
    def exchanges(self) -> AsyncExchangesResource:
        return AsyncExchangesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTournamentsResourceWithRawResponse:
        return AsyncTournamentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTournamentsResourceWithStreamingResponse:
        return AsyncTournamentsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        organization_slug: str | Omit = omit,
        archived: Literal["active", "archived", "all"] | Omit = omit,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerTournamentList:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Admin-only endpoint that lists tournaments, optionally scoped to a single organization. Requires an API key with the `admin` scope.

        Args:
            organization_slug: Filter to a single organization's tournaments.
            archived: Select active tournaments (default), archived tournaments, or all tournaments.
            limit: Query parameter.
            cursor: Opaque pagination cursor from a prior response.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerTournamentList: Tournaments page.

        Example:
            ```python
            tournament = await client.dmm.tournaments.list()
            ```
        """
        return await self._get(
            "/dmm/tournaments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_slug": organization_slug, "archived": archived, "limit": limit, "cursor": cursor},
                    tournament_list_params.TournamentListParams,
                ),
            ),
            cast_to=DesignatedMarketMakerTournamentList,
        )

    async def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        start_date: Union[str, datetime] | Omit = omit,
        end_date: Union[str, datetime],
        initial_virtual_balance: float | Omit = omit,
        auto_enroll_on_signup: bool | Omit = omit,
        currency_name: str | Omit = omit,
        organization_slug: str,
        mode: Literal["cfmm", "p2p"] | Omit = omit,
        visibility: Literal["private", "open"] | Omit = omit,
        logo_url: Optional[str] | Omit = omit,
        banner_url: Optional[str] | Omit = omit,
        market_group_ids: SequenceNotStr[str] | Omit = omit,
        user_group_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerTournamentCreate:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Admin-only designated-market-maker endpoint for creating an organization-scoped tournament. Requires an API key with the `admin` scope and an admin role on the caller's account.

        Optional `marketGroupIds` / `userGroupIds` bind existing groups of the tournament's organization in the same transaction as the tournament row; the response echoes the bound ids. The groups' markets and members are then materialized asynchronously, exactly as when a group is bound later.

        Args:
            name: Body parameter.
            description: Body parameter.
            start_date: Tournament start. Defaults to the time of the request when omitted. When supplied, it must not be more than 60 seconds in the past (400), and `endDate` must be after it (400).
            end_date: Body parameter.
            initial_virtual_balance: Body parameter.
            auto_enroll_on_signup: Defaults false. Enable only for open, scheduled organization tournaments. Applies to future registrations only; default-tournament selection is independent.
            currency_name: Display name for the tournament's virtual currency. When the owning organization locks its currency name, this must match that name exactly — any other value is rejected with 400. Omit it to inherit the organization's name.
            organization_slug: Slug of the organization that will own this tournament. Org slugs are immutable.
            mode: Trading mode. `p2p` = peer-to-peer orderbook seeded with maker quotes (default). `cfmm` = constant-function market maker (automatic price curve).
            visibility: `private` requires tournament membership, except for owners and admins of the organization, who can browse every organization tournament and are enrolled on first action. `open` allows organization members to browse and be enrolled on first action.
            logo_url: Body parameter.
            banner_url: Body parameter.
            market_group_ids: Existing market groups of the tournament's organization to bind at creation (duplicates are ignored). Their markets are attached asynchronously, as with POST /dmm/tournaments/{slug}/market-groups. An unknown id returns 404; a group from another organization, or one containing a market already attached to another organization's tournament, returns 400.
            user_group_ids: Existing user groups of the tournament's organization to bind at creation (duplicates are ignored). Their members are enrolled asynchronously, as with POST /dmm/tournaments/{slug}/user-groups. An unknown id returns 404; a group from another organization returns 400.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerTournamentCreate: Tournament created, with any groups bound.

        Example:
            ```python
            tournament = await client.dmm.tournaments.create(
                name="Alpha Tournament",
                end_date="2026-07-01T00:00:00.000Z",
                organization_slug="acme-corp",
            )
            ```
        """
        return await self._post(
            "/dmm/tournaments",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "start_date": start_date,
                    "end_date": end_date,
                    "initial_virtual_balance": initial_virtual_balance,
                    "auto_enroll_on_signup": auto_enroll_on_signup,
                    "currency_name": currency_name,
                    "organization_slug": organization_slug,
                    "mode": mode,
                    "visibility": visibility,
                    "logo_url": logo_url,
                    "banner_url": banner_url,
                    "market_group_ids": market_group_ids,
                    "user_group_ids": user_group_ids,
                },
                tournament_create_params.TournamentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignatedMarketMakerTournamentCreate,
        )

    async def update(
        self,
        slug: str,
        *,
        name: str | Omit = omit,
        description: Optional[str] | Omit = omit,
        start_date: Union[str, datetime] | Omit = omit,
        initial_virtual_balance: float | Omit = omit,
        auto_enroll_on_signup: bool | Omit = omit,
        currency_name: str | Omit = omit,
        visibility: Literal["private", "open"] | Omit = omit,
        logo_url: Optional[str] | Omit = omit,
        banner_url: Optional[str] | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerTournament:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Admin-only designated-market-maker endpoint for updating tournament settings. Requires an API key with the `admin` scope and an admin role on the caller's account. The body must contain at least one field, and unknown fields are rejected.

        - Ended tournaments cannot be modified (409).
        - `startDate` must not be more than 60 seconds in the past whenever it is supplied (400), even when it equals the stored start, so omit it unless you are changing it. Changing it is allowed only while the tournament is a draft (not yet started); otherwise 409.
        - `initialVirtualBalance` can change only while the tournament is a draft; otherwise 409. Sending the current value is accepted. Changing it on a draft resets every existing member's balance to the new amount.
        - `endDate` must be after the start date (400), and an active tournament cannot be given an `endDate` in the past (409).
        - Currency name changes are rejected after the tournament's first trade (409); sending the current currency name remains valid. A name that diverges from a locked organization currency name returns 400.
        - The organization's default tournament cannot be made `private` (409). The visibility of Ongoing Play cannot be changed (400), and a tournament without an organization cannot be made `open` (400).
        - `autoEnrollOnSignup: true` requires an open, scheduled organization tournament (400 otherwise).
        - While another tournament operation (such as a balance reset) is in progress, the update returns 409; retry after it completes.

        Args:
            slug: Tournament slug.
            name: Body parameter.
            description: Body parameter.
            start_date: New start date. When supplied, it must not be more than 60 seconds in the past (400) — even if it equals the stored value — so omit it unless you are changing it. Changing it is allowed only while the tournament is a draft (409 otherwise).
            initial_virtual_balance: Body parameter.
            auto_enroll_on_signup: Defaults false. Enable only for open, scheduled organization tournaments. Applies to future registrations only; default-tournament selection is independent.
            currency_name: Display name for the tournament's virtual currency. When the owning organization locks its currency name, this must match that name exactly — any other value is rejected with 400. Omit it to inherit the organization's name.
            visibility: `private` requires tournament membership, except for owners and admins of the organization, who can browse every organization tournament and are enrolled on first action. `open` allows organization members to browse and be enrolled on first action.
            logo_url: Body parameter.
            banner_url: Body parameter.
            end_date: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerTournament: Tournament updated.

        Example:
            ```python
            tournament = await client.dmm.tournaments.update(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._patch(
            path_template("/dmm/tournaments/{slug}", **{"slug": slug}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "start_date": start_date,
                    "initial_virtual_balance": initial_virtual_balance,
                    "auto_enroll_on_signup": auto_enroll_on_signup,
                    "currency_name": currency_name,
                    "visibility": visibility,
                    "logo_url": logo_url,
                    "banner_url": banner_url,
                    "end_date": end_date,
                },
                tournament_update_params.TournamentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignatedMarketMakerTournament,
        )

    async def delete(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Admin-only designated-market-maker endpoint for deleting a draft tournament. Active and ended tournaments cannot be deleted, nor can the organization's default tournament or a tournament with an attached market already settled for its organization. The API key's owner must have an email address, which is recorded in the deletion audit.

        Args:
            slug: Tournament slug.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Tournament deleted.

        Example:
            ```python
            await client.dmm.tournaments.delete(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/dmm/tournaments/{slug}", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_reset_balances(
        self,
        slug: str,
        *,
        confirm: str,
        reset_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerResetBalances:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Admin-only endpoint that cancels open tournament orders, deletes tournament-scoped holdings, position lots, portfolio snapshots, and the tournament's super-signal data (market signals, signal elites, signal trader metrics, and cohort cuts), and resets every member balance to the tournament's initial virtual balance. Each affected member gets a `BALANCE_RESET` ledger transaction for the difference. Past trades and transactions remain for audit. Ended tournaments cannot be reset. The API key's owner must have an email address, which is recorded in the admin audit.

        **Destructive.** Body must contain `{ "confirm": "<slug>", "resetKey": "<stable-key>" }`; `confirm` must match the path slug. The client-supplied `resetKey` is required so timeouts and lost responses can be retried safely. A committed attempt replays its stored response without repeating the destructive DB or engine phases; an interrupted attempt is resumed. Treat `503 TX_CONFLICT` as transient and retry with backoff using the same key.

        Args:
            slug: Tournament slug.
            confirm: Must match the path `slug` exactly. Guards against accidental destructive calls.
            reset_key: Required stable client retry key. Reuse the same value after a timeout or `503 TX_CONFLICT`; a committed reset is replayed and an interrupted reset is resumed.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerResetBalances: Tournament live state reset.

        Example:
            ```python
            tournament = await client.dmm.tournaments.create_reset_balances(
                slug="alpha-tournament",
                confirm="alpha-tournament",
                reset_key="quarterly-reset-2026-q3",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._post(
            path_template("/dmm/tournaments/{slug}/reset-balances", **{"slug": slug}),
            body=await async_maybe_transform(
                {
                    "confirm": confirm,
                    "reset_key": reset_key,
                },
                tournament_create_reset_balances_params.TournamentCreateResetBalancesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignatedMarketMakerResetBalances,
        )

    async def list_rankings(
        self,
        slug: str,
        *,
        market_type: Literal[
            "global",
            "Election Outcome",
            "Financial Product",
            "Freeform",
            "Economic Indicator",
            "Sports Outcome",
            "Corporate Earnings",
            "Imported Market",
        ]
        | Omit = omit,
        sort_by: Literal[
            "smartScore",
            "smartScoreRaw",
            "roi",
            "sharpe",
            "winRate",
            "realizedPnl",
            "unrealizedPnl",
            "totalStake",
            "trades",
            "balance",
        ]
        | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        limit: int | Omit = omit,
        offset: Optional[int] | Omit = omit,
        user_group_id: str | Omit = omit,
        market_group_id: str | Omit = omit,
        period: Literal["1d", "7d", "30d", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerTournamentRankings:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Per-tournament user rankings. Requires owner/admin role in the tournament's organization. Reads from the latest `tournament_trader_metrics` snapshot for the requested `marketType` by default, joined with `tournament_members` so members without a snapshot still appear (with zeroed metric fields). Adds the current authoritative engine balance and exposes it as a sortable column.

        Pass `userGroupId` to restrict rows to members of a user group bound to this tournament; ranks are recomputed within the filtered set.

        Pass `marketGroupId` and/or `period` to switch to an on-demand recompute that scopes trader metrics to trades inside that market group and/or within the calendar-aligned window. The response `computed` field indicates which path served the request. Ranks use standard competition ranking: tied entries share a rank and the positions that follow skip by the size of the tie (1-1-3).

        Args:
            slug: Tournament slug.
            market_type: Trader-metrics bucket: `global` aggregates across all market types; any other value restricts metrics to that market type. Defaults to `global`.
            sort_by: Column to rank by. `balance` is the member's current virtual-cash balance; everything else comes from the latest trader-metrics snapshot.
            order: Query parameter.
            limit: Query parameter.
            offset: Query parameter.
            user_group_id: Optional user-group filter. Must be a group bound to the tournament via `tournament_user_groups`; otherwise the request is rejected with a validation error. Ranks are recomputed within the filtered set.
            market_group_id: Optional market-group filter. Must be a `market_group` belonging to the tournament's organization; otherwise the request is rejected with a validation error. Switches the response to on-demand metrics scoped to trades within the group.
            period: Calendar-aligned period filter (UTC). `1d` = today, `7d` = since most recent Sunday, `30d` = since 1st of the current month, `all` = no time filter. When set to anything other than `all`, metrics are recomputed on-demand and `computed` will be `on-demand`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerTournamentRankings: Tournament rankings page.

        Example:
            ```python
            tournament = await client.dmm.tournaments.list_rankings(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/dmm/tournaments/{slug}/rankings", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "market_type": market_type,
                        "sort_by": sort_by,
                        "order": order,
                        "limit": limit,
                        "offset": offset,
                        "user_group_id": user_group_id,
                        "market_group_id": market_group_id,
                        "period": period,
                    },
                    tournament_list_rankings_params.TournamentListRankingsParams,
                ),
            ),
            cast_to=DesignatedMarketMakerTournamentRankings,
        )

    async def list_market_assignments(
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
    ) -> TournamentListMarketAssignmentsResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Returns administrative assignment metadata for markets attached directly or supplied by bound market groups, newest first, with opaque cursor pagination. This is not a market-data feed: use `/markets` with the appropriate API-key scope or `tournamentId` for exchange IDs and prices.

        Args:
            slug: Tournament slug.
            limit: Page size (default 50, max 200).
            cursor: Opaque pagination cursor from a prior response. It marks the last row served rather than a row offset, so rows added or removed between pages neither repeat a row nor hide an unseen one.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TournamentListMarketAssignmentsResponse: Tournament market assignments page.

        Example:
            ```python
            tournament = await client.dmm.tournaments.list_market_assignments(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/dmm/tournaments/{slug}/market-assignments", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit, "cursor": cursor},
                    tournament_list_market_assignments_params.TournamentListMarketAssignmentsParams,
                ),
            ),
            cast_to=TournamentListMarketAssignmentsResponse,
        )

    async def list_trades(
        self,
        slug: str,
        *,
        from_: Union[str, datetime] | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerTradeList:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Returns executed trades for the league, newest first, with both sides' identity fields. Org-scoped: an org API key may only read its own organization's tournaments. Supports `from`/`to` windowing and opaque cursor pagination.

        Args:
            slug: Tournament slug.
            from_: Inclusive lower bound on the row timestamp (ISO-8601 UTC).
            to: Inclusive upper bound on the row timestamp (ISO-8601 UTC).
            limit: Query parameter.
            cursor: Opaque time cursor returned as `nextCursor` by a prior page.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerTradeList: Trades page.

        Example:
            ```python
            designated_market_maker_trades = await client.dmm.tournaments.list_trades(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/dmm/tournaments/{slug}/trades", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"from_": from_, "to": to, "limit": limit, "cursor": cursor},
                    tournament_list_trades_params.TournamentListTradesParams,
                ),
            ),
            cast_to=DesignatedMarketMakerTradeList,
        )

    async def list_orders(
        self,
        slug: str,
        *,
        from_: Union[str, datetime] | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerOrderList:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Returns orders placed in the league, newest first, with the placing trader's identity fields. Org-scoped. Supports `from`/`to` windowing and opaque cursor pagination.

        Args:
            slug: Tournament slug.
            from_: Inclusive lower bound on the row timestamp (ISO-8601 UTC).
            to: Inclusive upper bound on the row timestamp (ISO-8601 UTC).
            limit: Query parameter.
            cursor: Opaque time cursor returned as `nextCursor` by a prior page.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerOrderList: Orders page.

        Example:
            ```python
            designated_market_maker_orders = await client.dmm.tournaments.list_orders(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/dmm/tournaments/{slug}/orders", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"from_": from_, "to": to, "limit": limit, "cursor": cursor},
                    tournament_list_orders_params.TournamentListOrdersParams,
                ),
            ),
            cast_to=DesignatedMarketMakerOrderList,
        )

    async def list_transactions(
        self,
        slug: str,
        *,
        from_: Union[str, datetime] | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerTransactionList:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Returns the league's virtual-balance ledger (opening balances, nominal trade cost/proceeds, separate ALL collateral advances/repayments/releases, settlement payouts/refunds/corrections, and balance resets), newest first, with the affected trader's identity fields. The nominal execution price is never rewritten: a collateral entry records the capital-efficiency adjustment atomically alongside its trade or lifecycle command. Tournaments run on virtual currency, so there are no real-money deposits, withdrawals, or fees. Org-scoped. Supports `from`/`to` windowing and opaque cursor pagination.

        Args:
            slug: Tournament slug.
            from_: Inclusive lower bound on the row timestamp (ISO-8601 UTC).
            to: Inclusive upper bound on the row timestamp (ISO-8601 UTC).
            limit: Query parameter.
            cursor: Opaque time cursor returned as `nextCursor` by a prior page.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerTransactionList: Transactions page.

        Example:
            ```python
            designated_market_maker_transactions = await client.dmm.tournaments.list_transactions(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/dmm/tournaments/{slug}/transactions", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"from_": from_, "to": to, "limit": limit, "cursor": cursor},
                    tournament_list_transactions_params.TournamentListTransactionsParams,
                ),
            ),
            cast_to=DesignatedMarketMakerTransactionList,
        )

    async def list_inventory(
        self,
        slug: str,
        *,
        market: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmmInventory:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Read-only snapshot of the managed `market_maker`'s inventory and risk across one P2P tournament. The maker's position is synthetic (it holds no `holdings` rows), so net inventory and net cash are reconstructed from its filled trades. Returns one row per outcome that the maker either holds inventory on or is quoting on (fully-closed, unquoted outcomes are omitted), grouped by market with a tournament-level rollup. Each row reports net inventory + net cash, mark-to-market value + unrealized PnL (via the tournament valuation price), resting bid/ask exposure, and worst-case settlement loss. Same admin / org-ownership gates as the liquidity endpoints.

        Args:
            slug: Tournament slug.
            market: Optional market id. When provided, the snapshot is scoped to that single market instead of every market the maker has exposure on, and the `summary` totals reflect only that market. The market must belong to the tournament (otherwise 404). Omit to list all markets.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DmmInventory: Inventory and exposure snapshot.

        Example:
            ```python
            tournament = await client.dmm.tournaments.list_inventory(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/dmm/tournaments/{slug}/inventory", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"market": market}, tournament_list_inventory_params.TournamentListInventoryParams
                ),
            ),
            cast_to=DmmInventory,
        )


class TournamentsResourceWithRawResponse:
    def __init__(self, tournaments: TournamentsResource) -> None:
        self._tournaments = tournaments

        self.list = to_raw_response_wrapper(
            tournaments.list,
        )
        self.create = to_raw_response_wrapper(
            tournaments.create,
        )
        self.update = to_raw_response_wrapper(
            tournaments.update,
        )
        self.delete = to_raw_response_wrapper(
            tournaments.delete,
        )
        self.create_reset_balances = to_raw_response_wrapper(
            tournaments.create_reset_balances,
        )
        self.list_rankings = to_raw_response_wrapper(
            tournaments.list_rankings,
        )
        self.list_market_assignments = to_raw_response_wrapper(
            tournaments.list_market_assignments,
        )
        self.list_trades = to_raw_response_wrapper(
            tournaments.list_trades,
        )
        self.list_orders = to_raw_response_wrapper(
            tournaments.list_orders,
        )
        self.list_transactions = to_raw_response_wrapper(
            tournaments.list_transactions,
        )
        self.list_inventory = to_raw_response_wrapper(
            tournaments.list_inventory,
        )

    @cached_property
    def end_settlement(self) -> EndSettlementResourceWithRawResponse:
        return EndSettlementResourceWithRawResponse(self._tournaments.end_settlement)

    @cached_property
    def settlement_overrides(self) -> SettlementOverridesResourceWithRawResponse:
        return SettlementOverridesResourceWithRawResponse(self._tournaments.settlement_overrides)

    @cached_property
    def markets(self) -> MarketsResourceWithRawResponse:
        return MarketsResourceWithRawResponse(self._tournaments.markets)

    @cached_property
    def members(self) -> MembersResourceWithRawResponse:
        return MembersResourceWithRawResponse(self._tournaments.members)

    @cached_property
    def market_groups(self) -> MarketGroupsResourceWithRawResponse:
        return MarketGroupsResourceWithRawResponse(self._tournaments.market_groups)

    @cached_property
    def user_groups(self) -> UserGroupsResourceWithRawResponse:
        return UserGroupsResourceWithRawResponse(self._tournaments.user_groups)

    @cached_property
    def exchanges(self) -> ExchangesResourceWithRawResponse:
        return ExchangesResourceWithRawResponse(self._tournaments.exchanges)


class AsyncTournamentsResourceWithRawResponse:
    def __init__(self, tournaments: AsyncTournamentsResource) -> None:
        self._tournaments = tournaments

        self.list = async_to_raw_response_wrapper(
            tournaments.list,
        )
        self.create = async_to_raw_response_wrapper(
            tournaments.create,
        )
        self.update = async_to_raw_response_wrapper(
            tournaments.update,
        )
        self.delete = async_to_raw_response_wrapper(
            tournaments.delete,
        )
        self.create_reset_balances = async_to_raw_response_wrapper(
            tournaments.create_reset_balances,
        )
        self.list_rankings = async_to_raw_response_wrapper(
            tournaments.list_rankings,
        )
        self.list_market_assignments = async_to_raw_response_wrapper(
            tournaments.list_market_assignments,
        )
        self.list_trades = async_to_raw_response_wrapper(
            tournaments.list_trades,
        )
        self.list_orders = async_to_raw_response_wrapper(
            tournaments.list_orders,
        )
        self.list_transactions = async_to_raw_response_wrapper(
            tournaments.list_transactions,
        )
        self.list_inventory = async_to_raw_response_wrapper(
            tournaments.list_inventory,
        )

    @cached_property
    def end_settlement(self) -> AsyncEndSettlementResourceWithRawResponse:
        return AsyncEndSettlementResourceWithRawResponse(self._tournaments.end_settlement)

    @cached_property
    def settlement_overrides(self) -> AsyncSettlementOverridesResourceWithRawResponse:
        return AsyncSettlementOverridesResourceWithRawResponse(self._tournaments.settlement_overrides)

    @cached_property
    def markets(self) -> AsyncMarketsResourceWithRawResponse:
        return AsyncMarketsResourceWithRawResponse(self._tournaments.markets)

    @cached_property
    def members(self) -> AsyncMembersResourceWithRawResponse:
        return AsyncMembersResourceWithRawResponse(self._tournaments.members)

    @cached_property
    def market_groups(self) -> AsyncMarketGroupsResourceWithRawResponse:
        return AsyncMarketGroupsResourceWithRawResponse(self._tournaments.market_groups)

    @cached_property
    def user_groups(self) -> AsyncUserGroupsResourceWithRawResponse:
        return AsyncUserGroupsResourceWithRawResponse(self._tournaments.user_groups)

    @cached_property
    def exchanges(self) -> AsyncExchangesResourceWithRawResponse:
        return AsyncExchangesResourceWithRawResponse(self._tournaments.exchanges)


class TournamentsResourceWithStreamingResponse:
    def __init__(self, tournaments: TournamentsResource) -> None:
        self._tournaments = tournaments

        self.list = to_streamed_response_wrapper(
            tournaments.list,
        )
        self.create = to_streamed_response_wrapper(
            tournaments.create,
        )
        self.update = to_streamed_response_wrapper(
            tournaments.update,
        )
        self.delete = to_streamed_response_wrapper(
            tournaments.delete,
        )
        self.create_reset_balances = to_streamed_response_wrapper(
            tournaments.create_reset_balances,
        )
        self.list_rankings = to_streamed_response_wrapper(
            tournaments.list_rankings,
        )
        self.list_market_assignments = to_streamed_response_wrapper(
            tournaments.list_market_assignments,
        )
        self.list_trades = to_streamed_response_wrapper(
            tournaments.list_trades,
        )
        self.list_orders = to_streamed_response_wrapper(
            tournaments.list_orders,
        )
        self.list_transactions = to_streamed_response_wrapper(
            tournaments.list_transactions,
        )
        self.list_inventory = to_streamed_response_wrapper(
            tournaments.list_inventory,
        )

    @cached_property
    def end_settlement(self) -> EndSettlementResourceWithStreamingResponse:
        return EndSettlementResourceWithStreamingResponse(self._tournaments.end_settlement)

    @cached_property
    def settlement_overrides(self) -> SettlementOverridesResourceWithStreamingResponse:
        return SettlementOverridesResourceWithStreamingResponse(self._tournaments.settlement_overrides)

    @cached_property
    def markets(self) -> MarketsResourceWithStreamingResponse:
        return MarketsResourceWithStreamingResponse(self._tournaments.markets)

    @cached_property
    def members(self) -> MembersResourceWithStreamingResponse:
        return MembersResourceWithStreamingResponse(self._tournaments.members)

    @cached_property
    def market_groups(self) -> MarketGroupsResourceWithStreamingResponse:
        return MarketGroupsResourceWithStreamingResponse(self._tournaments.market_groups)

    @cached_property
    def user_groups(self) -> UserGroupsResourceWithStreamingResponse:
        return UserGroupsResourceWithStreamingResponse(self._tournaments.user_groups)

    @cached_property
    def exchanges(self) -> ExchangesResourceWithStreamingResponse:
        return ExchangesResourceWithStreamingResponse(self._tournaments.exchanges)


class AsyncTournamentsResourceWithStreamingResponse:
    def __init__(self, tournaments: AsyncTournamentsResource) -> None:
        self._tournaments = tournaments

        self.list = async_to_streamed_response_wrapper(
            tournaments.list,
        )
        self.create = async_to_streamed_response_wrapper(
            tournaments.create,
        )
        self.update = async_to_streamed_response_wrapper(
            tournaments.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            tournaments.delete,
        )
        self.create_reset_balances = async_to_streamed_response_wrapper(
            tournaments.create_reset_balances,
        )
        self.list_rankings = async_to_streamed_response_wrapper(
            tournaments.list_rankings,
        )
        self.list_market_assignments = async_to_streamed_response_wrapper(
            tournaments.list_market_assignments,
        )
        self.list_trades = async_to_streamed_response_wrapper(
            tournaments.list_trades,
        )
        self.list_orders = async_to_streamed_response_wrapper(
            tournaments.list_orders,
        )
        self.list_transactions = async_to_streamed_response_wrapper(
            tournaments.list_transactions,
        )
        self.list_inventory = async_to_streamed_response_wrapper(
            tournaments.list_inventory,
        )

    @cached_property
    def end_settlement(self) -> AsyncEndSettlementResourceWithStreamingResponse:
        return AsyncEndSettlementResourceWithStreamingResponse(self._tournaments.end_settlement)

    @cached_property
    def settlement_overrides(self) -> AsyncSettlementOverridesResourceWithStreamingResponse:
        return AsyncSettlementOverridesResourceWithStreamingResponse(self._tournaments.settlement_overrides)

    @cached_property
    def markets(self) -> AsyncMarketsResourceWithStreamingResponse:
        return AsyncMarketsResourceWithStreamingResponse(self._tournaments.markets)

    @cached_property
    def members(self) -> AsyncMembersResourceWithStreamingResponse:
        return AsyncMembersResourceWithStreamingResponse(self._tournaments.members)

    @cached_property
    def market_groups(self) -> AsyncMarketGroupsResourceWithStreamingResponse:
        return AsyncMarketGroupsResourceWithStreamingResponse(self._tournaments.market_groups)

    @cached_property
    def user_groups(self) -> AsyncUserGroupsResourceWithStreamingResponse:
        return AsyncUserGroupsResourceWithStreamingResponse(self._tournaments.user_groups)

    @cached_property
    def exchanges(self) -> AsyncExchangesResourceWithStreamingResponse:
        return AsyncExchangesResourceWithStreamingResponse(self._tournaments.exchanges)
