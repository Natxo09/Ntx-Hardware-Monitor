import subprocess
import re
import json

def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error ejecutando el comando {command}: {e}")
        return ""

def parse_vm_stat(vm_stat_output):
    page_size = 16384  # Tamaño de página en bytes (16 KB)

    # Capturamos los valores importantes de vm_stat
    active_pages = int(re.search(r"Pages active:\s+(\d+).", vm_stat_output).group(1))
    inactive_pages = int(re.search(r"Pages inactive:\s+(\d+).", vm_stat_output).group(1))
    wired_pages = int(re.search(r"Pages wired down:\s+(\d+).", vm_stat_output).group(1))
    free_pages = int(re.search(r"Pages free:\s+(\d+).", vm_stat_output).group(1))
    compressed_pages = int(re.search(r"Pages occupied by compressor:\s+(\d+).", vm_stat_output).group(1))

    # Convertimos las páginas a GB
    free_gb = (free_pages * page_size) / (1024 ** 3)
    active_gb = (active_pages * page_size) / (1024 ** 3)
    inactive_gb = (inactive_pages * page_size) / (1024 ** 3)
    wired_gb = (wired_pages * page_size) / (1024 ** 3)
    compressed_gb = (compressed_pages * page_size) / (1024 ** 3)

    # Calculamos la memoria usada incluyendo la memoria activa, wired y comprimida
    used_gb = active_gb + wired_gb + compressed_gb  # Memoria realmente utilizada

    return free_gb, used_gb, compressed_gb

def parse_sysctl_memory_info(sysctl_output):
    total_memory_bytes = int(re.search(r"hw.memsize:\s+(\d+)", sysctl_output).group(1))
    total_gb = total_memory_bytes / (1024 ** 3)
    return total_gb

def parse_swap_info(swap_output):
    swap_used_gb = float(re.search(r"used = (\d+,\d+)M", swap_output).group(1).replace(',', '.'))
    return swap_used_gb / 1024  # Convertimos a GB

def parse_system_profiler_info(profiler_output):
    ram_type = re.search(r"Type:\s+(.+)", profiler_output).group(1)
    ram_manufacturer = re.search(r"Manufacturer:\s+(.+)", profiler_output).group(1)
    return ram_type, ram_manufacturer

def get_filtered_ram_info():
    sysctl_info = run_command(['sysctl', 'hw.memsize'])
    vm_stat_info = run_command(['vm_stat'])
    swap_info = run_command(['sysctl', 'vm.swapusage'])
    profiler_info = run_command(['system_profiler', 'SPMemoryDataType'])

    total_memory = parse_sysctl_memory_info(sysctl_info)
    free_memory, used_memory, compressed_memory = parse_vm_stat(vm_stat_info)
    swap_used = parse_swap_info(swap_info)
    ram_type, ram_manufacturer = parse_system_profiler_info(profiler_info)

    ram_info = {
        "Memoria total (GB)": round(total_memory, 2),
        "Memoria usada (GB)": round(used_memory, 2),
        "Memoria libre (GB)": round(total_memory - used_memory, 2),  # Calculamos la memoria libre
        "Memoria comprimida (GB)": round(compressed_memory, 2),
        "Swap usada (GB)": round(swap_used, 2),
        "Tipo de RAM": ram_type,
        "Fabricante de RAM": ram_manufacturer
    }

    return ram_info

if __name__ == "__main__":
    ram_info = get_filtered_ram_info()
    print(json.dumps(ram_info, indent=2, ensure_ascii=False))
