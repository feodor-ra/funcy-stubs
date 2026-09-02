from abc import abstractmethod
from collections.abc import Mapping, Sequence
from functools import partial
from functools import reduce as reduce
from re import Pattern
from typing import (
    Any,
    AnyStr,
    Callable,
    Hashable,
    Iterable,
    Protocol,
    TypeVar,
    overload,
)

from typing_extensions import ParamSpec, TypeAlias, TypeAliasType

_P = ParamSpec("_P")
_T = TypeVar("_T")
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
_T4 = TypeVar("_T4")
_T5 = TypeVar("_T5")
_S = TypeVar("_S")
_D = TypeVar("_D")
_KT = TypeVar("_KT", bound=Hashable)
_VT = TypeVar("_VT")
_H = TypeVar("_H", bound=Hashable)
_T_co = TypeVar("_T_co", covariant=True)

class _SupportsBool(Protocol):
    @abstractmethod
    def __bool__(self) -> bool: ...

_B = TypeVar("_B", bound=_SupportsBool)

_Boolean = TypeAliasType("_Boolean", bool | _B, type_params=(_B,))
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

def identity(x: _T) -> _T: ...
def constantly(x: _T) -> Callable[..., _T]: ...
def caller(
    *args: _P.args,  # type: ignore[valid-type]  # ty: ignore[unbound-type-variable]
    **kwargs: _P.kwargs,  # type: ignore[valid-type]
) -> Callable[[Callable[_P, _T]], _T]: ...

func_partial: TypeAlias = partial[Any]  # ruff: ignore[snake-case-type-alias]

rpartial: TypeAlias = partial[Any]  # ruff: ignore[snake-case-type-alias]

class CurryCallable(Protocol[_T_co]):
    def __call__(self, arg: Any, /) -> _T_co | CurryCallable[_T_co]: ...

class AutoCurryCallable(Protocol[_T_co]):
    def __call__(self, *args: Any, **kwds: Any) -> _T_co | AutoCurryCallable[_T_co]: ...

def curry(func: Callable[..., _T], n: int = ...) -> CurryCallable[_T]: ...
def rcurry(func: Callable[..., _T], n: int = ...) -> CurryCallable[_T]: ...
def autocurry(func: Callable[..., _T], n: int = ..., /) -> AutoCurryCallable[_T]: ...

Default = TypeAliasType("Default", Callable[[_T], _D] | _D, type_params=(_T, _D))

