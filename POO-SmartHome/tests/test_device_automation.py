"""
Tests para la clase DeviceAutomation
Estos tests verifican la relación entre dispositivos y automatizaciones.
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "models"))

from models.device_automation import DeviceAutomation


class TestDeviceAutomation:
    """Tests para la clase DeviceAutomation"""

    def test_crear_device_automation_set_state(self):
        """Test: Crear relación dispositivo-automatización con acción 'set_state'"""
        device_automation = DeviceAutomation(1, 1, "set_state")

        assert device_automation.get_device_id() == 1
        assert device_automation.get_automation_id() == 1
        assert device_automation.get_action() == "set_state"

    def test_crear_device_automation_toggle(self):
        """Test: Crear relación con acción 'toggle'"""
        device_automation = DeviceAutomation(18, 5, "toggle")

        assert device_automation.get_device_id() == 18
        assert device_automation.get_automation_id() == 5
        assert device_automation.get_action() == "toggle"

    def test_automation_encender_luces_salon(self):
        """Test: Dispositivos para automatización 'Encender Luces Salón'"""
        # Automatización 1: Encender Luces Salón
        device_auto1 = DeviceAutomation(1, 1, "set_state")  # Luz Principal Sala
        device_auto2 = DeviceAutomation(4, 1, "set_state")  # Luz Cocina Principal

        assert device_auto1.get_automation_id() == 1
        assert device_auto2.get_automation_id() == 1
        assert device_auto1.get_action() == "set_state"
        assert device_auto2.get_action() == "set_state"

    def test_automation_apagar_todas_luces(self):
        """Test: Dispositivos para automatización 'Apagar Todas Luces'"""
        # Automatización 2: Apagar Todas Luces
        device_auto1 = DeviceAutomation(1, 2, "set_state")  # Luz Principal Sala
        device_auto2 = DeviceAutomation(4, 2, "set_state")  # Luz Cocina Principal
        device_auto3 = DeviceAutomation(5, 2, "set_state")  # Luz Bajo Muebles
        device_auto4 = DeviceAutomation(8, 2, "set_state")  # Luz Dormitorio

        # Todos pertenecen a la misma automatización
        assert device_auto1.get_automation_id() == 2
        assert device_auto2.get_automation_id() == 2
        assert device_auto3.get_automation_id() == 2
        assert device_auto4.get_automation_id() == 2

        # Todos usan la misma acción
        assert device_auto1.get_action() == "set_state"
        assert device_auto4.get_action() == "set_state"

    def test_automation_modo_nocturno(self):
        """Test: Dispositivos para automatización 'Modo Nocturno'"""
        # Automatización 3: Modo Nocturno
        device_auto1 = DeviceAutomation(1, 3, "set_state")  # Luz Principal Sala
        device_auto2 = DeviceAutomation(2, 3, "set_state")  # Termostato Central
        device_auto3 = DeviceAutomation(8, 3, "set_state")  # Luz Dormitorio

        assert device_auto1.get_automation_id() == 3
        assert device_auto2.get_automation_id() == 3
        assert device_auto3.get_automation_id() == 3

    def test_cambiar_action(self):
        """Test: Modificar la acción de un dispositivo en automatización"""
        # Arrange
        device_automation = DeviceAutomation(5, 2, "set_state")
        nueva_action = "toggle"

        # Act
        device_automation.set_action(nueva_action)

        # Assert
        assert device_automation.get_action() == "toggle"
        assert device_automation.get_device_id() == 5  # Device ID no cambia
        assert device_automation.get_automation_id() == 2  # Automation ID no cambia

    def test_diferentes_acciones(self):
        """Test: Verificar diferentes tipos de acciones"""
        device_auto1 = DeviceAutomation(10, 1, "set_state")
        device_auto2 = DeviceAutomation(15, 4, "toggle")
        device_auto3 = DeviceAutomation(20, 6, "activate")

        assert device_auto1.get_action() == "set_state"
        assert device_auto2.get_action() == "toggle"
        assert device_auto3.get_action() == "activate"

    def test_types_device_automation(self):
        """Test: Verificar tipos de datos correctos"""
        device_automation = DeviceAutomation(1, 1, "set_state")

        assert isinstance(device_automation.get_device_id(), int)
        assert isinstance(device_automation.get_automation_id(), int)
        assert isinstance(device_automation.get_action(), str)


# Tests simples
def test_device_automation_basico():
    """Test básico: Crear relación dispositivo-automatización"""
    device_auto = DeviceAutomation(1, 1, "set_state")
    assert device_auto.get_device_id() == 1
    assert device_auto.get_automation_id() == 1
    assert device_auto.get_action() == "set_state"


def test_accion_toggle():
    """Test: Acción toggle"""
    device_auto = DeviceAutomation(5, 2, "toggle")
    assert device_auto.get_action() == "toggle"


def test_cambiar_accion():
    """Test: Cambiar acción de dispositivo"""
    device_auto = DeviceAutomation(3, 1, "set_state")
    device_auto.set_action("toggle")
    assert device_auto.get_action() == "toggle"


def test_multiples_dispositivos_misma_automation():
    """Test: Múltiples dispositivos en la misma automatización"""
    device_auto1 = DeviceAutomation(1, 1, "set_state")
    device_auto2 = DeviceAutomation(2, 1, "set_state")
    device_auto3 = DeviceAutomation(3, 1, "toggle")

    # Todos pertenecen a la misma automatización
    assert device_auto1.get_automation_id() == 1
    assert device_auto2.get_automation_id() == 1
    assert device_auto3.get_automation_id() == 1

    # Pero pueden tener diferentes acciones
    assert device_auto1.get_action() == "set_state"
    assert device_auto3.get_action() == "toggle"


def test_mismo_dispositivo_multiples_automations():
    """Test: Un dispositivo puede estar en múltiples automatizaciones"""
    device_auto1 = DeviceAutomation(1, 1, "set_state")  # Luz en automatización 1
    device_auto2 = DeviceAutomation(1, 2, "set_state")  # Misma luz en automatización 2
    device_auto3 = DeviceAutomation(1, 3, "toggle")  # Misma luz en automatización 3

    # Mismo dispositivo
    assert device_auto1.get_device_id() == 1
    assert device_auto2.get_device_id() == 1
    assert device_auto3.get_device_id() == 1

    # Diferentes automatizaciones
    assert device_auto1.get_automation_id() == 1
    assert device_auto2.get_automation_id() == 2
    assert device_auto3.get_automation_id() == 3