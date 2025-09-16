class Automation:
    def __init__(
        self, id: int, name: str, description: str, active: bool, home_id: int
    ):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__active = active
        self.__home_id = home_id

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description

    def get_active(self) -> bool:
        return self.__active

    def get_home_id(self) -> int:
        return self.__home_id

    def set_name(self, name: str) -> None:
        self.__name = name

    def set_description(self, description: str) -> None:
        self.__description = description

    def set_active(self, active: bool) -> None:
        self.__active = active

    def __str__(self) -> str:
        return f"Automation(id={self.__id}, name='{self.__name}', active={self.__active}, description='{self.__description}')"