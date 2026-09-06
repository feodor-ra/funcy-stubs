from abc import abstractmethod
from collections.abc import (
    Container,
    ItemsView,
    Iterable,
    Iterator,
    KeysView,
    Mapping,
    Sequence,
    ValuesView,
)
from re import Pattern
from typing import (
    Any,
    AnyStr,
    Callable,
    Hashable,
    MutableMapping,
    Protocol,
    SupportsIndex,
    TypeVar,
    overload,
)

from typing_extensions import TypeAliasType, TypeGuard

_T = TypeVar("_T")
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_S = TypeVar("_S")
_B = TypeVar("_B")
_KT = TypeVar("_KT", bound=Hashable)
_VT = TypeVar("_VT")
_H = TypeVar("_H", bound=Hashable)
_T_co = TypeVar("_T_co", covariant=True)
_T_contra = TypeVar("_T_contra", contravariant=True)

_Coll = TypeVar("_Coll", bound=Iterable[Any])
_M = TypeVar("_M", bound=Mapping[str, Any])
_KT1 = TypeVar("_KT1", bound=Hashable)
_StrT = TypeVar("_StrT", bound=str)
_SeqT = TypeVar("_SeqT", bound=Sequence[Any])
_StrColl = TypeVar("_StrColl", bound=Iterable[str])
_SeqColl = TypeVar("_SeqColl", bound=Iterable[Sequence[Any]])
_HashColl = TypeVar("_HashColl", bound=Iterable[Hashable])
_SeqKeyPairs = TypeVar("_SeqKeyPairs", bound=Iterable[tuple[Sequence[Any], Any]])
_SeqValuePairs = TypeVar("_SeqValuePairs", bound=Iterable[tuple[Any, Sequence[Any]]])

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

class _ItemsProtocol(Protocol[_T_co]):
    @abstractmethod
    def items(self) -> _T_co: ...

class _ValuesProtocol(Protocol[_T_co]):
    @abstractmethod
    def values(self) -> _T_co: ...

class _GetCollectionProtocol(Protocol[_T_co, _T_contra]):
    @abstractmethod
    def __getitem__(self, i: _T_contra, /) -> _T_co: ...

class _SetCollectionProtocol(Protocol[_T_contra]):
    @abstractmethod
    def __setitem__(self, key: SupportsIndex, value: _T_contra, /) -> None: ...
    @abstractmethod
    def __getitem__(self, i: SupportsIndex, /) -> Any: ...

class _DelCollectionProtocol(Protocol):
    @abstractmethod
    def __delitem__(self, key: Any, /) -> None: ...
    @abstractmethod
    def __getitem__(self, i: Any, /) -> Any: ...

_DelCollectionType = TypeVar("_DelCollectionType", bound=_DelCollectionProtocol)

