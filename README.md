
# Hardware Monitor Project

Este proyecto es una aplicación ligera de monitoreo de hardware que obtiene información del sistema, incluyendo CPU, RAM, GPU, discos, red, y sistema operativo. Está diseñado para consumir pocos recursos y ser compatible con Windows. Los datos se recopilan utilizando varias librerías de Python.

## Características

- **CPU**: Nombre, uso, núcleos, hilos, frecuencia.
- **RAM**: Total, usado, libre, swap, tipo y velocidad.
- **GPU**: Nombre, uso, VRAM, velocidad.
- **Discos**: Modelo, tamaño, uso, tipo de interfaz, velocidad.
- **Red**: Dirección IP, tipo de conexión (Wi-Fi o Ethernet).
- **Sistema Operativo**: Nombre, versión, arquitectura, estado de la batería (si es portátil).

## Requisitos

Para ejecutar este proyecto, necesitarás tener Python instalado y las siguientes dependencias:

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` contiene:

```
psutil
wmi
py-cpuinfo
GPUtil
```

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/Natxo09/Ntx-Hardware-Monitor
cd Ntx-Hardware-Monitor
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Uso

Ejecuta los scripts para obtener la información del hardware. Cada archivo está diseñado para recoger diferentes datos:

- **CPU**: `cpu.py`
- **RAM**: `ram.py`
- **GPU**: `gpu.py`
- **Discos**: `disk_info_wmi.py` y `partitions_info_psutil.py`
- **Red**: `network.py`
- **Sistema Operativo**: `os.py`

### Ejemplo de ejecución:

```bash
python cpu.py
```

Puedes combinar estos scripts para generar un informe completo del sistema.

## Contribuir

Las contribuciones son bienvenidas. Si tienes alguna idea para mejorar este proyecto o encuentras un error, no dudes en abrir un issue o enviar un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo [LICENSE](./LICENSE).
