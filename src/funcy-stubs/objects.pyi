from types import ModuleType
from typing import (
    Any,
    Callable,
    ContextManager,
    Generic,
    NoReturn,
    TypeVar,
)

from ._types import P, S, T

_Prop = TypeVar("_Prop", bound=property)

class cached_property(property, Generic[T, S]):
    fset: Any = None
    fdel: Any = None

    def __init__(self, fget: Callable[[T], S] | None) -> None: ...
    def __get__(self, instance: T, owner: type | None = None, /) -> S: ...

class cached_readonly(cached_property[T, S]):
    def __set__(self, instance: Any, owner: Any) -> NoReturn: ...

def wrap_prop(ctx: ContextManager[Any]) -> Callable[[_Prop], _Prop]: ...
def monkey(
    cls: type | ModuleType,
    name: str = ...,
) -> Callable[[Callable[P, T]], Callable[P, T]]: ...

class LazyObject:
    def __init__(self, init: Any) -> None: ...

__all__ = ("LazyObject", "cached_property", "cached_readonly", "monkey", "wrap_prop")
