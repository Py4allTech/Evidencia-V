class DeviceAutomation:
    def __init__(self, device_id: int, automation_id: int, action: str):
        self.__device_id = device_id
        self.__automation_id = automation_id
        self.__action = action

    def get_device_id(self) -> int:
        return self.__device_id

    def get_automation_id(self) -> int:
        return self.__automation_id

    def get_action(self) -> str:
        return self.__action

    def set_action(self, action: str) -> None:
        self.__action = action