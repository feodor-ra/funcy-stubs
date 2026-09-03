from abc import abstractmethod
from collections.abc import Iterable
from contextlib import AbstractContextManager, nullcontext, suppress
from datetime import datetime, timedelta
from threading import Lock
from types import TracebackType
from typing import (
    Any,
    Callable,
    NoReturn,
    Protocol,
    SupportsBytes,
    TypeVar,
    overload,
)

from typing_extensions import ParamSpec

_P = ParamSpec("_P")
_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_S = TypeVar("_S")
_D = TypeVar("_D")

class _SupportsString(Protocol):
    @abstractmethod
    def __str__(self) -> str: ...

class ErrorRateExceeded(Exception): ...  # ruff: ignore[error-suffix-on-exception-name]

class _ExceptionProtocol(Protocol[_P]):
    def __new__(cls) -> BaseException: ...
    def __init__(self, *args: _P.args, **kwargs: _P.kwargs) -> None: ...

class _LimitRateCallableProtocol(Protocol[_P, _T_co]):
    fails: int
    blocked: datetime | None

    def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> _T_co: ...

class _ThrottleCallableProtocol(Protocol[_P, _T_co]):
    blocked_until: datetime | None

    def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> _T_co: ...

class _OncePerCallableProtocol(Protocol[_P, _T]):
    lock: Lock
    done_set: set[_T]
    done_list: list[_T]

    def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> _T: ...

@overload
def raiser(exception_or_class: str) -> Callable[..., NoReturn]: ...
@overload
def raiser(
    exception_or_class: type[_ExceptionProtocol[_P]],
    *args: _P.args,
    **kwargs: _P.kwargs,
) -> Callable[..., NoReturn]: ...
@overload
def ignore(
    errors: Iterable[type[Exception]] | type[Exception],
    default: None = None,
) -> Callable[[Callable[_P, _T]], Callable[_P, _T | None]]: ...
@overload
def ignore(
    errors: Iterable[type[Exception]] | type[Exception],
    default: _D,
) -> Callable[[Callable[_P, _T]], Callable[_P, _T | _D]]: ...
def silent(func: Callable[_P, _T]) -> Callable[_P, _T]: ...

class _ReraiseContext(Protocol):
    def __enter__(self) -> None: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
    def __call__(self, func: Callable[_P, _T], /) -> Callable[_P, _T]: ...

def reraise(
    errors: Iterable[type[Exception]] | type[Exception],
    into: Callable[[Exception], Exception] | type[Exception] | Exception,
) -> _ReraiseContext: ...
def retry(
    tries: int,
    errors: Iterable[type[Exception]] | type[Exception] = ...,
    timeout: int | Callable[[int], int] = 0,
    filter_errors: Callable[[Exception], bool] | None = None,
) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]: ...
def fallback(
    *approaches: Callable[[], _T]
    | tuple[Callable[[], _T], type[Exception] | Iterable[type[Exception]]],
) -> _T | None: ...
def limit_error_rate(
    fails: int,
    timeout: timedelta | int,
    exception: type[Exception] | Exception = ...,
) -> Callable[[Callable[_P, _T]], _LimitRateCallableProtocol[_P, _T]]: ...
def throttle(
    period: float | timedelta,
) -> Callable[[Callable[_P, _T]], _ThrottleCallableProtocol[_P, _T]]: ...
def post_processing(
    func: Callable[[_T], _S],
) -> Callable[[Callable[_P, _T]], Callable[_P, _S]]: ...
def collecting(func: Callable[_P, Iterable[_T]]) -> Callable[_P, list[_T]]: ...
@overload
def joining(
    sep: str,
) -> Callable[[Callable[_P, Iterable[_SupportsString]]], Callable[_P, str]]: ...
@overload
def joining(
    sep: bytes,
) -> Callable[[Callable[_P, Iterable[SupportsBytes]]], Callable[_P, bytes]]: ...
def once_per(
    *argnames: str,
) -> Callable[[Callable[_P, _T]], _OncePerCallableProtocol[_P, _T]]: ...
def once(func: Callable[_P, _T]) -> _OncePerCallableProtocol[_P, _T]: ...
def once_per_args(func: Callable[_P, _T]) -> _OncePerCallableProtocol[_P, _T]: ...
def wrap_with(
    ctx: AbstractContextManager[Any],
) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]: ...

__all__ = [
    "ErrorRateExceeded",
    "collecting",
    "fallback",
    "ignore",
    "joining",
    "limit_error_rate",
    "nullcontext",
    "once",
    "once_per",
    "once_per_args",
    "post_processing",
    "raiser",
    "reraise",
    "retry",
    "silent",
    "suppress",
    "throttle",
    "wrap_with",
]
