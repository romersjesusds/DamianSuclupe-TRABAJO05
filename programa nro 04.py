#input
cliente=input("cliente:")
empresa_azucarera=input("empresa azucarera:")
quintales_azucar=int(input("ingrese el nro de quintales de azucar:"))
precio_quintal=int(input("precio por cada quintal de azuca:"))

#processing
total=quintales_azucar*precio_quintal
igv=total*0.18
total_pagar=total+igv

#verificador
comerciante=(total_pagar>700
             )
#output
print("#############################################################")
print("#           AZUCAR       POMALCA		           #")
print("#############################################################")
print("cliente:", cliente          ,"empresa azucarera:", empresa_azucarera)
print("#############################################################")
print("#")
print("#item:", quintales_azucar, "quintales de azucar")
print("#P.U.:", precio_quintal)
print("#total:", total)
print("#IGV:", igv)
print("total a pagar:", total_pagar)
print("#############################################################")
print("el cliente es un comerciante de azucar ?", comerciante)
