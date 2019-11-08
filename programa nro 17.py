print("\n")
#INPUT
cliente=input("ingrese le nombre del cliente:")
n_horas=int(input("ingrese cantidad de horas:"))
precio_hora=float(input("ingrese precio por hora"))

#PROCESSING
total=(precio_hora*n_horas)

#VERIFICADOR
cobro_alto=(total>250)

# OUTPUT
print("#######################")
print("BOLETA DE VENTA")
print("#######################")
print("#")
print("#cliente:",cliente)
print("#ITEM: ",n_horas,"horas")
print("#P.U.: s/.",precio_hora)
print("# total.: s/.",total)
print("#######################")
print("¿Cobro alto?:",Cobro_alto)
