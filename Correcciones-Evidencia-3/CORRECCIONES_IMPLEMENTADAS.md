#  DOCUMENTACIÓN DE CORRECCIONES IMPLEMENTADAS
## Sistema de Automatización de Hogar - ABP Programador

 
**Desarrolladores**: Fernando Moyano, Santiago Ortega, Rafael Perazzolo 

---

##  RESUMEN

Este documento detalla todas las correcciones implementadas en el proyecto ABP Programador en respuesta a las observaciones realizadas por los profesores. Se han corregido 4 puntos principales y se han implementado múltiples mejoras técnicas adicionales.



##  CORRECCIÓN 1: FORMATO DE INPUTS MEJORADO
---

###  Problema identificado:
> "Luego de los input, dejar un espacio o escribir dos puntos (para una mejor lectura)"

###  Solución implementada:

**Archivo modificado**: `utils/helpers.py`

```python
# Código anterior: sin formato apropiado
def get_user_input(message: str) -> str:
    return input(message).strip()

# 🔨 Nuevo código: agregamos ': ' automáticamente para mejor legibilidad
def get_user_input(message: str) -> str:
    if not message.endswith(': ') and not message.endswith(':'):
        message += ': '
    return input(message).strip()
```


---

##  CORRECCIÓN 2: DOCUMENTACIÓN DE AUTOMATIZACIONES (EV2)
---

###  Problema identificado:
> "Falta Doc. sobre las automatizaciones seleccionadas (EV2)"

###  Solución implementada:

**Archivo creado**: `DOCUMENTACION_AUTOMATIZACIONES.md`

#### Contenido de la documentación:

1. **Automatizaciones implementadas (3 total)**:
   - Encender luces del salón (ID: 1)
   - Apagar todas las luces (ID: 2)  
   - Encender luz de oficina (ID: 3)

2. **Estructura de datos detallada**:
   ```python
   automation = {
       'id': int,               # Identificador único
       'name': varchar,         # Nombre descriptivo
       'description': text,     # Descripción detallada
       'active': boolean,       # Estado activo/inactivo
       'home_id': int          # ID del hogar
   }
   ```

3. **Flujo de ejecución completo**:
   - Autorización de usuario
   - Validación de estado
   - Ejecución de lógica
   - Actualización de dispositivos
   - Confirmación al usuario

4. **Consideraciones de seguridad**:
   - Control de acceso por hogar
   - Separación de roles
   - Trazabilidad de acciones

---

##  CORRECCIÓN 3: COHERENCIA CON MODELO RELACIONAL
---


###  Problema identificado:
> "Revisar coherencia con el modelo relacional"

###  Solución implementada:

####  **3.1 Actualización de campos en tablas existentes**

**Tabla `role`** - Archivo: `model/rol.py`
```python
# Código anterior: inconsistente con modelo relacional
roles = [
    {"id": 1, "nombre": types_of_roles["ADMIN"]},
    {"id": 2, "nombre": types_of_roles["STANDAR"]},
]

# 🔨 Nuevo código: coherente con modelo relacional
roles = [
    {"id": 1, "name": types_of_roles["ADMIN"]},
    {"id": 2, "name": types_of_roles["STANDARD"]},
]
```

**Tabla `user`** - Archivo: `model/user.py`
```python
# Código anterior: campo inconsistente
"id_rol": roles[0]["id"]

# 🔨 Nuevo código: campo según modelo relacional
"role_id": roles[0]["id"]
```

**Tabla `automation`** - Archivo: `model/automaions_data.py`
```python
# Código anterior: campos inconsistentes
{
    'nombre': 'Encender luces del salón',
    'id_hogar': 1,
    'activa': True
}

# 🔨 Nuevo código: coherente con modelo relacional
{
    'name': 'Encender luces del salón',
    'description': 'Automatización para encender las luces del salón principal',
    'active': True,
    'home_id': 1,
}
```



**Archivos corregidos para coincidir con BD**:

