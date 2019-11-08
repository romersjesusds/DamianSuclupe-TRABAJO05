#input
cliente=input("cliente:")
cajero=input("cajero:")
botellas=int(input("ingresar nro de botellas de aceite:"))
pu=int(input("ingresar el precio de una botella de aceite:"))

#processing
consumo_total=botellas*pu
igv=consumo_total*0.18
total_pagar=consumo_total+igv

#verificador
limite=(total_pagar<100)

#output
print("#############################################################")
print("#	BOLETA	   DE	   VENTA			    #")
print("#############################################################")
print("cliente:", cliente              , "cajero:", cajero)
print("#############################################################")
print("#")
print("#item:", botellas, "botellas de aceite")
print("#P.U.: s/.", pu, "c/u")
print("#consumo:", consumo_total)
print("#IGV: s/.", igv)
print("total a pagar: s/.", total_pagar)
print("#############################################################")
print("el total a pagar es menor que el limite?", limite)
