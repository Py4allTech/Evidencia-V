from datetime import datetime

class Event:
    def __init__(
        self,
        id: int,
        datetime_value: datetime,
        description: str,
        device_id: int = None,
        user_email: str = None,
        source: str = "manual",
    ):
        self.__id = id
        self.__datetime = datetime_value
        self.__description = description
        self.__device_id = device_id
        self.__user_email = user_email
        self.__source = source or "manual"

    def get_id(self) -> int:
        return self.__id

    def get_datetime(self) -> datetime:
        return self.__datetime

    def get_description(self) -> str:
        return self.__description

    def get_device_id(self) -> int:
        return self.__device_id

    def get_user_email(self) -> str:
        return self.__user_email

    def get_source(self) -> str:
        return self.__source

    def set_description(self, description: str) -> None:
        self.__description = description
