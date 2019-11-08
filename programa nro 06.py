#input
cliente=input("cliente:")
vendedor=input("vendedor:")
kg_papas=int(input("ingresar los kg de papas:"))
precio_kg=int(input("precio de un kg de papas:"))

#processing
consumo_total=kg_papas*precio_kg
igv=consumo_total*0.18
total_pagar=consumo_total+igv

#verificador
consumo_limite=(total_pagar>100)
#output
print("#############################################################")
print("#	BODEGA  -       MI FERNANDITO			    #")
print("#############################################################")
print("cliente:", cliente,    "     vendedor:", vendedor)
print("#############################################################")
print("#")
print("#item:", kg_papas, "kg de papas")
print("#Precio por kg: s/.", precio_kg)
print("#consumo: s/.", consumo_total)
print("#IGV: s/.", igv)
print("total a pagar: s/.", total_pagar)
print("#############################################################")
print("El consumo del cliente supera el limite?", consumo_limite)
