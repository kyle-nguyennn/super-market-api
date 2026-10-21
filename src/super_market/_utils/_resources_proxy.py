from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `super_market.resources` module.

    This is used so that we can lazily import `super_market.resources` only when
    needed *and* so that users can just import `super_market` and reference `super_market.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("super_market.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
