import abc
import dataclasses
import typing


@dataclasses.dataclass()
class Param:

    type: type
    multiple: bool = False
    is_flag: bool = False
    help: str = None


class Handler(abc.ABC):

    def __init__(
        self,
        name: str,
        extensions: typing.List[str]
    ):
        self.name = name
        self.extensions = extensions

    @abc.abstractmethod
    def read(self, path: str, **kwargs):
        ...

    def read_params(self) -> typing.Dict[str, typing.Union[Param, type]]:
        return {}

    @abc.abstractmethod
    def write(self, x: typing.Any, path: str, **kwargs):
        ...

    def write_params(self) -> typing.Dict[str, typing.Union[Param, type]]:
        return {}
