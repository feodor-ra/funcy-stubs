from collections.abc import Iterator, Mapping, Sequence
from functools import partial, reduce
from typing import Any, AnyStr, Callable, Protocol, overload

from typing_extensions import TypeAlias, TypeAliasType

from ._types import (
    KT,
    T1,
    T2,
    T3,
    T4,
    T5,
    VT,
    B,
    Boolean,
    D,
    H,
    MatchType,
    P,
    RegexType,
    S,
    T,
    T_co,
)

def identity(x: T) -> T: ...
def constantly(x: T) -> Callable[..., T]: ...
def caller(
    *args: P.args,  # type: ignore[reportGeneralTypeIssues]
    **kwargs: P.kwargs,
) -> Callable[[Callable[P, T]], T]: ...

func_partial: TypeAlias = partial[Any]  # noqa: PYI042

rpartial: TypeAlias = partial[Any]  # noqa: PYI042

class CurryCallable(Protocol[T_co]):
    def __call__(self, arg: Any, /) -> T_co | CurryCallable[T_co]: ...

class AutoCurryCallable(Protocol[T_co]):
    def __call__(self, *args: Any, **kwds: Any) -> T_co | AutoCurryCallable[T_co]: ...

def curry(func: Callable[..., T], n: int = ...) -> CurryCallable[T]: ...
def rcurry(func: Callable[..., T], n: int = ...) -> CurryCallable[T]: ...
def autocurry(func: Callable[..., T], n: int = ..., /) -> AutoCurryCallable[T]: ...

Default = TypeAliasType("Default", Callable[[T], D] | D, type_params=(T, D))

