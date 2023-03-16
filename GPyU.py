from tabulate import tabulate
import GPUtil
import socket 
import urllib.request

def print_title(title: str) -> None:
    print("="*50, title, "="*50)


def print_cpu_info():
    print_title('GPU DETAILS')
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        # get the GPU id
        gpu_id = gpu.id
        # name of GPU
        gpu_name = gpu.name
        # get % percentage of GPU usage of that GPU
        gpu_load = f"{gpu.load*100}%"
        # get free memory in MB format
        gpu_free_memory = f"{gpu.memoryFree}MB"
        # get used memory
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        # get total memory
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        # get GPU temperature in Celsius
        gpu_temperature = f"{gpu.temperature} °C"
        gpu_uuid = gpu.uuid
        list_gpus.append([gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory, gpu_total_memory, gpu_temperature])#, gpu_uuid])

    head = ("id", "nombre", "carga", "memoria libre", "memoria usada", "memoria total", "temperatura")#, "uuid")
    print(tabulate(list_gpus, 
                headers=head,
                tablefmt='fancy_grid',
                stralign='center',
                floatfmt='.0f'))



def get_pc_name():
    # concatenar los archivos con el nombre de la pc
    return str(socket.gethostname())

# Funcion para obtener las IP
def get_private_ip():
    pc_name = socket.gethostname()
    return str(socket.gethostbyname(pc_name))

def get_public_ip():
    return str(urllib.request.urlopen('https://ident.me').read().decode('utf8'))
      
def print_name_ip_table():
    print_title('IP INFO')
    ip_info_list = [[get_pc_name(), get_private_ip(), get_public_ip()]]
    head = ('Nombre PC', 'IP privada', 'IP Publica')
    
    print(tabulate(ip_info_list, 
    headers=head, 
    tablefmt='fancy_grid', 
    stralign='center', 
    floatfmt='.0f'))

if __name__ == '__main__':
    print_cpu_info()
    print_name_ip_table()