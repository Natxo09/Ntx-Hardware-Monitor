import psutil
import socket
import json

# Obtener la dirección IP
def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.error as e:
        return f"Error al obtener la dirección IP: {e}"

# Determinar si la conexión es Wifi o Ethernet
def get_network_type():
    try:
        # psutil.net_if_addrs() nos da las interfaces de red disponibles
        interfaces = psutil.net_if_addrs()
        network_data = []

        for interface, addrs in interfaces.items():
            for addr in addrs:
                if addr.family == socket.AF_INET:  # IPv4
                    network_type = "Ethernet" if "eth" in interface.lower() or "en" in interface.lower() else "Wi-Fi"
                    network_info = {
                        "Interfaz": interface,
                        "Dirección IP": addr.address,
                        "Tipo de conexión": network_type
                    }
                    network_data.append(network_info)

        return network_data
    except Exception as e:
        return f"Error al obtener el tipo de red: {e}"

def main():
    try:
        network_info = get_network_type()
        print(json.dumps(network_info, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
