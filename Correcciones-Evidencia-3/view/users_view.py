from typing import Dict, Optional
from utils.helpers import get_user_input
from model.user import isExist
from model.rol import roles
from controllers.user_controller import login, register


def show_welcome():
    print("--------------#-------------")
    print("Bienvenido a 🕹️Hogar Boot🕹️")
    print("--------------#-------------")


def show_login_message() -> None:
    print("Inicia sesion para continuar o crea una cuenta si no tienes")


def show_user_menu() -> None:
    print("1. Consultar los datos personales.")
    print("2. Ejecutar automatización.")
    print("3. Listar Dispositivos.")
    print("0. Salir")


def show_admin_menu() -> None:
    print("1. Consultar automatizaciones activas.")
    print("2. Agregar dispositivo.")
    print("3. Listar Dispositivos.")
    print("4. Buscar Dispositivo.")
    print("5. Eliminar Dispositivo.")
    print("6. Modificar el rol de un usuario.")
    print("0. Salir")


def show_login() -> Dict:
    email: str = get_user_input("Ingresa tu email").strip()
    password: str = get_user_input("ingresa tu contraseña").strip()
    return {"email": email, "password": password}


def show_register() -> Dict:
    username: str = get_user_input("Ingresa tu nombre de usuario: ").strip()
    email: str = get_user_input("Ingresa tu email: ").strip()
    password: str = get_user_input("ingresa tu contraseña: ").strip()
    return {"username": username, "email": email, "password": password}


def main_login() -> Optional[Dict]:
    """Maneja el proceso de login/registro y retorna los datos del usuario logueado"""
    show_welcome()
    show_login_message()

    while True:
        user_login_data = show_login()

        if not isExist(user_login_data["email"]):
            print("No tienes cuenta, regístrate a continuación...")
            user_register_data = show_register()
            result = register(user_register_data)
            print(result["message"])

            if result["success"]:
                # Después del registro exitoso, hacer login automático
                login_result = login(user_login_data)
                if login_result["success"]:
                    print(login_result["message"])
                    return login_result["user_data"]
        else:
            result = login(user_login_data)
            print(result["message"])

            if result["success"]:
                return result["user_data"]
            # Si falla el login, continúa el bucle para intentar de nuevo


def show_menu_by_role(user_data: Dict) -> None:
    """Muestra el menú apropiado según el rol del usuario"""
    print(f"\n¡Bienvenido, {user_data['name']}!")

    # Código anterior: verificaba con "id_rol"
    # 🔨 Actualizado para usar "role_id" coherente con modelo relacional
    # Verificar si es admin (roles[0] es admin, roles[1] es usuario normal)
    if user_data["role_id"] == roles[0]["id"]:
        print("=== MENÚ ADMINISTRADOR ===")
        show_admin_menu()
    else:
        print("=== MENÚ USUARIO ===")
        show_user_menu()
