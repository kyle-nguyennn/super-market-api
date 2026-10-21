# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing_extensions import Literal

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.market_list_response import MarketListResponse
from ..types import (
    market_list_params,
    market_create_params,
    market_retrieve_params,
    market_update_params,
    market_list_orderbook_params,
    market_list_nodes_params,
)
from ..types.market_create import MarketCreate
from ..types.market import Market
from ..types.market_thumbnail_patch import MarketThumbnailPatch
from ..types.market_list_orderbook_response import MarketListOrderbookResponse
from ..types.market_list_nodes_response import MarketListNodesResponse

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
        tournament_id: str | Omit = omit,
        search: str | Omit = omit,
        sort: Literal["recent", "trending", "closing", "oldest"] | Omit = omit,
        status: Literal["open", "closed", "settled", "resolved", "any"] | Omit = omit,
        category: Literal[
            "sports-outcome",
            "election-outcome",
            "economic-indicator",
            "financial-product",
            "freeform",
            "existing-market",
            "corporate-earnings",
        ]
        | Omit = omit,
        ids: str | Omit = omit,
        is_composite: Literal["true", "false"] | Omit = omit,
        is_multi_outcome: Literal["true", "false"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketListResponse:
        """
        Canonical discovery endpoint. With an unbound API key, returns public globally visible markets with one public context. With an organization-bound API key, returns one deduplicated row per market directly attached to any accessible tournament in that organization; each row's `contexts` contain tournament metadata, currency, and context-specific exchange prices. Markets present only through a bound market group are not included until assigned to the tournament. Pass `tournamentId` to return only that accessible tournament context; `/tournaments/{slug}/markets` provides the equivalent slug-based view.

        Args:
            limit: Number of results per page (max 100).
            cursor: Pagination cursor from a previous response.
            tournament_id: Optional tournament UUID for an explicit tournament context. Omit to use the API key's default scope: public global markets for an unbound key, or all accessible tournaments in the bound organization for an organization-bound key.
            search: Case-insensitive title keyword search (at most 200 characters).
            sort: Sort order.
            status: Filter by market lifecycle status. `resolved` is a deprecated alias for `settled`.
            category: Filter by category slug. A market's category is the single contract type all of its legs share; markets mixing several types are composite and match no slug (use `is_composite`).
            ids: Comma-separated list of market IDs to fetch.
            is_composite: Filter composite (multi-condition) markets.
            is_multi_outcome: Filter multi-outcome markets (more than one exchange).
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketListResponse: Paginated list of markets.

        Example:
            ```python
            market = client.markets.list(
                limit=20,
                sort="recent",
                status="any",
            )
            ```
        """
        return self._get(
            "/markets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "cursor": cursor,
                        "tournament_id": tournament_id,
                        "search": search,
                        "sort": sort,
                        "status": status,
                        "category": category,
                        "ids": ids,
                        "is_composite": is_composite,
                        "is_multi_outcome": is_multi_outcome,
                    },
                    market_list_params.MarketListParams,
                ),
            ),
            cast_to=MarketListResponse,
        )

    def create(
        self,
        *,
        market_submission: market_create_params.MarketSubmission,
        custom_thumbnail_url: str | Omit = omit,
        generate_video: bool | Omit = omit,
        liquidity_amount: float | Omit = omit,
        super_signal: bool | Omit = omit,
        is_signal_anonymous: bool | Omit = omit,
        tournament_id: str | Omit = omit,
        tournament_initial_price: float | Omit = omit,
        global_tournament_id: str | Omit = omit,
        make_tournament_only: bool | Omit = omit,
        preserve_submitted_title: bool | Omit = omit,
        latest_price: str | Omit = omit,
        latest_prices: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketCreate:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Unaccepted current documents return 403 `TERMS_NOT_ACKNOWLEDGED` with `error.details.missingDocuments` containing `documentId`, `kind`, `version`, `organizationId`, `organizationSlug`, `organizationName`, `supportEmail`, `currencyName`, `url`, and `host`; `error.details.legacyCode` is also `TERMS_NOT_ACKNOWLEDGED`. Create a prediction market. The API-key owner is recorded as the creator. Unbound keys pay creation fees from the owner's balance. Organization-bound keys create markets free of charge, including free `generateVideo`; `superSignal: true` and positive `liquidityAmount` are rejected. With an organization-bound key, omitting all tournament fields requires organization owner/admin authority and atomically creates a tournament-only market attached to that organization's default tournament. Supplying an explicit tournament field attaches only to the requested context; it does not also add the market to the organization's default tournament. **Required scope:** `trade`; explicit tournament fields additionally require `admin`.

        Args:
            market_submission: Body parameter.
            custom_thumbnail_url: Previously uploaded market-thumbnail URL owned by the API key's organization namespace, or by the platform namespace for an unbound platform key.
            generate_video: Opt-in AI video generation. Free for org-bound API keys; otherwise charges `video_upgrade_fee` from the caller's balance.
            liquidity_amount: Initial paid liquidity. Values greater than 0 are rejected for org-bound API keys because organization market creation is free.
            super_signal: Paid Super Signal promotion. `true` is rejected for org-bound API keys because organization market creation is free.
            is_signal_anonymous: Body parameter.
            tournament_id: Attach the market to a private tournament at creation time. Admin-only.
            tournament_initial_price: Override the seed price for the tournament's isolated order book.
            global_tournament_id: Enrol the market in a global tournament. Admin-only. Independent of `tournamentId`.
            make_tournament_only: Hide the market from the global real-money surface. Admin-only. Requires `tournamentId` or `globalTournamentId`.
            preserve_submitted_title: Store `marketSubmission.title` verbatim instead of the server-generated title. Organization-bound API keys only; single-contract markets only.
            latest_price: Decimal in (0, 1). Seeds a single price across outcomes.
            latest_prices: Comma-separated decimals in (0, 1) — one per settlement option. Multi-outcome custom seeding. Mutually exclusive with `latestPrice`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketCreate: Market created.

        Example:
            ```python
            market = client.markets.create(
                market_submission={"title": "Will it rain tomorrow in NYC?", "root_node": {"node_type": "contract", "position": 0}},
            )
            ```
        """
        return self._post(
            "/markets",
            body=maybe_transform(
                {
                    "market_submission": market_submission,
                    "custom_thumbnail_url": custom_thumbnail_url,
                    "generate_video": generate_video,
                    "liquidity_amount": liquidity_amount,
                    "super_signal": super_signal,
                    "is_signal_anonymous": is_signal_anonymous,
                    "tournament_id": tournament_id,
                    "tournament_initial_price": tournament_initial_price,
                    "global_tournament_id": global_tournament_id,
                    "make_tournament_only": make_tournament_only,
                    "preserve_submitted_title": preserve_submitted_title,
                },
                market_create_params.MarketCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"latest_price": latest_price, "latest_prices": latest_prices},
                    market_create_params.MarketCreateParams,
                ),
            ),
            cast_to=MarketCreate,
        )

    def retrieve(
        self,
        id: str,
        *,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Market:
        """
        Returns the canonical market in the same public, organization-wide, or explicit tournament scope as `GET /markets`, including its accessible pricing contexts.

        Args:
            id: Market ID.
            tournament_id: Optional explicit tournament UUID. Omit for the API key's public or organization-wide default scope.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Market: Market detail.

        Example:
            ```python
            market = client.markets.retrieve(
                id="26",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/markets/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"tournament_id": tournament_id}, market_retrieve_params.MarketRetrieveParams),
            ),
            cast_to=Market,
        )

    def update(
        self,
        id: str,
        *,
        thumbnail_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketThumbnailPatch:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Replace a market thumbnail with an owned URL or uploaded file. Organization-bound keys may update only markets exclusive to their organization; unbound platform keys may update any market. Existing video status fields are preserved. Returns `409 CONFLICT` while media generation is in progress. **Required scope:** `trade`.

        Args:
            id: Market ID.
            thumbnail_url: Owned market-thumbnail URL in the API key principal's namespace.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketThumbnailPatch: Thumbnail replaced.

        Example:
            ```python
            market = client.markets.update(
                id="26",
                thumbnail_url="https://r2.thesuper.market/market-thumbnails/platform/123e4567-e89b-12d3-a456-426614174000.webp",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/markets/{id}", **{"id": id}),
            body=maybe_transform(
                {"thumbnail_url": thumbnail_url},
                market_update_params.MarketUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketThumbnailPatch,
        )

    def list_orderbook(
        self,
        id: str,
        *,
        tournament_id: str | Omit = omit,
        depth: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketListOrderbookResponse:
        """
        Returns YES-perspective orderbooks for every exchange in the market, plus overround. Each side is capped at `depth` price rungs. Each exchange's book, including those in `contexts[]`, carries its own `asOf`: the engine version it was read at, `{ sequence, at }`, the same version realtime `books` carry (compare by `sequence`, then `at`). `asOf` is null when the book is served without an engine version. Organization-bound requests include one `contexts` entry per accessible attached tournament; the legacy top-level fields mirror the organization's default tournament when the market is attached there, otherwise the first accessible context. Pass `tournamentId` for one explicit context. Unbound requests retain the public orderbook context.

        Args:
            id: Market ID.
            tournament_id: Optional explicit tournament UUID. Omit for the API key's public or organization-wide default scope.
            depth: Price rungs returned per side, per exchange (default 20, max 200).
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketListOrderbookResponse: Combined orderbook.

        Example:
            ```python
            market = client.markets.list_orderbook(
                id="26",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/markets/{id}/orderbook", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"tournament_id": tournament_id, "depth": depth},
                    market_list_orderbook_params.MarketListOrderbookParams,
                ),
            ),
            cast_to=MarketListOrderbookResponse,
        )

    def list_nodes(
        self,
        id: str,
        *,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketListNodesResponse:
        """
        Returns the resolution logic tree in the same public, organization-wide, or explicit tournament visibility scope as market discovery. Contract (leaf) nodes carry the contract type, settlement date, settled outcome and contract-type-specific details. Operator nodes (AND / OR / NOT / IF) combine their children.

        Args:
            id: Market ID.
            tournament_id: Optional explicit tournament UUID. Omit for the API key's public or organization-wide default scope.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketListNodesResponse: Market node tree.

        Example:
            ```python
            market = client.markets.list_nodes(
                id="26",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/markets/{id}/nodes", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"tournament_id": tournament_id}, market_list_nodes_params.MarketListNodesParams),
            ),
            cast_to=MarketListNodesResponse,
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
        tournament_id: str | Omit = omit,
        search: str | Omit = omit,
        sort: Literal["recent", "trending", "closing", "oldest"] | Omit = omit,
        status: Literal["open", "closed", "settled", "resolved", "any"] | Omit = omit,
        category: Literal[
            "sports-outcome",
            "election-outcome",
            "economic-indicator",
            "financial-product",
            "freeform",
            "existing-market",
            "corporate-earnings",
        ]
        | Omit = omit,
        ids: str | Omit = omit,
        is_composite: Literal["true", "false"] | Omit = omit,
        is_multi_outcome: Literal["true", "false"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketListResponse:
        """
        Canonical discovery endpoint. With an unbound API key, returns public globally visible markets with one public context. With an organization-bound API key, returns one deduplicated row per market directly attached to any accessible tournament in that organization; each row's `contexts` contain tournament metadata, currency, and context-specific exchange prices. Markets present only through a bound market group are not included until assigned to the tournament. Pass `tournamentId` to return only that accessible tournament context; `/tournaments/{slug}/markets` provides the equivalent slug-based view.

        Args:
            limit: Number of results per page (max 100).
            cursor: Pagination cursor from a previous response.
            tournament_id: Optional tournament UUID for an explicit tournament context. Omit to use the API key's default scope: public global markets for an unbound key, or all accessible tournaments in the bound organization for an organization-bound key.
            search: Case-insensitive title keyword search (at most 200 characters).
            sort: Sort order.
            status: Filter by market lifecycle status. `resolved` is a deprecated alias for `settled`.
            category: Filter by category slug. A market's category is the single contract type all of its legs share; markets mixing several types are composite and match no slug (use `is_composite`).
            ids: Comma-separated list of market IDs to fetch.
            is_composite: Filter composite (multi-condition) markets.
            is_multi_outcome: Filter multi-outcome markets (more than one exchange).
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketListResponse: Paginated list of markets.

        Example:
            ```python
            market = await client.markets.list(
                limit=20,
                sort="recent",
                status="any",
            )
            ```
        """
        return await self._get(
            "/markets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "cursor": cursor,
                        "tournament_id": tournament_id,
                        "search": search,
                        "sort": sort,
                        "status": status,
                        "category": category,
                        "ids": ids,
                        "is_composite": is_composite,
                        "is_multi_outcome": is_multi_outcome,
                    },
                    market_list_params.MarketListParams,
                ),
            ),
            cast_to=MarketListResponse,
        )

    async def create(
        self,
        *,
        market_submission: market_create_params.MarketSubmission,
        custom_thumbnail_url: str | Omit = omit,
        generate_video: bool | Omit = omit,
        liquidity_amount: float | Omit = omit,
        super_signal: bool | Omit = omit,
        is_signal_anonymous: bool | Omit = omit,
        tournament_id: str | Omit = omit,
        tournament_initial_price: float | Omit = omit,
        global_tournament_id: str | Omit = omit,
        make_tournament_only: bool | Omit = omit,
        preserve_submitted_title: bool | Omit = omit,
        latest_price: str | Omit = omit,
        latest_prices: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketCreate:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Unaccepted current documents return 403 `TERMS_NOT_ACKNOWLEDGED` with `error.details.missingDocuments` containing `documentId`, `kind`, `version`, `organizationId`, `organizationSlug`, `organizationName`, `supportEmail`, `currencyName`, `url`, and `host`; `error.details.legacyCode` is also `TERMS_NOT_ACKNOWLEDGED`. Create a prediction market. The API-key owner is recorded as the creator. Unbound keys pay creation fees from the owner's balance. Organization-bound keys create markets free of charge, including free `generateVideo`; `superSignal: true` and positive `liquidityAmount` are rejected. With an organization-bound key, omitting all tournament fields requires organization owner/admin authority and atomically creates a tournament-only market attached to that organization's default tournament. Supplying an explicit tournament field attaches only to the requested context; it does not also add the market to the organization's default tournament. **Required scope:** `trade`; explicit tournament fields additionally require `admin`.

        Args:
            market_submission: Body parameter.
            custom_thumbnail_url: Previously uploaded market-thumbnail URL owned by the API key's organization namespace, or by the platform namespace for an unbound platform key.
            generate_video: Opt-in AI video generation. Free for org-bound API keys; otherwise charges `video_upgrade_fee` from the caller's balance.
            liquidity_amount: Initial paid liquidity. Values greater than 0 are rejected for org-bound API keys because organization market creation is free.
            super_signal: Paid Super Signal promotion. `true` is rejected for org-bound API keys because organization market creation is free.
            is_signal_anonymous: Body parameter.
            tournament_id: Attach the market to a private tournament at creation time. Admin-only.
            tournament_initial_price: Override the seed price for the tournament's isolated order book.
            global_tournament_id: Enrol the market in a global tournament. Admin-only. Independent of `tournamentId`.
            make_tournament_only: Hide the market from the global real-money surface. Admin-only. Requires `tournamentId` or `globalTournamentId`.
            preserve_submitted_title: Store `marketSubmission.title` verbatim instead of the server-generated title. Organization-bound API keys only; single-contract markets only.
            latest_price: Decimal in (0, 1). Seeds a single price across outcomes.
            latest_prices: Comma-separated decimals in (0, 1) — one per settlement option. Multi-outcome custom seeding. Mutually exclusive with `latestPrice`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketCreate: Market created.

        Example:
            ```python
            market = await client.markets.create(
                market_submission={"title": "Will it rain tomorrow in NYC?", "root_node": {"node_type": "contract", "position": 0}},
            )
            ```
        """
        return await self._post(
            "/markets",
            body=await async_maybe_transform(
                {
                    "market_submission": market_submission,
                    "custom_thumbnail_url": custom_thumbnail_url,
                    "generate_video": generate_video,
                    "liquidity_amount": liquidity_amount,
                    "super_signal": super_signal,
                    "is_signal_anonymous": is_signal_anonymous,
                    "tournament_id": tournament_id,
                    "tournament_initial_price": tournament_initial_price,
                    "global_tournament_id": global_tournament_id,
                    "make_tournament_only": make_tournament_only,
                    "preserve_submitted_title": preserve_submitted_title,
                },
                market_create_params.MarketCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"latest_price": latest_price, "latest_prices": latest_prices},
                    market_create_params.MarketCreateParams,
                ),
            ),
            cast_to=MarketCreate,
        )

    async def retrieve(
        self,
        id: str,
        *,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Market:
        """
        Returns the canonical market in the same public, organization-wide, or explicit tournament scope as `GET /markets`, including its accessible pricing contexts.

        Args:
            id: Market ID.
            tournament_id: Optional explicit tournament UUID. Omit for the API key's public or organization-wide default scope.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Market: Market detail.

        Example:
            ```python
            market = await client.markets.retrieve(
                id="26",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/markets/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tournament_id": tournament_id}, market_retrieve_params.MarketRetrieveParams
                ),
            ),
            cast_to=Market,
        )

    async def update(
        self,
        id: str,
        *,
        thumbnail_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketThumbnailPatch:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Replace a market thumbnail with an owned URL or uploaded file. Organization-bound keys may update only markets exclusive to their organization; unbound platform keys may update any market. Existing video status fields are preserved. Returns `409 CONFLICT` while media generation is in progress. **Required scope:** `trade`.

        Args:
            id: Market ID.
            thumbnail_url: Owned market-thumbnail URL in the API key principal's namespace.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketThumbnailPatch: Thumbnail replaced.

        Example:
            ```python
            market = await client.markets.update(
                id="26",
                thumbnail_url="https://r2.thesuper.market/market-thumbnails/platform/123e4567-e89b-12d3-a456-426614174000.webp",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/markets/{id}", **{"id": id}),
            body=await async_maybe_transform(
                {"thumbnail_url": thumbnail_url},
                market_update_params.MarketUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarketThumbnailPatch,
        )

    async def list_orderbook(
        self,
        id: str,
        *,
        tournament_id: str | Omit = omit,
        depth: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketListOrderbookResponse:
        """
        Returns YES-perspective orderbooks for every exchange in the market, plus overround. Each side is capped at `depth` price rungs. Each exchange's book, including those in `contexts[]`, carries its own `asOf`: the engine version it was read at, `{ sequence, at }`, the same version realtime `books` carry (compare by `sequence`, then `at`). `asOf` is null when the book is served without an engine version. Organization-bound requests include one `contexts` entry per accessible attached tournament; the legacy top-level fields mirror the organization's default tournament when the market is attached there, otherwise the first accessible context. Pass `tournamentId` for one explicit context. Unbound requests retain the public orderbook context.

        Args:
            id: Market ID.
            tournament_id: Optional explicit tournament UUID. Omit for the API key's public or organization-wide default scope.
            depth: Price rungs returned per side, per exchange (default 20, max 200).
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketListOrderbookResponse: Combined orderbook.

        Example:
            ```python
            market = await client.markets.list_orderbook(
                id="26",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/markets/{id}/orderbook", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tournament_id": tournament_id, "depth": depth},
                    market_list_orderbook_params.MarketListOrderbookParams,
                ),
            ),
            cast_to=MarketListOrderbookResponse,
        )

    async def list_nodes(
        self,
        id: str,
        *,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketListNodesResponse:
        """
        Returns the resolution logic tree in the same public, organization-wide, or explicit tournament visibility scope as market discovery. Contract (leaf) nodes carry the contract type, settlement date, settled outcome and contract-type-specific details. Operator nodes (AND / OR / NOT / IF) combine their children.

        Args:
            id: Market ID.
            tournament_id: Optional explicit tournament UUID. Omit for the API key's public or organization-wide default scope.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketListNodesResponse: Market node tree.

        Example:
            ```python
            market = await client.markets.list_nodes(
                id="26",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/markets/{id}/nodes", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tournament_id": tournament_id}, market_list_nodes_params.MarketListNodesParams
                ),
            ),
            cast_to=MarketListNodesResponse,
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
        self.list_orderbook = to_raw_response_wrapper(
            markets.list_orderbook,
        )
        self.list_nodes = to_raw_response_wrapper(
            markets.list_nodes,
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
        self.list_orderbook = async_to_raw_response_wrapper(
            markets.list_orderbook,
        )
        self.list_nodes = async_to_raw_response_wrapper(
            markets.list_nodes,
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
        self.list_orderbook = to_streamed_response_wrapper(
            markets.list_orderbook,
        )
        self.list_nodes = to_streamed_response_wrapper(
            markets.list_nodes,
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
        self.list_orderbook = async_to_streamed_response_wrapper(
            markets.list_orderbook,
        )
        self.list_nodes = async_to_streamed_response_wrapper(
            markets.list_nodes,
        )
