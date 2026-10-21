# Super Market API

This library provides convenient access to the Super Market API from Python.

The full API of this library can be found in [api.md](./api.md).

<br />

## Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Reference](./api.md)
- [Async](#async)
- [Authentication](#authentication)
- [Errors](#errors)
- [Client Options](#client-options)
- [Retries and Timeouts](#retries-and-timeouts)
- [Helpers](#helpers)
- [Logging](#logging)
- [Requirements](#requirements)

<br />

## Installation

```sh
pip install super-market
```

<br />

## Usage

```python
import os

from super_market import SuperMarketAPI

client = SuperMarketAPI(
    bearer_auth=os.environ.get("BEARER_AUTH"),
)

market = client.markets.list(
    limit=20,
    sort="recent",
    status="any",
)

print(market)
```

The examples in the following sections assume a `client` configured as shown above.

See the [API reference](./api.md) for every available operation.

<br />

## Async

Every client has an `Async` counterpart (`AsyncSuperMarketAPI`) exposing the same resource tree with `await`.

```python
import asyncio

from super_market import AsyncSuperMarketAPI


async def main() -> None:
    client = AsyncSuperMarketAPI()
    market = await client.markets.list(
        limit=20,
        sort="recent",
        status="any",
    )


asyncio.run(main())
```

<br />

## Authentication

Pass credentials to the generated client constructor. Environment variables are read automatically when supported by the target runtime.

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `bearer_auth` | `str \| None` | - | API key created under My Profile → API Keys (Create Key); organization Integration API keys are created under the organization's Admin → Settings tab. Use as `Authorization: Bearer <key>` or `X-API-Key: <key>`. Defaults to BEARER_AUTH. |

Declared schemes:

- `bearerAuth` bearer token

<br />

## Errors

Non-success responses throw generated API errors. Error objects expose status, headers, response body, and request metadata where the target runtime supports it.

```python
from super_market import APIStatusError

try:
    market = client.markets.list(
        limit=20,
        sort="recent",
        status="any",
    )
except APIStatusError as err:
    print(err.status_code, err.message)
    raise
```

Documented error statuses: `400`, `401`, `403`, `404`, `409`, `422`, `429`, `500`, `502`, `503`.

<br />

## Client Options

Configure the generated client by setting any of these options when you create it.

```python
from super_market import SuperMarketAPI

client = SuperMarketAPI(
    timeout=60.0,
    max_retries=2,
)
```

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `bearer_auth` | `str \| None` | `os.environ.get("BEARER_AUTH")` | API key created under My Profile → API Keys (Create Key); organization Integration API keys are created under the organization's Admin → Settings tab. Use as `Authorization: Bearer <key>` or `X-API-Key: <key>`. |
| `base_url` | `str \| httpx.URL \| None` | - | Override the default API base URL. |
| `timeout` | `float \| Timeout \| None` | `60.0` | Maximum time in seconds to wait for a response before aborting a request. |
| `max_retries` | `int` | `2` | Number of retries for temporary failures. |
| `default_headers` | `Mapping[str, str] \| None` | - | Headers sent with every request. |
| `default_query` | `Mapping[str, object] \| None` | - | Query parameters sent with every request. |

<br />

## Retries and Timeouts

Generated clients support request timeouts and retry temporary failures such as network errors, 408, 409, 429, and 5xx responses. Retry delays honor `Retry-After` headers when present. Tune the retry and timeout client options shown above, or override them per request.

<br />

## Helpers

- Use `client.with_raw_response.<resource>.<method>(...)` to access the raw `httpx.Response` and parse it yourself.
- Use `client.with_streaming_response.<resource>.<method>(...)` to stream a response body without buffering it.

<br />

## Logging

- Set the `DEFAULT_TEAM_7RVB5_LOG` environment variable to `info` or `debug` to enable HTTP logging.
- Logs are emitted through the standard `logging` module under the `super_market` logger.

<br />

## Requirements

- Python 3.9 or newer

Powered by Scalar.

## Package publishing

This is a **Scalar-generated** Python SDK. The PyPI distribution is
`super-market` (imported as `super_market`). Publishing is managed through
GitHub Actions with OIDC Trusted Publishing, not a stored PyPI token.

See [Publishing and release instructions](docs/PUBLISHING.md) for
one-time PyPI registration and version-tagged releases.

> **Trading safety:** This client defaults to automatic request retries.
> For SIG order placement/cancellation use `max_retries=0` and implement
> durable idempotency, unknown-order reconciliation and pretrade risk in
> the calling application. Do not run `tests/smoke-test.py` against
> a real participant account: it includes order-creating endpoints.
