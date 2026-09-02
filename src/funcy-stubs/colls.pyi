from abc import abstractmethod
from collections.abc import (
    Container,
    ItemsView,
    Iterable,
    Iterator,
    KeysView,
    Mapping,
    ValuesView,
)
from typing import (
    Any,
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
_KT = TypeVar("_KT", bound=Hashable)
_VT = TypeVar("_VT")
_H = TypeVar("_H", bound=Hashable)
_T_co = TypeVar("_T_co", covariant=True)
_T_contra = TypeVar("_T_contra", contravariant=True)

class _SupportsBool(Protocol):
    @abstractmethod
    def __bool__(self) -> bool: ...

_B = TypeVar("_B", bound=_SupportsBool)

_Boolean = TypeAliasType("_Boolean", bool | _B, type_params=(_B,))

_Coll = TypeVar("_Coll", bound=Iterable[Any])
_KT1 = TypeVar("_KT1", bound=Hashable)

class ItemsProtocol(Protocol[_T_co]):
    @abstractmethod
    def items(self) -> _T_co: ...

class ValuesProtocol(Protocol[_T_co]):
    @abstractmethod
    def values(self) -> _T_co: ...

class GetCollectionProtocol(Protocol[_T_co, _T_contra]):
    @abstractmethod
    def __getitem__(self, i: _T_contra, /) -> _T_co: ...

class SetCollectionProtocol(Protocol[_T_contra]):
    @abstractmethod
    def __setitem__(self, key: SupportsIndex, value: _T_contra, /) -> None: ...
    @abstractmethod
    def __getitem__(self, i: SupportsIndex, /) -> Any: ...

class DelCollectionProtocol(Protocol):
    @abstractmethod
    def __delitem__(self, key: SupportsIndex, /) -> None: ...
    @abstractmethod
    def __getitem__(self, i: SupportsIndex, /) -> Any: ...

_DelCollectionType = TypeVar("_DelCollectionType", bound=DelCollectionProtocol)

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
def iteritems(coll: ItemsProtocol[_T]) -> _T: ...
@overload
def iteritems(coll: _T) -> _T: ...
@overload
def itervalues(coll: ValuesProtocol[_T]) -> _T: ...
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
def select(
    pred: Callable[[tuple[_KT, _VT]], _Boolean[_B]],
    coll: dict[_KT, _VT],
) -> dict[_KT, _VT]: ...
@overload
def select(pred: Callable[[_T], _Boolean[_B]], coll: list[_T]) -> list[_T]: ...
@overload
def select(
    pred: Callable[[_T], _Boolean[_B]], coll: tuple[_T, ...]
) -> tuple[_T, ...]: ...
@overload
def select(pred: Callable[[_T], _Boolean[_B]], coll: set[_T]) -> set[_T]: ...
@overload
def select(pred: Callable[[Any], _Boolean[_B]], coll: _Coll) -> _Coll: ...
def select_keys(
    pred: Callable[[_KT], _Boolean[_B]],
    coll: dict[_KT, _VT],
) -> dict[_KT, _VT]: ...
def select_values(
    pred: Callable[[_VT], _Boolean[_B]],
    coll: dict[_KT, _VT],
) -> dict[_KT, _VT]: ...
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
def all(seq: Iterable[_Boolean[_B]], /) -> bool: ...
@overload
def all(pred: Callable[[_T], _Boolean[_B]], seq: Iterable[_T]) -> bool: ...
@overload
def any(seq: Iterable[_Boolean[_B]], /) -> bool: ...
@overload
def any(pred: Callable[[_T], _Boolean[_B]], seq: Iterable[_T]) -> bool: ...
@overload
def none(seq: Iterable[_Boolean[_B]], /) -> bool: ...
@overload
def none(pred: Callable[[_T], _Boolean[_B]], seq: Iterable[_T]) -> bool: ...
@overload
def one(seq: Iterable[_Boolean[_B]], /) -> bool: ...
@overload
def one(pred: Callable[[_T], _Boolean[_B]], seq: Iterable[_T]) -> bool: ...
@overload
def some(seq: Iterable[_Boolean[_B]], /) -> _B: ...
@overload
def some(pred: Callable[[_T], TypeGuard[_S]], seq: Iterable[_T]) -> _S: ...
def zipdict(keys: Iterable[_KT], vals: Iterable[_VT]) -> dict[_KT, _VT]: ...
def flip(mapping: Mapping[_KT, _KT1]) -> dict[_KT1, _KT]: ...
def project(mapping: Mapping[_KT, _VT], keys: Container[_KT]) -> dict[_KT, _VT]: ...
def omit(mapping: Mapping[_KT, _VT], keys: Container[_KT]) -> dict[_KT, _VT]: ...
def zip_values(*dicts: Mapping[Any, _VT]) -> Iterable[tuple[_VT, ...]]: ...
def zip_dicts(*dicts: Mapping[_KT, _VT]) -> Iterable[tuple[_KT, tuple[_VT, ...]]]: ...
@overload
def get_in(
    coll: GetCollectionProtocol[_T, _T1],
    path: Iterable[_T1],
    default: None = None,
) -> _T | None: ...
@overload
def get_in(
    coll: GetCollectionProtocol[_T, _T1],
    path: Iterable[_T1],
    default: _S,
) -> _T | _S: ...
@overload
def get_in(
    coll: Mapping[_KT, _VT],
    path: Iterable[_KT],
    default: None = None,
) -> _VT | None: ...
@overload
def get_in(
    coll: Mapping[_KT, _VT],
    path: Iterable[_KT],
    default: _S,
) -> _VT | _S: ...
@overload
def get_lax(
    coll: GetCollectionProtocol[_T, _T1],
    path: Iterable[_T1],
    default: None = None,
) -> _T | None: ...
@overload
def get_lax(
    coll: GetCollectionProtocol[_T, _T1],
    path: Iterable[_T1],
    default: _S,
) -> _T | _S: ...
@overload
def get_lax(
    coll: Mapping[_KT, _VT],
    path: Iterable[_KT],
    default: None = None,
) -> _VT | None: ...
@overload
def get_lax(
    coll: Mapping[_KT, _VT],
    path: Iterable[_KT],
    default: _S,
) -> _VT | _S: ...
@overload
def set_in(
    coll: SetCollectionProtocol[_T],
    path: Iterable[int | Hashable],
    value: _T,
) -> SetCollectionProtocol[_T]: ...
@overload
def set_in(
    coll: MutableMapping[_KT, _VT],
    path: Iterable[_KT],
    value: _T,
) -> Mapping[_KT, _T]: ...
@overload
def update_in(
    coll: SetCollectionProtocol[_T],
    path: Iterable[int | Hashable],
    update: Callable[[SetCollectionProtocol[_T]], Any],
    default: _T | None = None,
) -> SetCollectionProtocol[_T]: ...
@overload
def update_in(
    coll: MutableMapping[_KT, _VT],
    path: Iterable[_KT],
    update: Callable[[SetCollectionProtocol[_T]], Any],
    default: _T | None = None,
) -> Mapping[_KT, _T]: ...
def del_in(
    coll: _DelCollectionType,
    path: Iterable[int | Hashable],
) -> _DelCollectionType: ...
@overload
def has_path(coll: GetCollectionProtocol[Any, _T], path: Iterable[_T]) -> bool: ...
@overload
def has_path(coll: Mapping[_KT, Any], path: Iterable[_KT]) -> bool: ...
def where(
    mappings: Iterable[Mapping[str, _VT]],
    **cond: _VT,
) -> Iterable[Mapping[str, _VT]]: ...
def lwhere(
    mappings: Iterable[Mapping[str, _VT]],
    **cond: _VT,
) -> list[Mapping[str, _VT]]: ...
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

__all__ = (
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
)
