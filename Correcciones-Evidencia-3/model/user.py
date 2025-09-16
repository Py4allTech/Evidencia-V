from model.rol import roles
from typing import Dict, Optional

# Código anterior: estructura inconsistente con el modelo relacional
# usado "id_rol" en lugar de "role_id"

# 🔨 Usuario ADMIN almacenado en la tabla user (coherente con modelo relacional)
# ✅ CORREGIDO: Agregados usuarios faltantes referenciados en user_home_data.py
users = [
    {
        "email": "fernandomoyano21@gmail.com",
        "password": "admin123",
        "name": "Fernando",
        "role_id": 1,  # Admin
    },
    {
        "email": "santiagoortega@gmail.com",
        "password": "user123",
        "name": "Santiago Ortega",
        "role_id": 2,  # User
    },
    {
        "email": "rafaelperazzolo@gmail.com",
        "password": "user123",
        "name": "Rafael Perazzolo",
        "role_id": 2,  # User
    },
    {
        "email": "maria.garcia@ejemplo.com",
        "password": "user123",
        "name": "Maria Garcia",
        "role_id": 2,  # User
    },
    {
        "email": "invitado@smarthome.com",
        "password": "guest123",
        "name": "Usuario Invitado",
        "role_id": 2,  # User
    }
]


def isExist(email) -> bool:
    """Funcion que valida si el usuario ya existe"""
    for user in users:
        if user["email"] == email:
            return True
    return False


def check_username(username):
    """Funcion que valida si el username coincide"""
    for user in users:
        if user["name"] == username:
            return True
    return False


def check_email(email):
    """Funcion que valida si el email coincide"""
    for user in users:
        if user["email"] == email:
            return True
    return False


def check_password(password):
    """Funcion que valida si la contraseña coincide"""
    for user in users:
        if user["password"] == password:
            return True
    return False


def get_user_by_email(email: str) -> Optional[Dict]:
    """Obtener usuario completo por email"""
    for user in users:
        if user["email"] == email:
            # Código anterior: retornaba "id_rol"
            # 🔨 se retorna una copia del usuario sin la contraseña por seguridad
            return {
                "email": user["email"],
                "name": user["name"],
                "role_id": user["role_id"],  # Campo actualizado según modelo relacional
            }
    return None


def validate_login(email: str, password: str) -> bool:
    """Validar login completo (email Y contraseña del mismo usuario)"""
    for user in users:
        if user["email"] == email and user["password"] == password:
            return True
    return False


def save(user: Dict):
    """guardar un usuario en la base de datos"""
    # Código anterior: usaba "id_rol" inconsistente con modelo relacional
    # 🔨 Nuevo código: coherente con tabla 'user' del modelo relacional
    # ✅ CORREGIDO: Uso de ID directo en lugar de referencia dinámica
    user_to_save = {
        "email": user["email"],
        "password": user["password"],
        "name": user["username"],
        "role_id": 2,  # Role User por defecto (ID directo)
    }
    users.append(user_to_save)
