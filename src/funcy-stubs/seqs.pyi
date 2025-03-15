from abc import abstractmethod
from collections import defaultdict
from collections.abc import Iterable, Iterator, Mapping, Sequence
from itertools import accumulate, chain, count, cycle, repeat
from typing import Any, AnyStr, Callable, Protocol, overload

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
    H,
    MatchType,
    RegexType,
    S,
    T,
    T_contra,
)

class SupportsAdd(Protocol[T_contra]):
    @abstractmethod
    def __add__(self, value: T_contra, /) -> SupportsAdd[T_contra]: ...

@overload
def repeatedly(f: Callable[[], T], /) -> Iterator[T]: ...
@overload
def repeatedly(f: Callable[[], T], n: int) -> Iterator[T]: ...
def iterate(f: Callable[[T], T], x: T) -> Iterator[T]: ...
def take(n: int, seq: Iterable[T]) -> list[T]: ...
def drop(n: int, seq: Iterable[T]) -> Iterator[T]: ...
def first(seq: Iterable[T]) -> T | None: ...
def second(seq: Iterable[T]) -> T | None: ...
def nth(n: int, seq: Iterable[T]) -> T | None: ...
def last(seq: Iterable[T]) -> T | None: ...
def rest(seq: Iterable[T]) -> Iterator[T]: ...
def butlast(seq: Iterable[T]) -> Iterator[T]: ...
def ilen(seq: Iterable[Any]) -> int: ...
@overload
def lmap(
    f: Callable[[T1], S],
    iter1: Iterable[T1],
    /,
) -> list[S]: ...
@overload
def lmap(
    f: Callable[[T1, T2], S],
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    /,
) -> list[S]: ...
@overload
def lmap(
    f: Callable[[T1, T2, T3], S],
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    iter3: Iterable[T3],
    /,
) -> list[S]: ...
@overload
def lmap(
    f: Callable[[T1, T2, T3, T4], S],
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    iter3: Iterable[T3],
    iter4: Iterable[T4],
    /,
) -> list[S]: ...
@overload
def lmap(
    f: Callable[[T1, T2, T3, T4, T5], S],
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    iter3: Iterable[T3],
    iter4: Iterable[T4],
    iter5: Iterable[T5],
    /,
) -> list[S]: ...
@overload
def lmap(
    f: Callable[..., S],
    iter1: Iterable[Any],
    iter2: Iterable[Any],
    iter3: Iterable[Any],
    iter4: Iterable[Any],
    iter5: Iterable[Any],
    iter6: Iterable[Any],
    /,
    *iterables: Iterable[Any],
) -> list[S]: ...
@overload
def lmap(f: None, iter1: Iterable[T1], /) -> list[T1]: ...
@overload
def lmap(
    f: RegexType[AnyStr],
    iter1: Iterable[str],
    /,
) -> list[MatchType[AnyStr] | None]: ...
@overload
def lmap(f: int, iter1: Iterable[Sequence[T1]], /) -> list[T1]: ...
@overload
def lmap(f: slice, iter1: Iterable[Sequence[T1]], /) -> list[Sequence[T1]]: ...
@overload
def lmap(f: Mapping[KT, VT], iter1: Iterable[KT], /) -> list[VT]: ...
@overload
def lmap(f: set[H], iter1: Iterable[H], /) -> list[bool]: ...
@overload
def map(f: Callable[[T1], S], iter1: Iterable[T1], /) -> Iterator[S]: ...
@overload
def map(
    f: Callable[[T1, T2], S],
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    /,
) -> Iterator[S]: ...
@overload
def map(
    f: Callable[[T1, T2, T3], S],
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    iter3: Iterable[T3],
    /,
) -> Iterator[S]: ...
@overload
def map(
    f: Callable[[T1, T2, T3, T4], S],
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    iter3: Iterable[T3],
    iter4: Iterable[T4],
    /,
) -> Iterator[S]: ...
@overload
def map(
    f: Callable[[T1, T2, T3, T4, T5], S],
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    iter3: Iterable[T3],
    iter4: Iterable[T4],
    iter5: Iterable[T5],
    /,
) -> Iterator[S]: ...
@overload
def map(
    f: Callable[..., S],
    iter1: Iterable[Any],
    iter2: Iterable[Any],
    iter3: Iterable[Any],
    iter4: Iterable[Any],
    iter5: Iterable[Any],
    iter6: Iterable[Any],
    /,
    *iterables: Iterable[Any],
) -> Iterator[S]: ...
@overload
def map(f: None, iter1: Iterable[T1], /) -> Iterator[T1]: ...
@overload
def map(
    f: RegexType[AnyStr],
    iter1: Iterable[str],
    /,
) -> Iterator[MatchType[AnyStr] | None]: ...
@overload
def map(f: int, iter1: Iterable[Sequence[T1]], /) -> Iterator[T1]: ...
@overload
def map(f: slice, iter1: Iterable[Sequence[T1]], /) -> Iterator[Sequence[T1]]: ...
@overload
def map(f: Mapping[KT, VT], iter1: Iterable[KT], /) -> Iterator[VT]: ...
@overload
def map(f: set[H], iter1: Iterable[H], /) -> Iterator[bool]: ...
@overload
def lfilter(pred: Callable[[T], Boolean[B]], seq: Iterable[T]) -> list[T]: ...
@overload
def lfilter(pred: None, seq: Iterable[T]) -> list[T]: ...
@overload
def lfilter(pred: RegexType[AnyStr], seq: Iterable[str]) -> list[str]: ...
@overload
def lfilter(pred: int, seq: Iterable[Sequence[T]]) -> list[Sequence[T]]: ...
@overload
def lfilter(pred: slice, seq: Iterable[Sequence[T]]) -> list[Sequence[T]]: ...
@overload
def lfilter(pred: Mapping[KT, VT], seq: Iterable[KT]) -> list[KT]: ...
@overload
def lfilter(pred: set[H], seq: Iterable[H]) -> list[H]: ...
@overload
def filter(pred: Callable[[T], Boolean[B]], seq: Iterable[T]) -> Iterator[T]: ...
@overload
def filter(pred: None, seq: Iterable[T]) -> Iterator[T]: ...
@overload
def filter(pred: RegexType[AnyStr], seq: Iterable[str]) -> Iterator[str]: ...
@overload
def filter(pred: int, seq: Iterable[Sequence[T]]) -> Iterator[Sequence[T]]: ...
@overload
def filter(pred: slice, seq: Iterable[Sequence[T]]) -> Iterator[Sequence[T]]: ...
@overload
def filter(pred: Mapping[KT, VT], seq: Iterable[KT]) -> Iterator[KT]: ...
@overload
def filter(pred: set[H], seq: Iterable[H]) -> Iterator[H]: ...
@overload
def lremove(pred: Callable[[T], Boolean[B]], seq: Iterable[T]) -> list[T]: ...
@overload
def lremove(pred: None, seq: Iterable[T]) -> list[T]: ...
@overload
def lremove(pred: RegexType[AnyStr], seq: Iterable[str]) -> list[str]: ...
@overload
def lremove(pred: int, seq: Iterable[Sequence[T]]) -> list[Sequence[T]]: ...
@overload
def lremove(pred: slice, seq: Iterable[Sequence[T]]) -> list[Sequence[T]]: ...
@overload
def lremove(pred: Mapping[KT, VT], seq: Iterable[KT]) -> list[KT]: ...
@overload
def lremove(pred: set[H], seq: Iterable[H]) -> list[H]: ...
@overload
def remove(pred: Callable[[T], Boolean[B]], seq: Iterable[T]) -> Iterator[T]: ...
@overload
def remove(pred: None, seq: Iterable[T]) -> Iterator[T]: ...
@overload
def remove(pred: RegexType[AnyStr], seq: Iterable[str]) -> Iterator[str]: ...
@overload
def remove(pred: int, seq: Iterable[Sequence[T]]) -> Iterator[Sequence[T]]: ...
@overload
def remove(pred: slice, seq: Iterable[Sequence[T]]) -> Iterator[Sequence[T]]: ...
@overload
def remove(pred: Mapping[KT, VT], seq: Iterable[KT]) -> Iterator[KT]: ...
@overload
def remove(pred: set[H], seq: Iterable[H]) -> Iterator[H]: ...
@overload
def lkeep(f: Iterable[T]) -> list[T]: ...
@overload
def lkeep(f: Callable[[T], Boolean[B]], seq: Iterable[T]) -> list[T]: ...
@overload
def lkeep(f: None, seq: Iterable[T]) -> list[T]: ...
@overload
def lkeep(
    f: RegexType[AnyStr],
    seq: Iterable[str],
) -> list[MatchType[AnyStr] | None]: ...
@overload
def lkeep(f: int, seq: Iterable[Sequence[T]]) -> list[T]: ...
@overload
def lkeep(f: slice, seq: Iterable[Sequence[T]]) -> list[Sequence[T]]: ...
@overload
def lkeep(f: Mapping[KT, VT], seq: Iterable[KT]) -> list[VT]: ...
@overload
def lkeep(f: set[H], seq: Iterable[H]) -> list[bool]: ...
@overload
def keep(f: Iterable[T]) -> Iterator[T]: ...
@overload
def keep(f: Callable[[T], Boolean[B]], seq: Iterable[T]) -> Iterator[T]: ...
@overload
def keep(f: None, seq: Iterable[T]) -> Iterator[T]: ...
@overload
def keep(
    f: RegexType[AnyStr],
    seq: Iterable[str],
) -> Iterator[MatchType[AnyStr] | None]: ...
@overload
def keep(f: int, seq: Iterable[Sequence[T]]) -> Iterator[T]: ...
@overload
def keep(f: slice, seq: Iterable[Sequence[T]]) -> Iterator[Sequence[T]]: ...
@overload
def keep(f: Mapping[KT, VT], seq: Iterable[KT]) -> Iterator[VT]: ...
@overload
def keep(f: set[H], seq: Iterable[H]) -> Iterator[bool]: ...
def without(seq: Iterable[T], *items: T) -> Iterator[T]: ...
def lwithout(seq: Iterable[T], *items: T) -> list[T]: ...
def lconcat(*seqs: Iterable[T]) -> list[T]: ...
def concat(*seqs: Iterable[T]) -> Iterator[T]: ...
def lcat(seqs: Iterable[Iterable[T]]) -> list[T]: ...
def cat(seqs: Iterable[Iterable[T]]) -> Iterator[T]: ...
def flatten(
    seq: Iterable[T],
    follow: Callable[[T], Boolean[B]] = ...,
) -> Iterator[T]: ...
def lflatten(seq: Iterable[T], follow: Callable[[T], Boolean[B]] = ...) -> list[T]: ...
@overload
def lmapcat(
    f: Callable[[T1], Iterable[S]],
    iter1: Iterable[T1],
    /,
) -> list[S]: ...
@overload
def lmapcat(
    f: Callable[[T1, T2], Iterable[S]],
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    /,
) -> list[S]: ...
@overload
def lmapcat(
    f: Callable[[T1, T2, T3], Iterable[S]],
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    iter3: Iterable[T3],
    /,
) -> list[S]: ...
@overload
def lmapcat(
    f: Callable[[T1, T2, T3, T4], Iterable[S]],
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    iter3: Iterable[T3],
    iter4: Iterable[T4],
    /,
) -> list[S]: ...
@overload
def lmapcat(
    f: Callable[[T1, T2, T3, T4, T5], Iterable[S]],
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    iter3: Iterable[T3],
    iter4: Iterable[T4],
    iter5: Iterable[T5],
    /,
) -> list[S]: ...
@overload
def lmapcat(
    f: Callable[..., Iterable[S]],
    iter1: Iterable[Any],
    iter2: Iterable[Any],
    iter3: Iterable[Any],
    iter4: Iterable[Any],
    iter5: Iterable[Any],
    iter6: Iterable[Any],
    /,
    *iterables: Iterable[Any],
) -> list[S]: ...
@overload
def lmapcat(f: None, iter1: Iterable[Iterable[T1]], /) -> list[T1]: ...
@overload
def lmapcat(
    f: RegexType[AnyStr],
    iter1: Iterable[str],
    /,
) -> list[MatchType[AnyStr] | None]: ...
@overload
def lmapcat(f: int, iter1: Iterable[Sequence[T1]], /) -> list[T1]: ...
@overload
def lmapcat(f: slice, iter1: Iterable[Sequence[T1]], /) -> list[T1]: ...
@overload
def lmapcat(f: Mapping[KT, VT], iter1: Iterable[KT], /) -> list[VT]: ...
@overload
def lmapcat(f: set[H], iter1: Iterable[H], /) -> list[bool]: ...
@overload
def mapcat(
    f: Callable[[T1], Iterable[S]],
    iter1: Iterable[T1],
    /,
) -> Iterator[S]: ...
@overload
def mapcat(
    f: Callable[[T1, T2], Iterable[S]],
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    /,
) -> Iterator[S]: ...
@overload
def mapcat(
    f: Callable[[T1, T2, T3], Iterable[S]],
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    iter3: Iterable[T3],
    /,
) -> Iterator[S]: ...
@overload
def mapcat(
    f: Callable[[T1, T2, T3, T4], Iterable[S]],
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    iter3: Iterable[T3],
    iter4: Iterable[T4],
    /,
) -> Iterator[S]: ...
@overload
def mapcat(
    f: Callable[[T1, T2, T3, T4, T5], Iterable[S]],
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    iter3: Iterable[T3],
    iter4: Iterable[T4],
    iter5: Iterable[T5],
    /,
) -> Iterator[S]: ...
@overload
def mapcat(
    f: Callable[..., Iterable[S]],
    iter1: Iterable[Any],
    iter2: Iterable[Any],
    iter3: Iterable[Any],
    iter4: Iterable[Any],
    iter5: Iterable[Any],
    iter6: Iterable[Any],
    /,
    *iterables: Iterable[Any],
) -> Iterator[S]: ...
@overload
def mapcat(f: None, iter1: Iterable[Iterable[T1]], /) -> Iterator[T1]: ...
@overload
def mapcat(
    f: RegexType[AnyStr],
    iter1: Iterable[str],
    /,
) -> Iterator[MatchType[AnyStr] | None]: ...
@overload
def mapcat(f: int, iter1: Iterable[Sequence[T1]], /) -> Iterator[T1]: ...
@overload
def mapcat(f: slice, iter1: Iterable[Sequence[T1]], /) -> Iterator[T1]: ...
@overload
def mapcat(f: Mapping[KT, VT], iter1: Iterable[KT], /) -> Iterator[VT]: ...
@overload
def mapcat(f: set[H], iter1: Iterable[H], /) -> Iterator[bool]: ...
@overload
def interleave(
    iter1: Iterable[T1],
    /,
) -> Iterator[T1]: ...
@overload
def interleave(
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    /,
) -> Iterator[T1 | T2]: ...
@overload
def interleave(
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    iter3: Iterable[T3],
    /,
) -> Iterator[T1 | T2 | T3]: ...
@overload
def interleave(
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    iter3: Iterable[T3],
    iter4: Iterable[T4],
    /,
) -> Iterator[T1 | T2 | T3 | T4]: ...
@overload
def interleave(
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    iter3: Iterable[T3],
    iter4: Iterable[T4],
    iter5: Iterable[T5],
    /,
    *iterables: T,
) -> Iterator[T1 | T2 | T3 | T4 | T5 | T]: ...
def interpose(sep: T1, seq: Iterable[T2]) -> Iterator[T1 | T2]: ...
@overload
def takewhile(seq: Iterable[T], /) -> Iterator[T]: ...
@overload
def takewhile(pred: Callable[[T], Boolean[B]], seq: Iterable[T]) -> Iterator[T]: ...
@overload
def takewhile(pred: None, seq: Iterable[T]) -> Iterator[T]: ...
@overload
def takewhile(pred: RegexType[AnyStr], seq: Iterable[str]) -> Iterator[str]: ...
@overload
def takewhile(pred: int, seq: Iterable[Sequence[T]]) -> Iterator[Sequence[T]]: ...
@overload
def takewhile(pred: slice, seq: Iterable[Sequence[T]]) -> Iterator[Sequence[T]]: ...
@overload
def takewhile(pred: Mapping[KT, VT], seq: Iterable[KT]) -> Iterator[KT]: ...
@overload
def takewhile(pred: set[H], seq: Iterable[H]) -> Iterator[H]: ...
@overload
def dropwhile(seq: Iterable[T], /) -> Iterator[T]: ...
@overload
def dropwhile(pred: Callable[[T], Boolean[B]], seq: Iterable[T]) -> Iterator[T]: ...
@overload
def dropwhile(pred: None, seq: Iterable[T]) -> Iterator[T]: ...
@overload
def dropwhile(pred: RegexType[AnyStr], seq: Iterable[str]) -> Iterator[str]: ...
@overload
def dropwhile(pred: int, seq: Iterable[Sequence[T]]) -> Iterator[Sequence[T]]: ...
@overload
def dropwhile(pred: slice, seq: Iterable[Sequence[T]]) -> Iterator[Sequence[T]]: ...
@overload
def dropwhile(pred: Mapping[KT, VT], seq: Iterable[KT]) -> Iterator[KT]: ...
@overload
def dropwhile(pred: set[H], seq: Iterable[H]) -> Iterator[H]: ...
@overload
def ldistinct(seq: Iterable[H], /) -> list[H]: ...
@overload
def ldistinct(seq: Iterable[T], key: Callable[[T], H]) -> Iterable[T]: ...
@overload
def ldistinct(seq: Iterable[T], key: None) -> list[T]: ...
@overload
def ldistinct(seq: Iterable[str], key: RegexType[AnyStr]) -> list[str]: ...
@overload
def ldistinct(seq: Iterable[Sequence[KT]], key: int) -> list[KT]: ...
@overload
def ldistinct(seq: Iterable[tuple[KT]], key: slice) -> list[tuple[KT]]: ...
@overload
def ldistinct(seq: Iterable[KT], key: Mapping[KT, H]) -> list[KT]: ...
@overload
def ldistinct(seq: Iterable[H], key: set[H]) -> list[H]: ...
@overload
def distinct(seq: Iterable[H], /) -> Iterator[H]: ...
@overload
def distinct(seq: Iterable[T], key: Callable[[T], H]) -> Iterable[T]: ...
@overload
def distinct(seq: Iterable[T], key: None) -> Iterator[T]: ...
@overload
def distinct(seq: Iterable[str], key: RegexType[AnyStr]) -> Iterator[str]: ...
@overload
def distinct(seq: Iterable[Sequence[KT]], key: int) -> Iterator[KT]: ...
@overload
def distinct(seq: Iterable[tuple[KT]], key: slice) -> Iterator[tuple[KT]]: ...
@overload
def distinct(seq: Iterable[KT], key: Mapping[KT, H]) -> Iterator[KT]: ...
@overload
def distinct(seq: Iterable[H], key: set[H]) -> Iterator[H]: ...
@overload
def split(
    pred: Callable[[T], bool],
    seq: Iterable[T],
) -> tuple[Iterator[T], Iterator[T]]: ...
@overload
def split(pred: None, seq: Iterable[T]) -> tuple[Iterator[T], Iterator[T]]: ...
@overload
def split(
    pred: RegexType[AnyStr],
    seq: Iterable[str],
) -> tuple[Iterator[str], Iterator[str]]: ...
@overload
def split(pred: int, seq: Iterable[Sequence[T]]) -> tuple[Iterator[T], Iterator[T]]: ...
@overload
def split(
    pred: slice,
    seq: Iterable[Sequence[T]],
) -> tuple[Iterator[Sequence[T]], Iterator[Sequence[T]]]: ...
@overload
def split(
    pred: Mapping[KT, bool],
    seq: Iterable[KT],
) -> tuple[Iterator[KT], Iterator[KT]]: ...
@overload
def split(pred: set[H], seq: Iterable[H]) -> tuple[Iterator[H], Iterator[H]]: ...
@overload
def lsplit(pred: Callable[[T], bool], seq: Iterable[T]) -> tuple[list[T], list[T]]: ...
@overload
def lsplit(pred: None, seq: Iterable[T]) -> tuple[list[T], list[T]]: ...
@overload
def lsplit(
    pred: RegexType[AnyStr],
    seq: Iterable[str],
) -> tuple[list[str], list[str]]: ...
@overload
def lsplit(pred: int, seq: Iterable[Sequence[T]]) -> tuple[list[T], list[T]]: ...
@overload
def lsplit(
    pred: slice,
    seq: Iterable[Sequence[T]],
) -> tuple[list[Sequence[T]], list[Sequence[T]]]: ...
@overload
def lsplit(pred: Mapping[KT, bool], seq: Iterable[KT]) -> tuple[list[KT], list[KT]]: ...
@overload
def lsplit(pred: set[H], seq: Iterable[H]) -> tuple[list[H], list[H]]: ...
def split_at(n: int, seq: Iterable[T]) -> tuple[Iterator[T], Iterator[T]]: ...
def lsplit_at(n: int, seq: Iterator[T]) -> tuple[list[T], list[T]]: ...
@overload
def split_by(
    pred: Callable[[T], bool],
    seq: Iterable[T],
) -> tuple[Iterator[T], Iterator[T]]: ...
@overload
def split_by(pred: None, seq: Iterable[T]) -> tuple[Iterator[T], Iterator[T]]: ...
@overload
def split_by(
    pred: RegexType[AnyStr],
    seq: Iterable[str],
) -> tuple[Iterator[str], Iterator[str]]: ...
@overload
def split_by(
    pred: int | slice,
    seq: Iterable[Sequence[T]],
) -> tuple[Iterator[Sequence[T]], Iterator[Sequence[T]]]: ...
@overload
def split_by(
    pred: Mapping[KT, VT],
    seq: Iterable[KT],
) -> tuple[Iterator[KT], Iterator[KT]]: ...
@overload
def split_by(pred: set[H], seq: Iterable[H]) -> tuple[Iterator[H], Iterator[H]]: ...
@overload
def lsplit_by(
    pred: Callable[[T], bool],
    seq: Iterable[T],
) -> tuple[list[T], list[T]]: ...
@overload
def lsplit_by(pred: None, seq: Iterable[T]) -> tuple[list[T], list[T]]: ...
@overload
def lsplit_by(
    pred: RegexType[AnyStr],
    seq: Iterable[str],
) -> tuple[list[str], list[str]]: ...
@overload
def lsplit_by(
    pred: int | slice,
    seq: Iterable[Sequence[T]],
) -> tuple[list[Sequence[T]], list[Sequence[T]]]: ...
@overload
def lsplit_by(
    pred: Mapping[KT, VT],
    seq: Iterable[KT],
) -> tuple[list[KT], list[KT]]: ...
@overload
def lsplit_by(pred: set[H], seq: Iterable[H]) -> tuple[list[H], list[H]]: ...
@overload
def group_by(f: Callable[[T], KT], seq: Iterable[T]) -> defaultdict[KT, list[T]]: ...
@overload
def group_by(f: None, seq: Iterable[KT]) -> defaultdict[KT, list[KT]]: ...
@overload
def group_by(
    f: RegexType[AnyStr],
    seq: Iterable[str],
) -> defaultdict[MatchType[AnyStr] | None, list[str]]: ...
@overload
def group_by(
    f: int,
    seq: Iterable[Sequence[KT]],
) -> defaultdict[KT, list[Sequence[KT]]]: ...
@overload
def group_by(
    f: slice,
    seq: Iterable[tuple[H, ...]],
) -> defaultdict[tuple[H, ...], list[tuple[H, ...]]]: ...
@overload
def group_by(f: Mapping[KT, H], seq: Iterable[KT]) -> defaultdict[H, list[KT]]: ...
@overload
def group_by(f: set[H], seq: Iterable[H]) -> defaultdict[bool, list[H]]: ...
@overload
def group_by_keys(
    get_keys: Callable[[T], Iterable[KT]],
    seq: Iterable[T],
) -> defaultdict[KT, list[T]]: ...
@overload
def group_by_keys(get_keys: None, seq: Iterable[KT]) -> defaultdict[KT, list[KT]]: ...
@overload
def group_by_keys(
    get_keys: int,
    seq: Iterable[Sequence[Iterable[KT]]],
) -> defaultdict[KT, list[Sequence[Iterable[KT]]]]: ...
@overload
def group_by_keys(
    get_keys: slice,
    seq: Iterable[Sequence[KT]],
) -> defaultdict[KT, list[Sequence[KT]]]: ...
@overload
def group_by_keys(
    get_keys: Mapping[KT, Iterable[H]],
    seq: Iterable[KT],
) -> defaultdict[H, list[KT]]: ...
def group_values(seq: Iterable[tuple[KT, VT]]) -> defaultdict[KT, list[VT]]: ...
@overload
def count_by(f: Callable[[T], KT], seq: Iterable[T]) -> defaultdict[KT, int]: ...
@overload
def count_by(f: None, seq: Iterable[KT]) -> defaultdict[KT, int]: ...
@overload
def count_by(
    f: RegexType[AnyStr],
    seq: Iterable[str],
) -> defaultdict[MatchType[AnyStr] | None, int]: ...
@overload
def count_by(f: int, seq: Iterable[Sequence[KT]]) -> defaultdict[KT, int]: ...
@overload
def count_by(
    f: slice,
    seq: Iterable[tuple[H, ...]],
) -> defaultdict[tuple[H, ...], int]: ...
@overload
def count_by(f: Mapping[KT, H], seq: Iterable[KT]) -> defaultdict[H, int]: ...
@overload
def count_by(f: set[H], seq: Iterable[H]) -> defaultdict[bool, int]: ...
def count_reps(seq: Iterable[KT]) -> defaultdict[KT, int]: ...
@overload
def partition(n: int, seq: Iterator[T], /) -> Iterator[list[T]]: ...
@overload
def partition(n: int, seq: Sequence[T], /) -> Iterator[Sequence[T]]: ...
@overload
def partition(n: int, step: int, seq: Iterator[T]) -> Iterator[list[T]]: ...
@overload
def partition(n: int, step: int, seq: Sequence[T]) -> Iterator[Sequence[T]]: ...
@overload
def lpartition(n: int, seq: Iterator[T], /) -> list[list[T]]: ...
@overload
def lpartition(n: int, seq: Sequence[T], /) -> list[Sequence[T]]: ...
@overload
def lpartition(n: int, step: int, seq: Iterator[T]) -> list[list[T]]: ...
@overload
def lpartition(n: int, step: int, seq: Sequence[T]) -> list[Sequence[T]]: ...
@overload
def chunks(n: int, seq: Iterator[T], /) -> Iterator[list[T]]: ...
@overload
def chunks(n: int, seq: Sequence[T], /) -> Iterator[Sequence[T]]: ...
@overload
def chunks(n: int, step: int, seq: Iterator[T]) -> Iterator[list[T]]: ...
@overload
def chunks(n: int, step: int, seq: Sequence[T]) -> Iterator[Sequence[T]]: ...
@overload
def lchunks(n: int, seq: Iterator[T], /) -> list[list[T]]: ...
@overload
def lchunks(n: int, seq: Sequence[T], /) -> list[Sequence[T]]: ...
@overload
def lchunks(n: int, step: int, seq: Iterator[T]) -> list[list[T]]: ...
@overload
def lchunks(n: int, step: int, seq: Sequence[T]) -> list[Sequence[T]]: ...
@overload
def partition_by(f: Callable[[T], KT], seq: Iterable[T]) -> Iterator[list[T]]: ...
@overload
def partition_by(f: None, seq: Iterable[KT]) -> Iterator[list[KT]]: ...
@overload
def partition_by(f: RegexType[AnyStr], seq: Iterable[str]) -> Iterator[list[str]]: ...
@overload
def partition_by(
    f: int,
    seq: Iterable[Sequence[KT]],
) -> Iterator[list[Sequence[KT]]]: ...
@overload
def partition_by(
    f: slice,
    seq: Iterable[tuple[H, ...]],
) -> Iterator[list[tuple[H, ...]]]: ...
@overload
def partition_by(f: Mapping[KT, H], seq: Iterable[KT]) -> Iterator[list[KT]]: ...
@overload
def partition_by(f: set[H], seq: Iterable[H]) -> Iterator[list[H]]: ...
@overload
def lpartition_by(f: Callable[[T], KT], seq: Iterable[T]) -> list[list[T]]: ...
@overload
def lpartition_by(f: None, seq: Iterable[KT]) -> list[list[KT]]: ...
@overload
def lpartition_by(f: RegexType[AnyStr], seq: Iterable[str]) -> list[list[str]]: ...
@overload
def lpartition_by(f: int, seq: Iterable[Sequence[KT]]) -> list[list[Sequence[KT]]]: ...
@overload
def lpartition_by(
    f: slice,
    seq: Iterable[tuple[H, ...]],
) -> list[list[tuple[H, ...]]]: ...
@overload
def lpartition_by(f: Mapping[KT, H], seq: Iterable[KT]) -> list[list[KT]]: ...
@overload
def lpartition_by(f: set[H], seq: Iterable[H]) -> list[list[H]]: ...
def with_prev(seq: Iterable[T1], fill: T2 = None) -> Iterator[tuple[T1, T1 | T2]]: ...
def with_next(seq: Iterable[T1], fill: T2 = None) -> Iterator[tuple[T1, T1 | T2]]: ...
def pairwise(seq: Iterable[T]) -> Iterator[tuple[T, T]]: ...
@overload
def lzip(*, strict: bool = ...) -> list[Any]: ...
@overload
def lzip(iter1: Iterable[T1], /, *, strict: bool = ...) -> list[tuple[T1]]: ...
@overload
def lzip(
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    /,
    *,
    strict: bool = ...,
) -> list[tuple[T1, T2]]: ...
@overload
def lzip(
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    iter3: Iterable[T3],
    /,
    *,
    strict: bool = ...,
) -> list[tuple[T1, T2, T3]]: ...
@overload
def lzip(
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    iter3: Iterable[T3],
    iter4: Iterable[T4],
    /,
    *,
    strict: bool = ...,
) -> list[tuple[T1, T2, T3, T4]]: ...
@overload
def lzip(
    iter1: Iterable[T1],
    iter2: Iterable[T2],
    iter3: Iterable[T3],
    iter4: Iterable[T4],
    iter5: Iterable[T5],
    /,
    *,
    strict: bool = ...,
) -> list[tuple[T1, T2, T3, T4, T5]]: ...
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
def reductions(f: Callable[[S, T], S], seq: Iterable[T]) -> Iterator[S]: ...
@overload
def reductions(f: Callable[[S, T], S], seq: Iterable[T], acc: S) -> Iterator[S]: ...
@overload
def lreductions(f: Callable[[S, T], S], seq: Iterable[T]) -> list[S]: ...
@overload
def lreductions(f: Callable[[S, T], S], seq: Iterable[T], acc: S) -> list[S]: ...
def sums(seq: Iterable[SupportsAdd[T]], acc: T = ...) -> Iterator[T]: ...
def lsums(seq: Iterable[SupportsAdd[T]], acc: T = ...) -> list[T]: ...

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
