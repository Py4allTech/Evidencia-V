class Home:
    def __init__(self, id: int, name: str):
        self.__id = id
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> int:
        return self.__id

    def set_name(self, name) -> None:
        self.__name = name