**`model/locations_data.py`** - Ubicaciones expandidas
```python
# Código anterior: solo 4 ubicaciones básicas
locations = [
    {'id': 1, 'name': 'Sala'},
    {'id': 2, 'name': 'Cocina'},
    {'id': 3, 'name': 'Dormitorio'},
    {'id': 4, 'name': 'Baño'}
]

# 🔨 Código corregido: 8 ubicaciones exactas de la BD
locations = [
    {'id': 1, 'name': 'Sala de Estar'},
    {'id': 2, 'name': 'Cocina'},
    {'id': 3, 'name': 'Dormitorio Principal'},
    {'id': 4, 'name': 'Dormitorio Secundario'},
    {'id': 5, 'name': 'Baño'},
    {'id': 6, 'name': 'Garaje'},
    {'id': 7, 'name': 'Jardín'},
    {'id': 8, 'name': 'Oficina'}
]
```

**`model/types_data.py`** - Tipos de dispositivos actualizados
```python
# Código anterior: tipos no coincidían con BD
{"id": 1, "name": "Luz", "characteristic": "..."}
{"id": 4, "name": "Cámara", "characteristic": "..."}
{"id": 5, "name": "Electrodoméstico", "characteristic": "..."}

# 🔨 Código corregido: tipos exactos de la BD
{"id": 1, "name": "Luz Inteligente", "characteristic": "Iluminación LED controlable"}
{"id": 4, "name": "Cerradura Inteligente", "characteristic": "Control de acceso"}
{"id": 5, "name": "Cámara de Seguridad", "characteristic": "Vigilancia remota"}
{"id": 6, "name": "Sensor de Movimiento", "characteristic": "Detección de presencia"}
```

**`model/homes_data.py`** - Hogares corregidos
```python
# Código anterior: hogares inconsistentes
{"id": 3, "name": "Apartamento"}
{"id": 4, "name": "Oficina"}

# 🔨 Código corregido: hogares exactos de la BD
{"id": 3, "name": "Departamento"}
# Eliminado: "Oficina" (no existe en BD)
```

**`model/states_data.py`** - Estados expandidos
```python
# Código anterior: solo 2 estados básicos
states = [
    {'id': 1, 'name': 'Encendido'},
    {'id': 2, 'name': 'Apagado'}
]

# 🔨 Código corregido: 6 estados completos de la BD
states = [
    {'id': 1, 'name': 'Encendido'},
    {'id': 2, 'name': 'Apagado'},
    {'id': 3, 'name': 'En Mantenimiento'},
    {'id': 4, 'name': 'Error'},
    {'id': 5, 'name': 'Standby'},
    {'id': 6, 'name': 'Configurando'}
]
```

**`model/devices_data.py`** - Dispositivos actualizados
```python
# Código anterior: nombres y relaciones incorrectas
{'id': 1, 'name': 'Luz del Salón', 'id_location': 1}  # "Sala"
{'id': 4, 'name': 'Luz de la Oficina', 'id_home': 2}  # Inconsistente

# 🔨 Código corregido: nombres exactos de la BD
devices = [
    {
        "id": 1,
        "name": "Luz Principal Sala",
        "state_id": 1,  # Encendido (corregido de 'id_state')
        "device_type_id": 1,  # Luz Inteligente (corregido de 'id_type')
        "location_id": 1,  # Sala de Estar (corregido de 'id_location')
        "home_id": 1,  # Casa Principal (corregido de 'id_home')
    },
    {
        "id": 2,
        "name": "Termostato Central",
        "state_id": 2,  # Apagado
        "device_type_id": 2,  # Termostato
        "location_id": 1,  # Sala de Estar
        "home_id": 1,  # Casa Principal
    },
    {
        "id": 3,
        "name": "Ventilador Techo Sala",
        "state_id": 1,  # Encendido
        "device_type_id": 3,  # Ventilador
        "location_id": 1,  # Sala de Estar
        "home_id": 1,  # Casa Principal
    },
    {
        "id": 4,
        "name": "Luz Cocina Principal",
        "state_id": 1,  # Encendido
        "device_type_id": 1,  # Luz Inteligente
        "location_id": 2,  # Cocina
        "home_id": 1,  # Casa Principal
    },
    {
        "id": 5,
        "name": "Luz Bajo Muebles",
        "state_id": 2,  # Apagado
        "device_type_id": 1,  # Luz Inteligente
        "location_id": 2,  # Cocina
        "home_id": 1,  # Casa Principal
    },
    {
        "id": 6,
        "name": "Cerradura Principal",
        "state_id": 1,  # Encendido (Activa)
        "device_type_id": 4,  # Cerradura Inteligente
        "location_id": 1,  # Sala de Estar
        "home_id": 1,  # Casa Principal
    },
    {
        "id": 7,
        "name": "Cámara Entrada",
        "state_id": 1,  # Encendido (Activa)
        "device_type_id": 5,  # Cámara de Seguridad
        "location_id": 1,  # Sala de Estar
        "home_id": 1,  # Casa Principal
    },
    {
        "id": 8,
        "name": "Luz Dormitorio",
        "state_id": 2,  # Apagado
        "device_type_id": 1,  # Luz Inteligente
        "location_id": 3,  # Dormitorio Principal
        "home_id": 1,  # Casa Principal
    },
]
```

