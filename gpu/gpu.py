import GPUtil
import json

# Obtener detalles de todas las GPUs disponibles
def get_gpu_details():
    gpus = GPUtil.getGPUs()
    gpu_data = []

    for gpu in gpus:
        gpu_info = {
            "Nombre": gpu.name,
            "Uso (%)": gpu.load * 100,
            "Temperatura (°C)": gpu.temperature,
            "VRAM total (MB)": gpu.memoryTotal,
            "VRAM usada (MB)": gpu.memoryUsed,
            "VRAM libre (MB)": gpu.memoryFree
        }
        gpu_data.append(gpu_info)

    return gpu_data

# Función principal
def main():
    gpu_data = get_gpu_details()
    print(json.dumps(gpu_data, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
