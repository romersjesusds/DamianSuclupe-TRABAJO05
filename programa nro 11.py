print("\n")
#INPUT
cliente=input("ingrese le nombre del cliente:")
kg=int(input("ingrese cantidad de kg de papa:"))
precio_uni=float(input("ingrese precio unitario"))

#PROCESSING
total=(precio_uni*kg)

#VERIFICADOR
comprador_compulsivo=(total>150)

# OUTPUT
print("#######################")
print("BOLETA DE VENTA")
print("#######################")
print("#")
print("#cliente:",cliente)
print("#ITEM: ",kg,"kg papa")
print("#P.U.: s/.",precio_uni)
print("# total.: s/.",total)
print("#######################")
print("¿Comprador Compulsivo?:",comprador_compulsivo)
