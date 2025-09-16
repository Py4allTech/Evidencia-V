from model.states_data import states
from model.types_data import device_types
from model.locations_data import locations

# Código anterior: importaba de 'homes_data' sin actualización
# 🔨 Actualizado para usar la estructura correcta
from model.home import homes
from model.rol import roles
from model.automaions_data import automations
from controllers.automation_controller import execute_automation, get_user_automations


from view.devices_view import (
    display_device_addition_result,
    show_user_devices,
    show_device_detail,
    display_device_deletion_result,
)

from controllers.devices_controller import (
    add_device,
    get_user_devices,
    search_device_by_name,
    delete_device_by_name,
)

from utils.devices_utils import request_and_validate_element
from view.users_view import main_login, show_menu_by_role


def main():
    # Proceso de login al inicio
    logged_user = main_login()

    if not logged_user:
        print("Error en el proceso de login. Saliendo...")
        return
    # Una vez logueado, mostrar el menú apropiado
    while True:
        show_menu_by_role(logged_user)

        option = input("Seleccione una opción: ").strip()

        # Usar el email del usuario logueado en lugar de uno hardcodeado
        email_user = logged_user["email"]

        if option == "1":
            # Código anterior: usaba "id_rol"
            # 🔨 Actualizado para usar "role_id" coherente con modelo relacional
            if logged_user["role_id"] == roles[0]["id"]:  # Admin
                print("=== AUTOMATIZACIONES DISPONIBLES (ADMIN) ===")
                # Código anterior: usaba campos 'activa' y 'nombre'
                # 🔨 Actualizado para usar 'active' y 'name' coherente con modelo relacional
                for auto in automations:  # Admin ve todas las automatizaciones
                    status = "🟢" if auto["active"] else "🔴"
                    print(f"{auto['id']}. {auto['name']} {status}")

                if automations:
                    try:
                        # Código anterior: input sin formato consistente
                        # 🔨 Mejoramos el formato para consistencia
                        auto_id = int(
                            input("Selecciona automatización a ejecutar (ID): ")
                        )
                        result = execute_automation(auto_id, email_user)
                        print(result)
                    except ValueError:
                        # 🔨 Agregado prefijo para documentar historia del fuente
                        print("[INPUT-ERROR] ❌ ID inválido")
                else:
                    # 🔨 Agregado prefijo para documentar historia del fuente
                    print("[AUTOMATION-INFO] No hay automatizaciones disponibles")
            else:  # Usuario normal
                print("Datos personales:")
                print(f"Nombre: {logged_user['name']}")
                print(f"Email: {logged_user['email']}")
                # Código anterior: usaba 'id_rol'
                # 🔨 Actualizado para usar 'role_id'
                print(
                    f"Rol: {'Administrador' if logged_user['role_id'] == roles[0]['id'] else 'Usuario'}"
                )

        elif option == "2":
            # Código anterior: usaba "id_rol"
            # 🔨 Actualizado para usar "role_id" coherente con modelo relacional
            if logged_user["role_id"] == roles[0]["id"]:  # Admin
                # Agregar dispositivo
                # Código anterior: input sin formato consistente
                # 🔨 Formato mejorado ya está correcto
                name = input("Nombre del dispositivo: ").strip()
                selected_state = request_and_validate_element(
                    "Estado (Ej: Encendido, Apagado): ", states, "name"
                )
                selected_type = request_and_validate_element(
                    "Tipo de dispositivo (Ej: Luz, Termostato): ", device_types, "name"
                )
                selected_location = request_and_validate_element(
                    "Ubicación (Ej: Sala, Cocina): ", locations, "name"
                )
                selected_home = request_and_validate_element(
                    "Hogar (Ej: Casa Principal): ", homes, "name"
                )

                success = add_device(
                    email_user,
                    name,
                    selected_state,
                    selected_type,
                    selected_location,
                    selected_home,
                )
                display_device_addition_result(success)
            else:  # Usuario normal
                print("=== MIS AUTOMATIZACIONES ===")
                user_autos = get_user_automations(email_user)

                if not user_autos:
                    # 🔨 Agregado prefijo para documentar historia del fuente
                    print("[USER-INFO] No tienes automatizaciones disponibles")
                else:
                    # Código anterior: usaba campos 'activa' y 'nombre'
                    # 🔨 Actualizado para usar 'active' y 'name' coherente con modelo relacional
                    for auto in user_autos:
                        status = "🟢" if auto["active"] else "🔴"
                        print(f"{auto['id']}. {auto['name']} {status}")

                    try:
                        auto_id = int(
                            input("Selecciona automatización a ejecutar (ID): ")
                        )
                        result = execute_automation(auto_id, email_user)
                        print(result)
                    except ValueError:
                        # 🔨 Agregado prefijo para documentar historia del fuente
                        print("[INPUT-ERROR] ID inválido")

        elif option == "3":
            # Listar dispositivos (disponible para ambos roles)
            results = get_user_devices(
                email_user, states, device_types, locations, homes
            )
            show_user_devices(results)

        elif option == "4" and logged_user["role_id"] == roles[0]["id"]:  # Solo admin
            # Código anterior: usaba "id_rol"
            # 🔨 Actualizado para usar "role_id"
            # Buscar dispositivo
            name = input("Nombre del dispositivo: ").strip()
            results = search_device_by_name(
                email_user, name, states, device_types, locations, homes
            )
            show_device_detail(results)

        elif option == "5" and logged_user["role_id"] == roles[0]["id"]:  # Solo admin
            # Código anterior: usaba "id_rol"
            # 🔨 Actualizado para usar "role_id"
            # Eliminar dispositivo
            name = input("Nombre del dispositivo: ").strip()
            success = delete_device_by_name(email_user, name)
            display_device_deletion_result(success)

        elif option == "6" and logged_user["role_id"] == roles[0]["id"]:  # Solo admin
            # Código anterior: usaba "id_rol"
            # 🔨 Actualizado para usar "role_id"
            print("Modificar rol de usuario - funcionalidad por implementar")

        elif option == "0":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
