from contextlib import ContextDecorator, contextmanager
from functools import wraps
from inspect import unwrap
from typing import Any, Callable, TypeVar

from typing_extensions import ParamSpec

_P = ParamSpec("_P")
_T = TypeVar("_T")

def decorator(
    deco: Callable[..., Any],
) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]: ...

__all__ = ["ContextDecorator", "contextmanager", "decorator", "unwrap", "wraps"]
