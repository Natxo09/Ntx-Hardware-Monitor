import json
import platform
import psutil
import subprocess

# Obtener información detallada de la CPU
def get_cpu_details():
    # Obtener nombre del procesador utilizando sysctl (comando disponible en macOS)
    try:
        cpu_name = subprocess.check_output(["sysctl", "-n", "machdep.cpu.brand_string"]).strip().decode('utf-8')
    except Exception as e:
        cpu_name = f"Desconocido (Error: {e})"
    
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
