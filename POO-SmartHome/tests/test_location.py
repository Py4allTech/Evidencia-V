"""
Tests para la clase Location
Estos tests verifican las ubicaciones dentro de los hogares.
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "models"))

from models.location import Location


class TestLocation:
    """Tests para la clase Location"""

    def test_crear_location_sala(self):
        """Test: Crear ubicación 'Sala de Estar'"""
        location = Location(1, "Sala de Estar")
        assert location.get_id() == 1
        assert location.get_name() == "Sala de Estar"

    def test_crear_location_cocina(self):
        """Test: Crear ubicación 'Cocina'"""
        location = Location(2, "Cocina")
        assert location.get_id() == 2
        assert location.get_name() == "Cocina"

    def test_crear_location_dormitorio(self):
        """Test: Crear ubicación 'Dormitorio Principal'"""
        location = Location(3, "Dormitorio Principal")
        assert location.get_id() == 3
        assert location.get_name() == "Dormitorio Principal"

    def test_modificar_nombre_location(self):
        """Test: Cambiar el nombre de una ubicación"""
        # Arrange
        location = Location(1, "Sala")
        nuevo_nombre = "Sala de Estar"

        # Act
        location.set_name(nuevo_nombre)

        # Assert
        assert location.get_name() == "Sala de Estar"
        assert location.get_id() == 1  # El ID permanece igual

    def test_location_con_espacios(self):
        """Test: Verificar que maneja nombres con espacios"""
        location = Location(5, "Baño Principal")
        assert location.get_name() == "Baño Principal"

    def test_types_location(self):
        """Test: Verificar tipos de datos"""
        location = Location(8, "Oficina")
        assert isinstance(location.get_id(), int)
        assert isinstance(location.get_name(), str)


# Tests simples
def test_location_simple():
    """Test básico: Crear una ubicación"""
    location = Location(1, "Jardín")
    assert location.get_name() == "Jardín"


def test_cambiar_nombre_location():
    """Test: Modificar nombre de ubicación"""
    location = Location(2, "Garaje")
    location.set_name("Cochera")
    assert location.get_name() == "Cochera"


def test_multiples_locations():
    """Test: Crear múltiples ubicaciones"""
    sala = Location(1, "Sala")
    cocina = Location(2, "Cocina")

    assert sala.get_name() == "Sala"
    assert cocina.get_name() == "Cocina"
    assert sala.get_id() != cocina.get_id()