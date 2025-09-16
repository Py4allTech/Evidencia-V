"""
Tests para la clase Device
Estos tests verifican el funcionamiento de los dispositivos inteligentes.
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "models"))

from models.device import Device


class TestDevice:
    """Tests para la clase Device"""

    def test_crear_device_luz_sala(self):
        """Test: Crear dispositivo 'Luz Principal Sala'"""
        device = Device(1, "Luz Principal Sala", 1, 1, 1, 1)

        assert device.get_id() == 1
        assert device.get_name() == "Luz Principal Sala"
        assert device.get_state_id() == 1
        assert device.get_device_type_id() == 1
        assert device.get_location_id() == 1
        assert device.get_home_id() == 1

    def test_crear_device_termostato(self):
        """Test: Crear dispositivo 'Termostato Central'"""
        device = Device(2, "Termostato Central", 2, 2, 1, 1)

        assert device.get_id() == 2
        assert device.get_name() == "Termostato Central"
        assert device.get_state_id() == 2  # Apagado
        assert device.get_device_type_id() == 2  # Termostato

    def test_cambiar_nombre_device(self):
        """Test: Modificar el nombre del dispositivo"""
        # Arrange
        device = Device(3, "Luz Cocina", 1, 1, 2, 1)
        nuevo_nombre = "Luz Principal Cocina"

        # Act
        device.set_name(nuevo_nombre)

        # Assert
        assert device.get_name() == "Luz Principal Cocina"
        assert device.get_id() == 3  # ID no cambia

    def test_cambiar_estado_device(self):
        """Test: Cambiar el estado del dispositivo"""
        # Arrange
        device = Device(4, "Ventilador", 2, 3, 1, 1)  # Estado 2 = Apagado
        nuevo_estado = 1  # Estado 1 = Encendido

        # Act
        device.set_state_id(nuevo_estado)

        # Assert
        assert device.get_state_id() == 1
        assert device.get_name() == "Ventilador"  # Nombre no cambia

    def test_buscar_device_por_nombre_encontrado(self):
        """Test: Buscar dispositivo por nombre - caso exitoso"""
        # Arrange
        device = Device(5, "Cámara Entrada Principal", 1, 5, 1, 1)

        # Act & Assert
        assert device.search_device_by_name("Cámara")
        assert device.search_device_by_name("Entrada")
        assert device.search_device_by_name("Principal")

    def test_buscar_device_por_nombre_no_encontrado(self):
        """Test: Buscar dispositivo por nombre - caso no encontrado"""
        # Arrange
        device = Device(6, "Luz Dormitorio", 2, 1, 3, 1)

        # Act & Assert
        assert not device.search_device_by_name("Cocina")
        assert not device.search_device_by_name("Garaje")

    def test_buscar_device_case_insensitive(self):
        """Test: Búsqueda insensible a mayúsculas/minúsculas"""
        # Arrange
        device = Device(7, "Sensor Movimiento", 1, 6, 3, 1)

        # Act & Assert
        assert device.search_device_by_name("sensor")
        assert device.search_device_by_name("MOVIMIENTO")
        assert device.search_device_by_name("SeNsOr")

    def test_buscar_device_string_vacio(self):
        """Test: Búsqueda con string vacío"""
        device = Device(8, "Cerradura Principal", 1, 4, 1, 1)

        assert not device.search_device_by_name("")
        assert not device.search_device_by_name("   ")  # Solo espacios

    def test_types_device(self):
        """Test: Verificar tipos de datos correctos"""
        device = Device(9, "Test Device", 1, 1, 1, 1)

        assert isinstance(device.get_id(), int)
        assert isinstance(device.get_name(), str)
        assert isinstance(device.get_state_id(), int)
        assert isinstance(device.get_device_type_id(), int)
        assert isinstance(device.get_location_id(), int)
        assert isinstance(device.get_home_id(), int)


# Tests simples
def test_device_basico():
    """Test básico: Crear un dispositivo"""
    device = Device(1, "Test Device", 1, 1, 1, 1)
    assert device.get_name() == "Test Device"


def test_encender_dispositivo():
    """Test: Simular encender un dispositivo (cambiar a estado 1)"""
    device = Device(2, "Luz Test", 2, 1, 1, 1)  # Empieza apagado (estado 2)
    device.set_state_id(1)  # Encender (estado 1)
    assert device.get_state_id() == 1


def test_buscar_nombre_parcial():
    """Test: Buscar por nombre parcial"""
    device = Device(3, "Luz Inteligente Sala", 1, 1, 1, 1)
    assert device.search_device_by_name("Inteligente")


def test_cambiar_ubicacion():
    """Test: Simular mover dispositivo a otra ubicación"""
    device = Device(4, "Ventilador Portátil", 1, 3, 1, 1)  # Empieza en ubicación 1
    device.set_state_id(
        1
    )  # Solo podemos cambiar el estado, no la ubicación directamente
    # Nota: En un sistema real, mover ubicación requeriría otro método
    assert device.get_location_id() == 1  # Verificar que mantiene la ubicación original