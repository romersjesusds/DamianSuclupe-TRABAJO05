print("\n")
#INPUT
cliente=input("ingrese le nombre del cliente:")
cant_litros=int(input("ingrese cantidad de litros de chicha morada:"))
precio_litro=float(input("ingrese precio unitario"))

#PROCESSING
total=(precio_litro*cant_litros)

#VERIFICADOR
comprador_compulsivo=(total>150)

# OUTPUT
print("#######################")
print("BOLETA DE VENTA")
print("#######################")
print("#")
print("#cliente:",cliente)
print("#ITEM: ",kg,"kg Fresa")
print("#P.U.: s/.",precio_litro)
print("# total.: s/.",total)
print("#######################")
print("¿Comprador Compulsivo?:",comprador_compulsivo)