@overload
def iffy(
    action: Callable[[_B], _S],
    /,
) -> Callable[[_B], _S | _B]: ...
@overload
def iffy(
    action: Callable[[_B], _S],
    /,
    *,
    default: Default[_B, _D],
) -> Callable[[_B], _S | _D]: ...
@overload
def iffy(
    pred: Callable[[_T], _Boolean[_B]],
    action: Callable[[_T], _S],
    /,
) -> Callable[[_T], _S | _T]: ...
@overload
def iffy(
    pred: Callable[[_T], _Boolean[_B]],
    action: Callable[[_T], _S],
    default: Default[_T, _D],
) -> Callable[[_T], _S | _D]: ...
@overload
def iffy(
    pred: None,
    action: Callable[[_B], _S],
    /,
) -> Callable[[_B], _S | _B]: ...
@overload
def iffy(
    pred: None,
    action: Callable[[_B], _S],
    default: Default[_B, _D],
) -> Callable[[_B], _S | _D]: ...
@overload
def iffy(
    pred: _RegexType[AnyStr],
    action: Callable[[str], _S],
    /,
) -> Callable[[str], _S | str]: ...
@overload
def iffy(
    pred: _RegexType[AnyStr],
    action: Callable[[str], _S],
    default: Default[str, _D],
) -> Callable[[str], _S | _D]: ...
@overload
def iffy(
    pred: int,
    action: Callable[[Sequence[_B]], _B],
    /,
) -> Callable[[Sequence[_B]], _B]: ...
@overload
def iffy(
    pred: int,
    action: Callable[[Sequence[_B]], _B],
    default: Default[Sequence[_B], _D],
) -> Callable[[Sequence[_B]], _B | _D]: ...
@overload
def iffy(
    pred: Mapping[_KT, _VT],
    action: Callable[[_KT], _S],
    /,
) -> Callable[[_KT], _S | _KT]: ...
@overload
def iffy(
    pred: Mapping[_KT, _VT],
    action: Callable[[_KT], _S],
    default: Default[_KT, _D],
) -> Callable[[_KT], _S | _D]: ...
@overload
def iffy(
    pred: set[_H],
    action: Callable[[_H], _S],
    /,
) -> Callable[[_H], _S | _H]: ...
@overload
def iffy(
    pred: set[_H],
    action: Callable[[_H], _S],
    default: Default[_H, _D],
) -> Callable[[_H], _S | _D]: ...
@overload
def compose() -> Callable[[_T], _T]: ...
@overload
def compose(fn1: Callable[_P, _T], /) -> Callable[_P, _T]: ...
@overload
def compose(
    fn1: Callable[[_T1], _S], fn2: Callable[_P, _T1], /
) -> Callable[_P, _S]: ...
@overload
def compose(
    fn1: Callable[[_T1], _S],
    fn2: Callable[[_T2], _T1],
    fn3: Callable[_P, _T2],
    /,
) -> Callable[_P, _S]: ...
@overload
def compose(
    fn1: Callable[[_T1], _S],
    fn2: Callable[[_T2], _T1],
    fn3: Callable[[_T3], _T2],
    fn4: Callable[_P, _T3],
    /,
) -> Callable[_P, _S]: ...
@overload
def compose(
    fn1: Callable[[_T1], _S],
    fn2: Callable[[_T2], _T1],
    fn3: Callable[[_T3], _T2],
    fn4: Callable[[_T4], _T3],
    fn5: Callable[_P, _T4],
    /,
) -> Callable[_P, _S]: ...
@overload
def compose(
    fn1: Callable[[_T1], _S],
    fn2: Callable[[_T2], _T1],
    fn3: Callable[[_T3], _T2],
    fn4: Callable[[_T4], _T3],
    fn5: Callable[[_T5], _T4],
    fn6: Callable[_P, _T5],
    /,
) -> Callable[_P, _S]: ...
@overload
def compose(*fs: Callable[[_T], _T]) -> Callable[[_T], _T]: ...
@overload
def compose(*fs: Callable[..., Any]) -> Callable[..., Any]: ...
@overload
def rcompose() -> Callable[[_T], _T]: ...
@overload
def rcompose(fn1: Callable[_P, _T], /) -> Callable[_P, _T]: ...
@overload
def rcompose(
    fn1: Callable[_P, _T1], fn2: Callable[[_T1], _S], /
) -> Callable[_P, _S]: ...
@overload
def rcompose(
    fn1: Callable[_P, _T1],
    fn2: Callable[[_T1], _T2],
    fn3: Callable[[_T2], _S],
    /,
) -> Callable[_P, _S]: ...
@overload
def rcompose(
    fn1: Callable[_P, _T1],
    fn2: Callable[[_T1], _T2],
    fn3: Callable[[_T2], _T3],
    fn4: Callable[[_T3], _S],
    /,
) -> Callable[_P, _S]: ...
@overload
def rcompose(
    fn1: Callable[_P, _T1],
    fn2: Callable[[_T1], _T2],
    fn3: Callable[[_T2], _T3],
    fn4: Callable[[_T3], _T4],
    fn5: Callable[[_T4], _S],
    /,
) -> Callable[_P, _S]: ...
@overload
def rcompose(
    fn1: Callable[_P, _T1],
    fn2: Callable[[_T1], _T2],
    fn3: Callable[[_T2], _T3],
    fn4: Callable[[_T3], _T4],
    fn5: Callable[[_T4], _T5],
    fn6: Callable[[_T5], _S],
    /,
) -> Callable[_P, _S]: ...
@overload
def rcompose(fn: Callable[_P, _T], /, *fs: Callable[[_T], _T]) -> Callable[_P, _T]: ...
@overload
def rcompose(*fs: Callable[..., Any]) -> Callable[..., Any]: ...
@overload
def complement(pred: Callable[_P, _Boolean[_B]]) -> Callable[_P, bool]: ...
@overload
def complement(pred: None) -> Callable[[_Boolean[_B]], bool]: ...
@overload
def ljuxt(*fs: Callable[_P, _T]) -> Callable[_P, list[_T]]: ...
@overload
def ljuxt(*fs: None) -> Callable[[_T], list[_T]]: ...
@overload
def ljuxt(
    *fs: _RegexType[AnyStr],
) -> Callable[[str], list[_MatchType[AnyStr] | None]]: ...
@overload
def ljuxt(*fs: int) -> Callable[[Sequence[_T]], list[_T]]: ...
@overload
def ljuxt(*fs: slice) -> Callable[[Sequence[_T]], list[Sequence[_T]]]: ...
@overload
def ljuxt(*fs: Mapping[_KT, _VT]) -> Callable[[_KT], list[_VT]]: ...
@overload
def ljuxt(*fs: set[_H]) -> Callable[[_H], list[bool]]: ...
@overload
def juxt(*fs: Callable[_P, _T]) -> Callable[_P, Iterable[_T]]: ...
@overload
def juxt(*fs: None) -> Callable[[_T], Iterable[_T]]: ...
@overload
def juxt(
    *fs: _RegexType[AnyStr],
) -> Callable[[str], Iterable[_MatchType[AnyStr] | None]]: ...
@overload
def juxt(*fs: int) -> Callable[[Sequence[_T]], Iterable[_T]]: ...
@overload
def juxt(*fs: slice) -> Callable[[Sequence[_T]], Iterable[Sequence[_T]]]: ...
@overload
def juxt(*fs: Mapping[_KT, _VT]) -> Callable[[_KT], Iterable[_VT]]: ...
@overload
def juxt(*fs: set[_H]) -> Callable[[_H], Iterable[bool]]: ...

__all__ = (
    "autocurry",
    "caller",
    "complement",
    "compose",
    "constantly",
    "curry",
    "func_partial",
    "identity",
    "iffy",
    "juxt",
    "ljuxt",
    "partial",
    "rcompose",
    "rcurry",
    "rpartial",
)
