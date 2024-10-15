import subprocess

def execute_script(script_path):
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
    scripts = [
        "cpu/cpu.py",
        "disk/disk_info_wmi.py",
        "disk/partitions_info_psutil.py",
        "gpu/gpu.py",
        "network/network.py",
        "os/os.py",
        "ram/ram.py"
    ]
    
    for script in scripts:
        execute_script(script)

if __name__ == "__main__":
    main()
