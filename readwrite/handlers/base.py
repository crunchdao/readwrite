import abc
import dataclasses
import typing


@dataclasses.dataclass()
class Param:

    type: type
    multiple: bool = False
    is_flag: bool = False
    help: str = None


class Handler:

    def __init__(
        self,
        name: str,
        extensions: typing.List[str]
    ):
        self.name = name
        self.extensions = extensions

    def read(self, path: str, **kwargs):
        raise NotImplementedError(f"unsupported read for {self.__class__.__name__}")

    def read_params(self) -> typing.Dict[str, typing.Union[Param, type]]:
        return {}

    @abc.abstractmethod
    def write(self, x: typing.Any, path: str, **kwargs):
        raise NotImplementedError(f"unsupported write for {self.__class__.__name__}")

    def write_params(self) -> typing.Dict[str, typing.Union[Param, type]]:
        return {}
