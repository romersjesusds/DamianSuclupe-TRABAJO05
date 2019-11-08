#input
velocidad_1=int(input("velocidad del primer movil:"))
velocidad_2=int(input("velocidad del segundo movil:"))
distancia=int(input("distancia de separacion:"))

#processig
tiempo_alcance=(distancia)/(velocidad_2-velocidad_1)

#verificador
tiempo_previsto=(tiempo_alcance>15
                 )
#output
print("####################################################")
print("#    CALCULO DEL TIEMPO DE ALCANCE     #")
print("####################################################")
print("#")
print("#velocidad primer movil:", velocidad_1, "m/s")
print("#velocidad segundo movil:", velocidad_2, "m/s")
print("#distancia de separacion:", distancia, "metros")
print("#tiempo de alcance:", tiempo_alcance, "segundos")
print("#")
print("#####################################################")
print("El movil 2 alcannzo al movil 1  en el tiempo previsto?", tiempo_previsto)
