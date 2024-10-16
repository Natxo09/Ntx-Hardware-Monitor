import platform
import subprocess
import json

def get_battery_info():
    try:
        # Ejecutar el comando 'pmset -g batt' para obtener el estado de la batería
        result = subprocess.run(["pmset", "-g", "batt"], capture_output=True, text=True)
        if result.returncode == 0 and "Battery" in result.stdout:
            # Buscar el porcentaje de la batería en la salida
            for line in result.stdout.splitlines():
                if "%" in line:
                    percentage = line.split("%")[0].split()[-1]
                    return f"{percentage}%"
        return "Sin batería"
    except Exception as e:
        print(f"Error al obtener información de la batería: {e}")
        return "Error obteniendo batería"

def get_os_details():
    os_name = platform.system()  # macOS se detecta como 'Darwin'
    os_version = platform.mac_ver()[0]  # Obtener la versión de macOS
    architecture = platform.machine()  # Obtener la arquitectura (x86_64, arm64, etc.)

    # Verificar si es un portátil y obtener la información de la batería
    battery_info = get_battery_info()

    return {
        "Nombre del sistema operativo": "macOS" if os_name == "Darwin" else os_name,
        "Versión": os_version,
        "Arquitectura": architecture,
        "Batería": battery_info
    }

def main():
    os_data = get_os_details()
    print(json.dumps(os_data, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
