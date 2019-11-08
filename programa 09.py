#input
velocidad_1=int(input("velocidad del primer movil:"))
velocidad_2=int(input("velocidad del segundo movil:"))
distancia=int(input("distancia de separacion:"))

#processing
tiempo_encuentro=(distancia)/(velocidad_1+velocidad_2)

#verificador
tiempo_previsto=(tiempo_encuentro>10)

#output
print("####################################################")
print("#    CALCULO DEL TIEMPO DE ENCUENTRO     #")
print("####################################################")
print("#")
print("#velocidad primer movil:", velocidad_1, "m/s")
print("#velocidad segundo movil:", velocidad_2, "m/s")
print("#distancia de separacion:", distancia, "metros")
print("#tiempo de encuentro:", tiempo_encuentro)
print("#")
print("#####################################################")
print("los moviles se encontraron en el tiempo previsto?", tiempo_previsto)