**`model/home.py`** - Archivo utilizado por main.py
```python
# Código anterior: faltaba "Departamento"
homes = [
    {"id": 1, "name": "Casa Principal"},
    {"id": 2, "name": "Casa de Campo"}
]

# 🔨 Código corregido: completo según BD
homes = [
    {"id": 1, "name": "Casa Principal"},
    {"id": 2, "name": "Casa de Campo"},
    {"id": 3, "name": "Departamento"}
]
```

**`model/usersxhomes_data.py`** - Relaciones usuario-hogar actualizadas
```python
# Código anterior: referencias incorrectas y usuarios faltantes
userxhome = [
    {"email": "fernandomoyano21@gmail.com", "home_id": 1},
    {"email": "santiagoortega@gmail.com", "home_id": 2},
    {"email": "rafaelperazzolo@gmail.com", "home_id": 3}  # "Apartamento"
]

# 🔨 Código corregido: relaciones exactas de la BD
user_homes = [
    {
        "user_email": "fernandomoyano21@gmail.com",
        "home_id": 1,  # Casa Principal
    },
    {
        "user_email": "fernandomoyano21@gmail.com",
        "home_id": 2,  # Casa de Campo
    },
    {
        "user_email": "santiagoortega@gmail.com",
        "home_id": 2,  # Casa de Campo
    },
    {
        "user_email": "rafaelperazzolo@gmail.com",
        "home_id": 3,  # Departamento
    },
    {
        "user_email": "maria.garcia@ejemplo.com",
        "home_id": 1,  # Casa Principal
    },
    {
        "user_email": "invitado@smarthome.com",
        "home_id": 1,  # Casa Principal
    },
]
```


**Archivos modificados en esta corrección:**

1. `model/usersxhomes_data.py` - Deprecado
2. `model/device_automation_data.py` - Referencias corregidas
3. `model/types_data.py` - Nomenclatura corregida
4. `model/user.py` - Usuarios agregados + funcion save() corregida
5. `model/user_home_data.py` - Estructura y datos actualizados
6. `model/devices_data.py` - Nomenclatura de campos corregida
7. `main.py` - Importaciones y referencias actualizadas
8. `controllers/automation_controller.py` - Campos y nombres de dispositivos corregidos
9. `controllers/devices_controller.py` - Campos, importaciones y referencias actualizadas
10. `utils/devices_utils.py` - Nomenclatura de campos y parametros corregidos
11. `model/automaions_data.py` - Automatizacion 3 actualizada

#### **3.3 CORRECCIONES DE FUNCIONALIDAD**

**PROBLEMA DETECTADO**: Al ejecutar `python main.py` despues de las correcciones de consistencia, se presentaron errores de importacion y referencias que impedian el funcionamiento del programa.

**Error inicial:**
```
ImportError: cannot import name 'types_device' from 'model.types_data'
```

**CORRECCIONES APLICADAS PARA RESTAURAR FUNCIONALIDAD**

**1. Actualizacion de Importaciones en main.py**
```python
# ANTES (causaba error):
from model.types_data import types_device

# CORREGIDO:
from model.types_data import device_types
```

