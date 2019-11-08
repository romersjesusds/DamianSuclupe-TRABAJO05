print("\n")
#INPUT
cliente=input("ingrese le nombre del cliente:")
cant_pantalones=int(input("ingrese cantidad de pantalones:"))
precio_uni=float(input("ingrese precio unitario:"))

#PROCESSING
total=(precio_uni*cant_pantalones)

#VERIFICADOR
comprador_compulsivo=(total==200)

# OUTPUT
print("#######################")
print("BOLETA DE VENTA")
print("#######################")
print("#")
print("#cliente:",cliente)
print("#ITEM: ",cant_pantalones,"pantalones")
print("#P.U.: s/.",precio_uni)
print("# total.: s/.",total)
print("#######################")
print("¿Comprador Compulsivo?:",comprador_compulsivo)
