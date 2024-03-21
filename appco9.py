import subprocess
import os




def liberar_espacio(ruta):

    #command_file = rf'Get-ChildItem -Path "{ruta}" -File | Select-Object -Property Name, CreationTime | Sort-Object -Property CreationTime'
    command_folder = rf'Get-ChildItem -Path "{ruta}" -Directory | Select-Object -Property Name, CreationTime | Sort-Object -Property CreationTime'
    output = subprocess.check_output(["powershell", "-Command", command_folder])
    salida= output.decode("utf-8")
    print(salida)

    lineas = salida.splitlines()[3:-2]  # Elimina los espacios vacios de la lista
    print ("el ultimo archivo creado es: ", lineas[-1])



    #print("cantidad de archivos a eliminar: ", len(lineas) - 2)
    #print ("se elimina los archivos en orden hasta: ", lineas[-3])

    archivos_zip = []

    for archivo in os.listdir(ruta):
        if archivo.endswith(".zip"):
            archivos_zip.append(archivo)
            delete = f'Remove-Item -Path "{ruta}{archivo} -Force"'
            subprocess.run(["powershell.exe", "-Command", delete], check=True)

    if len(lineas) > 2:

        print ("numero total de archivos: ",len(lineas))
        for i in range(len(lineas) - 2):
            elemento = lineas[i].split()[0]
            print(elemento)
            delete = f'Remove-Item -Path "{ruta}{elemento}" -Recurse -Force'
            subprocess.run(["powershell.exe", "-Command", delete], check=True)
        

    

        print(archivos_zip)


if __name__ == '__main__':


    path = ["C:\\Users\\T.I\\Documents\\Proyectos_Automatizacion_copia\\"]

    for ruta in path:
        liberar_espacio(ruta)

    

