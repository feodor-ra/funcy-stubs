from datetime import timedelta
from typing import Any, Callable, Hashable, Protocol, overload

from ._types import P, T, T_co

class MemoizeProtocol(Protocol[P, T_co]):
    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T_co: ...
    def invalidate(self, *args: P.args, **kwargs: P.kwargs) -> None: ...
    def invalidate_all(self) -> None: ...

@overload
def memoize(
    *,
    key_func: Callable[P, Hashable] | None = None,
) -> Callable[[Callable[P, T_co]], MemoizeProtocol[P, T_co]]: ...
@overload
def memoize(
    func: Callable[P, T],
    /,
    *,
    key_func: Callable[P, Hashable] | None = None,
) -> MemoizeProtocol[P, T]: ...
def cache(
    timeout: float | timedelta,
    *,
    key_func: Callable[P, Hashable] | None = None,
) -> Callable[[Callable[P, T_co]], MemoizeProtocol[P, T_co]]: ...
def make_lookuper(fucn: Callable[..., T]) -> Callable[[Any], T]: ...
def silent_lookuper(fucn: Callable[..., T]) -> Callable[[Any], T]: ...

__all__ = ("cache", "make_lookuper", "memoize", "silent_lookuper")