**2. Correccion de Referencias en main.py (4 referencias)**
```python
# ANTES:
selected_type = request_and_validate_element("Tipo de dispositivo: ", types_device, "name")
results = get_user_devices(email_user, states, types_device, locations, homes)
results = search_device_by_name(email_user, name, states, types_device, locations, homes)

# CORREGIDO:
selected_type = request_and_validate_element("Tipo de dispositivo: ", device_types, "name")
results = get_user_devices(email_user, states, device_types, locations, homes)
results = search_device_by_name(email_user, name, states, device_types, locations, homes)
```

**3. Correcciones Completas en controllers/automation_controller.py**

*Importaciones:*
```python
# ANTES (archivo deprecado):
from model.usersxhomes_data import userxhome

# CORREGIDO:
from model.user_home_data import user_homes
```

*Referencias de variables:*
```python
# ANTES:
user_home_ids = get_home_ids_by_email(email_user, userxhome)

# CORREGIDO:
user_home_ids = get_home_ids_by_email(email_user, user_homes)
```

*Campos de dispositivos (3 referencias):*
```python
# ANTES:
device['id_state'] = 1  # Encendido

# CORREGIDO:
device['state_id'] = 1  # Encendido
```

*Nombres de dispositivos:*
```python
# ANTES (dispositivos inexistentes):
if device['name'] == 'Luz del Salon':
if device['name'] == 'Luz de la Oficina':

# CORREGIDO (dispositivos existentes):
if device['name'] == 'Luz Principal Sala':
if device['name'] == 'Luz Dormitorio':
```

**4. Correcciones Masivas en controllers/devices_controller.py**

*Importaciones:*
```python
# ANTES:
from model.usersxhomes_data import userxhome

# CORREGIDO:
from model.user_home_data import user_homes
```

*Referencias de variables (6 referencias):*
```python
# ANTES:
if not is_user_authorized_for_home(email_user, home_id, userxhome):
home_ids = get_home_ids_by_email(email_user, userxhome)

# CORREGIDO:
if not is_user_authorized_for_home(email_user, home_id, user_homes):
home_ids = get_home_ids_by_email(email_user, user_homes)
```

*Campos de dispositivos:*
```python
# ANTES:
device = {
    'id': device_id,
    'name': name,
    'id_state': selected_state['id'],
    'id_type': selected_type['id'],
    'id_location': selected_location['id'],
    'id_home': home_id
}

# CORREGIDO:
device = {
    'id': device_id,
    'name': name,
    'state_id': selected_state['id'],
    'device_type_id': selected_type['id'],
    'location_id': selected_location['id'],
    'home_id': home_id
}
```

*Parametros de funciones (4 referencias):*
```python
# ANTES:
def get_user_devices(email_user: str, states: dict, types_device: dict, locations: dict, homes: dict):
def search_device_by_name(email_user: str, device_name: str, states: dict, types_device: dict, locations: dict, homes: dict):

# CORREGIDO:
def get_user_devices(email_user: str, states: dict, device_types: dict, locations: dict, homes: dict):
def search_device_by_name(email_user: str, device_name: str, states: dict, device_types: dict, locations: dict, homes: dict):
```

*Filtros de dispositivos (3 referencias):*
```python
# ANTES:
user_devices = [device for device in devices if device['id_home'] in home_ids]
if device['id_home'] in home_ids and device['name'].lower() == device_name.lower():

# CORREGIDO:
user_devices = [device for device in devices if device['home_id'] in home_ids]
if device['home_id'] in home_ids and device['name'].lower() == device_name.lower():
```

**5. Correcciones en utils/devices_utils.py**

*Campo en funcion get_home_ids_by_email:*
```python
# ANTES (campo incorrecto):
return [entry['home_id'] for entry in user_home_data if entry['email'] == email_user]

# CORREGIDO:
return [entry['home_id'] for entry in user_home_data if entry['user_email'] == email_user]
```

