from collections.abc import Mapping
from collections.abc import Set as AbstractSet
from typing import AnyStr, Callable, Literal, Sequence, overload

from ._types import KT, VT, H, MatchType, P, RegexType, T

@overload
def make_func(f: Callable[P, T], test: bool = ...) -> Callable[P, T]: ...
@overload
def make_func(f: None, test: Literal[True]) -> type[bool]: ...
@overload
def make_func(f: None, test: bool = ...) -> Callable[[T], T]: ...
@overload
def make_func(f: RegexType[AnyStr], test: Literal[True]) -> Callable[[str], bool]: ...
@overload
def make_func(
    f: RegexType[AnyStr], test: Literal[False]
) -> Callable[[str], MatchType[AnyStr] | None]: ...
@overload
def make_func(f: int, test: bool = ...) -> Callable[[Sequence[T]], T]: ...
@overload
def make_func(f: slice, test: bool = ...) -> Callable[[Sequence[T]], Sequence[T]]: ...
@overload
def make_func(f: Mapping[KT, VT], test: bool = ...) -> Callable[[KT], VT]: ...
@overload
def make_func(f: set[H], test: bool = ...) -> Callable[[H], bool]: ...
@overload
def make_pred(pred: Callable[P, T]) -> Callable[P, T]: ...
@overload
def make_pred(pred: None) -> type[bool]: ...
@overload
def make_pred(pred: RegexType[AnyStr]) -> Callable[[str], bool]: ...
@overload
def make_pred(pred: int) -> Callable[[Sequence[T]], T]: ...
@overload
def make_pred(pred: slice) -> Callable[[Sequence[T]], Sequence[T]]: ...
@overload
def make_pred(pred: Mapping[KT, VT]) -> Callable[[KT], VT]: ...
@overload
def make_pred(pred: AbstractSet[H]) -> Callable[[H], bool]: ...

__all__ = ("make_func", "make_pred")
