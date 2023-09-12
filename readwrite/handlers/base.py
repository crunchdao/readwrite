import abc
import typing
import dataclasses


@dataclasses.dataclass()
class Param:
    type: type
    multiple: bool = False


class Handler:

    def __init__(self, name: str, extensions: typing.List[str]):
        self.name = name
        self.extensions = extensions

    @abc.abstractmethod
    def read(self, path: str, **kwargs):
        raise NotImplemented()

    @abc.abstractmethod
    def read_params(self) -> typing.Dict[str, typing.Union[Param, type]]:
        return {}

    @abc.abstractmethod
    def write(self, x: typing.Any, path: str, **kwargs):
        raise NotImplemented()

    @abc.abstractmethod
    def write_params(self) -> typing.Dict[str, typing.Union[Param, type]]:
        return {}
