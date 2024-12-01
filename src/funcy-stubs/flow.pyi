from collections.abc import Iterable
from contextlib import nullcontext, suppress
from datetime import datetime, timedelta
from threading import Lock
from types import TracebackType
from typing import (
    Any,
    Callable,
    ContextManager,
    NoReturn,
    Protocol,
    SupportsBytes,
    overload,
)

from funcy.flow import ErrorRateExceeded

from ._types import D, P, S, SupportsString, T, T_co

class ExceptionProtocol(Protocol[P]):
    def __new__(cls) -> BaseException: ...
    def __init__(self, *args: P.args, **kwargs: P.kwargs) -> None: ...

class LimitRateCallableProtocol(Protocol[P, T_co]):
    fails: int
    blocked: datetime | None

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T_co: ...

class ThrottleCallableProtocol(Protocol[P, T_co]):
    blocked_until: datetime | None

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T_co: ...

class OncePerCallableProtocol(Protocol[P, T]):
    lock: Lock
    done_set: set[T]
    done_list: list[T]

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T: ...

@overload
def raiser(exception_or_class: str) -> Callable[..., NoReturn]: ...
@overload
def raiser(
    exception_or_class: type[ExceptionProtocol[P]],
    *args: P.args,
    **kwargs: P.kwargs,
) -> Callable[..., NoReturn]: ...
def ignore(
    errors: Iterable[type[Exception]] | type[Exception],
    default: D = None,
) -> Callable[[Callable[P, T]], Callable[P, T | D]]: ...
def silent(func: Callable[P, T]) -> Callable[P, T]: ...

class reraise:
    def __init__(
        self,
        errors: Iterable[type[Exception]] | type[Exception],
        into: Callable[[Exception], Exception] | type[Exception],
    ) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...

def retry(
    tries: int,
    errors: Iterable[type[Exception]] | type[Exception] = ...,
    timeout: int | Callable[[int], int] = 0,
    filter_errors: Callable[[Exception], bool] | None = None,
) -> Callable[[Callable[P, T]], Callable[P, T]]: ...
def fallback(
    *approaches: Callable[[], T]
    | tuple[Callable[[], T], type[Exception] | Iterable[type[Exception]]],
) -> T | None: ...
def limit_error_rate(
    fails: int,
    timeout: timedelta | int,
    exception: Exception = ...,
) -> Callable[[Callable[P, T]], LimitRateCallableProtocol[P, T]]: ...
def throttle(
    period: float | timedelta,
) -> Callable[[Callable[P, T]], ThrottleCallableProtocol[P, T]]: ...
def post_processing(
    func: Callable[[T], S],
) -> Callable[[Callable[P, T]], Callable[P, S]]: ...
def collecting(func: Callable[P, Iterable[T]]) -> Callable[P, list[T]]: ...
@overload
def joining(
    sep: str,
) -> Callable[[Callable[P, Iterable[SupportsString]]], Callable[P, str]]: ...
@overload
def joining(
    sep: bytes,
) -> Callable[[Callable[P, Iterable[SupportsBytes]]], Callable[P, bytes]]: ...
def once_per(
    *argsnames: Any,
) -> Callable[[Callable[P, T]], OncePerCallableProtocol[P, T]]: ...
def once(func: Callable[P, T]) -> OncePerCallableProtocol[P, T]: ...
def once_per_args(func: Callable[P, T]) -> OncePerCallableProtocol[P, T]: ...
def wrap_with(
    ctx: ContextManager[Any],
) -> Callable[[Callable[P, T]], Callable[P, T]]: ...

__all__ = (
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
)
