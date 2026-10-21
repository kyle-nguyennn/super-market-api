---
name: super-market-api-python-sdk
description: "Python SDK for Super Market API. Use when writing Python code that calls Super Market API with the super-market package: installing it, constructing and authenticating the client, and calling API operations."
---

# Super Market API Python SDK

Generated Python client for Super Market API, published as `super-market`. Use the generated client instead of hand-writing HTTP requests.

## Install

```sh
pip install super-market
```

## Client setup and authentication

```python
import os

from super_market import SuperMarketAPI

client = SuperMarketAPI(
    bearer_auth=os.environ.get("BEARER_AUTH"),
)
```

Provide credentials using the options below. Environment variables are read automatically when the target runtime supports them:

- `bearer_auth` (env: `BEARER_AUTH`) — API key created under My Profile → API Keys (Create Key); organization Integration API keys are created under the organization's Admin → Settings tab. Use as `Authorization: Bearer <key>` or `X-API-Key: <key>`.

## Calling operations

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

Method names, parameter shapes, and response types are generated from the API description — do not guess them. Look up the exact call signature in [api.md](./api.md) before writing a call.

## Error handling

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

## Requirements

- Python 3.9 or newer

## Reference files

- [README.md](./README.md) — full feature tour: client options, retries and timeouts, logging.
- [api.md](./api.md) — complete catalogue of every operation with request and response types.
