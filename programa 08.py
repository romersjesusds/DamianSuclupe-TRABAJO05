#input
usuario=input("ingresar el nombre del usuario:")
operadora_internet=input("nombre de operadora:")
gigas_usadas=int(input("total gigas usadas:"))
costo_giga=int(input("costo por cada giga de internet usada:"))

#processing
total=gigas_usadas*costo_giga
igv=total*0.18
total_pagar=total+igv

#verificador
gigas_limite=(gigas_usadas>50)

#output
print("#############################################################")
print("#	BITEL- TELEFONIA DE TODOS			                   #")
print("#############################################################")
print("cliente:", usuario,             "operadora:", operadora_internet)
print("#############################################################")
print("#")
print("#gigas usadas:", gigas_usadas)
print("#costo por giga:", costo_giga)
print("#total:", total)
print("#IGV:", igv)
print("total a pagar:", total_pagar)
print("#############################################################")
print("el cliente se exedio en el uso de gigas?", gigas_limite)
