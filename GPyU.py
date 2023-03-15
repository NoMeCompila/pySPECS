from tabulate import tabulate
import GPUtil

def print_cpu_info():
    print("="*40, "GPU Details", "="*40)
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

if __name__ == '__main__':
    print_cpu_info()


# rios3 = [['Río', 'Long. (Km.)'],
#          ['Almanzora', 105],
#          ['Guadiaro', 79],
#          ['Guadalhorce', 154],
#          ['Guadalmedina', 51.5]]

# print(tabulate(rios3,
#                headers='firstrow',
#                tablefmt='fancy_grid',
#                stralign='center',
#                floatfmt='.0f'))