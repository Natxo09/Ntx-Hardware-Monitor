import platform
import subprocess

def execute_script(script_path):
    # python3 solo funciona en mac y linux, en windows se ejecuta con python
    # hacer 2 clientes separados para windows y para mac/linux
    try:
        print(f"Ejecutando: {script_path}")
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
        else:
            print(f"Error ejecutando {script_path}: {result.stderr}")
    except Exception as e:
        print(f"Excepción ejecutando {script_path}: {e}")

def main():
    system = platform.system().lower()

    # Convertir "darwin" a "macos" para los scripts
    if system == 'darwin':
        system = 'mac'

    print(f"Sistema detectado: {system}")

    # Lista de scripts a ejecutar según el sistema operativo
    scripts = [
        f"cpu/cpu-{system}.py",
        f"gpu/gpu-{system}.py",
        f"network/network-{system}.py",
        f"os/os-{system}.py",
        f"ram/ram-{system}.py"
    ]

    # Solo en Windows ejecutamos los scripts de disco
    if system == 'windows':
        scripts.extend([
            "disk/disk_info_wmi-windows.py",
            "disk/partitions_info_psutil-windows.py"
        ])
    if system == 'mac':
        scripts.extend([
            "disk/disk-mac.py"
        ])

    # Ejecutar los scripts correspondientes al sistema operativo
    for script in scripts:
        try:
            execute_script(script)
        except FileNotFoundError:
            print(f"Archivo {script} no encontrado, asegúrate de que el archivo existe para el sistema operativo {system}.")

if __name__ == "__main__":
    main()
