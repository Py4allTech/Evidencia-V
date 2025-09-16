class State:
    def __init__(self, id: int, name: str):
        self.__id = id
        self.__name = name

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name
