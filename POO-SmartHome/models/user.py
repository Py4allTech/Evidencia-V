class User:
    def __init__(self, email: str, password: str, name: str, role_id: int):
        self.__email = email
        self.__password = password
        self.__name = name
        self.__role_id = role_id

    def get_email(self) -> str:
        return self.__email

    def get_name(self) -> str:
        return self.__name

    def get_role_id(self) -> int:
        return self.__role_id

    def set_name(self, name: str) -> None:
        self.__name = name

    def set_password(self, password: str) -> None:
        self.__password = password

    def validate_credentials(self, email: str, password: str) -> bool:
        return self.__email == email and self.__password == password
