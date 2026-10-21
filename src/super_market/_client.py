# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import os
import threading
from typing import TYPE_CHECKING, Any, Mapping, cast
from typing_extensions import Literal, Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, is_mapping_t, get_async_library
from ._compat import cached_property
from ._exceptions import APIStatusError, SuperMarketAPIError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._version import __version__

if TYPE_CHECKING:
    from .resources import (
        markets,
        exchanges,
        orders,
        portfolio,
        account,
        tournaments,
        leaderboards,
        dmm,
        realtime,
        relationships_all,
    )
    from .resources.markets import MarketsResource, AsyncMarketsResource
    from .resources.exchanges import ExchangesResource, AsyncExchangesResource
    from .resources.orders import OrdersResource, AsyncOrdersResource
    from .resources.portfolio import PortfolioResource, AsyncPortfolioResource
    from .resources.account import AccountResource, AsyncAccountResource
    from .resources.tournaments import TournamentsResource, AsyncTournamentsResource
    from .resources.leaderboards import LeaderboardsResource, AsyncLeaderboardsResource
    from .resources.dmm import DmmResource, AsyncDmmResource
    from .resources.realtime import RealtimeResource, AsyncRealtimeResource
    from .resources.relationships_all import RelationshipsAllResource, AsyncRelationshipsAllResource

# Serializes lazy resource imports so concurrent cold access from multiple
# threads cannot deadlock on CPython import locks (see CPython 3.14).
_RESOURCE_IMPORT_LOCK = threading.RLock()

ENVIRONMENTS: dict[str, str] = {
    "production": "https://www.thesuper.market/api/v1",
    "current_environment": "/api/v1",
}

__all__ = [
    "ENVIRONMENTS",
    "SuperMarketAPI",
    "AsyncSuperMarketAPI",
    "Client",
    "AsyncClient",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
]


