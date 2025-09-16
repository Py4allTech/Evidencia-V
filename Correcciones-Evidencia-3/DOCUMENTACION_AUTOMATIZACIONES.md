#  DOCUMENTACIÓN DE AUTOMATIZACIONES SELECCIONADAS (EV2)
## Sistema de Automatización de Hogar - Proyecto ABP

## AUTOMATIZACIONES IMPLEMENTADAS
---


### 1. Encender luces del salón (ID: 1)
**Descripción**: Automatización para encender las luces del salón principal
**Hogar**: Casa Principal (ID: 1) 
**Estado**: Activa
**Funcionalidad**:
- Busca el dispositivo "Luz del Salón" en la base de datos
- Cambia su estado a "Encendido" (state_id = 1)
- Devuelve confirmación de ejecución exitosa
**Código asociado**: automation_controller.py - líneas 29-35

### 2. Apagar todas las luces (ID: 2)
**Descripción**: Automatización para apagar todas las luces de la casa
**Hogar**: Casa Principal (ID: 1)
**Estado**: Activa
**Funcionalidad**:
- Recorre todos los dispositivos en la base de datos
- Identifica dispositivos que contienen "Luz" en su nombre
- Cambia el estado de todas las luces a "Apagado" (state_id = 2)
- Devuelve lista de luces que fueron apagadas
**Código asociado**: automation_controller.py - líneas 37-49

### 3. Encender luz de oficina (ID: 3)
**Descripción**: Automatización para encender la luz de la oficina en casa de campo
**Hogar**: Casa de Campo (ID: 2)
**Estado**: Activa
**Funcionalidad**:
- Busca específicamente el dispositivo "Luz de la Oficina"
- Cambia su estado a "Encendido" (state_id = 1)
- Devuelve confirmación de ejecución exitosa
**Código asociado**: automation_controller.py - líneas 51-56

## ESTRUCTURA DE DATOS

### Tabla automation (model/automaions_data.py)
```python
{
    'id': int,               # Identificador único de la automatización
    'name': varchar,         # Nombre descriptivo
    'description': text,     # Descripción detallada de la funcionalidad
    'active': boolean,       # Estado activo/inactivo
    'home_id': int          # ID del hogar al que pertenece
}
```

### Tabla device_automation (model/device_automation_data.py)
```python
{
    'id': int,              # Identificador único
    'device_id': int,       # ID del dispositivo a controlar  
    'automation_id': int,   # ID de la automatización
    'action': varchar       # Acción a realizar (turn_on, turn_off, etc.)
}
```
