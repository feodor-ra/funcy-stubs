from abc import abstractmethod
from collections.abc import Iterable
from re import RegexFlag
from typing import (
    AnyStr,
    Callable,
    Protocol,
    SupportsBytes,
    overload,
)

import typing_extensions

from ._types import MatchType, RegexType

FlagsType: typing_extensions.TypeAlias = int | RegexFlag

class SupportsString(Protocol):
    @abstractmethod
    def __str__(self) -> str: ...

def re_iter(
    regex: RegexType[AnyStr],
    s: str,
    flags: FlagsType = 0,
) -> Iterable[MatchType[AnyStr]]: ...
def re_all(
    regex: RegexType[AnyStr],
    s: str,
    flags: FlagsType = 0,
) -> list[MatchType[AnyStr]]: ...
def re_find(
    regex: RegexType[AnyStr],
    s: str,
    flags: FlagsType = 0,
) -> MatchType[AnyStr] | None: ...
def re_test(regex: RegexType[AnyStr], s: str, flags: FlagsType = 0) -> bool: ...
def re_finder(
    regex: RegexType[AnyStr],
    flags: FlagsType = 0,
) -> Callable[[str], MatchType[AnyStr] | None]: ...
def re_tester(
    regex: RegexType[AnyStr],
    flags: FlagsType = 0,
) -> Callable[[str], bool]: ...
@overload
def str_join(seq: Iterable[SupportsString | str], /) -> str: ...
@overload
def str_join(sep: str, seq: Iterable[SupportsString | str]) -> str: ...
@overload
def str_join(sep: bytes, seq: Iterable[SupportsBytes | bytes]) -> bytes: ...
def cut_prefix(s: AnyStr, prefix: AnyStr) -> AnyStr: ...
def cut_suffix(s: AnyStr, prefix: AnyStr) -> AnyStr: ...

__all__ = (
    "cut_prefix",
    "cut_suffix",
    "re_all",
    "re_find",
    "re_finder",
    "re_iter",
    "re_test",
    "re_tester",
    "str_join",
)
