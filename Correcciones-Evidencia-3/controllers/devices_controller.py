from model.devices_data import devices
from model.user_home_data import user_homes

from utils.devices_utils import (
    generate_device_id, 
    is_user_authorized_for_home,
    get_home_ids_by_email,
    map_device_data_for_view
)

def add_device(email_user, name, selected_state, selected_type, selected_location, selected_home) -> bool:
    """Agrega un nuevo dispositivo si el usuario está autorizado para el hogar seleccionado."""
    home_id = selected_home['id']
    if not is_user_authorized_for_home(email_user, home_id, user_homes):
        return False  # No se permite agregar si el hogar no pertenece al usuario

    device_id = generate_device_id()  # Generar un ID único para el dispositivo

    device = {
        'id': device_id,
        'name': name,
        'state_id': selected_state['id'],
        'device_type_id': selected_type['id'],
        'location_id': selected_location['id'],
        'home_id': home_id
    }

    devices.append(device)  # Guardar el dispositivo en la "base de datos"
    return True


def get_user_devices(email_user: str, states: dict, device_types: dict, locations: dict, homes: dict) -> list[dict]:
    """Devuelve una lista de dispositivos asociados a los hogares del usuario, mapeados con datos legibles."""
    home_ids = get_home_ids_by_email(email_user, user_homes)
    
    # Filtrar solo los dispositivos que pertenecen a hogares del usuario
    user_devices = [device for device in devices if device['home_id'] in home_ids]

    # Mapear los datos para visualización (convertir IDs en nombres)
    return [map_device_data_for_view(d, states, device_types, locations, homes) for d in user_devices]


def search_device_by_name(email_user: str, device_name: str, states: dict, device_types: dict, locations: dict, homes: dict) -> dict | None:
    """Busca un dispositivo por nombre dentro de los hogares del usuario."""
    home_ids = get_home_ids_by_email(email_user, user_homes)
    
    for device in devices:
        if device['home_id'] in home_ids and device['name'].lower() == device_name.lower():
            return map_device_data_for_view(device, states, device_types, locations, homes)
    
    return None  # No se encontró el dispositivo


def delete_device_by_name(email_user: str, device_name: str) -> bool:
    """Elimina un dispositivo si el usuario está autorizado para el hogar al que pertenece."""
    home_ids = get_home_ids_by_email(email_user, user_homes)

    for i, device in enumerate(devices):
        if device['home_id'] in home_ids and device['name'].lower() == device_name.lower():
            del devices[i]  # Eliminar el dispositivo por índice
            return True
    
    return False  # No se encontró o no se tiene permiso