class SuperMarketAPI(SyncAPIClient):
    # client options
    bearer_auth: str

    _environment: Literal["production", "current_environment"] | NotGiven

    def __init__(
        self,
        *,
        bearer_auth: str | None = None,
        environment: Literal["production", "current_environment"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous SuperMarketAPI client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `bearer_auth` from `BEARER_AUTH`
        """
        if bearer_auth is None:
            bearer_auth = os.environ.get("BEARER_AUTH")
        if bearer_auth is None:
            raise SuperMarketAPIError(
                "The bearer_auth client option must be set either by passing bearer_auth to the client or by setting the BEARER_AUTH environment variable"
            )
        self.bearer_auth = bearer_auth
        self._environment = environment
        base_url_env = os.environ.get("DEFAULT_TEAM_7RVB5_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # An explicit `base_url` wins over `environment` so callers can point a
            # pinned-environment client at a proxy or mock, and so `copy()` can pass
            # both the inherited host and the inherited environment without conflict.
            base_url = cast("str | httpx.URL", base_url)
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; the base URL environment variable and the `environment` argument are both set. Pass base_url=None to use the environment.",
                )
            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"
            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        custom_headers_env = os.environ.get("DEFAULT_TEAM_7RVB5_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}
        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )
        self._idempotency_header = None
        self._default_stream_cls = Stream

    @cached_property
    def markets(self) -> "MarketsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.markets import MarketsResource
        return MarketsResource(self)

    @cached_property
    def exchanges(self) -> "ExchangesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.exchanges import ExchangesResource
        return ExchangesResource(self)

    @cached_property
    def orders(self) -> "OrdersResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.orders import OrdersResource
        return OrdersResource(self)

    @cached_property
    def portfolio(self) -> "PortfolioResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.portfolio import PortfolioResource
        return PortfolioResource(self)

    @cached_property
    def account(self) -> "AccountResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.account import AccountResource
        return AccountResource(self)

    @cached_property
    def tournaments(self) -> "TournamentsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.tournaments import TournamentsResource
        return TournamentsResource(self)

    @cached_property
    def leaderboards(self) -> "LeaderboardsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.leaderboards import LeaderboardsResource
        return LeaderboardsResource(self)

    @cached_property
    def dmm(self) -> "DmmResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.dmm import DmmResource
        return DmmResource(self)

    @cached_property
    def realtime(self) -> "RealtimeResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.realtime import RealtimeResource
        return RealtimeResource(self)

    @cached_property
    def relationships_all(self) -> "RelationshipsAllResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.relationships_all import RelationshipsAllResource
        return RelationshipsAllResource(self)

    @cached_property
    def with_raw_response(self) -> SuperMarketAPIWithRawResponse:
        return SuperMarketAPIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SuperMarketAPIWithStreamedResponse:
        return SuperMarketAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {
            **self._bearer_auth_header_auth,
        }

    @override
    def _auth_query(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @override
    def _auth_cookies(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @property
    def _bearer_auth_header_auth(self) -> dict[str, str]:
        value = self.bearer_auth
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Scalar-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(
        self,
        headers: Headers,
        custom_headers: Headers,
        params: Mapping[str, object],
        cookies: Mapping[str, str],
    ) -> None:
        if headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return
        raise TypeError(
            '"Could not resolve authentication method. Expected the bearer_auth to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        bearer_auth: str | None = None,
        environment: Literal["production", "current_environment"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """Create a new client reusing this client's options with optional overrides."""
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")
        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")
        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers
        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query
        http_client = http_client or self._client
        copied_base_url: str | httpx.URL | None = base_url if base_url is not None else self.base_url
        # Environment overrides must resolve their own URL instead of reusing this client's host.
        if environment is not None and base_url is None:
            copied_base_url = None
        return self.__class__(
            bearer_auth=bearer_auth or self.bearer_auth,
            environment=environment if environment is not None else self._environment,
            base_url=copied_base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            _strict_response_validation=self._strict_response_validation,
            **_extra_kwargs,
        )

    with_options = copy

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)
        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)
        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)
        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)
        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)
        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)
        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncSuperMarketAPI(AsyncAPIClient):
    # client options
    bearer_auth: str

    _environment: Literal["production", "current_environment"] | NotGiven

    def __init__(
        self,
        *,
        bearer_auth: str | None = None,
        environment: Literal["production", "current_environment"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncSuperMarketAPI client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `bearer_auth` from `BEARER_AUTH`
        """
        if bearer_auth is None:
            bearer_auth = os.environ.get("BEARER_AUTH")
        if bearer_auth is None:
            raise SuperMarketAPIError(
                "The bearer_auth client option must be set either by passing bearer_auth to the client or by setting the BEARER_AUTH environment variable"
            )
        self.bearer_auth = bearer_auth
        self._environment = environment
        base_url_env = os.environ.get("DEFAULT_TEAM_7RVB5_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # An explicit `base_url` wins over `environment` so callers can point a
            # pinned-environment client at a proxy or mock, and so `copy()` can pass
            # both the inherited host and the inherited environment without conflict.
            base_url = cast("str | httpx.URL", base_url)
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; the base URL environment variable and the `environment` argument are both set. Pass base_url=None to use the environment.",
                )
            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"
            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        custom_headers_env = os.environ.get("DEFAULT_TEAM_7RVB5_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}
        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )
        self._idempotency_header = None
        self._default_stream_cls = AsyncStream

    @cached_property
    def markets(self) -> "AsyncMarketsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.markets import AsyncMarketsResource
        return AsyncMarketsResource(self)

    @cached_property
    def exchanges(self) -> "AsyncExchangesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.exchanges import AsyncExchangesResource
        return AsyncExchangesResource(self)

    @cached_property
    def orders(self) -> "AsyncOrdersResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.orders import AsyncOrdersResource
        return AsyncOrdersResource(self)

    @cached_property
    def portfolio(self) -> "AsyncPortfolioResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.portfolio import AsyncPortfolioResource
        return AsyncPortfolioResource(self)

    @cached_property
    def account(self) -> "AsyncAccountResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.account import AsyncAccountResource
        return AsyncAccountResource(self)

    @cached_property
    def tournaments(self) -> "AsyncTournamentsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.tournaments import AsyncTournamentsResource
        return AsyncTournamentsResource(self)

    @cached_property
    def leaderboards(self) -> "AsyncLeaderboardsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.leaderboards import AsyncLeaderboardsResource
        return AsyncLeaderboardsResource(self)

    @cached_property
    def dmm(self) -> "AsyncDmmResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.dmm import AsyncDmmResource
        return AsyncDmmResource(self)

    @cached_property
    def realtime(self) -> "AsyncRealtimeResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.realtime import AsyncRealtimeResource
        return AsyncRealtimeResource(self)

    @cached_property
    def relationships_all(self) -> "AsyncRelationshipsAllResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.relationships_all import AsyncRelationshipsAllResource
        return AsyncRelationshipsAllResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncSuperMarketAPIWithRawResponse:
        return AsyncSuperMarketAPIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSuperMarketAPIWithStreamedResponse:
        return AsyncSuperMarketAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {
            **self._bearer_auth_header_auth,
        }

    @override
    def _auth_query(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @override
    def _auth_cookies(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @property
    def _bearer_auth_header_auth(self) -> dict[str, str]:
        value = self.bearer_auth
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Scalar-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(
        self,
        headers: Headers,
        custom_headers: Headers,
        params: Mapping[str, object],
        cookies: Mapping[str, str],
    ) -> None:
        if headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return
        raise TypeError(
            '"Could not resolve authentication method. Expected the bearer_auth to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        bearer_auth: str | None = None,
        environment: Literal["production", "current_environment"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """Create a new client reusing this client's options with optional overrides."""
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")
        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")
        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers
        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query
        http_client = http_client or self._client
        copied_base_url: str | httpx.URL | None = base_url if base_url is not None else self.base_url
        # Environment overrides must resolve their own URL instead of reusing this client's host.
        if environment is not None and base_url is None:
            copied_base_url = None
        return self.__class__(
            bearer_auth=bearer_auth or self.bearer_auth,
            environment=environment if environment is not None else self._environment,
            base_url=copied_base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            _strict_response_validation=self._strict_response_validation,
            **_extra_kwargs,
        )

    with_options = copy

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)
        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)
        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)
        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)
        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)
        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)
        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class SuperMarketAPIWithRawResponse:
    _client: SuperMarketAPI

    def __init__(self, client: SuperMarketAPI) -> None:
        self._client = client

    @cached_property
    def markets(self) -> markets.MarketsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.markets import MarketsResourceWithRawResponse
        return MarketsResourceWithRawResponse(self._client.markets)

    @cached_property
    def exchanges(self) -> exchanges.ExchangesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.exchanges import ExchangesResourceWithRawResponse
        return ExchangesResourceWithRawResponse(self._client.exchanges)

    @cached_property
    def orders(self) -> orders.OrdersResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.orders import OrdersResourceWithRawResponse
        return OrdersResourceWithRawResponse(self._client.orders)

    @cached_property
    def portfolio(self) -> portfolio.PortfolioResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.portfolio import PortfolioResourceWithRawResponse
        return PortfolioResourceWithRawResponse(self._client.portfolio)

    @cached_property
    def account(self) -> account.AccountResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.account import AccountResourceWithRawResponse
        return AccountResourceWithRawResponse(self._client.account)

    @cached_property
    def tournaments(self) -> tournaments.TournamentsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.tournaments import TournamentsResourceWithRawResponse
        return TournamentsResourceWithRawResponse(self._client.tournaments)

    @cached_property
    def leaderboards(self) -> leaderboards.LeaderboardsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.leaderboards import LeaderboardsResourceWithRawResponse
        return LeaderboardsResourceWithRawResponse(self._client.leaderboards)

    @cached_property
    def dmm(self) -> dmm.DmmResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.dmm import DmmResourceWithRawResponse
        return DmmResourceWithRawResponse(self._client.dmm)

    @cached_property
    def realtime(self) -> realtime.RealtimeResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.realtime import RealtimeResourceWithRawResponse
        return RealtimeResourceWithRawResponse(self._client.realtime)

    @cached_property
    def relationships_all(self) -> relationships_all.RelationshipsAllResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.relationships_all import RelationshipsAllResourceWithRawResponse
        return RelationshipsAllResourceWithRawResponse(self._client.relationships_all)


