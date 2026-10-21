# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

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
from ...types.tournaments.portfolio_list_positions_response import PortfolioListPositionsResponse
from ...types.tournaments.portfolio_list_transactions_response import PortfolioListTransactionsResponse
from ...types.tournaments import (
    portfolio_list_transactions_params,
    portfolio_list_fills_params,
    portfolio_list_history_params,
    portfolio_list_settlements_params,
    portfolio_list_pnl_params,
)
from ...types.tournaments.portfolio_list_fills_response import PortfolioListFillsResponse
from ...types.tournaments.portfolio_list_history_response import PortfolioListHistoryResponse
from ...types.tournaments.portfolio_list_settlements_response import PortfolioListSettlementsResponse
from ...types.tournaments.portfolio_list_pnl_response import PortfolioListPnlResponse

__all__ = ["PortfolioResource", "AsyncPortfolioResource"]


class PortfolioResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PortfolioResourceWithRawResponse:
        return PortfolioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PortfolioResourceWithStreamingResponse:
        return PortfolioResourceWithStreamingResponse(self)

    def list_positions(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioListPositionsResponse:
        """
        Returns the caller's open positions within the tournament with FIFO lot breakdown and unrealized P&L. Prices use tournament valuation_price. If nonzero holdings exist without valuation_price, returns 409 instead of valuing them at a neutral default.

        Args:
            slug: Tournament slug.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListPositionsResponse: Tournament positions and summary.

        Example:
            ```python
            portfolio = client.tournaments.portfolio.list_positions(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/tournaments/{slug}/portfolio/positions", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortfolioListPositionsResponse,
        )

    def list_transactions(
        self,
        slug: str,
        *,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioListTransactionsResponse:
        """
        Returns a cursor-paginated audit trail of the caller's trades and transactions within the tournament, newest first.

        Args:
            slug: Tournament slug.
            limit: Results per page (max 200).
            cursor: Opaque pagination cursor from a previous response.
            type: Comma-separated event type filter. Valid values: trade, settlement, deposit, fee, market_creation.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListTransactionsResponse: Paginated tournament transaction history.

        Example:
            ```python
            portfolio = client.tournaments.portfolio.list_transactions(
                slug="alpha-tournament",
                limit=50,
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/tournaments/{slug}/portfolio/transactions", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit, "cursor": cursor, "type": type},
                    portfolio_list_transactions_params.PortfolioListTransactionsParams,
                ),
            ),
            cast_to=PortfolioListTransactionsResponse,
        )

    def list_fills(
        self,
        slug: str,
        *,
        exchange_id: str | Omit = omit,
        market_id: str | Omit = omit,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioListFillsResponse:
        """
        Returns all trade fills for the caller within this tournament, newest first.

        Args:
            slug: Tournament slug.
            exchange_id: Filter to a specific exchange.
            market_id: Filter to all exchanges in a market.
            limit: Results per page (max 200).
            cursor: Pagination cursor from a previous response.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListFillsResponse: Paginated list of tournament fills.

        Example:
            ```python
            portfolio = client.tournaments.portfolio.list_fills(
                slug="alpha-tournament",
                limit=50,
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/tournaments/{slug}/portfolio/fills", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"exchange_id": exchange_id, "market_id": market_id, "limit": limit, "cursor": cursor},
                    portfolio_list_fills_params.PortfolioListFillsParams,
                ),
            ),
            cast_to=PortfolioListFillsResponse,
        )

    def list_history(
        self,
        slug: str,
        *,
        interval: Literal["1h", "6h", "1d", "1w", "all"] | Omit = omit,
        from_: str | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioListHistoryResponse:
        """
        Returns the caller's tournament portfolio-value series from tournament snapshots plus a live tournament valuation. A member with no snapshots receives an initial-virtual-balance seed at their joined-at time. The requested window is capped per interval — `1h` 31 days, `6h` 366 days, `1d` 1827 days, `1w` 1827 days, `all` 1827 days — and responses carry at most 2000 points.

        Args:
            slug: Tournament slug.
            interval: `1h` and `6h` linearly interpolate between selected tournament history points; `all` returns selected stored points without weekly downsampling.
            from_: ISO-8601 start date (inclusive). Must not be after `to`.
            to: ISO-8601 end date (inclusive). Defaults to now.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListHistoryResponse: Tournament portfolio value time series.

        Example:
            ```python
            portfolio = client.tournaments.portfolio.list_history(
                slug="alpha-tournament",
                interval="1d",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/tournaments/{slug}/portfolio/history", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"interval": interval, "from_": from_, "to": to},
                    portfolio_list_history_params.PortfolioListHistoryParams,
                ),
            ),
            cast_to=PortfolioListHistoryResponse,
        )

    def list_settlements(
        self,
        slug: str,
        *,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        type: str | Omit = omit,
        market_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioListSettlementsResponse:
        """
        Returns settlement entries (win/loss/refund/correction) for the caller within this tournament. Payouts apply to the tournament virtual balance.

        Args:
            slug: Tournament slug.
            limit: Results per page (max 200).
            cursor: Opaque pagination cursor from a previous response.
            type: Comma-separated settlement type filter. Valid values: win, loss, refund, correction.
            market_id: Restrict to settlements on a single market.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListSettlementsResponse: Paginated list of tournament settlement entries.

        Example:
            ```python
            portfolio = client.tournaments.portfolio.list_settlements(
                slug="alpha-tournament",
                limit=50,
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/tournaments/{slug}/portfolio/settlements", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit, "cursor": cursor, "type": type, "market_id": market_id},
                    portfolio_list_settlements_params.PortfolioListSettlementsParams,
                ),
            ),
            cast_to=PortfolioListSettlementsResponse,
        )

    def list_pnl(
        self,
        slug: str,
        *,
        period: Literal["day", "week", "month", "quarter", "year", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioListPnlResponse:
        """
        Returns the caller's tournament account value, unrealized P&L, period P&L, ROI, and Sharpe ratio. All figures are scoped to the tournament's virtual balance and tournament valuation prices. If nonzero holdings exist without valuation_price, returns 409 instead of valuing them at a neutral default. Bounded periods are rolling windows measured back from the request time (`day` 1, `week` 7, `month` 30, `quarter` 90, `year` 365 days), unlike the calendar-aligned leaderboard periods. Period P&L and ROI use the latest tournament snapshot at or before the period start, falling back to the initial virtual balance for members who joined inside the window; `periodPnl` is null for `all`. For `period=all`, ROI is computed relative to the tournament's initial virtual balance. Sharpe is the mean daily return over its standard deviation annualized by √252, and null when the daily returns have no usable variance.

        Args:
            slug: Tournament slug.
            period: Rolling lookback window measured back from the request time; `all` is unbounded.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListPnlResponse: Tournament P&L summary.

        Example:
            ```python
            portfolio = client.tournaments.portfolio.list_pnl(
                slug="alpha-tournament",
                period="quarter",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/tournaments/{slug}/portfolio/pnl", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"period": period}, portfolio_list_pnl_params.PortfolioListPnlParams),
            ),
            cast_to=PortfolioListPnlResponse,
        )


class AsyncPortfolioResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPortfolioResourceWithRawResponse:
        return AsyncPortfolioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPortfolioResourceWithStreamingResponse:
        return AsyncPortfolioResourceWithStreamingResponse(self)

    async def list_positions(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioListPositionsResponse:
        """
        Returns the caller's open positions within the tournament with FIFO lot breakdown and unrealized P&L. Prices use tournament valuation_price. If nonzero holdings exist without valuation_price, returns 409 instead of valuing them at a neutral default.

        Args:
            slug: Tournament slug.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListPositionsResponse: Tournament positions and summary.

        Example:
            ```python
            portfolio = await client.tournaments.portfolio.list_positions(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/tournaments/{slug}/portfolio/positions", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortfolioListPositionsResponse,
        )

    async def list_transactions(
        self,
        slug: str,
        *,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioListTransactionsResponse:
        """
        Returns a cursor-paginated audit trail of the caller's trades and transactions within the tournament, newest first.

        Args:
            slug: Tournament slug.
            limit: Results per page (max 200).
            cursor: Opaque pagination cursor from a previous response.
            type: Comma-separated event type filter. Valid values: trade, settlement, deposit, fee, market_creation.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListTransactionsResponse: Paginated tournament transaction history.

        Example:
            ```python
            portfolio = await client.tournaments.portfolio.list_transactions(
                slug="alpha-tournament",
                limit=50,
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/tournaments/{slug}/portfolio/transactions", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit, "cursor": cursor, "type": type},
                    portfolio_list_transactions_params.PortfolioListTransactionsParams,
                ),
            ),
            cast_to=PortfolioListTransactionsResponse,
        )

    async def list_fills(
        self,
        slug: str,
        *,
        exchange_id: str | Omit = omit,
        market_id: str | Omit = omit,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioListFillsResponse:
        """
        Returns all trade fills for the caller within this tournament, newest first.

        Args:
            slug: Tournament slug.
            exchange_id: Filter to a specific exchange.
            market_id: Filter to all exchanges in a market.
            limit: Results per page (max 200).
            cursor: Pagination cursor from a previous response.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListFillsResponse: Paginated list of tournament fills.

        Example:
            ```python
            portfolio = await client.tournaments.portfolio.list_fills(
                slug="alpha-tournament",
                limit=50,
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/tournaments/{slug}/portfolio/fills", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"exchange_id": exchange_id, "market_id": market_id, "limit": limit, "cursor": cursor},
                    portfolio_list_fills_params.PortfolioListFillsParams,
                ),
            ),
            cast_to=PortfolioListFillsResponse,
        )

    async def list_history(
        self,
        slug: str,
        *,
        interval: Literal["1h", "6h", "1d", "1w", "all"] | Omit = omit,
        from_: str | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioListHistoryResponse:
        """
        Returns the caller's tournament portfolio-value series from tournament snapshots plus a live tournament valuation. A member with no snapshots receives an initial-virtual-balance seed at their joined-at time. The requested window is capped per interval — `1h` 31 days, `6h` 366 days, `1d` 1827 days, `1w` 1827 days, `all` 1827 days — and responses carry at most 2000 points.

        Args:
            slug: Tournament slug.
            interval: `1h` and `6h` linearly interpolate between selected tournament history points; `all` returns selected stored points without weekly downsampling.
            from_: ISO-8601 start date (inclusive). Must not be after `to`.
            to: ISO-8601 end date (inclusive). Defaults to now.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListHistoryResponse: Tournament portfolio value time series.

        Example:
            ```python
            portfolio = await client.tournaments.portfolio.list_history(
                slug="alpha-tournament",
                interval="1d",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/tournaments/{slug}/portfolio/history", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"interval": interval, "from_": from_, "to": to},
                    portfolio_list_history_params.PortfolioListHistoryParams,
                ),
            ),
            cast_to=PortfolioListHistoryResponse,
        )

    async def list_settlements(
        self,
        slug: str,
        *,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        type: str | Omit = omit,
        market_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioListSettlementsResponse:
        """
        Returns settlement entries (win/loss/refund/correction) for the caller within this tournament. Payouts apply to the tournament virtual balance.

        Args:
            slug: Tournament slug.
            limit: Results per page (max 200).
            cursor: Opaque pagination cursor from a previous response.
            type: Comma-separated settlement type filter. Valid values: win, loss, refund, correction.
            market_id: Restrict to settlements on a single market.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListSettlementsResponse: Paginated list of tournament settlement entries.

        Example:
            ```python
            portfolio = await client.tournaments.portfolio.list_settlements(
                slug="alpha-tournament",
                limit=50,
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/tournaments/{slug}/portfolio/settlements", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit, "cursor": cursor, "type": type, "market_id": market_id},
                    portfolio_list_settlements_params.PortfolioListSettlementsParams,
                ),
            ),
            cast_to=PortfolioListSettlementsResponse,
        )

    async def list_pnl(
        self,
        slug: str,
        *,
        period: Literal["day", "week", "month", "quarter", "year", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioListPnlResponse:
        """
        Returns the caller's tournament account value, unrealized P&L, period P&L, ROI, and Sharpe ratio. All figures are scoped to the tournament's virtual balance and tournament valuation prices. If nonzero holdings exist without valuation_price, returns 409 instead of valuing them at a neutral default. Bounded periods are rolling windows measured back from the request time (`day` 1, `week` 7, `month` 30, `quarter` 90, `year` 365 days), unlike the calendar-aligned leaderboard periods. Period P&L and ROI use the latest tournament snapshot at or before the period start, falling back to the initial virtual balance for members who joined inside the window; `periodPnl` is null for `all`. For `period=all`, ROI is computed relative to the tournament's initial virtual balance. Sharpe is the mean daily return over its standard deviation annualized by √252, and null when the daily returns have no usable variance.

        Args:
            slug: Tournament slug.
            period: Rolling lookback window measured back from the request time; `all` is unbounded.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListPnlResponse: Tournament P&L summary.

        Example:
            ```python
            portfolio = await client.tournaments.portfolio.list_pnl(
                slug="alpha-tournament",
                period="quarter",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/tournaments/{slug}/portfolio/pnl", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"period": period}, portfolio_list_pnl_params.PortfolioListPnlParams),
            ),
            cast_to=PortfolioListPnlResponse,
        )


