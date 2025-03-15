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

from typing_extensions import TypeGuard

from ._types import KT, T1, T2, VT, B, Boolean, H, S, T, T_co, T_contra

_Coll = TypeVar("_Coll", bound=Iterable[Any])
_KT1 = TypeVar("_KT1", bound=Hashable)

class ItemsProtocol(Protocol[T_co]):
    @abstractmethod
    def items(self) -> T_co: ...

class ValuesProtocol(Protocol[T_co]):
    @abstractmethod
    def values(self) -> T_co: ...

class GetCollectionProtocol(Protocol[T_co, T_contra]):
    @abstractmethod
    def __getitem__(self, i: T_contra, /) -> T_co: ...

class SetCollectionProtocol(Protocol[T_contra]):
    @abstractmethod
    def __setitem__(self, key: SupportsIndex, value: T_contra, /) -> None: ...
    @abstractmethod
    def __getitem__(self, i: SupportsIndex, /) -> Any: ...

class DelCollectionProtocol(Protocol):
    @abstractmethod
    def __delitem__(self, key: SupportsIndex, /) -> None: ...
    @abstractmethod
    def __getitem__(self, i: SupportsIndex, /) -> Any: ...

_DelCollectionType = TypeVar("_DelCollectionType", bound=DelCollectionProtocol)

