def borrar_pantalla():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')     #Limpia pantalla tanto en Windows como en Linux y MacOS


def esperar_tecla():
    input("\t\t\t\n Presiona Enter para continuar ... ")

def menu_inicio_sesion():
    print("\n\t\t\t .:: LLANTASA AZTECA ::.")
    print("\n\t\t\t 1-. Iniciar Sesion", "\n\t\t\t 2-. Registrarse", "\n\t\t\t 3-. Salir")

    opcion = input("\t\t\t\n Teclea una opción:  ").upper().strip()
    return opcion 


def menu_llantas(usuario_id, nombre, apellidos):
    print("\n\t\t\t LLANTAS AZTECA")
    print("\n\t\t\t 1.- 🆕 Agregar Llantas",
        "\n\t\t\t 2.- 👁️  Mostrar Llantas",
        "\n\t\t\t 3.- 🔍 Buscar Llantas",
        "\n\t\t\t 4.- ❌ Eliminar Llantas",
        "\n\t\t\t 5.- 💸 Vender Llantas",
        "\n\t\t\t 6.- 📜 Registro de ventas",
        "\n\t\t\t 7.- 📤 Exportar",
        "\n\t\t\t 8.- 🚪 Cerrar sesión")

    opcion = input("\n\t\t\t Elija una opción: ")
    return opcion