class PortfolioResourceWithRawResponse:
    def __init__(self, portfolio: PortfolioResource) -> None:
        self._portfolio = portfolio

        self.list_positions = to_raw_response_wrapper(
            portfolio.list_positions,
        )
        self.list_transactions = to_raw_response_wrapper(
            portfolio.list_transactions,
        )
        self.list_fills = to_raw_response_wrapper(
            portfolio.list_fills,
        )
        self.list_history = to_raw_response_wrapper(
            portfolio.list_history,
        )
        self.list_settlements = to_raw_response_wrapper(
            portfolio.list_settlements,
        )
        self.list_pnl = to_raw_response_wrapper(
            portfolio.list_pnl,
        )


class AsyncPortfolioResourceWithRawResponse:
    def __init__(self, portfolio: AsyncPortfolioResource) -> None:
        self._portfolio = portfolio

        self.list_positions = async_to_raw_response_wrapper(
            portfolio.list_positions,
        )
        self.list_transactions = async_to_raw_response_wrapper(
            portfolio.list_transactions,
        )
        self.list_fills = async_to_raw_response_wrapper(
            portfolio.list_fills,
        )
        self.list_history = async_to_raw_response_wrapper(
            portfolio.list_history,
        )
        self.list_settlements = async_to_raw_response_wrapper(
            portfolio.list_settlements,
        )
        self.list_pnl = async_to_raw_response_wrapper(
            portfolio.list_pnl,
        )


