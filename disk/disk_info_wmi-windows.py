import wmi
import json

# Inicializar WMI
w = wmi.WMI()

# Obtener detalles de los discos físicos con WMI
def get_disk_info():
    disk_data = []

    for disk in w.Win32_DiskDrive():
        disk_size_gb = int(disk.Size) // (1024 ** 3)  # Convertir a GB
        disk_info = {
            "Nombre": disk.Caption,
            "Tamaño (GB)": disk_size_gb,
            "Tipo de Interfaz": disk.InterfaceType,
            "Tipo de Medio": disk.MediaType,
            "Firmware": disk.FirmwareRevision,
            "Número de serie": disk.SerialNumber,
            "Número de particiones": disk.Partitions
        }
        disk_data.append(disk_info)
    
    return disk_data

def main():
    try:
        disk_info = get_disk_info()
        print(json.dumps(disk_info, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
