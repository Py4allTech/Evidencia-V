# 🔨 Nueva tabla: device_automation según el modelo relacional
# Relación entre devices y automations especificando qué acción realizar
device_automations = [
    {
        "id": 1,
        "device_id": 1,  # Luz del Salón
        "automation_id": 1,  # Encender luces del salón
        "action": "turn_on",
    },
    {
        "id": 2,
        "device_id": 1,  # Luz del Salón
        "automation_id": 2,  # Apagar todas las luces
        "action": "turn_off",
    },
    {
        "id": 3,
        "device_id": 2,  # Termostato Cocina
        "automation_id": 2,  # Apagar todas las luces
        "action": "turn_off",
    },
    {
        "id": 4,
        "device_id": 3,  # Ventilador Dormitorio
        "automation_id": 2,  # Apagar todas las luces
        "action": "turn_off",
    },
    # ELIMINADO: device_id=4 con automation_id=3 (referencia incorrecta)
    # device_id=4 está en home_id=1 pero automation_id=3 es para home_id=2
]
