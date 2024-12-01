from contextlib import ContextDecorator, contextmanager
from functools import wraps
from inspect import unwrap
from typing import Any, Callable

from ._types import P, T

def decorator(
    deco: Callable[..., Any],
) -> Callable[[Callable[P, T]], Callable[P, T]]: ...

__all__ = ("ContextDecorator", "contextmanager", "decorator", "unwrap", "wraps")
