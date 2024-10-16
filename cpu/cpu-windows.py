import json
import platform
import os
import psutil
from cpuinfo import get_cpu_info as get_cpu_info_external

# Obtener información detallada de la CPU
def get_cpu_details():
    cpu_info = get_cpu_info_external()
    cpu_name = cpu_info.get('brand_raw', 'Desconocido')
    cpu_usage = psutil.cpu_percent(interval=0.1)
    physical_cores = psutil.cpu_count(logical=False)
    logical_cores = psutil.cpu_count(logical=True)
    cpu_freq = psutil.cpu_freq()

    return {
        "Nombre": cpu_name,
        "Uso (%)": cpu_usage,
        "Núcleos físicos": physical_cores,
        "Hilos (lógicos)": logical_cores,
        "Frecuencia actual (MHz)": cpu_freq.current if cpu_freq else None
    }

# Función principal
def main():
    cpu_data = get_cpu_details()
    print(json.dumps(cpu_data, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
