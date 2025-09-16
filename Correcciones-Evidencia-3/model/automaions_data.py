# Código anterior: campos inconsistentes con modelo relacional
# usaba 'nombre', 'id_hogar', 'activa' en lugar de 'name', 'home_id', 'active'

# 🔨 Tabla automation coherente con el modelo relacional actualizado
automations = [
    {
        "id": 1,
        "name": "Encender luces del salón",  # Campo 'name' según modelo
        "description": "Automatización para encender las luces del salón principal",  # Campo description agregado
        "active": True,  # Campo 'active' según modelo
        "home_id": 1,  # Campo 'home_id' según modelo
    },
    {
        "id": 2,
        "name": "Apagar todas las luces",
        "description": "Automatización para apagar todas las luces de la casa",
        "active": True,
        "home_id": 1,
    },
    {
        "id": 3,
        "name": "Encender luz de dormitorio",
        "description": "Automatización para encender la luz del dormitorio principal",
        "active": True,
        "home_id": 1,
    },
]
