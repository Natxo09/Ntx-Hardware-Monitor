import platform
import psutil
import json

# Obtener información del sistema operativo
def get_os_info():
    os_info = {
        "Nombre": platform.system(),  # Sistema operativo (Windows, Linux, etc.)
        "Versión": platform.release(),  # Versión del sistema operativo
        "Arquitectura": platform.architecture()[0],  # Arquitectura (64 bits, 32 bits)
    }
    return os_info

# Verificar si el dispositivo tiene batería (indica si es portátil)
def get_battery_info():
    if psutil.sensors_battery():
        battery = psutil.sensors_battery()
        battery_info = {
            "Batería presente": True,
            "Porcentaje": battery.percent,
            "En carga": battery.power_plugged
        }
    else:
        battery_info = {
            "Batería presente": False
        }
    return battery_info

def main():
    # Obtener información del sistema operativo
    os_info = get_os_info()
    
    # Obtener información de la batería si es un portátil
    battery_info = get_battery_info()

    # Combinar la información de sistema operativo y batería
    system_info = {**os_info, **battery_info}

    # Mostrar el resultado en formato JSON
    print(json.dumps(system_info, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
