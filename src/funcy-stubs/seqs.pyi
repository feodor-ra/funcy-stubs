from abc import abstractmethod
from collections import defaultdict
from collections.abc import Iterable, Mapping, Sequence
from itertools import accumulate, chain, count, cycle, repeat
from re import Pattern
from typing import Any, AnyStr, Callable, Hashable, Protocol, TypeVar, overload

from typing_extensions import TypeAliasType

_T = TypeVar("_T")
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
_T4 = TypeVar("_T4")
_T5 = TypeVar("_T5")
_S = TypeVar("_S")
_KT = TypeVar("_KT", bound=Hashable)
_VT = TypeVar("_VT")
_H = TypeVar("_H", bound=Hashable)
_T_contra = TypeVar("_T_contra", contravariant=True)

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

class SupportsAdd(Protocol[_T_contra]):
    @abstractmethod
    def __add__(self, value: _T_contra, /) -> SupportsAdd[_T_contra]: ...

@overload
def repeatedly(f: Callable[[], _T], /) -> Iterable[_T]: ...
@overload
def repeatedly(f: Callable[[], _T], n: int) -> Iterable[_T]: ...
def iterate(f: Callable[[_T], _T], x: _T) -> Iterable[_T]: ...
def take(n: int, seq: Iterable[_T]) -> list[_T]: ...
def drop(n: int, seq: Iterable[_T]) -> Iterable[_T]: ...
def first(seq: Iterable[_T]) -> _T | None: ...
def second(seq: Iterable[_T]) -> _T | None: ...
def nth(n: int, seq: Iterable[_T]) -> _T | None: ...
def last(seq: Iterable[_T]) -> _T | None: ...
def rest(seq: Iterable[_T]) -> Iterable[_T]: ...
def butlast(seq: Iterable[_T]) -> Iterable[_T]: ...
def ilen(seq: Iterable[Any]) -> int: ...
@overload
def lmap(
    f: Callable[[_T1], _S],
    iter1: Iterable[_T1],
    /,
) -> list[_S]: ...
@overload
def lmap(
    f: Callable[[_T1, _T2], _S],
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    /,
) -> list[_S]: ...
@overload
def lmap(
    f: Callable[[_T1, _T2, _T3], _S],
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    iter3: Iterable[_T3],
    /,
) -> list[_S]: ...
@overload
def lmap(
    f: Callable[[_T1, _T2, _T3, _T4], _S],
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    iter3: Iterable[_T3],
    iter4: Iterable[_T4],
    /,
) -> list[_S]: ...
@overload
def lmap(
    f: Callable[[_T1, _T2, _T3, _T4, _T5], _S],
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    iter3: Iterable[_T3],
    iter4: Iterable[_T4],
    iter5: Iterable[_T5],
    /,
) -> list[_S]: ...
@overload
def lmap(
    f: Callable[..., _S],
    iter1: Iterable[Any],
    iter2: Iterable[Any],
    iter3: Iterable[Any],
    iter4: Iterable[Any],
    iter5: Iterable[Any],
    iter6: Iterable[Any],
    /,
    *iterables: Iterable[Any],
) -> list[_S]: ...
@overload
def lmap(f: None, iter1: Iterable[_T1], /) -> list[_T1]: ...
@overload
def lmap(
    f: _RegexType[AnyStr],
    iter1: Iterable[str],
    /,
) -> list[_MatchType[AnyStr] | None]: ...
@overload
def lmap(f: int, iter1: Iterable[Sequence[_T1]], /) -> list[_T1]: ...
@overload
def lmap(f: slice, iter1: Iterable[Sequence[_T1]], /) -> list[Sequence[_T1]]: ...
@overload
def lmap(f: Mapping[_KT, _VT], iter1: Iterable[_KT], /) -> list[_VT]: ...
@overload
def lmap(f: set[_H], iter1: Iterable[_H], /) -> list[bool]: ...
@overload
def map(f: Callable[[_T1], _S], iter1: Iterable[_T1], /) -> Iterable[_S]: ...
@overload
def map(
    f: Callable[[_T1, _T2], _S],
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    /,
) -> Iterable[_S]: ...
@overload
def map(
    f: Callable[[_T1, _T2, _T3], _S],
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    iter3: Iterable[_T3],
    /,
) -> Iterable[_S]: ...
@overload
def map(
    f: Callable[[_T1, _T2, _T3, _T4], _S],
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    iter3: Iterable[_T3],
    iter4: Iterable[_T4],
    /,
) -> Iterable[_S]: ...
@overload
def map(
    f: Callable[[_T1, _T2, _T3, _T4, _T5], _S],
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    iter3: Iterable[_T3],
    iter4: Iterable[_T4],
    iter5: Iterable[_T5],
    /,
) -> Iterable[_S]: ...
@overload
def map(
    f: Callable[..., _S],
    iter1: Iterable[Any],
    iter2: Iterable[Any],
    iter3: Iterable[Any],
    iter4: Iterable[Any],
    iter5: Iterable[Any],
    iter6: Iterable[Any],
    /,
    *iterables: Iterable[Any],
) -> Iterable[_S]: ...
@overload
def map(f: None, iter1: Iterable[_T1], /) -> Iterable[_T1]: ...
@overload
def map(
    f: _RegexType[AnyStr],
    iter1: Iterable[str],
    /,
) -> Iterable[_MatchType[AnyStr] | None]: ...
@overload
def map(f: int, iter1: Iterable[Sequence[_T1]], /) -> Iterable[_T1]: ...
@overload
def map(f: slice, iter1: Iterable[Sequence[_T1]], /) -> Iterable[Sequence[_T1]]: ...
@overload
def map(f: Mapping[_KT, _VT], iter1: Iterable[_KT], /) -> Iterable[_VT]: ...
@overload
def map(f: set[_H], iter1: Iterable[_H], /) -> Iterable[bool]: ...
@overload
def lfilter(pred: Callable[[_T], _Boolean[_B]], seq: Iterable[_T]) -> list[_T]: ...
@overload
def lfilter(pred: None, seq: Iterable[_T]) -> list[_T]: ...
@overload
def lfilter(pred: _RegexType[AnyStr], seq: Iterable[str]) -> list[str]: ...
@overload
def lfilter(pred: int, seq: Iterable[Sequence[_T]]) -> list[Sequence[_T]]: ...
@overload
def lfilter(pred: slice, seq: Iterable[Sequence[_T]]) -> list[Sequence[_T]]: ...
@overload
def lfilter(pred: Mapping[_KT, _VT], seq: Iterable[_KT]) -> list[_KT]: ...
@overload
def lfilter(pred: set[_H], seq: Iterable[_H]) -> list[_H]: ...
@overload
def filter(pred: Callable[[_T], _Boolean[_B]], seq: Iterable[_T]) -> Iterable[_T]: ...
@overload
def filter(pred: None, seq: Iterable[_T]) -> Iterable[_T]: ...
@overload
def filter(pred: _RegexType[AnyStr], seq: Iterable[str]) -> Iterable[str]: ...
@overload
def filter(pred: int, seq: Iterable[Sequence[_T]]) -> Iterable[Sequence[_T]]: ...
@overload
def filter(pred: slice, seq: Iterable[Sequence[_T]]) -> Iterable[Sequence[_T]]: ...
@overload
def filter(pred: Mapping[_KT, _VT], seq: Iterable[_KT]) -> Iterable[_KT]: ...
@overload
def filter(pred: set[_H], seq: Iterable[_H]) -> Iterable[_H]: ...
@overload
def lremove(pred: Callable[[_T], _Boolean[_B]], seq: Iterable[_T]) -> list[_T]: ...
@overload
def lremove(pred: None, seq: Iterable[_T]) -> list[_T]: ...
@overload
def lremove(pred: _RegexType[AnyStr], seq: Iterable[str]) -> list[str]: ...
@overload
def lremove(pred: int, seq: Iterable[Sequence[_T]]) -> list[Sequence[_T]]: ...
@overload
def lremove(pred: slice, seq: Iterable[Sequence[_T]]) -> list[Sequence[_T]]: ...
@overload
def lremove(pred: Mapping[_KT, _VT], seq: Iterable[_KT]) -> list[_KT]: ...
@overload
def lremove(pred: set[_H], seq: Iterable[_H]) -> list[_H]: ...
@overload
def remove(pred: Callable[[_T], _Boolean[_B]], seq: Iterable[_T]) -> Iterable[_T]: ...
@overload
def remove(pred: None, seq: Iterable[_T]) -> Iterable[_T]: ...
@overload
def remove(pred: _RegexType[AnyStr], seq: Iterable[str]) -> Iterable[str]: ...
@overload
def remove(pred: int, seq: Iterable[Sequence[_T]]) -> Iterable[Sequence[_T]]: ...
@overload
def remove(pred: slice, seq: Iterable[Sequence[_T]]) -> Iterable[Sequence[_T]]: ...
@overload
def remove(pred: Mapping[_KT, _VT], seq: Iterable[_KT]) -> Iterable[_KT]: ...
@overload
def remove(pred: set[_H], seq: Iterable[_H]) -> Iterable[_H]: ...
@overload
def lkeep(f: Iterable[_T]) -> list[_T]: ...
@overload
def lkeep(f: Callable[[_T], _Boolean[_B]], seq: Iterable[_T]) -> list[_T]: ...
@overload
def lkeep(f: None, seq: Iterable[_T]) -> list[_T]: ...
@overload
def lkeep(
    f: _RegexType[AnyStr],
    seq: Iterable[str],
) -> list[_MatchType[AnyStr] | None]: ...
@overload
def lkeep(f: int, seq: Iterable[Sequence[_T]]) -> list[_T]: ...
@overload
def lkeep(f: slice, seq: Iterable[Sequence[_T]]) -> list[Sequence[_T]]: ...
@overload
def lkeep(f: Mapping[_KT, _VT], seq: Iterable[_KT]) -> list[_VT]: ...
@overload
def lkeep(f: set[_H], seq: Iterable[_H]) -> list[bool]: ...
@overload
def keep(f: Iterable[_T]) -> Iterable[_T]: ...
@overload
def keep(f: Callable[[_T], _Boolean[_B]], seq: Iterable[_T]) -> Iterable[_T]: ...
@overload
def keep(f: None, seq: Iterable[_T]) -> Iterable[_T]: ...
@overload
def keep(
    f: _RegexType[AnyStr],
    seq: Iterable[str],
) -> Iterable[_MatchType[AnyStr] | None]: ...
@overload
def keep(f: int, seq: Iterable[Sequence[_T]]) -> Iterable[_T]: ...
@overload
def keep(f: slice, seq: Iterable[Sequence[_T]]) -> Iterable[Sequence[_T]]: ...
@overload
def keep(f: Mapping[_KT, _VT], seq: Iterable[_KT]) -> Iterable[_VT]: ...
@overload
def keep(f: set[_H], seq: Iterable[_H]) -> Iterable[bool]: ...
def without(seq: Iterable[_T], *items: _T) -> Iterable[_T]: ...
def lwithout(seq: Iterable[_T], *items: _T) -> list[_T]: ...
def lconcat(*seqs: Iterable[_T]) -> list[_T]: ...
def concat(*seqs: Iterable[_T]) -> Iterable[_T]: ...
def lcat(seqs: Iterable[Iterable[_T]]) -> list[_T]: ...
def cat(seqs: Iterable[Iterable[_T]]) -> Iterable[_T]: ...
def flatten(
    seq: Iterable[_T],
    follow: Callable[[_T], _Boolean[_B]] = ...,
) -> Iterable[_T]: ...
def lflatten(
    seq: Iterable[_T], follow: Callable[[_T], _Boolean[_B]] = ...
) -> list[_T]: ...
@overload
def lmapcat(
    f: Callable[[_T1], Iterable[_S]],
    iter1: Iterable[_T1],
    /,
) -> list[_S]: ...
@overload
def lmapcat(
    f: Callable[[_T1, _T2], Iterable[_S]],
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    /,
) -> list[_S]: ...
@overload
def lmapcat(
    f: Callable[[_T1, _T2, _T3], Iterable[_S]],
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    iter3: Iterable[_T3],
    /,
) -> list[_S]: ...
@overload
def lmapcat(
    f: Callable[[_T1, _T2, _T3, _T4], Iterable[_S]],
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    iter3: Iterable[_T3],
    iter4: Iterable[_T4],
    /,
) -> list[_S]: ...
@overload
def lmapcat(
    f: Callable[[_T1, _T2, _T3, _T4, _T5], Iterable[_S]],
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    iter3: Iterable[_T3],
    iter4: Iterable[_T4],
    iter5: Iterable[_T5],
    /,
) -> list[_S]: ...
@overload
def lmapcat(
    f: Callable[..., Iterable[_S]],
    iter1: Iterable[Any],
    iter2: Iterable[Any],
    iter3: Iterable[Any],
    iter4: Iterable[Any],
    iter5: Iterable[Any],
    iter6: Iterable[Any],
    /,
    *iterables: Iterable[Any],
) -> list[_S]: ...
@overload
def lmapcat(f: None, iter1: Iterable[Iterable[_T1]], /) -> list[_T1]: ...
@overload
def lmapcat(
    f: _RegexType[AnyStr],
    iter1: Iterable[str],
    /,
) -> list[_MatchType[AnyStr] | None]: ...
@overload
def lmapcat(f: int, iter1: Iterable[Sequence[_T1]], /) -> list[_T1]: ...
@overload
def lmapcat(f: slice, iter1: Iterable[Sequence[_T1]], /) -> list[_T1]: ...
@overload
def lmapcat(f: Mapping[_KT, _VT], iter1: Iterable[_KT], /) -> list[_VT]: ...
@overload
def lmapcat(f: set[_H], iter1: Iterable[_H], /) -> list[bool]: ...
@overload
def mapcat(
    f: Callable[[_T1], Iterable[_S]],
    iter1: Iterable[_T1],
    /,
) -> Iterable[_S]: ...
@overload
def mapcat(
    f: Callable[[_T1, _T2], Iterable[_S]],
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    /,
) -> Iterable[_S]: ...
@overload
def mapcat(
    f: Callable[[_T1, _T2, _T3], Iterable[_S]],
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    iter3: Iterable[_T3],
    /,
) -> Iterable[_S]: ...
@overload
def mapcat(
    f: Callable[[_T1, _T2, _T3, _T4], Iterable[_S]],
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    iter3: Iterable[_T3],
    iter4: Iterable[_T4],
    /,
) -> Iterable[_S]: ...
@overload
def mapcat(
    f: Callable[[_T1, _T2, _T3, _T4, _T5], Iterable[_S]],
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    iter3: Iterable[_T3],
    iter4: Iterable[_T4],
    iter5: Iterable[_T5],
    /,
) -> Iterable[_S]: ...
@overload
def mapcat(
    f: Callable[..., Iterable[_S]],
    iter1: Iterable[Any],
    iter2: Iterable[Any],
    iter3: Iterable[Any],
    iter4: Iterable[Any],
    iter5: Iterable[Any],
    iter6: Iterable[Any],
    /,
    *iterables: Iterable[Any],
) -> Iterable[_S]: ...
@overload
def mapcat(f: None, iter1: Iterable[Iterable[_T1]], /) -> Iterable[_T1]: ...
@overload
def mapcat(
    f: _RegexType[AnyStr],
    iter1: Iterable[str],
    /,
) -> Iterable[_MatchType[AnyStr] | None]: ...
@overload
def mapcat(f: int, iter1: Iterable[Sequence[_T1]], /) -> Iterable[_T1]: ...
@overload
def mapcat(f: slice, iter1: Iterable[Sequence[_T1]], /) -> Iterable[_T1]: ...
@overload
def mapcat(f: Mapping[_KT, _VT], iter1: Iterable[_KT], /) -> Iterable[_VT]: ...
@overload
def mapcat(f: set[_H], iter1: Iterable[_H], /) -> Iterable[bool]: ...
@overload
def interleave(
    iter1: Iterable[_T1],
    /,
) -> Iterable[_T1]: ...
@overload
def interleave(
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    /,
) -> Iterable[_T1 | _T2]: ...
@overload
def interleave(
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    iter3: Iterable[_T3],
    /,
) -> Iterable[_T1 | _T2 | _T3]: ...
@overload
def interleave(
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    iter3: Iterable[_T3],
    iter4: Iterable[_T4],
    /,
) -> Iterable[_T1 | _T2 | _T3 | _T4]: ...
@overload
def interleave(
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    iter3: Iterable[_T3],
    iter4: Iterable[_T4],
    iter5: Iterable[_T5],
    /,
    *iterables: Iterable[_T],
) -> Iterable[_T1 | _T2 | _T3 | _T4 | _T5 | _T]: ...
def interpose(sep: _T1, seq: Iterable[_T2]) -> Iterable[_T1 | _T2]: ...
@overload
def takewhile(seq: Iterable[_T], /) -> Iterable[_T]: ...
@overload
def takewhile(
    pred: Callable[[_T], _Boolean[_B]], seq: Iterable[_T]
) -> Iterable[_T]: ...
@overload
def takewhile(pred: None, seq: Iterable[_T]) -> Iterable[_T]: ...
@overload
def takewhile(pred: _RegexType[AnyStr], seq: Iterable[str]) -> Iterable[str]: ...
@overload
def takewhile(pred: int, seq: Iterable[Sequence[_T]]) -> Iterable[Sequence[_T]]: ...
@overload
def takewhile(pred: slice, seq: Iterable[Sequence[_T]]) -> Iterable[Sequence[_T]]: ...
@overload
def takewhile(pred: Mapping[_KT, _VT], seq: Iterable[_KT]) -> Iterable[_KT]: ...
@overload
def takewhile(pred: set[_H], seq: Iterable[_H]) -> Iterable[_H]: ...
@overload
def dropwhile(seq: Iterable[_T], /) -> Iterable[_T]: ...
@overload
def dropwhile(
    pred: Callable[[_T], _Boolean[_B]], seq: Iterable[_T]
) -> Iterable[_T]: ...
@overload
def dropwhile(pred: None, seq: Iterable[_T]) -> Iterable[_T]: ...
@overload
def dropwhile(pred: _RegexType[AnyStr], seq: Iterable[str]) -> Iterable[str]: ...
@overload
def dropwhile(pred: int, seq: Iterable[Sequence[_T]]) -> Iterable[Sequence[_T]]: ...
@overload
def dropwhile(pred: slice, seq: Iterable[Sequence[_T]]) -> Iterable[Sequence[_T]]: ...
@overload
def dropwhile(pred: Mapping[_KT, _VT], seq: Iterable[_KT]) -> Iterable[_KT]: ...
@overload
def dropwhile(pred: set[_H], seq: Iterable[_H]) -> Iterable[_H]: ...
@overload
def ldistinct(seq: Iterable[_H], /) -> list[_H]: ...
@overload
def ldistinct(seq: Iterable[_T], key: Callable[[_T], _H]) -> list[_T]: ...
@overload
def ldistinct(seq: Iterable[_T], key: None) -> list[_T]: ...
@overload
def ldistinct(seq: Iterable[str], key: _RegexType[AnyStr]) -> list[str]: ...
@overload
def ldistinct(seq: Iterable[Sequence[_KT]], key: int) -> list[_KT]: ...
@overload
def ldistinct(seq: Iterable[tuple[_KT, ...]], key: slice) -> list[tuple[_KT, ...]]: ...
@overload
def ldistinct(seq: Iterable[_KT], key: Mapping[_KT, _H]) -> list[_KT]: ...
@overload
def ldistinct(seq: Iterable[_H], key: set[_H]) -> list[_H]: ...
@overload
def distinct(seq: Iterable[_H], /) -> Iterable[_H]: ...
@overload
def distinct(seq: Iterable[_T], key: Callable[[_T], _H]) -> Iterable[_T]: ...
@overload
def distinct(seq: Iterable[_T], key: None) -> Iterable[_T]: ...
@overload
def distinct(seq: Iterable[str], key: _RegexType[AnyStr]) -> Iterable[str]: ...
@overload
def distinct(seq: Iterable[Sequence[_KT]], key: int) -> Iterable[_KT]: ...
@overload
def distinct(
    seq: Iterable[tuple[_KT, ...]], key: slice
) -> Iterable[tuple[_KT, ...]]: ...
@overload
def distinct(seq: Iterable[_KT], key: Mapping[_KT, _H]) -> Iterable[_KT]: ...
@overload
def distinct(seq: Iterable[_H], key: set[_H]) -> Iterable[_H]: ...
@overload
def split(
    pred: Callable[[_T], bool],
    seq: Iterable[_T],
) -> tuple[Iterable[_T], Iterable[_T]]: ...
@overload
def split(pred: None, seq: Iterable[_T]) -> tuple[Iterable[_T], Iterable[_T]]: ...
@overload
def split(
    pred: _RegexType[AnyStr],
    seq: Iterable[str],
) -> tuple[Iterable[str], Iterable[str]]: ...
@overload
def split(
    pred: int, seq: Iterable[Sequence[_T]]
) -> tuple[Iterable[_T], Iterable[_T]]: ...
@overload
def split(
    pred: slice,
    seq: Iterable[Sequence[_T]],
) -> tuple[Iterable[Sequence[_T]], Iterable[Sequence[_T]]]: ...
@overload
def split(
    pred: Mapping[_KT, bool],
    seq: Iterable[_KT],
) -> tuple[Iterable[_KT], Iterable[_KT]]: ...
@overload
def split(pred: set[_H], seq: Iterable[_H]) -> tuple[Iterable[_H], Iterable[_H]]: ...
@overload
def lsplit(
    pred: Callable[[_T], bool], seq: Iterable[_T]
) -> tuple[list[_T], list[_T]]: ...
@overload
def lsplit(pred: None, seq: Iterable[_T]) -> tuple[list[_T], list[_T]]: ...
@overload
def lsplit(
    pred: _RegexType[AnyStr],
    seq: Iterable[str],
) -> tuple[list[str], list[str]]: ...
@overload
def lsplit(pred: int, seq: Iterable[Sequence[_T]]) -> tuple[list[_T], list[_T]]: ...
@overload
def lsplit(
    pred: slice,
    seq: Iterable[Sequence[_T]],
) -> tuple[list[Sequence[_T]], list[Sequence[_T]]]: ...
@overload
def lsplit(
    pred: Mapping[_KT, bool], seq: Iterable[_KT]
) -> tuple[list[_KT], list[_KT]]: ...
@overload
def lsplit(pred: set[_H], seq: Iterable[_H]) -> tuple[list[_H], list[_H]]: ...
def split_at(n: int, seq: Iterable[_T]) -> tuple[Iterable[_T], Iterable[_T]]: ...
def lsplit_at(n: int, seq: Iterable[_T]) -> tuple[list[_T], list[_T]]: ...
@overload
def split_by(
    pred: Callable[[_T], bool],
    seq: Iterable[_T],
) -> tuple[Iterable[_T], Iterable[_T]]: ...
@overload
def split_by(pred: None, seq: Iterable[_T]) -> tuple[Iterable[_T], Iterable[_T]]: ...
@overload
def split_by(
    pred: _RegexType[AnyStr],
    seq: Iterable[str],
) -> tuple[Iterable[str], Iterable[str]]: ...
@overload
def split_by(
    pred: int | slice,
    seq: Iterable[Sequence[_T]],
) -> tuple[Iterable[Sequence[_T]], Iterable[Sequence[_T]]]: ...
@overload
def split_by(
    pred: Mapping[_KT, _VT],
    seq: Iterable[_KT],
) -> tuple[Iterable[_KT], Iterable[_KT]]: ...
@overload
def split_by(pred: set[_H], seq: Iterable[_H]) -> tuple[Iterable[_H], Iterable[_H]]: ...
@overload
def lsplit_by(
    pred: Callable[[_T], bool],
    seq: Iterable[_T],
) -> tuple[list[_T], list[_T]]: ...
@overload
def lsplit_by(pred: None, seq: Iterable[_T]) -> tuple[list[_T], list[_T]]: ...
@overload
def lsplit_by(
    pred: _RegexType[AnyStr],
    seq: Iterable[str],
) -> tuple[list[str], list[str]]: ...
@overload
def lsplit_by(
    pred: int | slice,
    seq: Iterable[Sequence[_T]],
) -> tuple[list[Sequence[_T]], list[Sequence[_T]]]: ...
@overload
def lsplit_by(
    pred: Mapping[_KT, _VT],
    seq: Iterable[_KT],
) -> tuple[list[_KT], list[_KT]]: ...
@overload
def lsplit_by(pred: set[_H], seq: Iterable[_H]) -> tuple[list[_H], list[_H]]: ...
@overload
def group_by(
    f: Callable[[_T], _KT], seq: Iterable[_T]
) -> defaultdict[_KT, list[_T]]: ...
@overload
def group_by(f: None, seq: Iterable[_KT]) -> defaultdict[_KT, list[_KT]]: ...
@overload
def group_by(
    f: _RegexType[AnyStr],
    seq: Iterable[str],
) -> defaultdict[_MatchType[AnyStr] | None, list[str]]: ...
@overload
def group_by(
    f: int,
    seq: Iterable[Sequence[_KT]],
) -> defaultdict[_KT, list[Sequence[_KT]]]: ...
@overload
def group_by(
    f: slice,
    seq: Iterable[tuple[_H, ...]],
) -> defaultdict[tuple[_H, ...], list[tuple[_H, ...]]]: ...
@overload
def group_by(f: Mapping[_KT, _H], seq: Iterable[_KT]) -> defaultdict[_H, list[_KT]]: ...
@overload
def group_by(f: set[_H], seq: Iterable[_H]) -> defaultdict[bool, list[_H]]: ...
@overload
def group_by_keys(
    get_keys: Callable[[_T], Iterable[_KT]],
    seq: Iterable[_T],
) -> defaultdict[_KT, list[_T]]: ...
@overload
def group_by_keys(
    get_keys: None, seq: Iterable[_KT]
) -> defaultdict[_KT, list[_KT]]: ...
@overload
def group_by_keys(
    get_keys: int,
    seq: Iterable[Sequence[Iterable[_KT]]],
) -> defaultdict[_KT, list[Sequence[Iterable[_KT]]]]: ...
@overload
def group_by_keys(
    get_keys: slice,
    seq: Iterable[Sequence[_KT]],
) -> defaultdict[_KT, list[Sequence[_KT]]]: ...
@overload
def group_by_keys(
    get_keys: Mapping[_KT, Iterable[_H]],
    seq: Iterable[_KT],
) -> defaultdict[_H, list[_KT]]: ...
def group_values(seq: Iterable[tuple[_KT, _VT]]) -> defaultdict[_KT, list[_VT]]: ...
@overload
def count_by(f: Callable[[_T], _KT], seq: Iterable[_T]) -> defaultdict[_KT, int]: ...
@overload
def count_by(f: None, seq: Iterable[_KT]) -> defaultdict[_KT, int]: ...
@overload
def count_by(
    f: _RegexType[AnyStr],
    seq: Iterable[str],
) -> defaultdict[_MatchType[AnyStr] | None, int]: ...
@overload
def count_by(f: int, seq: Iterable[Sequence[_KT]]) -> defaultdict[_KT, int]: ...
@overload
def count_by(
    f: slice,
    seq: Iterable[tuple[_H, ...]],
) -> defaultdict[tuple[_H, ...], int]: ...
@overload
def count_by(f: Mapping[_KT, _H], seq: Iterable[_KT]) -> defaultdict[_H, int]: ...
@overload
def count_by(f: set[_H], seq: Iterable[_H]) -> defaultdict[bool, int]: ...
def count_reps(seq: Iterable[_KT]) -> defaultdict[_KT, int]: ...
@overload
def partition(n: int, seq: Iterable[_T], /) -> Iterable[list[_T]]: ...
@overload
def partition(n: int, step: int, seq: Iterable[_T]) -> Iterable[list[_T]]: ...
@overload
def lpartition(n: int, seq: Iterable[_T], /) -> list[list[_T]]: ...
@overload
def lpartition(n: int, step: int, seq: Iterable[_T]) -> list[list[_T]]: ...
@overload
def chunks(n: int, seq: Iterable[_T], /) -> Iterable[list[_T]]: ...
@overload
def chunks(n: int, step: int, seq: Iterable[_T]) -> Iterable[list[_T]]: ...
@overload
def lchunks(n: int, seq: Iterable[_T], /) -> list[list[_T]]: ...
@overload
def lchunks(n: int, step: int, seq: Iterable[_T]) -> list[list[_T]]: ...
@overload
def partition_by(f: Callable[[_T], _KT], seq: Iterable[_T]) -> Iterable[list[_T]]: ...
@overload
def partition_by(f: None, seq: Iterable[_KT]) -> Iterable[list[_KT]]: ...
@overload
def partition_by(f: _RegexType[AnyStr], seq: Iterable[str]) -> Iterable[list[str]]: ...
@overload
def partition_by(
    f: int,
    seq: Iterable[Sequence[_KT]],
) -> Iterable[list[Sequence[_KT]]]: ...
@overload
def partition_by(
    f: slice,
    seq: Iterable[tuple[_H, ...]],
) -> Iterable[list[tuple[_H, ...]]]: ...
@overload
def partition_by(f: Mapping[_KT, _H], seq: Iterable[_KT]) -> Iterable[list[_KT]]: ...
@overload
def partition_by(f: set[_H], seq: Iterable[_H]) -> Iterable[list[_H]]: ...
@overload
def lpartition_by(f: Callable[[_T], _KT], seq: Iterable[_T]) -> list[list[_T]]: ...
@overload
def lpartition_by(f: None, seq: Iterable[_KT]) -> list[list[_KT]]: ...
@overload
def lpartition_by(f: _RegexType[AnyStr], seq: Iterable[str]) -> list[list[str]]: ...
@overload
def lpartition_by(
    f: int, seq: Iterable[Sequence[_KT]]
) -> list[list[Sequence[_KT]]]: ...
@overload
def lpartition_by(
    f: slice,
    seq: Iterable[tuple[_H, ...]],
) -> list[list[tuple[_H, ...]]]: ...
@overload
def lpartition_by(f: Mapping[_KT, _H], seq: Iterable[_KT]) -> list[list[_KT]]: ...
@overload
def lpartition_by(f: set[_H], seq: Iterable[_H]) -> list[list[_H]]: ...
@overload
def with_prev(seq: Iterable[_T1]) -> Iterable[tuple[_T1, _T1 | None]]: ...
@overload
def with_prev(seq: Iterable[_T1], fill: _T2) -> Iterable[tuple[_T1, _T1 | _T2]]: ...
@overload
def with_next(seq: Iterable[_T1]) -> Iterable[tuple[_T1, _T1 | None]]: ...
@overload
def with_next(seq: Iterable[_T1], fill: _T2) -> Iterable[tuple[_T1, _T1 | _T2]]: ...
def pairwise(seq: Iterable[_T]) -> Iterable[tuple[_T, _T]]: ...
@overload
def lzip(*, strict: bool = ...) -> list[Any]: ...
@overload
def lzip(iter1: Iterable[_T1], /, *, strict: bool = ...) -> list[tuple[_T1]]: ...
@overload
def lzip(
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    /,
    *,
    strict: bool = ...,
) -> list[tuple[_T1, _T2]]: ...
@overload
def lzip(
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    iter3: Iterable[_T3],
    /,
    *,
    strict: bool = ...,
) -> list[tuple[_T1, _T2, _T3]]: ...
@overload
def lzip(
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    iter3: Iterable[_T3],
    iter4: Iterable[_T4],
    /,
    *,
    strict: bool = ...,
) -> list[tuple[_T1, _T2, _T3, _T4]]: ...
@overload
def lzip(
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    iter3: Iterable[_T3],
    iter4: Iterable[_T4],
    iter5: Iterable[_T5],
    /,
    *,
    strict: bool = ...,
) -> list[tuple[_T1, _T2, _T3, _T4, _T5]]: ...
@overload
def lzip(
    iter1: Iterable[Any],
    iter2: Iterable[Any],
    iter3: Iterable[Any],
    iter4: Iterable[Any],
    iter5: Iterable[Any],
    iter6: Iterable[Any],
    /,
    *iterables: Iterable[Any],
    strict: bool = ...,
) -> list[tuple[Any, ...]]: ...
@overload
def reductions(f: Callable[[_S, _T], _S], seq: Iterable[_T]) -> Iterable[_S]: ...
@overload
def reductions(
    f: Callable[[_S, _T], _S], seq: Iterable[_T], acc: _S
) -> Iterable[_S]: ...
@overload
def lreductions(f: Callable[[_S, _T], _S], seq: Iterable[_T]) -> list[_S]: ...
@overload
def lreductions(f: Callable[[_S, _T], _S], seq: Iterable[_T], acc: _S) -> list[_S]: ...
def sums(seq: Iterable[SupportsAdd[_T]], acc: _T = ...) -> Iterable[_T]: ...
def lsums(seq: Iterable[SupportsAdd[_T]], acc: _T = ...) -> list[_T]: ...

__all__ = (
    "accumulate",
    "butlast",
    "cat",
    "chain",
    "chunks",
    "concat",
    "count",
    "count_by",
    "count_reps",
    "cycle",
    "distinct",
    "drop",
    "dropwhile",
    "filter",
    "first",
    "flatten",
    "group_by",
    "group_by_keys",
    "group_values",
    "ilen",
    "interleave",
    "interpose",
    "iterate",
    "keep",
    "last",
    "lcat",
    "lchunks",
    "lconcat",
    "ldistinct",
    "lfilter",
    "lflatten",
    "lkeep",
    "lmap",
    "lmapcat",
    "lpartition",
    "lpartition_by",
    "lreductions",
    "lremove",
    "lsplit",
    "lsplit_at",
    "lsplit_by",
    "lsums",
    "lwithout",
    "lzip",
    "map",
    "mapcat",
    "nth",
    "pairwise",
    "partition",
    "partition_by",
    "reductions",
    "remove",
    "repeat",
    "repeatedly",
    "rest",
    "second",
    "split",
    "split_at",
    "split_by",
    "sums",
    "take",
    "takewhile",
    "with_next",
    "with_prev",
    "without",
)
