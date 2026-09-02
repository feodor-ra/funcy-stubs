from builtins import filter as filter
from builtins import map as map
from builtins import range as range
from builtins import zip as zip
from collections.abc import Hashable as Hashable
from collections.abc import Iterable as Iterable
from collections.abc import Iterator as Iterator
from collections.abc import Mapping as Mapping
from collections.abc import Sequence as Sequence
from collections.abc import Set as Set
from itertools import filterfalse as filterfalse
from typing import Any, Callable, Final, NoReturn, TypeVar

_T = TypeVar("_T")

basestring: tuple[type[bytes], type[str]]
PY2: Final[bool]
PY3: Final[bool]

def lmap(f: Callable[..., _T], *seqs: Iterable[Any]) -> list[_T]: ...
def lfilter(f: Callable[[_T], Any], seq: Iterable[_T]) -> list[_T]: ...
def raise_from(value: BaseException, from_value: BaseException | None) -> NoReturn: ...
