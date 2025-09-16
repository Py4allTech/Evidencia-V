class DeviceType:
    def __init__(self, id: int, name: str, characteristics: str):
        self.__id = id
        self.__name = name
        self.__characteristics = characteristics

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_characteristics(self) -> str:
        return self.__characteristics

    def set_name(self, name: str) -> None:
        self.__name = name

    def set_characteristics(self, characteristics: str) -> None:
        self.__characteristics = characteristics