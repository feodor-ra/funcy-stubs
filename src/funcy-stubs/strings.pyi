from abc import abstractmethod
from collections.abc import Iterable
from re import Pattern, RegexFlag
from typing import (
    AnyStr,
    Callable,
    Protocol,
    SupportsBytes,
    overload,
)

import typing_extensions

_RegexType = typing_extensions.TypeAliasType(
    "_RegexType",
    AnyStr | Pattern[AnyStr],
    type_params=(AnyStr,),
)
_MatchType = typing_extensions.TypeAliasType(
    "_MatchType",
    AnyStr | tuple[AnyStr, ...] | dict[str, AnyStr],
    type_params=(AnyStr,),
)

_FlagsType: typing_extensions.TypeAlias = int | RegexFlag

class _SupportsString(Protocol):
    @abstractmethod
    def __str__(self) -> str: ...

@overload
def re_iter(
    regex: _RegexType[str],
    s: str,
    flags: _FlagsType = 0,
) -> Iterable[_MatchType[str]]: ...
@overload
def re_iter(
    regex: _RegexType[bytes],
    s: bytes,
    flags: _FlagsType = 0,
) -> Iterable[_MatchType[bytes]]: ...
@overload
def re_all(
    regex: _RegexType[str],
    s: str,
    flags: _FlagsType = 0,
) -> list[_MatchType[str]]: ...
@overload
def re_all(
    regex: _RegexType[bytes],
    s: bytes,
    flags: _FlagsType = 0,
) -> list[_MatchType[bytes]]: ...
@overload
def re_find(
    regex: _RegexType[str],
    s: str,
    flags: _FlagsType = 0,
) -> _MatchType[str] | None: ...
@overload
def re_find(
    regex: _RegexType[bytes],
    s: bytes,
    flags: _FlagsType = 0,
) -> _MatchType[bytes] | None: ...
@overload
def re_test(regex: _RegexType[str], s: str, flags: _FlagsType = 0) -> bool: ...
@overload
def re_test(regex: _RegexType[bytes], s: bytes, flags: _FlagsType = 0) -> bool: ...
def re_finder(
    regex: _RegexType[AnyStr],
    flags: _FlagsType = 0,
) -> Callable[[AnyStr], _MatchType[AnyStr] | None]: ...
def re_tester(
    regex: _RegexType[AnyStr],
    flags: _FlagsType = 0,
) -> Callable[[AnyStr], bool]: ...
@overload
def str_join(seq: Iterable[_SupportsString | str], /) -> str: ...
@overload
def str_join(sep: str, seq: Iterable[_SupportsString | str]) -> str: ...
@overload
def str_join(sep: bytes, seq: Iterable[SupportsBytes | bytes]) -> bytes: ...
def cut_prefix(s: AnyStr, prefix: AnyStr) -> AnyStr: ...
def cut_suffix(s: AnyStr, suffix: AnyStr) -> AnyStr: ...

__all__ = [
    "cut_prefix",
    "cut_suffix",
    "re_all",
    "re_find",
    "re_finder",
    "re_iter",
    "re_test",
    "re_tester",
    "str_join",
]
