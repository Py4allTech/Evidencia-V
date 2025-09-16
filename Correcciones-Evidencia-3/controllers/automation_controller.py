from model.automaions_data import automations
from model.devices_data import devices
from utils.devices_utils import get_home_ids_by_email
from model.user_home_data import user_homes


def get_user_automations(email_user: str) -> list[dict]:
    """Obtiene automatizaciones del usuario"""
    user_home_ids = get_home_ids_by_email(email_user, user_homes)
    
    # Código anterior: usaba 'id_hogar'
    # 🟢 Actualizado para usar 'home_id' coherente con modelo relacional
    return [auto for auto in automations if auto['home_id'] in user_home_ids]

def execute_automation(automation_id: int, email_user: str) -> str:
    """Ejecuta una automatización"""
    user_automations = get_user_automations(email_user)
    automation = next((a for a in user_automations if a['id'] == automation_id), None)
    
    if not automation:
        # 🟢 Agregado prefijo para documentar historia del fuente
        return "[ACCESS-DENIED] No tienes acceso a esta automatización"
    
    if not automation['active']:
        # Código anterior: usaba 'activa'
        # 🟢 Actualizado para usar 'active' coherente con modelo relacional
        # 🟢 Agregado prefijo para documentar historia del fuente
        return "[AUTOMATION-DISABLED] Automatización desactivada"
    
    
    if automation_id == 1:  # Encender luces del salón
        # Buscar dispositivo "Luz del Salón" y encenderlo
        for device in devices:
            if device['name'] == 'Luz Principal Sala':
                device['state_id'] = 1  # Encendido
                # Código anterior: usaba 'nombre'
                # 🟢 Actualizado para usar 'name' coherente con modelo relacional
                # 🟢 Agregado prefijo para documentar historia del fuente
                return f"[AUTOMATION-SUCCESS] {automation['name']} ejecutada: Luz Principal Sala encendida"
    
    elif automation_id == 2:  # Apagar todas las luces
        # Buscar todas las luces y apagarlas
        lights_off = []
        for device in devices:
            if 'Luz' in device['name']:
                device['state_id'] = 2  # Apagado
                lights_off.append(device['name'])
        
        if lights_off:
            # Código anterior: usaba 'nombre'
            # 🟢 Actualizado para usar 'name' coherente con modelo relacional
            # 🟢 Agregado prefijo para documentar historia del fuente
            return f"[AUTOMATION-SUCCESS] {automation['name']} ejecutada: {', '.join(lights_off)} apagadas"
        else:
            return "[AUTOMATION-WARNING] No se encontraron luces para apagar"
            # 🟢 Agregado prefijo para documentar historia del fuente
    
    elif automation_id == 3:  # Encender luz de oficina
        for device in devices:
            if device['name'] == 'Luz Dormitorio':
                device['state_id'] = 1  # Encendido
                # Código anterior: usaba 'nombre'
                # 🟢 Actualizado para usar 'name' coherente con modelo relacional
                # 🟢 Agregado prefijo para documentar historia del fuente
                return f"[AUTOMATION-SUCCESS] {automation['name']} ejecutada: Luz Dormitorio encendida"
    
    # 🟢 Agregado prefijo para documentar historia del fuente
    return "[AUTOMATION-ERROR] Automatización no implementada"