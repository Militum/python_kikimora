from abc import ABCMeta, abstractmethod

class CommandBase(metaclass=ABCMeta):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def validate(self, options: dict) -> None:
        pass

    @abstractmethod
    def execute(self, options: dict) -> dict:
        pass
