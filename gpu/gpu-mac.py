import subprocess
import json

def get_gpu_info():
    try:
        # Ejecutar el comando 'system_profiler SPDisplaysDataType' para obtener la información de la GPU
        result = subprocess.run(["system_profiler", "SPDisplaysDataType", "-json"], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error al ejecutar el comando: {result.stderr}")
            return None

        # Convertir la salida JSON
        gpu_data = json.loads(result.stdout)

        # Filtrar la información relevante
        filtered_data = []
        for gpu in gpu_data.get("SPDisplaysDataType", []):
            gpu_info = {
                "Modelo": gpu.get("_name", "Desconocido"),
                "Núcleos": gpu.get("sppci_cores", "Desconocido"),
                "Soporte Metal": gpu.get("spdisplays_mtlgpufamilysupport", "Desconocido"),
                "Monitores": []
            }

            for display in gpu.get("spdisplays_ndrvs", []):
                monitor_info = {
                    "Nombre": display.get("_name", "Desconocido"),
                    "Resolución": display.get("spdisplays_resolution", "Desconocido"),
                    "Año de fabricación": display.get("_spdisplays_display-year", "Desconocido")
                }
                gpu_info["Monitores"].append(monitor_info)

            filtered_data.append(gpu_info)

        return filtered_data

    except Exception as e:
        print(f"Error al obtener la información de la GPU: {e}")
        return None

def main():
    gpu_info = get_gpu_info()
    if gpu_info:
        # Imprimir la información filtrada de manera bonita
        print(json.dumps(gpu_info, indent=2, ensure_ascii=False))
    else:
        print("No se encontraron GPUs o no se pudo obtener información.")

if __name__ == "__main__":
    main()