*Nomenclatura en funcion map_device_data_for_view:*
```python
# ANTES:
def map_device_data_for_view(device: dict, states: dict, types_device: dict, locations: dict, homes: dict):
    return {
        'state': get_name_by_id(states, device['id_state']),
        'type': get_name_by_id(types_device, device['id_type']),
        'location': get_name_by_id(locations, device['id_location']),
        'home': get_name_by_id(homes, device['id_home'])
    }

# CORREGIDO:
def map_device_data_for_view(device: dict, states: dict, device_types: dict, locations: dict, homes: dict):
    return {
        'state': get_name_by_id(states, device['state_id']),
        'type': get_name_by_id(device_types, device['device_type_id']),
        'location': get_name_by_id(locations, device['location_id']),
        'home': get_name_by_id(homes, device['home_id'])
    }
```

**6. Correccion de Automatizacion 3**
```python
# ANTES (automatizacion invalida):
{
    "name": "Encender luz de oficina",
    "description": "Automatizacion para encender la luz de la oficina en casa de campo",
    "home_id": 2,  # Casa sin dispositivos disponibles
}

# CORREGIDO:
{
    "name": "Encender luz de dormitorio", 
    "description": "Automatizacion para encender la luz del dormitorio principal",
    "home_id": 1,  # Casa con dispositivos disponibles
}
```

**7. Estandarizacion de Formato en devices_data.py**
```python
# ANTES (formato mixto):
"id": 1,  # Comillas dobles
'id': 1,  # Comillas simples

# CORREGIDO (formato consistente):
'id': 1,  # Todas comillas simples
```

### Impacto de las correcciones de funcionalidad:
- **Archivos modificados:** 7 archivos principales
- **Total de correcciones:** 25+ correcciones individuales
- **Compatibilidad:** 100% mantenida
- **Funcionalidad:** Completamente restaurada

**RESULTADO FINAL:**

**Estado:** PROGRAMA COMPLETAMENTE FUNCIONAL

El programa `main.py` ahora se ejecuta sin errores despues de aplicar todas estas correcciones.

---

##  CORRECCIÓN 4: PREFIJOS EN CONFIRMACIONES

---
###  Problema identificado:
> "Revisar que todas las confirmaciones tengan prefijos. Ayuda a documentar la historia del fuente"

###  Solución implementada:

####  **4.1 Sistema de prefijos implementado**

| Prefijo | Propósito | Ejemplo de uso |
|---------|-----------|----------------|
| `[AUTOMATION-SUCCESS]` | Automatización ejecutada correctamente | Encendido de luces |
| `[AUTOMATION-ERROR]` | Error en ejecución de automatización | Automatización no implementada |
| `[AUTOMATION-DISABLED]` | Automatización desactivada | Estado inactivo |
| `[AUTOMATION-WARNING]` | Advertencias del sistema | No hay luces para apagar |
| `[ACCESS-DENIED]` | Acceso denegado a recurso | Sin permisos para automatización |
| `[INPUT-ERROR]` | Error en entrada de datos | ID inválido |
| `[USER-INFO]` | Información para el usuario | Sin automatizaciones disponibles |

####  **4.2 Implementación en código**

**Archivo**: `controllers/automation_controller.py`
```python
# Código anterior: sin prefijos informativos
return "No tienes acceso a esta automatización"
return "Automatización desactivada"
return f"✅ {automation['name']} ejecutada: Luz del Salón encendida"

# 🔨 Código actualizado: con prefijos para documentar historia
return "[ACCESS-DENIED] No tienes acceso a esta automatización"
return "[AUTOMATION-DISABLED] Automatización desactivada"
return f"[AUTOMATION-SUCCESS] {automation['name']} ejecutada: Luz del Salón encendida"
```

**Archivo**: `main.py`
```python
# Código anterior: sin prefijos
print("❌ ID inválido")
print("No hay automatizaciones disponibles")
print("ID inválido")

# 🔨 Código actualizado: con prefijos informativos
print("[INPUT-ERROR] ❌ ID inválido")
print("[AUTOMATION-INFO] No hay automatizaciones disponibles")
print("[INPUT-ERROR] ID inválido")
```

####  **4.3 Beneficios del sistema de prefijos**

1. **Trazabilidad**: Cada mensaje identifica su origen y tipo
2. **Debugging**: Facilita identificación de problemas
3. **Auditoría**: Permite seguimiento de acciones del sistema
4. **Categorización**: Agrupa mensajes por tipo de operación
5. **Profesionalismo**: Mejora la experiencia de usuario




