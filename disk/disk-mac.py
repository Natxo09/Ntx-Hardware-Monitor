import json
import os
import psutil

def get_partition_info():
    partitions = psutil.disk_partitions(all=False)
    partition_info = []

    for partition in partitions:
        # Obtenemos el uso de la partición
        try:
            usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # En algunos sistemas, podría no tener permiso para acceder a ciertas particiones
            continue

        # Filtrar particiones pequeñas, snapshots o con poco uso
        if usage.total < 10 * 1024**3:  # Filtrar particiones menores de 10 GB
            continue

        # Filtrar particiones de simuladores (por ejemplo, si contienen "iOS" o "watchOS" en el nombre)
        if "iOS" in partition.device or "watchOS" in partition.device:
            continue

        # Filtrar volúmenes APFS con 0% de uso
        if usage.used == 0:
            continue

        # Guardar información relevante de la partición
        partition_info.append({
            "Partición": partition.device,
            "Sistema de archivos": partition.fstype,
            "Tamaño total (GB)": round(usage.total / 1024**3, 1),
            "Tamaño usado (GB)": round(usage.used / 1024**3, 1),
            "Tamaño libre (GB)": round(usage.free / 1024**3, 1),
            "Uso (%)": usage.percent
        })

    return partition_info

# Función principal
def main():
    filtered_partitions = get_partition_info()
    print(json.dumps(filtered_partitions, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
