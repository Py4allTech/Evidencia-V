# Dispositivos corregidos para coincidir con la base de datos
# ✅ CORREGIDO: Nomenclatura de campos actualizada para coincidir con esquema BD
devices = [
    {
        'id': 1,
        'name': 'Luz Principal Sala',
        'state_id': 1,        # Encendido (corregido de 'id_state')
        'device_type_id': 1,  # Luz Inteligente (corregido de 'id_type')
        'location_id': 1,     # Sala de Estar (corregido de 'id_location')
        'home_id': 1          # Casa Principal (corregido de 'id_home')
    },
    {
        'id': 2,
        'name': 'Termostato Central',
        'state_id': 2,        # Apagado
        'device_type_id': 2,  # Termostato
        'location_id': 1,     # Sala de Estar
        'home_id': 1          # Casa Principal
    },
    {
        'id': 3,
        'name': 'Ventilador Techo Sala',
        'state_id': 1,        # Encendido
        'device_type_id': 3,  # Ventilador
        'location_id': 1,     # Sala de Estar
        'home_id': 1          # Casa Principal
    },
    {
        'id': 4,
        'name': 'Luz Cocina Principal',
        'state_id': 1,        # Encendido
        'device_type_id': 1,  # Luz Inteligente
        'location_id': 2,     # Cocina
        'home_id': 1          # Casa Principal
    },
    {
        'id': 5,
        'name': 'Luz Bajo Muebles',
        'state_id': 2,        # Apagado
        'device_type_id': 1,  # Luz Inteligente
        'location_id': 2,     # Cocina
        'home_id': 1          # Casa Principal
    },
    {
        'id': 6,
        'name': 'Cerradura Principal',
        'state_id': 1,        # Encendido (Activa)
        'device_type_id': 4,  # Cerradura Inteligente
        'location_id': 1,     # Sala de Estar
        'home_id': 1          # Casa Principal
    },
    {
        'id': 7,
        'name': 'Cámara Entrada',
        'state_id': 1,        # Encendido (Activa)
        'device_type_id': 5,  # Cámara de Seguridad
        'location_id': 1,     # Sala de Estar
        'home_id': 1          # Casa Principal
    },
    {
        'id': 8,
        'name': 'Luz Dormitorio',
        'state_id': 2,        # Apagado
        'device_type_id': 1,  # Luz Inteligente
        'location_id': 3,     # Dormitorio Principal
        'home_id': 1          # Casa Principal
    }
]
