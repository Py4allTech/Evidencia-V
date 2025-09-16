# 🔨 Nueva tabla: event según el modelo relacional
# Registro de eventos del sistema con incremento automático en id
from datetime import datetime

events = [
    {
        "id": 1,
        "datetime": datetime(2025, 1, 15, 10, 30, 0),
        "description": "Dispositivo Luz del Salón encendido por automatización",
        "device_id": 1,  # Luz del Salón
        "user_email": "fernandomoyano21@gmail.com",
        "source": "automation",
    },
    {
        "id": 2,
        "datetime": datetime(2025, 1, 15, 11, 45, 0),
        "description": "Dispositivo Termostato Cocina apagado manualmente",
        "device_id": 2,  # Termostato Cocina
        "user_email": "fernandomoyano21@gmail.com",
        "source": "manual",
    },
    {
        "id": 3,
        "datetime": datetime(2025, 1, 15, 14, 20, 0),
        "description": "Dispositivo Ventilador Dormitorio encendido por usuario",
        "device_id": 3,  # Ventilador Dormitorio
        "user_email": "fernandomoyano21@gmail.com",
        "source": "user_action",
    },
]

# Contador para IDs incrementales
event_id_counter = len(events) + 1


def add_event(
    description: str, device_id: int, user_email: str, source: str = "system"
):
    """Agregar nuevo evento al sistema"""
    global event_id_counter
    new_event = {
        "id": event_id_counter,
        "datetime": datetime.now(),
        "description": description,
        "device_id": device_id,
        "user_email": user_email,
        "source": source,
    }
    events.append(new_event)
    event_id_counter += 1
    return new_event
