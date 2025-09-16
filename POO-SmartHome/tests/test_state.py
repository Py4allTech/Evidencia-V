"""
Tests para la clase State
Estos tests verifican el funcionamiento de los estados de dispositivos.
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "models"))

from models.state import State


class TestState:
    """Tests para la clase State"""

    def test_crear_state_encendido(self):
        """Test: Crear estado 'Encendido'"""
        # Arrange
        state_id = 1
        state_name = "Encendido"

        # Act
        state = State(state_id, state_name)

        # Assert
        assert state.get_id() == 1
        assert state.get_name() == "Encendido"

    def test_crear_state_apagado(self):
        """Test: Crear estado 'Apagado'"""
        state = State(2, "Apagado")
        assert state.get_id() == 2
        assert state.get_name() == "Apagado"

    def test_crear_state_mantenimiento(self):
        """Test: Crear estado 'En Mantenimiento'"""
        state = State(3, "En Mantenimiento")
        assert state.get_id() == 3
        assert state.get_name() == "En Mantenimiento"

    def test_crear_state_error(self):
        """Test: Crear estado 'Error'"""
        state = State(4, "Error")
        assert state.get_id() == 4
        assert state.get_name() == "Error"

    def test_modificar_nombre_state(self):
        """Test: Verificar que se puede cambiar el nombre del estado"""
        # Arrange
        state = State(1, "Encendido")
        nuevo_nombre = "Activo"

        # Act
        state.set_name(nuevo_nombre)

        # Assert
        assert state.get_name() == "Activo"
        assert state.get_id() == 1  # El ID no debe cambiar

    def test_types_state(self):
        """Test: Verificar tipos de datos correctos"""
        state = State(5, "Standby")
        assert isinstance(state.get_id(), int)
        assert isinstance(state.get_name(), str)


# Tests simples para principiantes
def test_state_basico():
    """Test básico: Crear un estado simple"""
    state = State(1, "Test")
    assert state.get_name() == "Test"


def test_cambiar_nombre_state():
    """Test: Cambiar nombre de un estado"""
    state = State(2, "Original")
    state.set_name("Modificado")
    assert state.get_name() == "Modificado"
