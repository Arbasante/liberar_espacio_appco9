import subprocess

#ruta = "C:\\Users\\T.I\\Documents\\python package"

command = rf'Get-ChildItem -Path "{ruta}" -File | Select-Object -Property Name, CreationTime'
output = subprocess.check_output(["powershell", "-Command", command])
salida= output.decode("utf-8")
print(salida)

lineas = salida.splitlines()[3:]  # Elimina las dos primeras líneas que contienen encabezados
print (lineas[1])