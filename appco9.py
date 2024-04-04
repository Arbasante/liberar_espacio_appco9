import subprocess
import os




def liberar_espacio(ruta):

    #command_file = rf'Get-ChildItem -Path "{ruta}" -File | Select-Object -Property Name, CreationTime | Sort-Object -Property CreationTime'
    command_folder = rf'Get-ChildItem -Path "{ruta}" -Directory | Select-Object -Property Name, CreationTime | Sort-Object -Property CreationTime'
    output = subprocess.check_output(["powershell", "-Command", command_folder])
    salida= output.decode("utf-8")
    print(salida)

    lineas = salida.splitlines()[3:-2]  # Elimina los espacios vacios de la lista
    print ("el ultimo archivo creado es: ", lineas)


    archivos_zip = []

    for archivo in os.listdir(ruta):
        if archivo.endswith(".zip"):
            delete = f'Remove-Item -Path "{ruta}\\{archivo}" -Force'
            print ("zip: ", archivo)
            subprocess.run(["powershell.exe", "-Command", delete], check=True)

        

    if len(lineas) > 2:

        print ("numero total de archivos: ",len(lineas))
        for i in range(len(lineas) - 2):
            elemento = lineas[i].split()[0]
            #elemento = " ".join(elemento[:-4])
            print("elementos: ", elemento)
            delete = f'Remove-Item -Path "{ruta}\\{elemento}" -Recurse -Force'
            print('ruta: ', delete)
            subprocess.run(["powershell.exe", "-Command", delete], check=True)
        
        
    

        


if __name__ == '__main__':

    path = ["C:\\Users\\Administrador\\Documents\\Instaladores\\SondasEbillProd","C:\\Users\\Administrador\\Documents\\Instaladores\\SondaProveedores",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\Ulibre","C:\\Users\\Administrador\\Documents\\Instaladores\\ArchivoSalidaNegVYR",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\ColasIndKactus","C:\\Users\\Administrador\\Documents\\Instaladores\\eBillToClienteV1",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\EbillToDian","C:\\Users\\Administrador\\Documents\\Instaladores\\EnvioCliente",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\Sonda de radicacion ftp vyr","C:\\Users\\Administrador\\Documents\\Instaladores\\Sonda_Asinc_NE",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\Sonda DSNO test","C:\\Users\\Administrador\\Documents\\Instaladores\\Pequeños",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\RestApi_NE_Test","C:\\Users\\Administrador\\Documents\\Instaladores\\Sonda Envio Posterior Test",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\SondaRadicDocBizagiAlianzaTest","C:\\Users\\Administrador\\Documents\\Instaladores\\qualaDSNOtest",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\RestApi_FE","C:\\Users\\Administrador\\Documents\\Instaladores\\Recepción Dev",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\Rezagos","C:\\Users\\Administrador\\Documents\\Instaladores\\Front validaciony registro test",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\ApiRestContingencia","C:\\Users\\Administrador\\Documents\\Instaladores\\EBillRestApiTest",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\SondaDocRef","C:\\Users\\Administrador\\Documents\\Instaladores\\Colas Kactus",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\Componente Recepcion", "C:\\Users\\Administrador\\Documents\\Instaladores\\Dian2ToeBill",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\eBillToClienteV2","C:\\Users\\Administrador\\Documents\\Instaladores\\Endosos-test",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\esalariumweb","C:\\Users\\Administrador\\Documents\\Instaladores\\EbillGateway",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\SondaCalificadora","C:\\Users\\Administrador\\Documents\\Instaladores\\apifinanciera",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\SondaVerificaEstadoBizagi","C:\\Users\\Administrador\\Documents\\Instaladores\\SetupSondaRadicadoraSIGED"
            "C:\\Users\\Administrador\\Documents\\Instaladores\\EbillToFTPCliente","C:\\Users\\Administrador\\Documents\\Instaladores\\eBillApiRestTestDev",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\Sonda Rezagos DIAN Test","C:\\Users\\Administrador\\Documents\\Instaladores\\Sonda rezagos dian x empresa",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\USTA","C:\\Users\\Administrador\\Documents\\Instaladores\\SondaEnvioMasivoEventosTest",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\Nomina","C:\\Users\\Administrador\\Documents\\Instaladores\\Sonda Confirming Negociacion",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\Sondas de notificacion ebill","C:\\Users\\Administrador\\Documents\\Instaladores\\Portal Back Office",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\Cufes","C:\\Users\\Administrador\\Documents\\Instaladores\\ebill fondeador juridico",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\Sonda transversal", "C:\\Users\\Administrador\\Documents\\Instaladores\\desatendido test",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\InformeC","C:\\Users\\Administrador\\Documents\\Instaladores\\ApieBillReceptorTest",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\ApiRestTransversalTest","C:\\Users\\Administrador\\Documents\\Instaladores\\Api ValyReg",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\Portal Pagador Web para V&R Test","C:\\Users\\Administrador\\Documents\\Instaladores\\FacturaManual",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\Ebill\\Web","C:\\Users\\Administrador\\Documents\\Instaladores\\Portal Proveedores",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\Sonda Colas Recepcion","C:\\Users\\Administrador\\Documents\\Instaladores\\SondaEbill",
            "C:\\Users\\Administrador\\Documents\\Instaladores\\ApiGateWayTest","C:\\Users\\Administrador\\Documents\\Instaladores\\FTP Apple"]
    

    for ruta in path:
        liberar_espacio(ruta)

    

