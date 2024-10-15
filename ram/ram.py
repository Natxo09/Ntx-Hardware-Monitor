import psutil
import wmi
import json

# Mapeo del tipo de RAM, incluyendo el valor 34 para DDR5
memory_type_mapping = {
    20: "DDR",
    21: "DDR2",
    24: "DDR3",
    26: "DDR4",
    30: "DDR5",
    34: "DDR5"  # Ajuste basado en tu sistema
}

# Inicializar WMI
w = wmi.WMI()

# Obtener detalles de la RAM
def get_ram_details():
    # Usar psutil para obtener total, usado, y libre
    virtual_mem = psutil.virtual_memory()
    swap_mem = psutil.swap_memory()

    # Usar WMI para obtener detalles de los módulos de RAM
    ram_modules = []
    for memory in w.Win32_PhysicalMemory():
        # Usar SMBIOSMemoryType si MemoryType no proporciona la información
        ram_type = memory_type_mapping.get(int(memory.SMBIOSMemoryType), "Desconocido")
        
        ram_info = {
            "Capacidad (MB)": int(memory.Capacity) // (1024 ** 2),  # Convertir a MB
            "Tipo": ram_type,
            "Velocidad (MHz)": memory.Speed,
            "MemoryType (raw)": memory.MemoryType,  # Mostrar el valor crudo
            "SMBIOSMemoryType (raw)": memory.SMBIOSMemoryType  # Mostrar el valor crudo
        }
        ram_modules.append(ram_info)

    return {
        "Total (MB)": virtual_mem.total // (1024 ** 2),
        "Usado (MB)": virtual_mem.used // (1024 ** 2),
        "Libre (MB)": virtual_mem.available // (1024 ** 2),
        "Swap total (MB)": swap_mem.total // (1024 ** 2),
        "Swap usado (MB)": swap_mem.used // (1024 ** 2),
        "Swap libre (MB)": swap_mem.free // (1024 ** 2),
        "Módulos RAM": ram_modules
    }

# Función principal
def main():
    ram_data = get_ram_details()
    print(json.dumps(ram_data, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
