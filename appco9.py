import subprocess
import datetime

lista = []

ruta = "C:\\Users\\T.I\\Documents\\python package"

#command = rf'Get-ChildItem -Path "{ruta}" -File | Select-Object -Property Name, CreationTime'
command = rf'Get-ChildItem -Path "{ruta}" -File | Select-Object -Property Name, CreationTime | Sort-Object -Property CreationTime'
output = subprocess.check_output(["powershell", "-Command", command])
salida= output.decode("utf-8")
print(salida)

lineas = salida.splitlines()[3:]  # Elimina las dos primeras líneas que contienen encabezados
print (lineas[-3])
print (len(lineas) - 3)
#print (lineas[83])

print("elementos a eliminar", len(lineas) - 5)
#print (lineas[82])
print (lineas[-5])

for i in range(len(lineas) - 4):
    elemento = lineas[i].split()[0]
    delete = f'Remove-Item -Path "{ruta}{elemento}"'
    subprocess.run(["powershell.exe", "-Command", delete], check=True)

    

