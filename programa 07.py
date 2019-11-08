#input
cliente=input("cliente:")
spa=input("spa:")
servicio1=input("servicio1:")
servicio2=input("servicio2:")
costo_servicio1=int(input("costo por el servicio 01:"))
costo_servicio2=int(input("costo servicio 02:"))

#processing
costo=costo_servicio1+costo_servicio2
igv=costo*0.18
total_pagar=costo+igv

#verificador
pago_limite=(total_pagar>100)

#output
print("#############################################################")
print("#  SPA - MI ANGELA			                               #")
print("#############################################################")
print("cliente:", cliente,               "spa:", spa)
print("#############################################################")
print("#")
print("#servicio 1:",servicio1)
print("#servicio 2", servicio2)
print("#precio servicio 1:", costo_servicio1)
print("precio servicio 2:", costo_servicio2)
print("#costo:", costo)
print("#IGV:", igv)
print("total a pagar:", total_pagar)
print("#############################################################")
print("el cliente supera el pago limite?", pago_limite)
