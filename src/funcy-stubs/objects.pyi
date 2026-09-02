from types import ModuleType
from typing import (
    Any,
    Callable,
    ContextManager,
    Generic,
    NoReturn,
    TypeVar,
    overload,
)

from typing_extensions import ParamSpec, Self

_P = ParamSpec("_P")
_S = TypeVar("_S")
_T = TypeVar("_T")

_Prop = TypeVar("_Prop", bound=property)

class cached_property(property, Generic[_T, _S]):
    fset: Any = None
    fdel: Any = None

    def __init__(self, fget: Callable[[_T], _S] | None) -> None: ...
    @overload
    def __get__(self, instance: None, owner: type | None = None, /) -> Self: ...
    @overload
    def __get__(self, instance: _T, owner: type | None = None, /) -> _S: ...

class cached_readonly(cached_property[_T, _S]):
    def __set__(self, instance: Any, value: Any) -> NoReturn: ...

def wrap_prop(ctx: ContextManager[Any]) -> Callable[[_Prop], _Prop]: ...
def monkey(
    cls: type | ModuleType,
    name: str | None = None,
) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]: ...

class LazyObject:
    def __init__(self, init: Any) -> None: ...

__all__ = ["LazyObject", "cached_property", "cached_readonly", "monkey", "wrap_prop"]