class AsyncSuperMarketAPIWithRawResponse:
    _client: AsyncSuperMarketAPI

    def __init__(self, client: AsyncSuperMarketAPI) -> None:
        self._client = client

    @cached_property
    def markets(self) -> markets.AsyncMarketsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.markets import AsyncMarketsResourceWithRawResponse
        return AsyncMarketsResourceWithRawResponse(self._client.markets)

    @cached_property
    def exchanges(self) -> exchanges.AsyncExchangesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.exchanges import AsyncExchangesResourceWithRawResponse
        return AsyncExchangesResourceWithRawResponse(self._client.exchanges)

    @cached_property
    def orders(self) -> orders.AsyncOrdersResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.orders import AsyncOrdersResourceWithRawResponse
        return AsyncOrdersResourceWithRawResponse(self._client.orders)

    @cached_property
    def portfolio(self) -> portfolio.AsyncPortfolioResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.portfolio import AsyncPortfolioResourceWithRawResponse
        return AsyncPortfolioResourceWithRawResponse(self._client.portfolio)

    @cached_property
    def account(self) -> account.AsyncAccountResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.account import AsyncAccountResourceWithRawResponse
        return AsyncAccountResourceWithRawResponse(self._client.account)

    @cached_property
    def tournaments(self) -> tournaments.AsyncTournamentsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.tournaments import AsyncTournamentsResourceWithRawResponse
        return AsyncTournamentsResourceWithRawResponse(self._client.tournaments)

    @cached_property
    def leaderboards(self) -> leaderboards.AsyncLeaderboardsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.leaderboards import AsyncLeaderboardsResourceWithRawResponse
        return AsyncLeaderboardsResourceWithRawResponse(self._client.leaderboards)

    @cached_property
    def dmm(self) -> dmm.AsyncDmmResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.dmm import AsyncDmmResourceWithRawResponse
        return AsyncDmmResourceWithRawResponse(self._client.dmm)

    @cached_property
    def realtime(self) -> realtime.AsyncRealtimeResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.realtime import AsyncRealtimeResourceWithRawResponse
        return AsyncRealtimeResourceWithRawResponse(self._client.realtime)

    @cached_property
    def relationships_all(self) -> relationships_all.AsyncRelationshipsAllResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.relationships_all import AsyncRelationshipsAllResourceWithRawResponse
        return AsyncRelationshipsAllResourceWithRawResponse(self._client.relationships_all)