@overload
def iffy(
    action: Callable[[B], S],
    /,
) -> Callable[[B], S | B]: ...
@overload
def iffy(
    action: Callable[[B], S],
    /,
    *,
    default: Default[B, D],
) -> Callable[[B], S | D]: ...
@overload
def iffy(
    pred: Callable[[T], Boolean[B]],
    action: Callable[[T], S],
    /,
) -> Callable[[T], S | T]: ...
@overload
def iffy(
    pred: Callable[[T], Boolean[B]],
    action: Callable[[T], S],
    default: Default[T, D],
) -> Callable[[T], S | D]: ...
@overload
def iffy(
    pred: None,
    action: Callable[[B], S],
    /,
) -> Callable[[B], S | B]: ...
@overload
def iffy(
    pred: None,
    action: Callable[[B], S],
    default: Default[B, D],
) -> Callable[[B], S | D]: ...
@overload
def iffy(
    pred: RegexType[AnyStr],
    action: Callable[[str], S],
    /,
) -> Callable[[str], S | str]: ...
@overload
def iffy(
    pred: RegexType[AnyStr],
    action: Callable[[str], S],
    default: Default[str, D],
) -> Callable[[str], S | D]: ...
@overload
def iffy(
    pred: int,
    action: Callable[[Sequence[B]], B],
    /,
) -> Callable[[Sequence[B]], B]: ...
@overload
def iffy(
    pred: int,
    action: Callable[[Sequence[B]], B],
    default: Default[Sequence[B], D],
) -> Callable[[Sequence[B]], B | D]: ...
@overload
def iffy(
    pred: Mapping[KT, VT],
    action: Callable[[KT], S],
    /,
) -> Callable[[KT], S | KT]: ...
@overload
def iffy(
    pred: Mapping[KT, VT],
    action: Callable[[KT], S],
    default: Default[KT, D],
) -> Callable[[KT], S | D]: ...
@overload
def iffy(
    pred: set[H],
    action: Callable[[H], S],
    /,
) -> Callable[[H], S | H]: ...
@overload
def iffy(
    pred: set[H],
    action: Callable[[H], S],
    default: Default[H, D],
) -> Callable[[H], S | D]: ...
@overload
def compose() -> Callable[[T], T]: ...
@overload
def compose(fn1: Callable[P, T], /) -> Callable[P, T]: ...
@overload
def compose(fn1: Callable[[T1], S], fn2: Callable[P, T1], /) -> Callable[P, S]: ...
@overload
def compose(
    fn1: Callable[[T1], S],
    fn2: Callable[[T2], T1],
    fn3: Callable[P, T2],
    /,
) -> Callable[P, S]: ...
@overload
def compose(
    fn1: Callable[[T1], S],
    fn2: Callable[[T2], T1],
    fn3: Callable[[T3], T2],
    fn4: Callable[P, T3],
    /,
) -> Callable[P, S]: ...
@overload
def compose(
    fn1: Callable[[T1], S],
    fn2: Callable[[T2], T1],
    fn3: Callable[[T3], T2],
    fn4: Callable[[T4], T3],
    fn5: Callable[P, T4],
    /,
) -> Callable[P, S]: ...
@overload
def compose(
    fn1: Callable[[T1], S],
    fn2: Callable[[T2], T1],
    fn3: Callable[[T3], T2],
    fn4: Callable[[T4], T3],
    fn5: Callable[[T5], T4],
    fn6: Callable[P, T5],
    /,
) -> Callable[P, S]: ...
@overload
def compose(*fs: Callable[[T], T], fn: Callable[P, T]) -> Callable[P, T]: ...
@overload
def rcompose() -> Callable[[T], T]: ...
@overload
def rcompose(fn1: Callable[P, T], /) -> Callable[P, T]: ...
@overload
def rcompose(fn1: Callable[P, T1], fn2: Callable[[T1], S], /) -> Callable[P, S]: ...
@overload
def rcompose(
    fn1: Callable[P, T1],
    fn2: Callable[[T1], T2],
    fn3: Callable[[T2], S],
    /,
) -> Callable[P, S]: ...
@overload
def rcompose(
    fn1: Callable[P, T1],
    fn2: Callable[[T1], T2],
    fn3: Callable[[T2], T3],
    fn4: Callable[[T3], S],
    /,
) -> Callable[P, S]: ...
@overload
def rcompose(
    fn1: Callable[P, T1],
    fn2: Callable[[T1], T2],
    fn3: Callable[[T2], T3],
    fn4: Callable[[T3], T4],
    fn5: Callable[[T4], S],
    /,
) -> Callable[P, S]: ...
@overload
def rcompose(
    fn1: Callable[P, T1],
    fn2: Callable[[T1], T2],
    fn3: Callable[[T2], T3],
    fn4: Callable[[T3], T4],
    fn5: Callable[[T4], T5],
    fn6: Callable[[T5], S],
    /,
) -> Callable[P, S]: ...
@overload
def rcompose(fn: Callable[P, T], /, *fs: Callable[[T], T]) -> Callable[P, T]: ...
@overload
def complement(pred: Callable[P, Boolean[B]]) -> Callable[P, bool]: ...
@overload
def complement(pred: None) -> Callable[[Boolean[B]], bool]: ...
@overload
def ljuxt(*fs: Callable[P, T]) -> Callable[P, list[T]]: ...
@overload
def ljuxt(*fs: None) -> Callable[[T], list[T]]: ...
@overload
def ljuxt(
    *fs: RegexType[AnyStr],
) -> Callable[[str], list[MatchType[AnyStr] | None]]: ...
@overload
def ljuxt(*fs: int) -> Callable[[Sequence[T]], list[T]]: ...
@overload
def ljuxt(*fs: slice) -> Callable[[Sequence[T]], list[Sequence[T]]]: ...
@overload
def ljuxt(*fs: Mapping[KT, VT]) -> Callable[[KT], list[VT]]: ...
@overload
def ljuxt(*fs: set[H]) -> Callable[[H], list[bool]]: ...
@overload
def juxt(*fs: Callable[P, T]) -> Callable[P, Iterator[T]]: ...
@overload
def juxt(*fs: None) -> Callable[[T], Iterator[T]]: ...
@overload
def juxt(
    *fs: RegexType[AnyStr],
) -> Callable[[str], Iterator[MatchType[AnyStr] | None]]: ...
@overload
def juxt(*fs: int) -> Callable[[Sequence[T]], Iterator[T]]: ...
@overload
def juxt(*fs: slice) -> Callable[[Sequence[T]], Iterator[Sequence[T]]]: ...
@overload
def juxt(*fs: Mapping[KT, VT]) -> Callable[[KT], Iterator[VT]]: ...
@overload
def juxt(*fs: set[H]) -> Callable[[H], Iterator[bool]]: ...

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
    "reduce",
    "rpartial",
)
