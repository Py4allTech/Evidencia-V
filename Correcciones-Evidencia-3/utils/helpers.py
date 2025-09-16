device_id_counter = 1  # Variable global para contar los IDs


def get_user_input(message: str) -> str:
    # Código anterior: input(message).strip() - sin formato apropiado
    # 🔨 Nuevo código: agregamos ': ' si no termina en ':' para mejor legibilidad
    if not message.endswith(": ") and not message.endswith(":"):
        message += ": "
    return input(message).strip()


def generate_device_id() -> int:
    global device_id_counter
    device_id = device_id_counter
    device_id_counter += 1
    return device_id
