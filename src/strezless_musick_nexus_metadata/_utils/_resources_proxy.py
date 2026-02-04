from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `strezless_musick_nexus_metadata.resources` module.

    This is used so that we can lazily import `strezless_musick_nexus_metadata.resources` only when
    needed *and* so that users can just import `strezless_musick_nexus_metadata` and reference `strezless_musick_nexus_metadata.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("strezless_musick_nexus_metadata.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
