print("\n")
#INPUT
cliente=input("ingrese le nombre del cliente:")
n_cachorros=int(input("ingrese cantidad de cachorros:"))
precio_cachorro=float(input("ingrese precio por cachorro"))

#PROCESSING
total=(n_cachorros*precio_cachorro)

#VERIFICADOR
malgastador=(total>3000)

# OUTPUT
print("#######################")
print("BOLETA DE VENTA")
print("#######################")
print("#")
print("#cliente:",cliente)
print("#ITEM: ",n_cachorros,"cachorros")
print("#P.U.: s/.",precio_cachorro)
print("# total.: s/.",total)
print("#######################")
print("¿malgastador?:",malgastador)
