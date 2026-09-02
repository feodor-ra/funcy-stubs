from collections.abc import Iterable, Iterator, Mapping, Sequence
from typing import Any, Callable, Hashable, TypeVar, overload

from typing_extensions import TypeAliasType, TypeGuard

_T = TypeVar("_T")
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
_T4 = TypeVar("_T4")
_T5 = TypeVar("_T5")

_C = TypeAliasType("_C", Callable[[Any], TypeGuard[_T]], type_params=(_T,))

@overload
def isa(t1: type[_T1], /) -> _C[_T1]: ...
@overload
def isa(t1: type[_T1], t2: type[_T2], /) -> _C[_T1 | _T2]: ...
@overload
def isa(t1: type[_T1], t2: type[_T2], t3: type[_T3], /) -> _C[_T1 | _T2 | _T3]: ...
@overload
def isa(
    t1: type[_T1], t2: type[_T2], t3: type[_T3], t4: type[_T4], /
) -> _C[_T1 | _T2 | _T3 | _T4]: ...
@overload
def isa(
    t1: type[_T1], t2: type[_T2], t3: type[_T3], t4: type[_T4], t5: type[_T5], /
) -> _C[_T1 | _T2 | _T3 | _T4 | _T5]: ...
@overload
def isa(*types: type) -> Callable[[Any], bool]: ...
def is_mapping(x: Any) -> TypeGuard[Mapping[Hashable, Any]]: ...
def is_set(x: Any) -> TypeGuard[set[Hashable]]: ...
def is_seq(x: Any) -> TypeGuard[Sequence[Any]]: ...
def is_list(x: Any) -> TypeGuard[list[Any]]: ...
def is_tuple(x: Any) -> TypeGuard[tuple[Any, ...]]: ...
def is_seqcoll(x: Any) -> TypeGuard[list[Any] | tuple[Any, ...]]: ...
def is_seqcont(
    x: Any,
) -> TypeGuard[list[Any] | tuple[Any, ...] | Iterator[Any] | range]: ...
def iterable(x: Any) -> TypeGuard[Iterable[Any]]: ...
def is_iter(x: Any) -> TypeGuard[Iterator[Any]]: ...

__all__ = (
    "is_iter",
    "is_list",
    "is_mapping",
    "is_seq",
    "is_seqcoll",
    "is_seqcont",
    "is_set",
    "is_tuple",
    "isa",
    "iterable",
)