class SuperMarketAPIWithStreamedResponse:
    _client: SuperMarketAPI

    def __init__(self, client: SuperMarketAPI) -> None:
        self._client = client

    @cached_property
    def markets(self) -> markets.MarketsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.markets import MarketsResourceWithStreamingResponse
        return MarketsResourceWithStreamingResponse(self._client.markets)

    @cached_property
    def exchanges(self) -> exchanges.ExchangesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.exchanges import ExchangesResourceWithStreamingResponse
        return ExchangesResourceWithStreamingResponse(self._client.exchanges)

    @cached_property
    def orders(self) -> orders.OrdersResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.orders import OrdersResourceWithStreamingResponse
        return OrdersResourceWithStreamingResponse(self._client.orders)

    @cached_property
    def portfolio(self) -> portfolio.PortfolioResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.portfolio import PortfolioResourceWithStreamingResponse
        return PortfolioResourceWithStreamingResponse(self._client.portfolio)

    @cached_property
    def account(self) -> account.AccountResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.account import AccountResourceWithStreamingResponse
        return AccountResourceWithStreamingResponse(self._client.account)

    @cached_property
    def tournaments(self) -> tournaments.TournamentsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.tournaments import TournamentsResourceWithStreamingResponse
        return TournamentsResourceWithStreamingResponse(self._client.tournaments)

    @cached_property
    def leaderboards(self) -> leaderboards.LeaderboardsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.leaderboards import LeaderboardsResourceWithStreamingResponse
        return LeaderboardsResourceWithStreamingResponse(self._client.leaderboards)

    @cached_property
    def dmm(self) -> dmm.DmmResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.dmm import DmmResourceWithStreamingResponse
        return DmmResourceWithStreamingResponse(self._client.dmm)

    @cached_property
    def realtime(self) -> realtime.RealtimeResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.realtime import RealtimeResourceWithStreamingResponse
        return RealtimeResourceWithStreamingResponse(self._client.realtime)

    @cached_property
    def relationships_all(self) -> relationships_all.RelationshipsAllResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.relationships_all import RelationshipsAllResourceWithStreamingResponse
        return RelationshipsAllResourceWithStreamingResponse(self._client.relationships_all)


