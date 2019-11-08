print("\n")
#INPUT
cliente=input("ingrese le nombre del cliente:")
n_personas=int(input("ingrese cantidad de personas:"))
costo_persona=float(input("ingrese precio por persona"))

#PROCESSING
total=(costo_persona*n_personas)

#VERIFICADOR
alto_dinero_recaudado=(total>2000)

# OUTPUT
print("#######################")
print("BOLETA DE VENTA")
print("#######################")
print("#")
print("#cliente:",cliente)
print("#ITEM: ",n_personas,"personas")
print("#P.U.: s/.",costo_persona)
print("# total.: s/.",total)
print("#######################")
print("¿alto dinero recaudado?:",alto_dinero_recaudado)
