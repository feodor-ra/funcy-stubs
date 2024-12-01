from collections.abc import Iterable
from types import TracebackType
from typing import Any, Callable, Generic, Literal, TypeVar, overload

from typing_extensions import Self, TypeAlias

from ._types import P, T

PrintFunc: TypeAlias = Callable[[str], Any]
Unit: TypeAlias = Literal["auto", "ns", "mks", "ms", "s"]
_PrintFuncType = TypeVar("_PrintFuncType", bound=PrintFunc)

def tap(x: T, label: str | None = None) -> T: ...
def log_calls(
    print_func: PrintFunc,
    errors: bool = True,
    stack: bool = True,
    repr_len: int = ...,
) -> Callable[[Callable[P, T]], Callable[P, T]]: ...
@overload
def print_calls(
    errors: bool = True,
    stack: bool = True,
    repr_len: int = ...,
) -> Callable[[Callable[P, T]], Callable[P, T]]: ...
@overload
def print_calls(func: Callable[P, T]) -> Callable[P, T]: ...
def log_enters(
    print_func: PrintFunc,
    repr_len: int = ...,
) -> Callable[[Callable[P, T]], Callable[P, T]]: ...
@overload
def print_enters(repr_len: int = ...) -> Callable[[Callable[P, T]], Callable[P, T]]: ...
@overload
def print_enters(func: Callable[P, T]) -> Callable[P, T]: ...
def log_exits(
    print_func: PrintFunc,
    errors: bool = True,
    stack: bool = True,
    repr_len: int = ...,
) -> Callable[[Callable[P, T]], Callable[P, T]]: ...
@overload
def print_exits(
    errors: bool = True,
    stack: bool = True,
    repr_len: int = ...,
) -> Callable[[Callable[P, T]], Callable[P, T]]: ...
@overload
def print_exits(func: Callable[P, T]) -> Callable[P, T]: ...

class LabeledContextDecorator(Generic[_PrintFuncType]):
    print_func: _PrintFuncType
    label: str | None
    repr_len: int

    def __enter__(self) -> Self: ...
    @overload
    def __exit__(
        self,
        exc_type: None,
        exc_value: None,
        exc_tb: None,
    ) -> None: ...
    @overload
    def __exit__(
        self,
        exc_type: type[BaseException],
        exc_value: BaseException,
        exc_tb: TracebackType,
    ) -> None: ...

class log_errors(LabeledContextDecorator[_PrintFuncType]):
    stack: int

    def __init__(
        self,
        print_func: _PrintFuncType,
        label: str | None = None,
        stack: bool = True,
        repr_len: int = ...,
    ) -> None: ...
    def __call__(
        self,
        func: Callable[P, T],
    ) -> Callable[P, T]: ...

class print_errors(log_errors[PrintFunc]):
    def __init__(
        self,
        label: str | None = None,
        stack: bool = True,
        repr_len: int = ...,
    ) -> None: ...
    def __call__(
        self,
        func: Callable[P, T],
    ) -> Callable[P, T]: ...

class log_durations(LabeledContextDecorator[_PrintFuncType]):
    format_time: Callable[[float], str]
    threshold: int
    start: float

    def __init__(
        self,
        print_func: _PrintFuncType,
        label: str | None = None,
        unit: Unit = "auto",
        threshold: int = -1,
        repr_len: int = ...,
    ) -> None: ...
    def __call__(
        self,
        func: Callable[P, T],
    ) -> Callable[P, T]: ...

class print_durations(log_durations[PrintFunc]):
    def __init__(
        self,
        label: str | None = None,
        unit: Unit = "auto",
        threshold: int = -1,
        repr_len: int = ...,
    ) -> None: ...
    def __call__(
        self,
        func: Callable[P, T],
    ) -> Callable[P, T]: ...

def log_iter_durations(
    seq: Iterable[T],
    print_func: PrintFunc,
    label: str | None = None,
    unit: Unit = "auto",
) -> Iterable[T]: ...
def print_iter_durations(
    seq: Iterable[T],
    label: str | None = None,
    unit: Unit = "auto",
) -> Iterable[T]: ...

__all__ = (
    "log_calls",
    "log_durations",
    "log_enters",
    "log_errors",
    "log_exits",
    "log_iter_durations",
    "print_calls",
    "print_durations",
    "print_enters",
    "print_errors",
    "print_exits",
    "print_iter_durations",
    "tap",
)
