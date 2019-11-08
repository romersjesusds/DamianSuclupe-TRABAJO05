print("\n")
#INPUT
cliente=input("ingrese le nombre del cliente:")
cant_libros=int(input("ingrese cantidad de libros:"))
precio_uni=float(input("ingrese precio unitario"))

#PROCESSING
total=(precio_uni*cant_libros)

#VERIFICADOR
comprador_compulsivo=(total>500)

# OUTPUT
print("#######################")
print("BOLETA DE VENTA")
print("#######################")
print("#")
print("#cliente:",cliente)
print("#ITEM: ",cant_libros,"libros")
print("#P.U.: s/.",precio_uni)
print("# total.: s/.",total)
print("#######################")
print("¿Comprador Compulsivo?:",comprador_compulsivo)
