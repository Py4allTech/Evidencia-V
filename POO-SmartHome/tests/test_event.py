"""
Tests para la clase Event
Estos tests verifican el funcionamiento del sistema de eventos.
"""

import sys
import os
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "models"))

from models.event import Event


class TestEvent:
    """Tests para la clase Event"""

    def test_crear_event_login(self):
        """Test: Crear evento de login"""
        fecha_hora = datetime(2025, 9, 15, 10, 30, 0)
        event = Event(
            1,
            fecha_hora,
            "Login Fernando",
            None,
            "fernandomoyano21@gmail.com",
            "user_action",
        )

        assert event.get_id() == 1
        assert event.get_datetime() == fecha_hora
        assert event.get_description() == "Login Fernando"
        assert event.get_device_id() is None
        assert event.get_user_email() == "fernandomoyano21@gmail.com"
        assert event.get_source() == "user_action"

    def test_crear_event_con_dispositivo(self):
        """Test: Crear evento que involucra un dispositivo"""
        fecha_hora = datetime(2025, 9, 15, 14, 15, 30)
        event = Event(
            2,
            fecha_hora,
            "Luz Sala cambió estado",
            1,
            "usuario@test.com",
            "user_action",
        )

        assert event.get_id() == 2
        assert event.get_description() == "Luz Sala cambió estado"
        assert event.get_device_id() == 1
        assert event.get_user_email() == "usuario@test.com"

    def test_crear_event_automatizacion(self):
        """Test: Crear evento de automatización"""
        fecha_hora = datetime.now()
        event = Event(
            3,
            fecha_hora,
            "Automatización ejecutada",
            None,
            "admin@test.com",
            "automation",
        )

        assert event.get_source() == "automation"
        assert (
            event.get_device_id() is None
        )  # Las automatizaciones pueden no tener dispositivo específico

    def test_crear_event_device_trigger(self):
        """Test: Crear evento disparado por dispositivo"""
        fecha_hora = datetime.now()
        event = Event(
            4, fecha_hora, "Sensor detectó movimiento", 10, None, "device_trigger"
        )

        assert event.get_source() == "device_trigger"
        assert event.get_device_id() == 10
        assert event.get_user_email() is None  # No hay usuario involucrado

    def test_crear_event_system_error(self):
        """Test: Crear evento de error del sistema"""
        fecha_hora = datetime.now()
        event = Event(5, fecha_hora, "Error de conexión", 22, None, "system_error")

        assert event.get_source() == "system_error"
        assert event.get_description() == "Error de conexión"

    def test_crear_event_con_source_por_defecto(self):
        """Test: Crear evento con source por defecto"""
        fecha_hora = datetime.now()
        event = Event(
            6, fecha_hora, "Evento test", 1, "user@test.com"
        )  # Sin especificar source

        assert event.get_source() == "manual"  # Valor por defecto

    def test_modificar_descripcion_event(self):
        """Test: Modificar la descripción del evento"""
        # Arrange
        fecha_hora = datetime.now()
        event = Event(
            7, fecha_hora, "Descripción original", 1, "user@test.com", "user_action"
        )
        nueva_descripcion = "Descripción modificada"

        # Act
        event.set_description(nueva_descripcion)

        # Assert
        assert event.get_description() == "Descripción modificada"
        assert event.get_id() == 7  # ID no cambia

    def test_event_con_datetime_especifico(self):
        """Test: Verificar que maneja fechas específicas correctamente"""
        fecha_especifica = datetime(2025, 12, 25, 9, 0, 0)  # Navidad 2025
        event = Event(
            8,
            fecha_especifica,
            "Evento navideño",
            None,
            "admin@test.com",
            "user_action",
        )

        assert event.get_datetime().year == 2025
        assert event.get_datetime().month == 12
        assert event.get_datetime().day == 25
        assert event.get_datetime().hour == 9

    def test_types_event(self):
        """Test: Verificar tipos de datos correctos"""
        fecha_hora = datetime.now()
        event = Event(9, fecha_hora, "Test", 1, "test@test.com", "user_action")

        assert isinstance(event.get_id(), int)
        assert isinstance(event.get_datetime(), datetime)
        assert isinstance(event.get_description(), str)
        assert isinstance(event.get_source(), str)
        # device_id y user_email pueden ser None, así que no verificamos tipo si son None


# Tests simples
def test_event_basico():
    """Test básico: Crear un evento"""
    fecha = datetime.now()
    event = Event(1, fecha, "Test event", None, "user@test.com", "user_action")
    assert event.get_description() == "Test event"


def test_event_sin_dispositivo():
    """Test: Evento sin dispositivo involucrado"""
    fecha = datetime.now()
    event = Event(2, fecha, "Login usuario", None, "user@test.com", "user_action")
    assert event.get_device_id() is None


def test_event_sin_usuario():
    """Test: Evento sin usuario (automático)"""
    fecha = datetime.now()
    event = Event(3, fecha, "Sensor activado", 5, None, "device_trigger")
    assert event.get_user_email() is None


def test_cambiar_descripcion():
    """Test: Modificar descripción de evento"""
    fecha = datetime.now()
    event = Event(4, fecha, "Original", 1, "user@test.com", "user_action")
    event.set_description("Modificada")
    assert event.get_description() == "Modificada"


def test_diferentes_sources():
    """Test: Verificar diferentes tipos de source"""
    fecha = datetime.now()

    event1 = Event(1, fecha, "Test 1", None, "user@test.com", "user_action")
    event2 = Event(2, fecha, "Test 2", None, None, "automation")
    event3 = Event(3, fecha, "Test 3", 5, None, "device_trigger")
    event4 = Event(4, fecha, "Test 4", 1, None, "system_error")

    assert event1.get_source() == "user_action"
    assert event2.get_source() == "automation"
    assert event3.get_source() == "device_trigger"
    assert event4.get_source() == "system_error"