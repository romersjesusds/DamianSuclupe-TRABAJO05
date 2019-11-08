#input
cliente=input("cliente:")
tienda=input("ingresar nombre de vendedor:")
nro_chompas=int(input("nro de chompas:"))
pu=int(input("precio de cada chompa:"))

#processing
pago_chompas=nro_chompas*pu
igv=pago_chompas*0.18
total_pagar=pago_chompas+igv

#verificador
limite=(nro_chompas>50)

#output
print("#############################################################")
print("#    Tienda -  ABRIGOS QUE ABRIGAN			    #")
print("#############################################################")
print("cliente:", cliente             ,"vendedor:", vendedor)
print("#############################################################")
print("#")
print("#item:", nro_chompas, "chompas")
print("#P.U.: s/.", pu)
print("#pago por chompas: s/.", pago_chompas)
print("#IGV: s/.", igv)
print("total a pagar: s/.", total_pagar)
print("#############################################################")
print("el cliente compra chompas en cantidad?", limite)
