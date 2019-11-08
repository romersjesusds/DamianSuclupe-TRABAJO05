#input
cliente=input("cliente:")
florista=input("florista:")
ramos_flores=int(input("ingresar la cantidad de ramos de flores:"))
pu=int(input("precio de un ramo de flores:"))
#processing
consumo_total=ramos_flores*pu
igv=consumo_total*0.18
total_pagar=consumo_total+igv

#verificador
revendedor=(total_pagar>150)

#output
print("#############################################################")
print("#	FLORERIA - MI ROSA      ")
print("#############################################################")
print("cliente:", cliente               ,"florista:", florista)
print("#############################################################")
print("#")
print("#item:", ramos_flores, "ramos de flores")
print("#P.U.: s/.", pu)
print("#consumo: s/.", consumo_total)
print("#IGV: s/.", igv)
print("total a pagar: s/.", total_pagar)
print("#############################################################")
print("el cliente es un revendedor de flores?", revendedor)
