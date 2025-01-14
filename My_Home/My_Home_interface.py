import abc, typing

class My_Home_interface(abc.ABC):

    @abc.abstractmethod
    def __start_app__(self: typing.Self, app: str) -> None:
        pass

    @abc.abstractmethod
    def __about_us__(self: typing.Self) -> None:
        pass

    @abc.abstractmethod
    def __exit__(self: typing.Self, event: str | None) -> None:
        pass