class PortfolioResourceWithStreamingResponse:
    def __init__(self, portfolio: PortfolioResource) -> None:
        self._portfolio = portfolio

        self.list_positions = to_streamed_response_wrapper(
            portfolio.list_positions,
        )
        self.list_transactions = to_streamed_response_wrapper(
            portfolio.list_transactions,
        )
        self.list_fills = to_streamed_response_wrapper(
            portfolio.list_fills,
        )
        self.list_history = to_streamed_response_wrapper(
            portfolio.list_history,
        )
        self.list_settlements = to_streamed_response_wrapper(
            portfolio.list_settlements,
        )
        self.list_pnl = to_streamed_response_wrapper(
            portfolio.list_pnl,
        )


class AsyncPortfolioResourceWithStreamingResponse:
    def __init__(self, portfolio: AsyncPortfolioResource) -> None:
        self._portfolio = portfolio

        self.list_positions = async_to_streamed_response_wrapper(
            portfolio.list_positions,
        )
        self.list_transactions = async_to_streamed_response_wrapper(
            portfolio.list_transactions,
        )
        self.list_fills = async_to_streamed_response_wrapper(
            portfolio.list_fills,
        )
        self.list_history = async_to_streamed_response_wrapper(
            portfolio.list_history,
        )
        self.list_settlements = async_to_streamed_response_wrapper(
            portfolio.list_settlements,
        )
        self.list_pnl = async_to_streamed_response_wrapper(
            portfolio.list_pnl,
        )
