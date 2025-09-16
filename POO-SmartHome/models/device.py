class Device:
    def __init__(
        self,
        id: int,
        name: str,
        state_id: int,
        device_type_id: int,
        location_id: int,
        home_id: int,
    ):
        self.__id = id
        self.__name = name
        self.__state_id = state_id
        self.__device_type_id = device_type_id
        self.__location_id = location_id
        self.__home_id = home_id

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_state_id(self) -> int:
        return self.__state_id

    def get_device_type_id(self) -> int:
        return self.__device_type_id

    def get_location_id(self) -> int:
        return self.__location_id

    def get_home_id(self) -> int:
        return self.__home_id

    def set_name(self, name: str) -> None:
        self.__name = name

    def set_state_id(self, state_id: int) -> None:
        self.__state_id = state_id

    def search_device_by_name(self, search_name: str) -> bool:
        if not search_name.strip():
            return False

        device_name_lower = self.__name.lower()
        search_name_lower = search_name.lower()

        return search_name_lower in device_name_lower