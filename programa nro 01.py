#input
cliente=input("cliente:")
cajero=input("cajero:")
pares_zapatos=int(input("cantidad de pares de zapatos:"))
pares_zapatillas=int(input("cantidad de pares de zapatillas:"))
pares_tacones=int(input("cantidad de pares de tacones:"))
precio_par_zapatos=int(input("precio del par de zapatos:"))
precio_par_zapatillas=int(input("precio del par de zapatillas:"))
precio_par_tacones=int(input("precio del par de tacones:"))

#processing
consumo_zapatos=pares_zapatos*precio_par_zapatos
consumo_zapatillas=pares_zapatillas*precio_par_zapatillas
consumo_tacones=pares_tacones*precio_par_tacones
consumo_total=consumo_zapatos+consumo_zapatillas+consumo_tacones
IGV=consumo_total*0.18
total_pagar=consumo_total+IGV

#verificador
comprador_compulsivo=(total_pagar>1000)

#output
print("#############################################################")
print("   ZAPATERIA - DAMIAN      ")
print("#############################################################")
print("cliente:", cliente               ,"cajero:", cajero)
print("#############################################################")
print("producto	        cantidad	     P.U.	             total")
print("#zapatos:",      pares_zapatos   ,precio_par_zapatos ,consumo_zapatos)
print("#zapatillas:",   pares_zapatillas ,precio_par_zapatillas ,consumo_zapatillas)
print("#tacones:",      pares_tacones    ,precio_par_tacones    ,consumo_tacones)
print("#############################################################")
print("#consumo:", consumo_total)
print("#IGV:", IGV)
print("total a pagar:", total_pagar)
print("#############################################################")
print("el cliente es un comprador compulsivo ?", comprador_compulsivo)
