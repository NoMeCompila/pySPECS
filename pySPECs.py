import socket  # libreria para saber nombre del PC
import platform  # libreria para obtener especificaciones de hardware
import urllib.request  # libreria para obtener ip publica y privada
import psutil  # libreria para el manejo de memoria
from io import open


def nombrePC():
    nombre_PC = socket.gethostname()
    archivo.write("Nombre de la PC: " + nombre_PC)  # concatenar los archivos con el nombre de la pc


# Funcion para obtener las IP
def IPpriv():
    nombre_PC = socket.gethostname()
    IPpriv = socket.gethostbyname(nombre_PC)
    archivo.write("IP privada: " + IPpriv)


def IPpub():
    ip_externa = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    archivo.write("IP publica: " + ip_externa)


# funcion  que devuelve nformacion del sistema
def sist():
    arqui_sist = platform.architecture()
    archivo.write("Arquitectura y SO: " + str(arqui_sist))
    vers = platform.release()
    archivo.write("\nVersion: " + vers)


# Funcion que devuelve informacion sobre el hardware
def Cores():
    tipo_mauina = platform.machine()
    archivo.write("Tipo de maquina: " + tipo_mauina)
    procesador = platform.processor()
    archivo.write("\n" + "Procesador: " + procesador)
    cores_fisicos = psutil.cpu_count(logical=False)
    cores_totales = psutil.cpu_count(logical=True)
    archivo.write("\n" + "cores fisicos: " + str(cores_fisicos) + "\n" + "cores totales: " + str(cores_totales))


# funcion de convfersion de unidades de almacenamiento
"""
    Reescala los bytes al formato adecuado
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
"""


def get_size(bytes, sufijo="B"):
    factor_conversion = 1024
    for unidad in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor_conversion:
            return f"{bytes:.2f}{unidad}{sufijo}"  # retorna la unidad de medida final redondeada a 2 decimales con su correspondiente abreviatura
        bytes /= factor_conversion


def memoriaRAM():
    ram = psutil.virtual_memory()
    archivo.write("\nMemoria RAM  total: " + get_size(ram.total))
    archivo.write("\nMemoria RAM usada: " + get_size(ram.used))
    archivo.write("\nMemoria RAM disponible: " + get_size(ram.available))


# funcion que devuelve el espacio en disco disponible

def espacioEnDisco():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        archivo.write(f"\n=== Disco Local: {partition.device} ===")
        archivo.write(f"\nPunto de montaje: {partition.mountpoint}")
        archivo.write(f"\nTipo de archivo del sistema: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        archivo.write("\nEspacio total en disco: " + get_size(partition_usage.total))
        archivo.write("\nEspacio usado en disco: " + get_size(partition_usage.used))
        archivo.write("\nEspacio libre en disco: " + get_size(partition_usage.free))


# Funcion que une a todas las anteriores y cierra el archivo
def EjecutarTodo():
    archivo.write("=" * 40 + "Nombre PC" + "=" * 40 + "\n")
    nombrePC()
    archivo.write("\n" + "=" * 40 + "Informacion IP" + "=" * 40 + "\n")
    IPpriv()
    archivo.write("\n")
    IPpub()
    archivo.write("\n" + "=" * 40 + "SISTEMA" + "=" * 40 + "\n")
    sist()
    archivo.write("\n" + "=" * 40 + "Hardware" + "=" * 40 + "\n")
    Cores()
    archivo.write("\n" + "=" * 40 + "Memoria RAM" + "=" * 40)
    memoriaRAM()
    archivo.write("\n" + "=" * 40 + "Memoria en Disco" + "=" * 40)
    espacioEnDisco()
    archivo.close()


if __name__ == '__main__':

    # abrir el archivo con una variable global
    archivo = open("info_pc.txt", "w")

    EjecutarTodo()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
