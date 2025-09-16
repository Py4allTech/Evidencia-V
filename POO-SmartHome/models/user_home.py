class UserHome:
    def __init__(self, user_email: str, home_id: int):
        self.__user_email = user_email
        self.__home_id = home_id

    def get_user_email(self) -> str:
        return self.__user_email

    def get_home_id(self) -> int:
        return self.__home_id
