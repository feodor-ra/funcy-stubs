from datetime import timedelta
from typing import Any, Callable, Hashable, Protocol, TypeVar, overload

from typing_extensions import ParamSpec

_P = ParamSpec("_P")
_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)

class MemoizeProtocol(Protocol[_P, _T_co]):
    def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> _T_co: ...
    def invalidate(self, *args: _P.args, **kwargs: _P.kwargs) -> None: ...
    def invalidate_all(self) -> None: ...

@overload
def memoize(
    *,
    key_func: Callable[_P, Hashable] | None = None,
) -> Callable[[Callable[_P, _T_co]], MemoizeProtocol[_P, _T_co]]: ...
@overload
def memoize(
    func: Callable[_P, _T],
    /,
    *,
    key_func: Callable[_P, Hashable] | None = None,
) -> MemoizeProtocol[_P, _T]: ...
def cache(
    timeout: float | timedelta,
    *,
    key_func: Callable[_P, Hashable] | None = None,
) -> Callable[[Callable[_P, _T_co]], MemoizeProtocol[_P, _T_co]]: ...
def make_lookuper(func: Callable[..., _T]) -> Callable[[Any], _T]: ...
def silent_lookuper(func: Callable[..., _T]) -> Callable[[Any], _T]: ...

__all__ = ("cache", "make_lookuper", "memoize", "silent_lookuper")
