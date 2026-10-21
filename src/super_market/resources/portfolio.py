# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing_extensions import Literal

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.portfolio_list_collateral_response import PortfolioListCollateralResponse
from ..types import (
    portfolio_list_collateral_params,
    portfolio_list_pnl_params,
    portfolio_list_history_params,
    portfolio_list_transactions_params,
    portfolio_list_settlements_params,
    portfolio_list_fills_params,
)
from ..types.portfolio_list_positions_response import PortfolioListPositionsResponse
from ..types.portfolio_list_pnl_response import PortfolioListPnlResponse
from ..types.portfolio_list_history_response import PortfolioListHistoryResponse
from ..types.portfolio_list_transactions_response import PortfolioListTransactionsResponse
from ..types.portfolio_list_settlements_response import PortfolioListSettlementsResponse
from ..types.portfolio_list_fills_response import PortfolioListFillsResponse

__all__ = ["PortfolioResource", "AsyncPortfolioResource"]


class PortfolioResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PortfolioResourceWithRawResponse:
        return PortfolioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PortfolioResourceWithStreamingResponse:
        return PortfolioResourceWithStreamingResponse(self)

    def list_collateral(
        self,
        *,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioListCollateralResponse:
        """
        Returns the authenticated user's component-level ALL collateral advances and guaranteed payout floors. When `tournamentId` is omitted, an organization-bound key reads its organization's default tournament and an unbound key reads the public global context. An explicit `tournamentId` reads one accessible tournament; organization-bound keys are limited to tournaments in their bound organization.

        Args:
            tournament_id: Return collateral from one accessible tournament. Omit to use the organization's default tournament for an organization-bound key or the public global context for an unbound key.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListCollateralResponse: Scope-filtered collateral components.

        Example:
            ```python
            portfolio = client.portfolio.list_collateral()
            ```
        """
        return self._get(
            "/portfolio/collateral",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"tournament_id": tournament_id}, portfolio_list_collateral_params.PortfolioListCollateralParams
                ),
            ),
            cast_to=PortfolioListCollateralResponse,
        )

    def list_positions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioListPositionsResponse:
        """
        Returns open positions for the authenticated user with FIFO lot breakdown and unrealized P&L. An organization-bound key resolves this endpoint to its organization's default tournament and uses tournament valuation prices; an unbound key reads global positions. Use `/tournaments/{slug}/portfolio/positions` for an explicit tournament scope.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListPositionsResponse: Open positions and portfolio summary.

        Example:
            ```python
            portfolio = client.portfolio.list_positions()
            ```
        """
        return self._get(
            "/portfolio/positions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortfolioListPositionsResponse,
        )

    def list_pnl(
        self,
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
        Returns account value, unrealized P&L, period P&L (vs the applicable stored-history baseline), ROI, and annualized Sharpe ratio. An organization-bound key resolves this endpoint to its organization's default tournament and uses the tournament's virtual balance, valuation prices, snapshots, and initial virtual balance; an unbound key reads global portfolio state. Use `/tournaments/{slug}/portfolio/pnl` for an explicit tournament scope.

        Args:
            period: Rolling lookback window for period P&L and Sharpe, measured back from the request time: `day` 1, `week` 7, `month` 30, `quarter` 90, `year` 365 days; `all` is unbounded. Unlike leaderboard periods, these are not calendar-aligned.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListPnlResponse: P&L summary.

        Example:
            ```python
            portfolio = client.portfolio.list_pnl(
                period="quarter",
            )
            ```
        """
        return self._get(
            "/portfolio/pnl",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"period": period}, portfolio_list_pnl_params.PortfolioListPnlParams),
            ),
            cast_to=PortfolioListPnlResponse,
        )

    def list_history(
        self,
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
        Returns continuous time-series portfolio value. An organization-bound key resolves this endpoint to its organization's default tournament and uses tournament snapshots, the member's joined-at seed when no snapshot exists, and a live tournament valuation; an unbound key reads global portfolio history. Use `/tournaments/{slug}/portfolio/history` for an explicit tournament scope. Under global engine authority, legacy daily snapshots strictly before the configured cutover are stitched to projection-backed points at and after the cutover, followed by a live engine-valued point. Before authority opens, the legacy daily-snapshot behavior is unchanged. The requested window is capped per interval — `1h` 31 days, `6h` 366 days, `1d` 1827 days, `1w` 1827 days, `all` 1827 days — and a longer range is rejected rather than truncated. Responses carry at most 2000 points; a series with more is thinned evenly, always keeping the first and last.

        Args:
            interval: `1h` and `6h` are linearly interpolated after selecting the stitched history points (flagged with `interpolated: true`). `all` returns the selected stored points without weekly downsampling.
            from_: ISO-8601 start date (inclusive). Must not be after `to`. Defaults to 1 year before `to`, or to the interval's maximum span where that is shorter (`1h` → 31 days).
            to: ISO-8601 end date (inclusive). Defaults to now.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListHistoryResponse: Portfolio value time series.

        Example:
            ```python
            portfolio = client.portfolio.list_history(
                interval="1d",
            )
            ```
        """
        return self._get(
            "/portfolio/history",
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

    def list_transactions(
        self,
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
        Returns a cursor-paginated audit trail of trades and transactions, newest first. An organization-bound key resolves this endpoint to its organization's default tournament; an unbound key reads global transactions. Use `/tournaments/{slug}/portfolio/transactions` for an explicit tournament scope.

        Args:
            limit: Results per page (max 200).
            cursor: Opaque pagination cursor from a previous response.
            type: Comma-separated event type filter. Valid values: trade, settlement, deposit, fee, market_creation.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListTransactionsResponse: Paginated transaction history.

        Example:
            ```python
            portfolio = client.portfolio.list_transactions(
                limit=50,
            )
            ```
        """
        return self._get(
            "/portfolio/transactions",
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

    def list_settlements(
        self,
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
        Returns settlement entries (win/loss/refund/correction) for the authenticated user. An organization-bound key resolves this endpoint to its organization's default tournament; an unbound key reads global settlements. Use `/tournaments/{slug}/portfolio/settlements` for an explicit tournament scope.

        Args:
            limit: Results per page (max 200).
            cursor: Pagination cursor from a previous response.
            type: Comma-separated settlement type filter. Valid values: win, loss, refund, correction.
            market_id: Restrict to settlements on a single market.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListSettlementsResponse: Paginated list of settlement entries.

        Example:
            ```python
            portfolio = client.portfolio.list_settlements(
                limit=50,
            )
            ```
        """
        return self._get(
            "/portfolio/settlements",
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

    def list_fills(
        self,
        *,
        exchange_id: str | Omit = omit,
        market_id: str | Omit = omit,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioListFillsResponse:
        """
        Returns all trade fills for the authenticated user across all orders, newest first. An organization-bound key resolves an omitted `tournamentId` to its organization's default tournament; an unbound key reads global fills. For per-order fills with aggregate stats, use `GET /orders/{id}/fills`. Every response includes projection `coverage` metadata.

        Args:
            exchange_id: Filter to a specific exchange.
            market_id: Filter to all exchanges in a market.
            limit: Results per page (max 200).
            cursor: Pagination cursor from a previous response.
            tournament_id: Return fills from one accessible tournament. Omit to use the organization's default tournament for an organization-bound key or the public global context for an unbound key.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListFillsResponse: Paginated list of fills.

        Example:
            ```python
            portfolio = client.portfolio.list_fills(
                limit=50,
            )
            ```
        """
        return self._get(
            "/portfolio/fills",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "exchange_id": exchange_id,
                        "market_id": market_id,
                        "limit": limit,
                        "cursor": cursor,
                        "tournament_id": tournament_id,
                    },
                    portfolio_list_fills_params.PortfolioListFillsParams,
                ),
            ),
            cast_to=PortfolioListFillsResponse,
        )


class AsyncPortfolioResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPortfolioResourceWithRawResponse:
        return AsyncPortfolioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPortfolioResourceWithStreamingResponse:
        return AsyncPortfolioResourceWithStreamingResponse(self)

    async def list_collateral(
        self,
        *,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioListCollateralResponse:
        """
        Returns the authenticated user's component-level ALL collateral advances and guaranteed payout floors. When `tournamentId` is omitted, an organization-bound key reads its organization's default tournament and an unbound key reads the public global context. An explicit `tournamentId` reads one accessible tournament; organization-bound keys are limited to tournaments in their bound organization.

        Args:
            tournament_id: Return collateral from one accessible tournament. Omit to use the organization's default tournament for an organization-bound key or the public global context for an unbound key.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListCollateralResponse: Scope-filtered collateral components.

        Example:
            ```python
            portfolio = await client.portfolio.list_collateral()
            ```
        """
        return await self._get(
            "/portfolio/collateral",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tournament_id": tournament_id}, portfolio_list_collateral_params.PortfolioListCollateralParams
                ),
            ),
            cast_to=PortfolioListCollateralResponse,
        )

    async def list_positions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioListPositionsResponse:
        """
        Returns open positions for the authenticated user with FIFO lot breakdown and unrealized P&L. An organization-bound key resolves this endpoint to its organization's default tournament and uses tournament valuation prices; an unbound key reads global positions. Use `/tournaments/{slug}/portfolio/positions` for an explicit tournament scope.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListPositionsResponse: Open positions and portfolio summary.

        Example:
            ```python
            portfolio = await client.portfolio.list_positions()
            ```
        """
        return await self._get(
            "/portfolio/positions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortfolioListPositionsResponse,
        )

    async def list_pnl(
        self,
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
        Returns account value, unrealized P&L, period P&L (vs the applicable stored-history baseline), ROI, and annualized Sharpe ratio. An organization-bound key resolves this endpoint to its organization's default tournament and uses the tournament's virtual balance, valuation prices, snapshots, and initial virtual balance; an unbound key reads global portfolio state. Use `/tournaments/{slug}/portfolio/pnl` for an explicit tournament scope.

        Args:
            period: Rolling lookback window for period P&L and Sharpe, measured back from the request time: `day` 1, `week` 7, `month` 30, `quarter` 90, `year` 365 days; `all` is unbounded. Unlike leaderboard periods, these are not calendar-aligned.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListPnlResponse: P&L summary.

        Example:
            ```python
            portfolio = await client.portfolio.list_pnl(
                period="quarter",
            )
            ```
        """
        return await self._get(
            "/portfolio/pnl",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"period": period}, portfolio_list_pnl_params.PortfolioListPnlParams),
            ),
            cast_to=PortfolioListPnlResponse,
        )

    async def list_history(
        self,
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
        Returns continuous time-series portfolio value. An organization-bound key resolves this endpoint to its organization's default tournament and uses tournament snapshots, the member's joined-at seed when no snapshot exists, and a live tournament valuation; an unbound key reads global portfolio history. Use `/tournaments/{slug}/portfolio/history` for an explicit tournament scope. Under global engine authority, legacy daily snapshots strictly before the configured cutover are stitched to projection-backed points at and after the cutover, followed by a live engine-valued point. Before authority opens, the legacy daily-snapshot behavior is unchanged. The requested window is capped per interval — `1h` 31 days, `6h` 366 days, `1d` 1827 days, `1w` 1827 days, `all` 1827 days — and a longer range is rejected rather than truncated. Responses carry at most 2000 points; a series with more is thinned evenly, always keeping the first and last.

        Args:
            interval: `1h` and `6h` are linearly interpolated after selecting the stitched history points (flagged with `interpolated: true`). `all` returns the selected stored points without weekly downsampling.
            from_: ISO-8601 start date (inclusive). Must not be after `to`. Defaults to 1 year before `to`, or to the interval's maximum span where that is shorter (`1h` → 31 days).
            to: ISO-8601 end date (inclusive). Defaults to now.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListHistoryResponse: Portfolio value time series.

        Example:
            ```python
            portfolio = await client.portfolio.list_history(
                interval="1d",
            )
            ```
        """
        return await self._get(
            "/portfolio/history",
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

    async def list_transactions(
        self,
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
        Returns a cursor-paginated audit trail of trades and transactions, newest first. An organization-bound key resolves this endpoint to its organization's default tournament; an unbound key reads global transactions. Use `/tournaments/{slug}/portfolio/transactions` for an explicit tournament scope.

        Args:
            limit: Results per page (max 200).
            cursor: Opaque pagination cursor from a previous response.
            type: Comma-separated event type filter. Valid values: trade, settlement, deposit, fee, market_creation.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListTransactionsResponse: Paginated transaction history.

        Example:
            ```python
            portfolio = await client.portfolio.list_transactions(
                limit=50,
            )
            ```
        """
        return await self._get(
            "/portfolio/transactions",
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

    async def list_settlements(
        self,
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
        Returns settlement entries (win/loss/refund/correction) for the authenticated user. An organization-bound key resolves this endpoint to its organization's default tournament; an unbound key reads global settlements. Use `/tournaments/{slug}/portfolio/settlements` for an explicit tournament scope.

        Args:
            limit: Results per page (max 200).
            cursor: Pagination cursor from a previous response.
            type: Comma-separated settlement type filter. Valid values: win, loss, refund, correction.
            market_id: Restrict to settlements on a single market.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListSettlementsResponse: Paginated list of settlement entries.

        Example:
            ```python
            portfolio = await client.portfolio.list_settlements(
                limit=50,
            )
            ```
        """
        return await self._get(
            "/portfolio/settlements",
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

    async def list_fills(
        self,
        *,
        exchange_id: str | Omit = omit,
        market_id: str | Omit = omit,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioListFillsResponse:
        """
        Returns all trade fills for the authenticated user across all orders, newest first. An organization-bound key resolves an omitted `tournamentId` to its organization's default tournament; an unbound key reads global fills. For per-order fills with aggregate stats, use `GET /orders/{id}/fills`. Every response includes projection `coverage` metadata.

        Args:
            exchange_id: Filter to a specific exchange.
            market_id: Filter to all exchanges in a market.
            limit: Results per page (max 200).
            cursor: Pagination cursor from a previous response.
            tournament_id: Return fills from one accessible tournament. Omit to use the organization's default tournament for an organization-bound key or the public global context for an unbound key.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PortfolioListFillsResponse: Paginated list of fills.

        Example:
            ```python
            portfolio = await client.portfolio.list_fills(
                limit=50,
            )
            ```
        """
        return await self._get(
            "/portfolio/fills",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "exchange_id": exchange_id,
                        "market_id": market_id,
                        "limit": limit,
                        "cursor": cursor,
                        "tournament_id": tournament_id,
                    },
                    portfolio_list_fills_params.PortfolioListFillsParams,
                ),
            ),
            cast_to=PortfolioListFillsResponse,
        )


class PortfolioResourceWithRawResponse:
    def __init__(self, portfolio: PortfolioResource) -> None:
        self._portfolio = portfolio

        self.list_collateral = to_raw_response_wrapper(
            portfolio.list_collateral,
        )
        self.list_positions = to_raw_response_wrapper(
            portfolio.list_positions,
        )
        self.list_pnl = to_raw_response_wrapper(
            portfolio.list_pnl,
        )
        self.list_history = to_raw_response_wrapper(
            portfolio.list_history,
        )
        self.list_transactions = to_raw_response_wrapper(
            portfolio.list_transactions,
        )
        self.list_settlements = to_raw_response_wrapper(
            portfolio.list_settlements,
        )
        self.list_fills = to_raw_response_wrapper(
            portfolio.list_fills,
        )


class AsyncPortfolioResourceWithRawResponse:
    def __init__(self, portfolio: AsyncPortfolioResource) -> None:
        self._portfolio = portfolio

        self.list_collateral = async_to_raw_response_wrapper(
            portfolio.list_collateral,
        )
        self.list_positions = async_to_raw_response_wrapper(
            portfolio.list_positions,
        )
        self.list_pnl = async_to_raw_response_wrapper(
            portfolio.list_pnl,
        )
        self.list_history = async_to_raw_response_wrapper(
            portfolio.list_history,
        )
        self.list_transactions = async_to_raw_response_wrapper(
            portfolio.list_transactions,
        )
        self.list_settlements = async_to_raw_response_wrapper(
            portfolio.list_settlements,
        )
        self.list_fills = async_to_raw_response_wrapper(
            portfolio.list_fills,
        )


class PortfolioResourceWithStreamingResponse:
    def __init__(self, portfolio: PortfolioResource) -> None:
        self._portfolio = portfolio

        self.list_collateral = to_streamed_response_wrapper(
            portfolio.list_collateral,
        )
        self.list_positions = to_streamed_response_wrapper(
            portfolio.list_positions,
        )
        self.list_pnl = to_streamed_response_wrapper(
            portfolio.list_pnl,
        )
        self.list_history = to_streamed_response_wrapper(
            portfolio.list_history,
        )
        self.list_transactions = to_streamed_response_wrapper(
            portfolio.list_transactions,
        )
        self.list_settlements = to_streamed_response_wrapper(
            portfolio.list_settlements,
        )
        self.list_fills = to_streamed_response_wrapper(
            portfolio.list_fills,
        )


class AsyncPortfolioResourceWithStreamingResponse:
    def __init__(self, portfolio: AsyncPortfolioResource) -> None:
        self._portfolio = portfolio

        self.list_collateral = async_to_streamed_response_wrapper(
            portfolio.list_collateral,
        )
        self.list_positions = async_to_streamed_response_wrapper(
            portfolio.list_positions,
        )
        self.list_pnl = async_to_streamed_response_wrapper(
            portfolio.list_pnl,
        )
        self.list_history = async_to_streamed_response_wrapper(
            portfolio.list_history,
        )
        self.list_transactions = async_to_streamed_response_wrapper(
            portfolio.list_transactions,
        )
        self.list_settlements = async_to_streamed_response_wrapper(
            portfolio.list_settlements,
        )
        self.list_fills = async_to_streamed_response_wrapper(
            portfolio.list_fills,
        )