@overload
def empty(coll: Iterator[T]) -> Iterator[T]: ...
@overload
def empty(coll: KeysView[KT]) -> list[KT]: ...
@overload
def empty(coll: ValuesView[VT]) -> list[VT]: ...
@overload
def empty(coll: ItemsView[KT, VT]) -> list[tuple[KT, VT]]: ...
@overload
def empty(coll: _Coll) -> _Coll: ...
@overload
def iteritems(coll: ItemsProtocol[T]) -> T: ...
@overload
def iteritems(coll: T) -> T: ...
@overload
def itervalues(coll: ValuesProtocol[T]) -> T: ...
@overload
def itervalues(coll: T) -> T: ...
@overload
def join(colls: Iterable[str | bytes]) -> str: ...
@overload
def join(colls: Iterable[MutableMapping[KT, VT]]) -> MutableMapping[KT, VT]: ...
@overload
def join(colls: Iterable[set[H]]) -> set[H]: ...
@overload
def join(colls: Iterable[range]) -> Iterator[int]: ...
@overload
def join(colls: Iterable[Iterable[T]]) -> Iterable[T]: ...
@overload
def merge(*colls: str | bytes) -> str: ...
@overload
def merge(*colls: MutableMapping[KT, VT]) -> MutableMapping[KT, VT]: ...
@overload
def merge(*colls: set[H]) -> set[H]: ...
@overload
def merge(*colls: range) -> Iterator[int]: ...
@overload
def merge(*colls: Iterable[T]) -> Iterable[T]: ...
def join_with(
    f: Callable[[list[VT]], T],
    dicts: Iterable[Mapping[KT, VT]],
    strict: bool = ...,
) -> dict[KT, T]: ...
def merge_with(f: Callable[[list[VT]], T], *dicts: Mapping[KT, VT]) -> dict[KT, T]: ...
@overload
def walk(f: Callable[[T], S], coll: list[T]) -> list[S]: ...
@overload
def walk(f: Callable[[T], S], coll: set[T]) -> set[S]: ...
@overload
def walk(f: Callable[[T], S], coll: tuple[T]) -> tuple[S]: ...
@overload
def walk(
    f: Callable[[tuple[KT, VT]], tuple[_KT1, S]],
    coll: dict[KT, VT],
) -> dict[_KT1, S]: ...
@overload
def walk(f: Callable[[T], S], coll: Iterable[T]) -> Iterable[S]: ...
@overload
def walk_keys(f: Callable[[T], S], coll: list[tuple[T, VT]]) -> list[tuple[S, VT]]: ...
@overload
def walk_keys(f: Callable[[T], S], coll: set[tuple[T, VT]]) -> set[tuple[S, VT]]: ...
@overload
def walk_keys(
    f: Callable[[T], S],
    coll: tuple[tuple[T, VT]],
) -> tuple[tuple[S, VT]]: ...
@overload
def walk_keys(f: Callable[[KT], _KT1], coll: dict[KT, VT]) -> dict[_KT1, VT]: ...
@overload
def walk_keys(
    f: Callable[[KT], _KT1],
    coll: Iterable[tuple[T, VT]],
) -> Iterable[tuple[T, VT]]: ...
@overload
def walk_values(
    f: Callable[[T], S],
    coll: list[tuple[KT, T]],
) -> list[tuple[KT, S]]: ...
@overload
def walk_values(f: Callable[[T], S], coll: set[tuple[KT, T]]) -> set[tuple[KT, S]]: ...
@overload
def walk_values(
    f: Callable[[T], S],
    coll: tuple[tuple[KT, T]],
) -> tuple[tuple[KT, S]]: ...
@overload
def walk_values(f: Callable[[VT], S], coll: dict[KT, VT]) -> dict[KT, S]: ...
@overload
def walk_values(
    f: Callable[[T2], S],
    coll: Iterable[tuple[T1, T2]],
) -> Iterable[tuple[T1, S]]: ...
@overload
def select(
    pred: Callable[[tuple[KT, VT]], Boolean[B]],
    coll: dict[KT, VT],
) -> dict[KT, VT]: ...
@overload
def select(pred: Callable[[T], Boolean[B]], coll: list[T]) -> list[T]: ...
@overload
def select(pred: Callable[[T], Boolean[B]], coll: tuple[T]) -> tuple[T]: ...
@overload
def select(pred: Callable[[T], Boolean[B]], coll: set[T]) -> set[T]: ...
@overload
def select(pred: Callable[[Any], Boolean[B]], coll: _Coll) -> _Coll: ...
def select_keys(
    pred: Callable[[KT], Boolean[B]],
    coll: dict[KT, VT],
) -> dict[KT, VT]: ...
def select_values(
    pred: Callable[[VT], Boolean[B]],
    coll: dict[KT, VT],
) -> dict[KT, VT]: ...
@overload
def compact(coll: dict[KT, VT]) -> dict[KT, VT]: ...
@overload
def compact(coll: list[B]) -> list[B]: ...
@overload
def compact(coll: tuple[B]) -> tuple[B]: ...
@overload
def compact(coll: set[B]) -> set[B]: ...
@overload
def compact(coll: Iterable[B]) -> Iterable[B]: ...
@overload
def is_distinct(coll: Iterable[Hashable], /) -> bool: ...
@overload
def is_distinct(coll: Iterable[T], key: Callable[[T], Hashable]) -> bool: ...
@overload
def all(seq: Iterable[Boolean[B]], /) -> bool: ...
@overload
def all(pred: Callable[[T], Boolean[B]], seq: Iterable[T]) -> bool: ...
@overload
def any(seq: Iterable[Boolean[B]], /) -> bool: ...
@overload
def any(pred: Callable[[T], Boolean[B]], seq: Iterable[T]) -> bool: ...
@overload
def none(seq: Iterable[Boolean[B]], /) -> bool: ...
@overload
def none(pred: Callable[[T], Boolean[B]], seq: Iterable[T]) -> bool: ...
@overload
def one(seq: Iterable[Boolean[B]], /) -> bool: ...
@overload
def one(pred: Callable[[T], Boolean[B]], seq: Iterable[T]) -> bool: ...
@overload
def some(seq: Iterable[Boolean[B]], /) -> B: ...
@overload
def some(pred: Callable[[T], TypeGuard[S]], seq: Iterable[T]) -> S: ...
def zipdict(keys: Iterable[KT], vals: Iterable[VT]) -> dict[KT, VT]: ...
def flip(mapping: Mapping[KT, _KT1]) -> dict[_KT1, KT]: ...
def project(mapping: Mapping[KT, VT], keys: Container[KT]) -> dict[KT, VT]: ...
def omit(mapping: Mapping[KT, VT], keys: Container[KT]) -> dict[KT, VT]: ...
def zip_values(
    *dicts: Mapping[KT, VT],
) -> Iterable[tuple[tuple[VT, ...]]]: ...
def zip_dicts(
    *dicts: Iterable[Mapping[KT, VT]],
) -> Iterable[tuple[KT, tuple[VT, ...]]]: ...
@overload
def get_in(
    coll: GetCollectionProtocol[T, T1],
    path: Iterable[T1],
    default: S = None,
) -> T | S: ...
@overload
def get_in(
    coll: Mapping[KT, VT],
    path: Iterable[KT],
    default: S = None,
) -> KT | S: ...
@overload
def get_lax(
    coll: GetCollectionProtocol[T, T1],
    path: Iterable[T1],
    default: S = None,
) -> T | S: ...
@overload
def get_lax(
    coll: Mapping[KT, VT],
    path: Iterable[KT],
    default: S = None,
) -> VT | S: ...
@overload
def set_in(
    coll: SetCollectionProtocol[T],
    path: Iterable[int | Hashable],
    value: T,
) -> SetCollectionProtocol[T]: ...
@overload
def set_in(
    coll: MutableMapping[KT, VT],
    path: Iterable[KT],
    value: T,
) -> Mapping[KT, T]: ...
@overload
def update_in(
    coll: SetCollectionProtocol[T],
    path: Iterable[int | Hashable],
    update: Callable[[SetCollectionProtocol[T]], Any],
    default: T | None = None,
) -> SetCollectionProtocol[T]: ...
@overload
def update_in(
    coll: MutableMapping[KT, VT],
    path: Iterable[KT],
    update: Callable[[SetCollectionProtocol[T]], Any],
    default: T | None = None,
) -> Mapping[KT, T]: ...
def del_in(
    coll: _DelCollectionType,
    path: Iterable[int | Hashable],
) -> _DelCollectionType: ...
@overload
def has_path(coll: GetCollectionProtocol[Any, T], path: Iterable[T]) -> bool: ...
@overload
def has_path(coll: Mapping[KT, Any], path: Iterable[KT]) -> bool: ...
def where(
    mappings: Iterable[Mapping[str, VT]],
    **cond: VT,
) -> Iterable[Mapping[str, VT]]: ...
def lwhere(
    mappings: Iterable[Mapping[str, VT]],
    **cond: VT,
) -> list[Mapping[str, VT]]: ...
def pluck(key: KT, mappings: Iterable[Mapping[KT, VT]]) -> Iterable[VT]: ...
def lpluck(key: KT, mappings: Iterable[Mapping[KT, VT]]) -> list[VT]: ...
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
