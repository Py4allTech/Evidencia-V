"""
Tests para la clase Home
Estos tests verifican el funcionamiento de los hogares en el sistema.
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "models"))

from models.home import Home


class TestHome:
    """Tests para la clase Home"""

    def test_crear_home_casa_principal(self):
        """Test: Crear 'Casa Principal'"""
        home = Home(1, "Casa Principal")

        assert home.get_id() == 1
        assert home.get_name() == "Casa Principal"

    def test_crear_home_casa_campo(self):
        """Test: Crear 'Casa de Campo'"""
        home = Home(2, "Casa de Campo")

        assert home.get_id() == 2
        assert home.get_name() == "Casa de Campo"

    def test_crear_home_departamento(self):
        """Test: Crear 'Departamento'"""
        home = Home(3, "Departamento")

        assert home.get_id() == 3
        assert home.get_name() == "Departamento"

    def test_modificar_nombre_home(self):
        """Test: Cambiar el nombre del hogar"""
        # Arrange
        home = Home(1, "Casa")
        nuevo_nombre = "Casa Renovada"

        # Act
        home.set_name(nuevo_nombre)

        # Assert
        assert home.get_name() == "Casa Renovada"
        assert home.get_id() == 1  # El ID no cambia

    def test_home_con_nombre_largo(self):
        """Test: Verificar que maneja nombres largos"""
        nombre_largo = "Casa de Vacaciones en la Montaña"
        home = Home(4, nombre_largo)

        assert home.get_name() == nombre_largo

    def test_types_home(self):
        """Test: Verificar tipos de datos correctos"""
        home = Home(5, "Oficina")

        assert isinstance(home.get_id(), int)
        assert isinstance(home.get_name(), str)


# Tests simples
def test_home_simple():
    """Test básico: Crear un hogar"""
    home = Home(1, "Mi Casa")
    assert home.get_name() == "Mi Casa"


def test_cambiar_nombre_home():
    """Test: Modificar nombre del hogar"""
    home = Home(2, "Casa Vieja")
    home.set_name("Casa Nueva")
    assert home.get_name() == "Casa Nueva"


def test_multiples_homes():
    """Test: Crear múltiples hogares"""
    casa1 = Home(1, "Casa 1")
    casa2 = Home(2, "Casa 2")

    assert casa1.get_name() == "Casa 1"
    assert casa2.get_name() == "Casa 2"
    assert casa1.get_id() != casa2.get_id()


def test_home_con_caracteres_especiales():
    """Test: Hogar con caracteres especiales"""
    home = Home(3, "Casa de María & José")
    assert home.get_name() == "Casa de María & José"