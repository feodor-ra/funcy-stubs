from abc import abstractmethod
from re import Pattern
from typing import AnyStr, Hashable, Protocol, TypeVar, Union

from typing_extensions import ParamSpec, TypeAliasType


class SupportsBool(Protocol):
    @abstractmethod
    def __bool__(self) -> bool: ...


class SupportsString(Protocol):
    @abstractmethod
    def __str__(self) -> str: ...


P = ParamSpec("P")
T = TypeVar("T")
T1 = TypeVar("T1")
T2 = TypeVar("T2")
T3 = TypeVar("T3")
T4 = TypeVar("T4")
T5 = TypeVar("T5")
T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)
S = TypeVar("S")
D = TypeVar("D")

KT = TypeVar("KT", bound=Hashable)
VT = TypeVar("VT")
H = TypeVar("H", bound=Hashable)

B = TypeVar("B", bound=SupportsBool)
Boolean = TypeAliasType("Boolean", Union[bool, B], type_params=(B,))

RegexType = TypeAliasType(
    "RegexType",
    Union[AnyStr, Pattern[AnyStr]],
    type_params=(AnyStr,),
)
MatchType = TypeAliasType(
    "MatchType",
    Union[AnyStr, tuple[AnyStr, ...], dict[str, AnyStr]],
    type_params=(AnyStr,),
)
