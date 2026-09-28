from datetime import timedelta
from typing import Any, Callable, Hashable, Protocol, TypeVar, overload

from typing_extensions import Concatenate, ParamSpec, Self

_P = ParamSpec("_P")
_P2 = ParamSpec("_P2")
_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_S = TypeVar("_S")
_S_contra = TypeVar("_S_contra", contravariant=True)

class _MemoizeProtocol(Protocol[_P, _T_co]):
    def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> _T_co: ...
    def invalidate(self, *args: _P.args, **kwargs: _P.kwargs) -> None: ...
    def invalidate_all(self) -> None: ...
    @overload
    def __get__(self, instance: None, owner: type[Any], /) -> Self: ...
    @overload
    def __get__(
        self: _MemoizeProtocol[Concatenate[_S, _P2], _T],
        instance: _S,
        owner: type[Any] | None = None,
        /,
    ) -> _BoundMemoizeProtocol[_S, _P2, _T]: ...
    @overload
    def __get__(self, instance: object, owner: type[Any] | None = None, /) -> Self: ...

class _BoundMemoizeProtocol(Protocol[_S_contra, _P, _T_co]):
    def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> _T_co: ...
    def invalidate(
        self, instance: _S_contra, /, *args: _P.args, **kwargs: _P.kwargs
    ) -> None: ...
    def invalidate_all(self) -> None: ...

@overload
def memoize(
    *,
    key_func: Callable[..., Hashable] | None = None,
) -> Callable[[Callable[_P, _T]], _MemoizeProtocol[_P, _T]]: ...
@overload
def memoize(
    func: Callable[_P, _T],
    /,
    *,
    key_func: Callable[_P, Hashable] | None = None,
) -> _MemoizeProtocol[_P, _T]: ...
@overload
def memoize(
    func: Callable[_P, _T],
    /,
    *,
    key_func: Callable[..., Hashable],
) -> _MemoizeProtocol[_P, _T]: ...
def cache(
    timeout: float | timedelta,
    *,
    key_func: Callable[..., Hashable] | None = None,
) -> Callable[[Callable[_P, _T]], _MemoizeProtocol[_P, _T]]: ...
def make_lookuper(func: Callable[..., _T]) -> Callable[[Any], _T]: ...
def silent_lookuper(func: Callable[..., _T]) -> Callable[[Any], _T]: ...

__all__ = ["cache", "make_lookuper", "memoize", "silent_lookuper"]
