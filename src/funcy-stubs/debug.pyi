from collections.abc import Iterable
from types import TracebackType
from typing import Any, Callable, Generic, Literal, TypeVar, overload

from typing_extensions import ParamSpec, Self, TypeAlias

_P = ParamSpec("_P")
_T = TypeVar("_T")

PrintFunc: TypeAlias = Callable[[str], Any]
Unit: TypeAlias = Literal["auto", "ns", "mks", "ms", "s"]
_PrintFuncType = TypeVar("_PrintFuncType", bound=PrintFunc)

def tap(x: _T, label: str | None = None) -> _T: ...
def log_calls(
    print_func: PrintFunc,
    errors: bool = True,
    stack: bool = True,
    repr_len: int = ...,
) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]: ...
@overload
def print_calls(
    errors: bool = True,
    stack: bool = True,
    repr_len: int = ...,
) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]: ...
@overload
def print_calls(func: Callable[_P, _T]) -> Callable[_P, _T]: ...
def log_enters(
    print_func: PrintFunc,
    repr_len: int = ...,
) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]: ...
@overload
def print_enters(
    repr_len: int = ...,
) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]: ...
@overload
def print_enters(func: Callable[_P, _T]) -> Callable[_P, _T]: ...
def log_exits(
    print_func: PrintFunc,
    errors: bool = True,
    stack: bool = True,
    repr_len: int = ...,
) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]: ...
@overload
def print_exits(
    errors: bool = True,
    stack: bool = True,
    repr_len: int = ...,
) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]: ...
@overload
def print_exits(func: Callable[_P, _T]) -> Callable[_P, _T]: ...

class LabeledContextDecorator(Generic[_PrintFuncType]):
    print_func: _PrintFuncType
    label: str | None
    repr_len: int

    def __init__(
        self,
        print_func: _PrintFuncType,
        label: str | None = None,
        repr_len: int = ...,
    ) -> None: ...
    @overload
    def __call__(self, label: Callable[_P, _T], /) -> Callable[_P, _T]: ...
    @overload
    def __call__(self, label: str | None = None, /, **kwargs: Any) -> Self: ...
    def decorator(self, func: Callable[_P, _T]) -> Callable[_P, _T]: ...
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
    stack: bool

    def __init__(
        self,
        print_func: _PrintFuncType,
        label: str | None = None,
        stack: bool = True,
        repr_len: int = ...,
    ) -> None: ...

print_errors: log_errors[PrintFunc]

class log_durations(LabeledContextDecorator[_PrintFuncType]):
    format_time: Callable[[float], str]
    threshold: float
    start: float

    def __init__(
        self,
        print_func: _PrintFuncType,
        label: str | None = None,
        unit: Unit = "auto",
        threshold: float = -1,
        repr_len: int = ...,
    ) -> None: ...

print_durations: log_durations[PrintFunc]

def log_iter_durations(
    seq: Iterable[_T],
    print_func: PrintFunc,
    label: str | None = None,
    unit: Unit = "auto",
) -> Iterable[_T]: ...
def print_iter_durations(
    seq: Iterable[_T],
    label: str | None = None,
    unit: Unit = "auto",
) -> Iterable[_T]: ...

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
