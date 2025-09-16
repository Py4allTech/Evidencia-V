"""
Tests para la clase UserHome
Estos tests verifican la relación entre usuarios y hogares.
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "models"))

from models.user_home import UserHome


class TestUserHome:
    """Tests para la clase User_home"""

    def test_crear_user_home_basico(self):
        """Test: Crear relación básica usuario-hogar"""
        user_home = UserHome("fernandomoyano21@gmail.com", 1)

        assert user_home.get_user_email() == "fernandomoyano21@gmail.com"
        assert user_home.get_home_id() == 1

    def test_crear_user_home_santiago(self):
        """Test: Crear relación para Santiago"""
        user_home = UserHome("santiagoortega@gmail.com", 2)

        assert user_home.get_user_email() == "santiagoortega@gmail.com"
        assert user_home.get_home_id() == 2

    def test_crear_user_home_rafael(self):
        """Test: Crear relación para Rafael"""
        user_home = UserHome("rafaelperazzolo@gmail.com", 3)

        assert user_home.get_user_email() == "rafaelperazzolo@gmail.com"
        assert user_home.get_home_id() == 3

    def test_usuario_multiples_hogares(self):
        """Test: Un usuario puede tener acceso a múltiples hogares"""
        # Fernando tiene acceso a Casa Principal (1) y Casa de Campo (2)
        user_home1 = UserHome("fernandomoyano21@gmail.com", 1)
        user_home2 = UserHome("fernandomoyano21@gmail.com", 2)

        assert user_home1.get_user_email() == user_home2.get_user_email()
        assert user_home1.get_home_id() != user_home2.get_home_id()
        assert user_home1.get_home_id() == 1
        assert user_home2.get_home_id() == 2

    def test_multiples_usuarios_mismo_hogar(self):
        """Test: Múltiples usuarios pueden tener acceso al mismo hogar"""
        # Casa Principal (1) tiene varios usuarios
        user_home1 = UserHome("fernandomoyano21@gmail.com", 1)
        user_home2 = UserHome("maria.garcia@ejemplo.com", 1)
        user_home3 = UserHome("invitado@smarthome.com", 1)

        assert user_home1.get_home_id() == 1
        assert user_home2.get_home_id() == 1
        assert user_home3.get_home_id() == 1

        # Pero diferentes usuarios
        assert user_home1.get_user_email() != user_home2.get_user_email()
        assert user_home2.get_user_email() != user_home3.get_user_email()

    def test_types_user_home(self):
        """Test: Verificar tipos de datos correctos"""
        user_home = UserHome("test@test.com", 1)

        assert isinstance(user_home.get_user_email(), str)
        assert isinstance(user_home.get_home_id(), int)

    def test_email_con_caracteres_especiales(self):
        """Test: Verificar que maneja emails con caracteres especiales"""
        user_home = UserHome("maría.josé@ejemplo.com", 1)
        assert user_home.get_user_email() == "maría.josé@ejemplo.com"

    def test_diferentes_dominios_email(self):
        """Test: Verificar que maneja diferentes dominios de email"""
        user_home1 = UserHome("usuario@gmail.com", 1)
        user_home2 = UserHome("usuario@hotmail.com", 1)
        user_home3 = UserHome("usuario@empresa.com.ar", 1)

        assert user_home1.get_user_email() == "usuario@gmail.com"
        assert user_home2.get_user_email() == "usuario@hotmail.com"
        assert user_home3.get_user_email() == "usuario@empresa.com.ar"


# Tests simples
def test_user_home_simple():
    """Test básico: Crear relación usuario-hogar"""
    user_home = UserHome("test@test.com", 1)
    assert user_home.get_user_email() == "test@test.com"
    assert user_home.get_home_id() == 1


def test_acceso_casa_principal():
    """Test: Usuario con acceso a Casa Principal"""
    user_home = UserHome("usuario@test.com", 1)  # 1 = Casa Principal
    assert user_home.get_home_id() == 1


def test_acceso_casa_campo():
    """Test: Usuario con acceso a Casa de Campo"""
    user_home = UserHome("usuario@test.com", 2)  # 2 = Casa de Campo
    assert user_home.get_home_id() == 2


def test_acceso_departamento():
    """Test: Usuario con acceso a Departamento"""
    user_home = UserHome("usuario@test.com", 3)  # 3 = Departamento
    assert user_home.get_home_id() == 3


def test_usuario_admin_multiple_acceso():
    """Test: Administrador con acceso a múltiples propiedades"""
    admin_casa1 = UserHome("admin@smarthome.com", 1)
    admin_casa2 = UserHome("admin@smarthome.com", 2)
    admin_depto = UserHome("admin@smarthome.com", 3)

    # Mismo usuario
    assert admin_casa1.get_user_email() == "admin@smarthome.com"
    assert admin_casa2.get_user_email() == "admin@smarthome.com"
    assert admin_depto.get_user_email() == "admin@smarthome.com"

    # Diferentes propiedades
    assert admin_casa1.get_home_id() == 1
    assert admin_casa2.get_home_id() == 2
    assert admin_depto.get_home_id() == 3
