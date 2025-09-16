"""
Tests para la clase Automation
Estos tests verifican el funcionamiento de las automatizaciones del sistema.
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "models"))

from models.automation import Automation


class TestAutomation:
    """Tests para la clase Automation"""

    def test_crear_automation_luces_salon(self):
        """Test: Crear automatización 'Encender Luces Salón'"""
        automation = Automation(
            1, "Encender Luces Salón", "Enciende luces del salón", True, 1
        )

        assert automation.get_id() == 1
        assert automation.get_name() == "Encender Luces Salón"
        assert automation.get_description() == "Enciende luces del salón"
        assert automation.get_active()
        assert automation.get_home_id() == 1

    def test_crear_automation_modo_nocturno(self):
        """Test: Crear automatización 'Modo Nocturno'"""
        automation = Automation(3, "Modo Nocturno", "Configuración nocturna", True, 1)

        assert automation.get_id() == 3
        assert automation.get_name() == "Modo Nocturno"
        assert automation.get_description() == "Configuración nocturna"
        assert automation.get_active()

    def test_crear_automation_inactiva(self):
        """Test: Crear automatización inactiva"""
        automation = Automation(7, "Ventilación Auto", "Control automático", False, 1)

        assert automation.get_id() == 7
        assert automation.get_name() == "Ventilación Auto"
        assert not automation.get_active()

    def test_cambiar_nombre_automation(self):
        """Test: Modificar el nombre de la automatización"""
        # Arrange
        automation = Automation(1, "Luces", "Descripción", True, 1)
        nuevo_nombre = "Luces Inteligentes"

        # Act
        automation.set_name(nuevo_nombre)

        # Assert
        assert automation.get_name() == "Luces Inteligentes"
        assert automation.get_id() == 1  # ID no cambia

    def test_cambiar_descripcion_automation(self):
        """Test: Modificar la descripción de la automatización"""
        # Arrange
        automation = Automation(2, "Test", "Descripción original", True, 1)
        nueva_descripcion = "Nueva descripción detallada"

        # Act
        automation.set_description(nueva_descripcion)

        # Assert
        assert automation.get_description() == "Nueva descripción detallada"
        assert automation.get_name() == "Test"  # Nombre no cambia

    def test_activar_automation(self):
        """Test: Activar una automatización inactiva"""
        # Arrange
        automation = Automation(4, "Seguridad", "Modo seguridad", False, 2)

        # Act
        automation.set_active(True)

        # Assert
        assert automation.get_active()

    def test_desactivar_automation(self):
        """Test: Desactivar una automatización activa"""
        # Arrange
        automation = Automation(5, "Ahorro", "Ahorro energía", True, 3)

        # Act
        automation.set_active(False)

        # Assert
        assert not automation.get_active()

    def test_str_automation(self):
        """Test: Verificar el método __str__"""
        automation = Automation(1, "Test Auto", "Descripción test", True, 1)
        result = str(automation)

        # Verificar que contiene la información clave
        assert "Test Auto" in result
        assert "Descripción test" in result
        assert "True" in result
        assert "1" in result

    def test_types_automation(self):
        """Test: Verificar tipos de datos correctos"""
        automation = Automation(6, "Test", "Desc", False, 2)

        assert isinstance(automation.get_id(), int)
        assert isinstance(automation.get_name(), str)
        assert isinstance(automation.get_description(), str)
        assert isinstance(automation.get_active(), bool)
        assert isinstance(automation.get_home_id(), int)


# Tests simples
def test_automation_basica():
    """Test básico: Crear una automatización"""
    automation = Automation(1, "Test", "Descripción test", True, 1)
    assert automation.get_name() == "Test"


def test_automation_activa():
    """Test: Verificar automatización activa"""
    automation = Automation(2, "Activa", "Test", True, 1)
    assert automation.get_active()


def test_automation_inactiva():
    """Test: Verificar automatización inactiva"""
    automation = Automation(3, "Inactiva", "Test", False, 1)
    assert not automation.get_active()


def test_cambiar_estado_automation():
    """Test: Cambiar estado de activa a inactiva"""
    automation = Automation(4, "Cambio", "Test", True, 1)
    automation.set_active(False)
    assert not automation.get_active()


def test_automation_descripcion_larga():
    """Test: Automatización con descripción larga"""
    descripcion_larga = (
        "Esta es una automatización muy compleja que realiza múltiples acciones"
    )
    automation = Automation(5, "Compleja", descripcion_larga, True, 1)
    assert automation.get_description() == descripcion_larga