print("\n")
#INPUT
cliente=input("ingrese le nombre del cliente:")
n_monedas=int(input("ingrese cantidad de monedas:"))
valor_moneda=float(input("ingrese el valor nominal de la moneda"))

#PROCESSING
total=(valor_moneda*n_monedas)

#VERIFICADOR
mucho_dinero=(total>500)

# OUTPUT
print("#######################")
print("BOLETA DE VENTA")
print("#######################")
print("#")
print("#cliente:",cliente)
print("#ITEM: ",n_monedas,"monedas")
print("#V.N.: s/.",valor_moneda)
print("# total.: s/.",total)
print("#######################")
print("¿Mucho dinero?:",mucho_dinero)
