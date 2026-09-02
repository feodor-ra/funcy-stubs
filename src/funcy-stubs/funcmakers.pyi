from collections.abc import Mapping
from collections.abc import Set as AbstractSet
from re import Pattern
from typing import AnyStr, Callable, Hashable, Literal, Sequence, TypeVar, overload

from typing_extensions import ParamSpec, TypeAliasType

_P = ParamSpec("_P")
_T = TypeVar("_T")
_KT = TypeVar("_KT", bound=Hashable)
_VT = TypeVar("_VT")
_H = TypeVar("_H", bound=Hashable)

_RegexType = TypeAliasType(
    "_RegexType",
    AnyStr | Pattern[AnyStr],
    type_params=(AnyStr,),
)
_MatchType = TypeAliasType(
    "_MatchType",
    AnyStr | tuple[AnyStr, ...] | dict[str, AnyStr],
    type_params=(AnyStr,),
)

@overload
def make_func(f: Callable[_P, _T], test: bool = ...) -> Callable[_P, _T]: ...
@overload
def make_func(f: None, test: Literal[True]) -> type[bool]: ...  # type: ignore[overload-overlap]
@overload
def make_func(f: None, test: bool = ...) -> Callable[[_T], _T]: ...
@overload
def make_func(f: _RegexType[AnyStr], test: Literal[True]) -> Callable[[str], bool]: ...
@overload
def make_func(
    f: _RegexType[AnyStr], test: Literal[False]
) -> Callable[[str], _MatchType[AnyStr] | None]: ...
@overload
def make_func(f: int, test: bool = ...) -> Callable[[Sequence[_T]], _T]: ...
@overload
def make_func(f: slice, test: bool = ...) -> Callable[[Sequence[_T]], Sequence[_T]]: ...
@overload
def make_func(f: Mapping[_KT, _VT], test: bool = ...) -> Callable[[_KT], _VT]: ...
@overload
def make_func(f: set[_H], test: bool = ...) -> Callable[[_H], bool]: ...
@overload
def make_pred(pred: Callable[_P, _T]) -> Callable[_P, _T]: ...
@overload
def make_pred(pred: None) -> type[bool]: ...
@overload
def make_pred(pred: _RegexType[AnyStr]) -> Callable[[str], bool]: ...
@overload
def make_pred(pred: int) -> Callable[[Sequence[_T]], _T]: ...
@overload
def make_pred(pred: slice) -> Callable[[Sequence[_T]], Sequence[_T]]: ...
@overload
def make_pred(pred: Mapping[_KT, _VT]) -> Callable[[_KT], _VT]: ...
@overload
def make_pred(pred: AbstractSet[_H]) -> Callable[[_H], bool]: ...

__all__ = ("make_func", "make_pred")
