import subprocess
import os

lista = []

ruta = "C:\\Users\\T.I\\Documents\\Proyectos_Automatizacion\\"


#command_file = rf'Get-ChildItem -Path "{ruta}" -File | Select-Object -Property Name, CreationTime | Sort-Object -Property CreationTime'
command_folder = rf'Get-ChildItem -Path "{ruta}" -Directory | Select-Object -Property Name, CreationTime | Sort-Object -Property CreationTime'
output = subprocess.check_output(["powershell", "-Command", command_folder])
salida= output.decode("utf-8")
print(salida)

lineas = salida.splitlines()[3:-2]  # Elimina los espacios vacios de la lista
print ("el ultimo archivo creado es: ", lineas[-1])
print ("numero total de archivos: ",len(lineas))


print("cantidad de archivos a eliminar: ", len(lineas) - 2)
print ("se elimina los archivos en ordes hasta: ", lineas[-3])

for i in range(len(lineas) - 2):
    elemento = lineas[i].split()[0]
    print(elemento)
    #delete = f'Remove-Item -Path "{ruta}{elemento}" -Recurse'
    #subprocess.run(["powershell.exe", "-Command", delete], check=True)
    
archivos_zip = []

for archivo in os.listdir(ruta):
    if archivo.endswith(".zip"):
      archivos_zip.append(archivo)
      #delete = f'Remove-Item -Path "{ruta}{archivo}"'
      #subprocess.run(["powershell.exe", "-Command", delete], check=True)
    

print(archivos_zip)

    

