# Código anterior: nombres inconsistentes con el modelo relacional
# types_of_roles = {"ADMIN": "Admin", "STANDAR": "standar"}
# roles con "nombre" en lugar de "name"

# 🔨 Nuevo código: coherente con el modelo relacional actualizado
# Tipos de roles
types_of_roles = {"ADMIN": "Admin", "STANDARD": "User"}

# Tabla role según el modelo relacional (campo 'name' no 'nombre')
roles = [
    {"id": 1, "name": types_of_roles["ADMIN"]},
    {"id": 2, "name": types_of_roles["STANDARD"]},
]
