"""
Tests para la clase User
Estos tests verifican el funcionamiento de los usuarios del sistema.
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "models"))

from models.user import User


class TestUser:
    """Tests para la clase User"""

    def test_crear_user_administrador(self):
        """Test: Crear usuario administrador"""
        user = User("admin@smarthome.com", "password123", "Administrador", 1)

        assert user.get_email() == "admin@smarthome.com"
        assert user.get_name() == "Administrador"
        assert user.get_role_id() == 1

    def test_crear_user_normal(self):
        """Test: Crear usuario normal"""
        user = User("usuario@gmail.com", "secreto456", "Usuario Normal", 2)

        assert user.get_email() == "usuario@gmail.com"
        assert user.get_name() == "Usuario Normal"
        assert user.get_role_id() == 2

    def test_crear_user_visitante(self):
        """Test: Crear usuario visitante"""
        user = User("invitado@smarthome.com", "temp789", "Usuario Invitado", 3)

        assert user.get_email() == "invitado@smarthome.com"
        assert user.get_name() == "Usuario Invitado"
        assert user.get_role_id() == 3

    def test_cambiar_nombre_user(self):
        """Test: Modificar el nombre del usuario"""
        # Arrange
        user = User("test@test.com", "pass", "Nombre Original", 2)
        nuevo_nombre = "Nombre Modificado"

        # Act
        user.set_name(nuevo_nombre)

        # Assert
        assert user.get_name() == "Nombre Modificado"
        assert user.get_email() == "test@test.com"  # Email no cambia

    def test_cambiar_password_user(self):
        """Test: Cambiar la contraseña del usuario"""
        # Arrange
        user = User("user@test.com", "password_vieja", "Usuario", 2)
        nueva_password = "password_nueva"

        # Act
        user.set_password(nueva_password)

        # Assert
        assert user.get_name() == "Usuario"  # Otros datos no cambian

    def test_validar_credenciales_correctas(self):
        """Test: Validar credenciales correctas"""
        # Arrange
        email = "usuario@test.com"
        password = "mi_password"
        user = User(email, password, "Test User", 2)

        # Act & Assert
        assert user.validate_credentials(email, password)

    def test_validar_credenciales_incorrectas_email(self):
        """Test: Validar credenciales con email incorrecto"""
        user = User("correcto@test.com", "password123", "Usuario", 2)

        # Email incorrecto
        assert not user.validate_credentials("incorrecto@test.com", "password123")

    def test_validar_credenciales_incorrectas_password(self):
        """Test: Validar credenciales con password incorrecta"""
        user = User("usuario@test.com", "password_correcta", "Usuario", 2)

        # Password incorrecta
        assert not user.validate_credentials("usuario@test.com", "password_incorrecta")

    def test_types_user(self):
        """Test: Verificar tipos de datos correctos"""
        user = User("test@test.com", "pass", "Test", 1)

        assert isinstance(user.get_email(), str)
        assert isinstance(user.get_name(), str)
        assert isinstance(user.get_role_id(), int)


# Tests simples
def test_user_basico():
    """Test básico: Crear un usuario"""
    user = User("test@test.com", "123", "Test", 1)
    assert user.get_email() == "test@test.com"


def test_login_exitoso():
    """Test: Login exitoso"""
    user = User("fernando@gmail.com", "mi_clave", "Fernando", 1)
    assert user.validate_credentials("fernando@gmail.com", "mi_clave")


def test_login_fallido():
    """Test: Login fallido"""
    user = User("santiago@gmail.com", "clave_secreta", "Santiago", 2)
    assert not user.validate_credentials("santiago@gmail.com", "clave_incorrecta")


def test_cambio_nombre():
    """Test: Cambiar nombre de usuario"""
    user = User("maria@test.com", "pass", "María Original", 2)
    user.set_name("María Modificada")
    assert user.get_name() == "María Modificada"
