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
from ..types.exchange_list_response import ExchangeListResponse
from ..types import (
    exchange_list_params,
    exchange_list_price_params,
    exchange_list_orderbook_params,
    exchange_list_price_history_params,
    exchange_list_trades_params,
    exchange_list_prices_params,
)
from ..types.exchange_list_price_response import ExchangeListPriceResponse
from ..types.exchange_list_orderbook_response import ExchangeListOrderbookResponse
from ..types.exchange_list_price_history_response import ExchangeListPriceHistoryResponse
from ..types.exchange_list_trades_response import ExchangeListTradesResponse
from ..types.exchange_list_prices_response import ExchangeListPricesResponse

__all__ = ["ExchangesResource", "AsyncExchangesResource"]


class ExchangesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExchangesResourceWithRawResponse:
        return ExchangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExchangesResourceWithStreamingResponse:
        return ExchangesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        market_id: str | Omit = omit,
        ids: str | Omit = omit,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExchangeListResponse:
        """
        Paginated list of tradable exchanges in the same scope as canonical market discovery. Unbound keys receive public exchanges with one public context. Organization-bound keys receive canonical, deduplicated exchanges from every accessible attached tournament, with context-specific prices in `contexts`. Pass `tournamentId` to return only one accessible tournament context. `marketId` and `ids` are mutually exclusive filters.

        Args:
            market_id: Filter to all exchanges in a single market. Mutually exclusive with `ids`.
            ids: Comma-separated list of exchange IDs (max 100). Mutually exclusive with `marketId`. Useful for bulk-refreshing a watchlist in one request.
            limit: Results per page (max 200).
            cursor: Pagination cursor from a previous response.
            tournament_id: Optional explicit tournament UUID. Omit for the API key's public or organization-wide default scope.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ExchangeListResponse: Paginated list of exchanges.

        Example:
            ```python
            exchange = client.exchanges.list(
                limit=50,
            )
            ```
        """
        return self._get(
            "/exchanges",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "market_id": market_id,
                        "ids": ids,
                        "limit": limit,
                        "cursor": cursor,
                        "tournament_id": tournament_id,
                    },
                    exchange_list_params.ExchangeListParams,
                ),
            ),
            cast_to=ExchangeListResponse,
        )

    def list_price(
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
    ) -> ExchangeListPriceResponse:
        """
        Returns the latest price, best bid, best ask, and spread for a single exchange (the API's tradable-contract unit). Best bid, best ask, and spread come from the same resting order book as `/exchanges/{id}/orderbook`. All prices are YES-normalized (0–1 probability). Pass `tournamentId` to get that tournament's price and bid/ask. When an organization-bound key omits it, this singular endpoint deterministically uses the organization's default tournament; an unbound key uses the public context. In tournament context, `latestPrice` is null until a tournament trade establishes a price; resting bids or asks may still exist, and the value never falls back to the global price.

        Args:
            id: Exchange ID.
            tournament_id: Tournament UUID returned as `id` by `GET /tournaments/{slug}`. When provided, returns the tournament-specific latest price and computes best bid/ask from that tournament's isolated orderbook.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ExchangeListPriceResponse: Exchange price snapshot.

        Example:
            ```python
            exchange = client.exchanges.list_price(
                id="36",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/exchanges/{id}/price", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"tournament_id": tournament_id}, exchange_list_price_params.ExchangeListPriceParams
                ),
            ),
            cast_to=ExchangeListPriceResponse,
        )

    def list_orderbook(
        self,
        id: str,
        *,
        depth: int | Omit = omit,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExchangeListOrderbookResponse:
        """
        Returns the limit order book for a single exchange (tradable contract). Prices are YES-normalized (0–1). Bids are sorted descending, asks ascending. `asOf` is the engine version the book was read at, `{ sequence, at }`, the same version realtime `books` carry (compare by `sequence`, then `at`); it is null when the book is served without an engine version. Pass `tournamentId` for one explicit tournament-isolated book. When an organization-bound key omits it, this singular endpoint deterministically uses the organization's default tournament; an unbound key uses the public book.

        Args:
            id: Exchange ID.
            depth: Maximum number of price levels per side (max 200).
            tournament_id: Tournament UUID returned as `id` by `GET /tournaments/{slug}`. When provided, returns only orders belonging to that tournament's isolated orderbook.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ExchangeListOrderbookResponse: Exchange orderbook.

        Example:
            ```python
            exchange = client.exchanges.list_orderbook(
                id="36",
                depth=20,
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/exchanges/{id}/orderbook", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"depth": depth, "tournament_id": tournament_id},
                    exchange_list_orderbook_params.ExchangeListOrderbookParams,
                ),
            ),
            cast_to=ExchangeListOrderbookResponse,
        )

    def list_price_history(
        self,
        id: str,
        *,
        tournament_id: str | Omit = omit,
        resolution: Literal["1m", "5m", "1h", "1d", "1w"] | Omit = omit,
        from_: str | Omit = omit,
        to: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExchangeListPriceHistoryResponse:
        """
        Returns OHLCV candles computed from trade history. All prices are YES-normalized, and buckets with no trades are omitted (sparse series). Without `from`, the response contains the newest `limit` candles ending at `to`. With `from`, candles are returned forward from that timestamp; if the requested window exceeds the bucket cap, the response contains the oldest `limit` candles and `coverage.complete` is false. For a capped explicit-from page, response `to` is the next candle's start and is an exclusive continuation boundary. Response `from` and `to` describe the window actually served. An explicit `from` or `to` is floored to the selected resolution's candle boundary; a range whose floored end is not after its floored start returns 400 `VALIDATION_ERROR`. Pass `tournamentId` for one explicit accessible tournament. When an organization-bound key omits it, the request uses the organization's default tournament; an unbound key uses public-global trade history.

        Args:
            id: Exchange ID.
            tournament_id: When provided, returns candles computed from that accessible tournament's trades. Omit for the organization's default tournament with an organization-bound key or public-global history with an unbound key.
            resolution: Candle size. Buckets are aligned to UTC multiples of the resolution measured from the Unix epoch, so `1w` buckets begin on Thursdays.
            from_: ISO-8601 start timestamp (inclusive). Floored down to the selected resolution's bucket boundary; the response `from` reflects the floored value. When omitted, returns the newest candles up to `to`.
            to: ISO-8601 end timestamp (exclusive). When supplied, floored down to the selected resolution's bucket boundary. Defaults to now (not floored).
            limit: Maximum number of candles to return (max 1000). Selects the newest candles when `from` is omitted and the oldest candles forward from an explicit `from`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ExchangeListPriceHistoryResponse: OHLCV candle series.

        Example:
            ```python
            exchange = client.exchanges.list_price_history(
                id="36",
                resolution="1h",
                limit=200,
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/exchanges/{id}/price-history", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "tournament_id": tournament_id,
                        "resolution": resolution,
                        "from_": from_,
                        "to": to,
                        "limit": limit,
                    },
                    exchange_list_price_history_params.ExchangeListPriceHistoryParams,
                ),
            ),
            cast_to=ExchangeListPriceHistoryResponse,
        )

    def list_trades(
        self,
        id: str,
        *,
        tournament_id: str | Omit = omit,
        from_: str | Omit = omit,
        to: str | Omit = omit,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExchangeListTradesResponse:
        """
        Returns the trade tape for a single exchange, newest first, cursor-paginated. Prices are YES-normalized so the series is directly comparable to `/price` and `/price-history`. Pass `tournamentId` for one explicit accessible tournament. When an organization-bound key omits it, the request uses the organization's default tournament; an unbound key uses public-global trades.

        Args:
            id: Exchange ID.
            tournament_id: When provided, returns trades from that accessible tournament. Omit for the organization's default tournament with an organization-bound key or public-global trades with an unbound key.
            from_: ISO-8601 start timestamp (inclusive). Defaults to the beginning of exchange history.
            to: ISO-8601 end timestamp (exclusive). Defaults to now.
            limit: Trades per page (max 200).
            cursor: Opaque pagination cursor from a previous response.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ExchangeListTradesResponse: Trade tape page.

        Example:
            ```python
            exchange = client.exchanges.list_trades(
                id="36",
                limit=50,
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/exchanges/{id}/trades", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"tournament_id": tournament_id, "from_": from_, "to": to, "limit": limit, "cursor": cursor},
                    exchange_list_trades_params.ExchangeListTradesParams,
                ),
            ),
            cast_to=ExchangeListTradesResponse,
        )

    def list_prices(
        self,
        *,
        ids: str,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExchangeListPricesResponse:
        """
        Returns latest price, best bid, best ask, and spread for up to 100 exchanges in a single round-trip. Same per-exchange shape as `/exchanges/{id}/price`; each quote comes from the same resting order book as `/exchanges/{id}/orderbook`. Pass `tournamentId` for one explicit accessible tournament. When an organization-bound key omits it, the request uses the organization's default tournament; an unbound key uses the public-global context. IDs outside the resolved context are returned in `missingIds`, and response `data` preserves request order.

        Args:
            ids: Required. Comma-separated list of exchange IDs (max 100).
            tournament_id: When provided, returns quotes from that accessible tournament. Omit for the organization's default tournament with an organization-bound key or public-global quotes with an unbound key. Exchanges outside the resolved context are reported in `missingIds`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ExchangeListPricesResponse: Bulk price snapshot.

        Example:
            ```python
            exchange = client.exchanges.list_prices(
                ids="36,37,42",
            )
            ```
        """
        return self._get(
            "/exchanges/prices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"ids": ids, "tournament_id": tournament_id}, exchange_list_prices_params.ExchangeListPricesParams
                ),
            ),
            cast_to=ExchangeListPricesResponse,
        )


class AsyncExchangesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExchangesResourceWithRawResponse:
        return AsyncExchangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExchangesResourceWithStreamingResponse:
        return AsyncExchangesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        market_id: str | Omit = omit,
        ids: str | Omit = omit,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExchangeListResponse:
        """
        Paginated list of tradable exchanges in the same scope as canonical market discovery. Unbound keys receive public exchanges with one public context. Organization-bound keys receive canonical, deduplicated exchanges from every accessible attached tournament, with context-specific prices in `contexts`. Pass `tournamentId` to return only one accessible tournament context. `marketId` and `ids` are mutually exclusive filters.

        Args:
            market_id: Filter to all exchanges in a single market. Mutually exclusive with `ids`.
            ids: Comma-separated list of exchange IDs (max 100). Mutually exclusive with `marketId`. Useful for bulk-refreshing a watchlist in one request.
            limit: Results per page (max 200).
            cursor: Pagination cursor from a previous response.
            tournament_id: Optional explicit tournament UUID. Omit for the API key's public or organization-wide default scope.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ExchangeListResponse: Paginated list of exchanges.

        Example:
            ```python
            exchange = await client.exchanges.list(
                limit=50,
            )
            ```
        """
        return await self._get(
            "/exchanges",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "market_id": market_id,
                        "ids": ids,
                        "limit": limit,
                        "cursor": cursor,
                        "tournament_id": tournament_id,
                    },
                    exchange_list_params.ExchangeListParams,
                ),
            ),
            cast_to=ExchangeListResponse,
        )

    async def list_price(
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
    ) -> ExchangeListPriceResponse:
        """
        Returns the latest price, best bid, best ask, and spread for a single exchange (the API's tradable-contract unit). Best bid, best ask, and spread come from the same resting order book as `/exchanges/{id}/orderbook`. All prices are YES-normalized (0–1 probability). Pass `tournamentId` to get that tournament's price and bid/ask. When an organization-bound key omits it, this singular endpoint deterministically uses the organization's default tournament; an unbound key uses the public context. In tournament context, `latestPrice` is null until a tournament trade establishes a price; resting bids or asks may still exist, and the value never falls back to the global price.

        Args:
            id: Exchange ID.
            tournament_id: Tournament UUID returned as `id` by `GET /tournaments/{slug}`. When provided, returns the tournament-specific latest price and computes best bid/ask from that tournament's isolated orderbook.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ExchangeListPriceResponse: Exchange price snapshot.

        Example:
            ```python
            exchange = await client.exchanges.list_price(
                id="36",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/exchanges/{id}/price", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tournament_id": tournament_id}, exchange_list_price_params.ExchangeListPriceParams
                ),
            ),
            cast_to=ExchangeListPriceResponse,
        )

    async def list_orderbook(
        self,
        id: str,
        *,
        depth: int | Omit = omit,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExchangeListOrderbookResponse:
        """
        Returns the limit order book for a single exchange (tradable contract). Prices are YES-normalized (0–1). Bids are sorted descending, asks ascending. `asOf` is the engine version the book was read at, `{ sequence, at }`, the same version realtime `books` carry (compare by `sequence`, then `at`); it is null when the book is served without an engine version. Pass `tournamentId` for one explicit tournament-isolated book. When an organization-bound key omits it, this singular endpoint deterministically uses the organization's default tournament; an unbound key uses the public book.

        Args:
            id: Exchange ID.
            depth: Maximum number of price levels per side (max 200).
            tournament_id: Tournament UUID returned as `id` by `GET /tournaments/{slug}`. When provided, returns only orders belonging to that tournament's isolated orderbook.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ExchangeListOrderbookResponse: Exchange orderbook.

        Example:
            ```python
            exchange = await client.exchanges.list_orderbook(
                id="36",
                depth=20,
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/exchanges/{id}/orderbook", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"depth": depth, "tournament_id": tournament_id},
                    exchange_list_orderbook_params.ExchangeListOrderbookParams,
                ),
            ),
            cast_to=ExchangeListOrderbookResponse,
        )

    async def list_price_history(
        self,
        id: str,
        *,
        tournament_id: str | Omit = omit,
        resolution: Literal["1m", "5m", "1h", "1d", "1w"] | Omit = omit,
        from_: str | Omit = omit,
        to: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExchangeListPriceHistoryResponse:
        """
        Returns OHLCV candles computed from trade history. All prices are YES-normalized, and buckets with no trades are omitted (sparse series). Without `from`, the response contains the newest `limit` candles ending at `to`. With `from`, candles are returned forward from that timestamp; if the requested window exceeds the bucket cap, the response contains the oldest `limit` candles and `coverage.complete` is false. For a capped explicit-from page, response `to` is the next candle's start and is an exclusive continuation boundary. Response `from` and `to` describe the window actually served. An explicit `from` or `to` is floored to the selected resolution's candle boundary; a range whose floored end is not after its floored start returns 400 `VALIDATION_ERROR`. Pass `tournamentId` for one explicit accessible tournament. When an organization-bound key omits it, the request uses the organization's default tournament; an unbound key uses public-global trade history.

        Args:
            id: Exchange ID.
            tournament_id: When provided, returns candles computed from that accessible tournament's trades. Omit for the organization's default tournament with an organization-bound key or public-global history with an unbound key.
            resolution: Candle size. Buckets are aligned to UTC multiples of the resolution measured from the Unix epoch, so `1w` buckets begin on Thursdays.
            from_: ISO-8601 start timestamp (inclusive). Floored down to the selected resolution's bucket boundary; the response `from` reflects the floored value. When omitted, returns the newest candles up to `to`.
            to: ISO-8601 end timestamp (exclusive). When supplied, floored down to the selected resolution's bucket boundary. Defaults to now (not floored).
            limit: Maximum number of candles to return (max 1000). Selects the newest candles when `from` is omitted and the oldest candles forward from an explicit `from`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ExchangeListPriceHistoryResponse: OHLCV candle series.

        Example:
            ```python
            exchange = await client.exchanges.list_price_history(
                id="36",
                resolution="1h",
                limit=200,
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/exchanges/{id}/price-history", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "tournament_id": tournament_id,
                        "resolution": resolution,
                        "from_": from_,
                        "to": to,
                        "limit": limit,
                    },
                    exchange_list_price_history_params.ExchangeListPriceHistoryParams,
                ),
            ),
            cast_to=ExchangeListPriceHistoryResponse,
        )

    async def list_trades(
        self,
        id: str,
        *,
        tournament_id: str | Omit = omit,
        from_: str | Omit = omit,
        to: str | Omit = omit,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExchangeListTradesResponse:
        """
        Returns the trade tape for a single exchange, newest first, cursor-paginated. Prices are YES-normalized so the series is directly comparable to `/price` and `/price-history`. Pass `tournamentId` for one explicit accessible tournament. When an organization-bound key omits it, the request uses the organization's default tournament; an unbound key uses public-global trades.

        Args:
            id: Exchange ID.
            tournament_id: When provided, returns trades from that accessible tournament. Omit for the organization's default tournament with an organization-bound key or public-global trades with an unbound key.
            from_: ISO-8601 start timestamp (inclusive). Defaults to the beginning of exchange history.
            to: ISO-8601 end timestamp (exclusive). Defaults to now.
            limit: Trades per page (max 200).
            cursor: Opaque pagination cursor from a previous response.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ExchangeListTradesResponse: Trade tape page.

        Example:
            ```python
            exchange = await client.exchanges.list_trades(
                id="36",
                limit=50,
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/exchanges/{id}/trades", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tournament_id": tournament_id, "from_": from_, "to": to, "limit": limit, "cursor": cursor},
                    exchange_list_trades_params.ExchangeListTradesParams,
                ),
            ),
            cast_to=ExchangeListTradesResponse,
        )

    async def list_prices(
        self,
        *,
        ids: str,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExchangeListPricesResponse:
        """
        Returns latest price, best bid, best ask, and spread for up to 100 exchanges in a single round-trip. Same per-exchange shape as `/exchanges/{id}/price`; each quote comes from the same resting order book as `/exchanges/{id}/orderbook`. Pass `tournamentId` for one explicit accessible tournament. When an organization-bound key omits it, the request uses the organization's default tournament; an unbound key uses the public-global context. IDs outside the resolved context are returned in `missingIds`, and response `data` preserves request order.

        Args:
            ids: Required. Comma-separated list of exchange IDs (max 100).
            tournament_id: When provided, returns quotes from that accessible tournament. Omit for the organization's default tournament with an organization-bound key or public-global quotes with an unbound key. Exchanges outside the resolved context are reported in `missingIds`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ExchangeListPricesResponse: Bulk price snapshot.

        Example:
            ```python
            exchange = await client.exchanges.list_prices(
                ids="36,37,42",
            )
            ```
        """
        return await self._get(
            "/exchanges/prices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"ids": ids, "tournament_id": tournament_id}, exchange_list_prices_params.ExchangeListPricesParams
                ),
            ),
            cast_to=ExchangeListPricesResponse,
        )


class ExchangesResourceWithRawResponse:
    def __init__(self, exchanges: ExchangesResource) -> None:
        self._exchanges = exchanges

        self.list = to_raw_response_wrapper(
            exchanges.list,
        )
        self.list_price = to_raw_response_wrapper(
            exchanges.list_price,
        )
        self.list_orderbook = to_raw_response_wrapper(
            exchanges.list_orderbook,
        )
        self.list_price_history = to_raw_response_wrapper(
            exchanges.list_price_history,
        )
        self.list_trades = to_raw_response_wrapper(
            exchanges.list_trades,
        )
        self.list_prices = to_raw_response_wrapper(
            exchanges.list_prices,
        )


class AsyncExchangesResourceWithRawResponse:
    def __init__(self, exchanges: AsyncExchangesResource) -> None:
        self._exchanges = exchanges

        self.list = async_to_raw_response_wrapper(
            exchanges.list,
        )
        self.list_price = async_to_raw_response_wrapper(
            exchanges.list_price,
        )
        self.list_orderbook = async_to_raw_response_wrapper(
            exchanges.list_orderbook,
        )
        self.list_price_history = async_to_raw_response_wrapper(
            exchanges.list_price_history,
        )
        self.list_trades = async_to_raw_response_wrapper(
            exchanges.list_trades,
        )
        self.list_prices = async_to_raw_response_wrapper(
            exchanges.list_prices,
        )


class ExchangesResourceWithStreamingResponse:
    def __init__(self, exchanges: ExchangesResource) -> None:
        self._exchanges = exchanges

        self.list = to_streamed_response_wrapper(
            exchanges.list,
        )
        self.list_price = to_streamed_response_wrapper(
            exchanges.list_price,
        )
        self.list_orderbook = to_streamed_response_wrapper(
            exchanges.list_orderbook,
        )
        self.list_price_history = to_streamed_response_wrapper(
            exchanges.list_price_history,
        )
        self.list_trades = to_streamed_response_wrapper(
            exchanges.list_trades,
        )
        self.list_prices = to_streamed_response_wrapper(
            exchanges.list_prices,
        )


class AsyncExchangesResourceWithStreamingResponse:
    def __init__(self, exchanges: AsyncExchangesResource) -> None:
        self._exchanges = exchanges

        self.list = async_to_streamed_response_wrapper(
            exchanges.list,
        )
        self.list_price = async_to_streamed_response_wrapper(
            exchanges.list_price,
        )
        self.list_orderbook = async_to_streamed_response_wrapper(
            exchanges.list_orderbook,
        )
        self.list_price_history = async_to_streamed_response_wrapper(
            exchanges.list_price_history,
        )
        self.list_trades = async_to_streamed_response_wrapper(
            exchanges.list_trades,
        )
        self.list_prices = async_to_streamed_response_wrapper(
            exchanges.list_prices,
        )
