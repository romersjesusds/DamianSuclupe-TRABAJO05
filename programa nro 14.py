print("\n")
#INPUT
cliente=input("ingrese le nombre del cliente:")
numero_kilos=int(input("ingrese cantidad de kg de arroz:"))
precio_kilo=float(input("ingrese precio unitario"))

#PROCESSING
total=(precio_kilo*numero_kilos)

#VERIFICADOR
comprador_compulsivo=(total>=50)

# OUTPUT
print("#######################")
print("BOLETA DE VENTA")
print("#######################")
print("#")
print("#cliente:",cliente)
print("#ITEM: ",numero_kilos,"kilos arroz")
print("#P.U.: s/.",precio_kilo)
print("# total.: s/.",total)
print("#######################")
print("¿Comprador Compulsivo?:",comprador_compulsivo)