@overload
def empty(coll: Iterator[_T]) -> Iterator[_T]: ...
@overload
def empty(coll: KeysView[_KT]) -> list[_KT]: ...
@overload
def empty(coll: ValuesView[_VT]) -> list[_VT]: ...
@overload
def empty(coll: ItemsView[_KT, _VT]) -> list[tuple[_KT, _VT]]: ...
@overload
def empty(coll: _Coll) -> _Coll: ...
@overload
def iteritems(coll: _ItemsProtocol[_T]) -> _T: ...
@overload
def iteritems(coll: _T) -> _T: ...
@overload
def itervalues(coll: _ValuesProtocol[_T]) -> _T: ...
@overload
def itervalues(coll: _T) -> _T: ...
@overload
def join(colls: Iterable[str | bytes]) -> str: ...
@overload
def join(colls: Iterable[MutableMapping[_KT, _VT]]) -> MutableMapping[_KT, _VT]: ...
@overload
def join(colls: Iterable[set[_H]]) -> set[_H]: ...
@overload
def join(colls: Iterable[range]) -> Iterator[int]: ...
@overload
def join(colls: Iterable[Iterable[_T]]) -> Iterable[_T]: ...
@overload
def merge(*colls: str | bytes) -> str: ...
@overload
def merge(*colls: MutableMapping[_KT, _VT]) -> MutableMapping[_KT, _VT]: ...
@overload
def merge(*colls: set[_H]) -> set[_H]: ...
@overload
def merge(*colls: range) -> Iterator[int]: ...
@overload
def merge(*colls: Iterable[_T]) -> Iterable[_T]: ...
def join_with(
    f: Callable[[list[_VT]], _T],
    dicts: Iterable[Mapping[_KT, _VT]],
    strict: bool = ...,
) -> dict[_KT, _T]: ...
def merge_with(
    f: Callable[[list[_VT]], _T], *dicts: Mapping[_KT, _VT]
) -> dict[_KT, _T]: ...
@overload
def walk(f: Callable[[_T], _S], coll: list[_T]) -> list[_S]: ...
@overload
def walk(f: Callable[[_T], _S], coll: set[_T]) -> set[_S]: ...
@overload
def walk(f: Callable[[_T], _S], coll: tuple[_T, ...]) -> tuple[_S, ...]: ...
@overload
def walk(
    f: Callable[[tuple[_KT, _VT]], tuple[_KT1, _S]],
    coll: dict[_KT, _VT],
) -> dict[_KT1, _S]: ...
@overload
def walk(f: Callable[[_T], _S], coll: Iterable[_T]) -> Iterable[_S]: ...
@overload
def walk(f: None, coll: _Coll) -> _Coll: ...
@overload
def walk(f: _RegexType[AnyStr], coll: list[str]) -> list[_MatchType[AnyStr] | None]: ...
@overload
def walk(f: _RegexType[AnyStr], coll: set[str]) -> set[_MatchType[AnyStr] | None]: ...
@overload
def walk(
    f: _RegexType[AnyStr], coll: tuple[str, ...]
) -> tuple[_MatchType[AnyStr] | None, ...]: ...
@overload
def walk(
    f: _RegexType[AnyStr], coll: Iterable[str]
) -> Iterable[_MatchType[AnyStr] | None]: ...
@overload
def walk(f: int, coll: Iterable[Sequence[_T]]) -> Iterable[_T]: ...
@overload
def walk(f: slice, coll: _SeqColl) -> _SeqColl: ...
@overload
def walk(f: Mapping[_KT, _VT], coll: list[_KT]) -> list[_VT]: ...
@overload
def walk(f: Mapping[_KT, _VT], coll: set[_KT]) -> set[_VT]: ...
@overload
def walk(f: Mapping[_KT, _VT], coll: tuple[_KT, ...]) -> tuple[_VT, ...]: ...
@overload
def walk(f: Mapping[_KT, _VT], coll: Iterable[_KT]) -> Iterable[_VT]: ...
@overload
def walk(f: set[_H], coll: list[_H]) -> list[bool]: ...
@overload
def walk(f: set[_H], coll: set[_H]) -> set[bool]: ...
@overload
def walk(f: set[_H], coll: tuple[_H, ...]) -> tuple[bool, ...]: ...
@overload
def walk(f: set[_H], coll: Iterable[_H]) -> Iterable[bool]: ...
@overload
def walk_keys(
    f: Callable[[_T], _S], coll: list[tuple[_T, _VT]]
) -> list[tuple[_S, _VT]]: ...
@overload
def walk_keys(
    f: Callable[[_T], _S], coll: set[tuple[_T, _VT]]
) -> set[tuple[_S, _VT]]: ...
@overload
def walk_keys(
    f: Callable[[_T], _S],
    coll: tuple[tuple[_T, _VT], ...],
) -> tuple[tuple[_S, _VT], ...]: ...
@overload
def walk_keys(f: Callable[[_KT], _KT1], coll: dict[_KT, _VT]) -> dict[_KT1, _VT]: ...  # type: ignore[overload-overlap]
@overload
def walk_keys(
    f: Callable[[_KT], _KT1],
    coll: Iterable[tuple[_T, _VT]],
) -> Iterable[tuple[_T, _VT]]: ...
@overload
def walk_keys(f: None, coll: _Coll) -> _Coll: ...
@overload
def walk_keys(
    f: _RegexType[AnyStr], coll: list[tuple[str, _VT]]
) -> list[tuple[_MatchType[AnyStr] | None, _VT]]: ...
@overload
def walk_keys(
    f: _RegexType[AnyStr], coll: set[tuple[str, _VT]]
) -> set[tuple[_MatchType[AnyStr] | None, _VT]]: ...
@overload
def walk_keys(
    f: _RegexType[AnyStr], coll: tuple[tuple[str, _VT], ...]
) -> tuple[tuple[_MatchType[AnyStr] | None, _VT], ...]: ...
@overload
def walk_keys(
    f: _RegexType[AnyStr], coll: dict[str, _VT]
) -> dict[_MatchType[AnyStr] | None, _VT]: ...
@overload
def walk_keys(
    f: _RegexType[AnyStr], coll: Iterable[tuple[str, _VT]]
) -> Iterable[tuple[_MatchType[AnyStr] | None, _VT]]: ...
@overload
def walk_keys(f: int, coll: dict[_SeqT, _VT]) -> dict[Any, _VT]: ...
@overload
def walk_keys(
    f: int, coll: Iterable[tuple[Sequence[_T], _VT]]
) -> Iterable[tuple[_T, _VT]]: ...
@overload
def walk_keys(f: slice, coll: dict[_SeqT, _VT]) -> dict[_SeqT, _VT]: ...
@overload
def walk_keys(f: slice, coll: _SeqKeyPairs) -> _SeqKeyPairs: ...
@overload
def walk_keys(
    f: Mapping[_KT, _KT1], coll: list[tuple[_KT, _VT]]
) -> list[tuple[_KT1, _VT]]: ...
@overload
def walk_keys(
    f: Mapping[_KT, _KT1], coll: set[tuple[_KT, _VT]]
) -> set[tuple[_KT1, _VT]]: ...
@overload
def walk_keys(
    f: Mapping[_KT, _KT1], coll: tuple[tuple[_KT, _VT], ...]
) -> tuple[tuple[_KT1, _VT], ...]: ...
@overload
def walk_keys(f: Mapping[_KT, _KT1], coll: dict[_KT, _VT]) -> dict[_KT1, _VT]: ...  # type: ignore[overload-overlap]
@overload
def walk_keys(
    f: Mapping[_KT, _KT1], coll: Iterable[tuple[_KT, _VT]]
) -> Iterable[tuple[_KT1, _VT]]: ...
@overload
def walk_keys(f: set[_H], coll: list[tuple[_H, _VT]]) -> list[tuple[bool, _VT]]: ...
@overload
def walk_keys(f: set[_H], coll: set[tuple[_H, _VT]]) -> set[tuple[bool, _VT]]: ...
@overload
def walk_keys(
    f: set[_H], coll: tuple[tuple[_H, _VT], ...]
) -> tuple[tuple[bool, _VT], ...]: ...
@overload
def walk_keys(f: set[_H], coll: dict[_H, _VT]) -> dict[bool, _VT]: ...  # type: ignore[overload-overlap]
@overload
def walk_keys(
    f: set[_H], coll: Iterable[tuple[_H, _VT]]
) -> Iterable[tuple[bool, _VT]]: ...
@overload
def walk_values(
    f: Callable[[_T], _S],
    coll: list[tuple[_KT, _T]],
) -> list[tuple[_KT, _S]]: ...
@overload
def walk_values(
    f: Callable[[_T], _S], coll: set[tuple[_KT, _T]]
) -> set[tuple[_KT, _S]]: ...
@overload
def walk_values(
    f: Callable[[_T], _S],
    coll: tuple[tuple[_KT, _T], ...],
) -> tuple[tuple[_KT, _S], ...]: ...
@overload
def walk_values(f: Callable[[_VT], _S], coll: dict[_KT, _VT]) -> dict[_KT, _S]: ...  # type: ignore[overload-overlap]
@overload
def walk_values(
    f: Callable[[_T2], _S],
    coll: Iterable[tuple[_T1, _T2]],
) -> Iterable[tuple[_T1, _S]]: ...
@overload
def walk_values(f: None, coll: _Coll) -> _Coll: ...
@overload
def walk_values(
    f: _RegexType[AnyStr], coll: list[tuple[_KT, str]]
) -> list[tuple[_KT, _MatchType[AnyStr] | None]]: ...
@overload
def walk_values(
    f: _RegexType[AnyStr], coll: set[tuple[_KT, str]]
) -> set[tuple[_KT, _MatchType[AnyStr] | None]]: ...
@overload
def walk_values(
    f: _RegexType[AnyStr], coll: tuple[tuple[_KT, str], ...]
) -> tuple[tuple[_KT, _MatchType[AnyStr] | None], ...]: ...
@overload
def walk_values(  # type: ignore[overload-overlap]
    f: _RegexType[AnyStr], coll: dict[_KT, str]
) -> dict[_KT, _MatchType[AnyStr] | None]: ...
@overload
def walk_values(
    f: _RegexType[AnyStr], coll: Iterable[tuple[_T, str]]
) -> Iterable[tuple[_T, _MatchType[AnyStr] | None]]: ...
@overload
def walk_values(f: int, coll: Mapping[_KT, Sequence[_T]]) -> dict[_KT, _T]: ...  # type: ignore[overload-overlap]
@overload
def walk_values(
    f: int, coll: Iterable[tuple[_T1, Sequence[_T2]]]
) -> Iterable[tuple[_T1, _T2]]: ...
@overload
def walk_values(f: slice, coll: dict[_KT, _SeqT]) -> dict[_KT, _SeqT]: ...  # type: ignore[overload-overlap]
@overload
def walk_values(f: slice, coll: _SeqValuePairs) -> _SeqValuePairs: ...
@overload
def walk_values(
    f: Mapping[_KT1, _S], coll: list[tuple[_KT, _KT1]]
) -> list[tuple[_KT, _S]]: ...
@overload
def walk_values(
    f: Mapping[_KT1, _S], coll: set[tuple[_KT, _KT1]]
) -> set[tuple[_KT, _S]]: ...
@overload
def walk_values(
    f: Mapping[_KT1, _S], coll: tuple[tuple[_KT, _KT1], ...]
) -> tuple[tuple[_KT, _S], ...]: ...
@overload
def walk_values(f: Mapping[_KT1, _S], coll: dict[_KT, _KT1]) -> dict[_KT, _S]: ...  # type: ignore[overload-overlap]
@overload
def walk_values(
    f: Mapping[_KT1, _S], coll: Iterable[tuple[_T, _KT1]]
) -> Iterable[tuple[_T, _S]]: ...
@overload
def walk_values(f: set[_H], coll: list[tuple[_KT, _H]]) -> list[tuple[_KT, bool]]: ...
@overload
def walk_values(f: set[_H], coll: set[tuple[_KT, _H]]) -> set[tuple[_KT, bool]]: ...
@overload
def walk_values(
    f: set[_H], coll: tuple[tuple[_KT, _H], ...]
) -> tuple[tuple[_KT, bool], ...]: ...
@overload
def walk_values(f: set[_H], coll: dict[_KT, _H]) -> dict[_KT, bool]: ...  # type: ignore[overload-overlap]
@overload
def walk_values(
    f: set[_H], coll: Iterable[tuple[_T, _H]]
) -> Iterable[tuple[_T, bool]]: ...
@overload
def select(
    pred: Callable[[tuple[_KT, _VT]], object],
    coll: dict[_KT, _VT],
) -> dict[_KT, _VT]: ...
@overload
def select(pred: Callable[[_T], object], coll: list[_T]) -> list[_T]: ...
@overload
def select(pred: Callable[[_T], object], coll: tuple[_T, ...]) -> tuple[_T, ...]: ...
@overload
def select(pred: Callable[[_T], object], coll: set[_T]) -> set[_T]: ...
@overload
def select(pred: Callable[[Any], object], coll: _Coll) -> _Coll: ...
@overload
def select(pred: None, coll: _Coll) -> _Coll: ...
@overload
def select(pred: _RegexType[AnyStr], coll: _StrColl) -> _StrColl: ...
@overload
def select(pred: int, coll: dict[_KT, _VT]) -> dict[_KT, _VT]: ...  # type: ignore[overload-overlap]
@overload
def select(pred: int, coll: _SeqColl) -> _SeqColl: ...
@overload
def select(pred: slice, coll: dict[_KT, _VT]) -> dict[_KT, _VT]: ...  # type: ignore[overload-overlap]
@overload
def select(pred: slice, coll: _SeqColl) -> _SeqColl: ...
@overload
def select(pred: Mapping[Any, Any], coll: _HashColl) -> _HashColl: ...
@overload
def select(pred: set[Any], coll: _HashColl) -> _HashColl: ...
@overload
def select_keys(
    pred: Callable[[_KT], object],
    coll: dict[_KT, _VT],
) -> dict[_KT, _VT]: ...
@overload
def select_keys(pred: None, coll: dict[_KT, _VT]) -> dict[_KT, _VT]: ...
@overload
def select_keys(
    pred: _RegexType[AnyStr], coll: dict[_StrT, _VT]
) -> dict[_StrT, _VT]: ...
@overload
def select_keys(pred: int, coll: dict[_SeqT, _VT]) -> dict[_SeqT, _VT]: ...
@overload
def select_keys(pred: slice, coll: dict[_SeqT, _VT]) -> dict[_SeqT, _VT]: ...
@overload
def select_keys(pred: Mapping[_KT, Any], coll: dict[_KT, _VT]) -> dict[_KT, _VT]: ...
@overload
def select_keys(pred: set[_KT], coll: dict[_KT, _VT]) -> dict[_KT, _VT]: ...
@overload
def select_values(
    pred: Callable[[_VT], object],
    coll: dict[_KT, _VT],
) -> dict[_KT, _VT]: ...
@overload
def select_values(pred: None, coll: dict[_KT, _VT]) -> dict[_KT, _VT]: ...
@overload
def select_values(
    pred: _RegexType[AnyStr], coll: dict[_KT, _StrT]
) -> dict[_KT, _StrT]: ...
@overload
def select_values(pred: int, coll: dict[_KT, _SeqT]) -> dict[_KT, _SeqT]: ...
@overload
def select_values(pred: slice, coll: dict[_KT, _SeqT]) -> dict[_KT, _SeqT]: ...
@overload
def select_values(pred: Mapping[_H, Any], coll: dict[_KT, _H]) -> dict[_KT, _H]: ...
@overload
def select_values(pred: set[_H], coll: dict[_KT, _H]) -> dict[_KT, _H]: ...
@overload
def compact(coll: dict[_KT, _VT]) -> dict[_KT, _VT]: ...
@overload
def compact(coll: list[_B]) -> list[_B]: ...
@overload
def compact(coll: tuple[_B, ...]) -> tuple[_B, ...]: ...
@overload
def compact(coll: set[_B]) -> set[_B]: ...
@overload
def compact(coll: Iterable[_B]) -> Iterable[_B]: ...
@overload
def is_distinct(coll: Iterable[Hashable], /) -> bool: ...
@overload
def is_distinct(coll: Iterable[_T], key: Callable[[_T], Hashable]) -> bool: ...
@overload
def all(seq: Iterable[object], /) -> bool: ...
@overload
def all(pred: Callable[[_T], object], seq: Iterable[_T]) -> bool: ...
@overload
def any(seq: Iterable[object], /) -> bool: ...
@overload
def any(pred: Callable[[_T], object], seq: Iterable[_T]) -> bool: ...
@overload
def none(seq: Iterable[object], /) -> bool: ...
@overload
def none(pred: Callable[[_T], object], seq: Iterable[_T]) -> bool: ...
@overload
def one(seq: Iterable[object], /) -> bool: ...
@overload
def one(pred: Callable[[_T], object], seq: Iterable[_T]) -> bool: ...
@overload
def some(seq: Iterable[_B], /) -> _B | None: ...
@overload
def some(pred: Callable[[_T], TypeGuard[_S]], seq: Iterable[_T]) -> _S | None: ...
@overload
def some(pred: Callable[[_T], object], seq: Iterable[_T]) -> _T | None: ...
def zipdict(keys: Iterable[_KT], vals: Iterable[_VT]) -> dict[_KT, _VT]: ...
def flip(mapping: Mapping[_KT, _KT1]) -> dict[_KT1, _KT]: ...
def project(mapping: Mapping[_KT, _VT], keys: Container[_KT]) -> dict[_KT, _VT]: ...
def omit(mapping: Mapping[_KT, _VT], keys: Container[_KT]) -> dict[_KT, _VT]: ...
def zip_values(*dicts: Mapping[Any, _VT]) -> Iterable[tuple[_VT, ...]]: ...
def zip_dicts(*dicts: Mapping[_KT, _VT]) -> Iterable[tuple[_KT, tuple[_VT, ...]]]: ...
@overload
def get_in(
    coll: _GetCollectionProtocol[_T, Any],
    path: Iterable[Hashable],
    default: None = None,
) -> _T | None: ...
@overload
def get_in(
    coll: _GetCollectionProtocol[_T, Any],
    path: Iterable[Hashable],
    default: _S,
) -> _T | _S: ...
@overload
def get_lax(
    coll: _GetCollectionProtocol[_T, Any],
    path: Iterable[Hashable],
    default: None = None,
) -> _T | None: ...
@overload
def get_lax(
    coll: _GetCollectionProtocol[_T, Any],
    path: Iterable[Hashable],
    default: _S,
) -> _T | _S: ...
@overload
def set_in(
    coll: _SetCollectionProtocol[_T],
    path: Sequence[Hashable],
    value: _T,
) -> _SetCollectionProtocol[_T]: ...
@overload
def set_in(
    coll: dict[_KT, _VT],
    path: Sequence[Hashable],
    value: _T,
) -> dict[_KT, _VT | _T]: ...
@overload
def set_in(
    coll: MutableMapping[_KT, _VT],
    path: Sequence[Hashable],
    value: _T,
) -> MutableMapping[_KT, _VT | _T]: ...
@overload
def update_in(
    coll: _SetCollectionProtocol[_T],
    path: Sequence[Hashable],
    update: Callable[[Any], Any],
    default: _T | None = None,
) -> _SetCollectionProtocol[_T]: ...
@overload
def update_in(
    coll: dict[_KT, _VT],
    path: Sequence[Hashable],
    update: Callable[[Any], _S],
    default: Any = None,
) -> dict[_KT, _VT | _S]: ...
@overload
def update_in(
    coll: MutableMapping[_KT, _VT],
    path: Sequence[Hashable],
    update: Callable[[Any], _S],
    default: Any = None,
) -> MutableMapping[_KT, _VT | _S]: ...
def del_in(
    coll: _DelCollectionType,
    path: Sequence[Hashable],
) -> _DelCollectionType: ...
def has_path(
    coll: _GetCollectionProtocol[Any, Any], path: Iterable[Hashable]
) -> bool: ...
def where(mappings: Iterable[_M], **cond: object) -> Iterable[_M]: ...
def lwhere(mappings: Iterable[_M], **cond: object) -> list[_M]: ...
def pluck(key: _KT, mappings: Iterable[Mapping[_KT, _VT]]) -> Iterable[_VT]: ...
def lpluck(key: _KT, mappings: Iterable[Mapping[_KT, _VT]]) -> list[_VT]: ...
def pluck_attr(attr: str, objects: Iterable[object]) -> Iterable[Any]: ...
def lpluck_attr(attr: str, objects: Iterable[object]) -> list[Any]: ...
def invoke(
    objects: Iterable[object], name: str, *args: Any, **kwargs: Any
) -> Iterable[Any]: ...
def linvoke(
    objects: Iterable[object], name: str, *args: Any, **kwargs: Any
) -> list[Any]: ...

__all__ = [
    "all",
    "any",
    "compact",
    "del_in",
    "empty",
    "flip",
    "get_in",
    "get_lax",
    "has_path",
    "invoke",
    "is_distinct",
    "iteritems",
    "itervalues",
    "join",
    "join_with",
    "linvoke",
    "lpluck",
    "lpluck_attr",
    "lwhere",
    "merge",
    "merge_with",
    "none",
    "omit",
    "one",
    "pluck",
    "pluck_attr",
    "project",
    "select",
    "select_keys",
    "select_values",
    "set_in",
    "some",
    "update_in",
    "walk",
    "walk_keys",
    "walk_values",
    "where",
    "zip_dicts",
    "zip_values",
    "zipdict",
]
