import psutil
import json

# Obtener detalles de las particiones con psutil
def get_partitions_info():
    partitions_info = []

    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            partition_size_gb = usage.total // (1024 ** 3)
            partition_info = {
                "Partición": partition.device,
                "Tamaño total (GB)": partition_size_gb,
                "Tamaño usado (GB)": usage.used // (1024 ** 3),
                "Tamaño libre (GB)": usage.free // (1024 ** 3),
                "Uso (%)": usage.percent
            }
            partitions_info.append(partition_info)
        except PermissionError:
            continue  # Ignorar particiones a las que no tenemos acceso
        except Exception as e:
            print(f"Error al obtener información de la partición {partition.device}: {e}")

    return partitions_info

def main():
    try:
        partitions_info = get_partitions_info()
        print(json.dumps(partitions_info, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
