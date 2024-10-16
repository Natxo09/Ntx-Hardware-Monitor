import subprocess
import json

def get_network_info():
    try:
        # Ejecutar el comando 'ifconfig' para obtener la información de la red
        result = subprocess.run(["ifconfig"], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error al ejecutar el comando: {result.stderr}")
            return None

        # Inicializar variables para almacenar la información
        network_data = []
        current_interface = {}

        # Procesar la salida de 'ifconfig' línea por línea
        for line in result.stdout.splitlines():
            if line and not line.startswith("\t"):  # Nueva interfaz
                if current_interface and current_interface.get("Dirección IP"):
                    network_data.append(current_interface)
                # Extraer el nombre de la interfaz
                interface_name = line.split(":")[0]
                current_interface = {"Interfaz": interface_name, "Dirección IP": None, "Tipo de conexión": None}
                # Determinar el tipo de conexión
                if interface_name == "en0":
                    current_interface["Tipo de conexión"] = "Ethernet"
                elif interface_name == "en1":
                    current_interface["Tipo de conexión"] = "Wifi"
            elif "inet " in line and "inet6" not in line:  # Buscar la dirección IPv4
                current_interface["Dirección IP"] = line.split()[1]
        
        # Añadir la última interfaz procesada
        if current_interface and current_interface.get("Dirección IP"):
            network_data.append(current_interface)

        return network_data

    except Exception as e:
        print(f"Error al obtener la información de la red: {e}")
        return None

def main():
    network_info = get_network_info()
    if network_info:
        # Imprimir la información filtrada de manera bonita
        print(json.dumps(network_info, indent=2, ensure_ascii=False))
    else:
        print("No se encontraron interfaces de red relevantes o no se pudo obtener información.")

if __name__ == "__main__":
    main()