class AsyncSuperMarketAPIWithStreamedResponse:
    _client: AsyncSuperMarketAPI

    def __init__(self, client: AsyncSuperMarketAPI) -> None:
        self._client = client

    @cached_property
    def markets(self) -> markets.AsyncMarketsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.markets import AsyncMarketsResourceWithStreamingResponse
        return AsyncMarketsResourceWithStreamingResponse(self._client.markets)

    @cached_property
    def exchanges(self) -> exchanges.AsyncExchangesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.exchanges import AsyncExchangesResourceWithStreamingResponse
        return AsyncExchangesResourceWithStreamingResponse(self._client.exchanges)

    @cached_property
    def orders(self) -> orders.AsyncOrdersResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.orders import AsyncOrdersResourceWithStreamingResponse
        return AsyncOrdersResourceWithStreamingResponse(self._client.orders)

    @cached_property
    def portfolio(self) -> portfolio.AsyncPortfolioResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.portfolio import AsyncPortfolioResourceWithStreamingResponse
        return AsyncPortfolioResourceWithStreamingResponse(self._client.portfolio)

    @cached_property
    def account(self) -> account.AsyncAccountResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.account import AsyncAccountResourceWithStreamingResponse
        return AsyncAccountResourceWithStreamingResponse(self._client.account)

    @cached_property
    def tournaments(self) -> tournaments.AsyncTournamentsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.tournaments import AsyncTournamentsResourceWithStreamingResponse
        return AsyncTournamentsResourceWithStreamingResponse(self._client.tournaments)

    @cached_property
    def leaderboards(self) -> leaderboards.AsyncLeaderboardsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.leaderboards import AsyncLeaderboardsResourceWithStreamingResponse
        return AsyncLeaderboardsResourceWithStreamingResponse(self._client.leaderboards)

    @cached_property
    def dmm(self) -> dmm.AsyncDmmResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.dmm import AsyncDmmResourceWithStreamingResponse
        return AsyncDmmResourceWithStreamingResponse(self._client.dmm)

    @cached_property
    def realtime(self) -> realtime.AsyncRealtimeResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.realtime import AsyncRealtimeResourceWithStreamingResponse
        return AsyncRealtimeResourceWithStreamingResponse(self._client.realtime)

    @cached_property
    def relationships_all(self) -> relationships_all.AsyncRelationshipsAllResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.relationships_all import AsyncRelationshipsAllResourceWithStreamingResponse
        return AsyncRelationshipsAllResourceWithStreamingResponse(self._client.relationships_all)


# Alias names for the documented `Client` / `AsyncClient` symbols.
Client = SuperMarketAPI
AsyncClient = AsyncSuperMarketAPI
