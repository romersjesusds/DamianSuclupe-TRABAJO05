#CALCULADORA nro6
# Esta calculadora realiza el calculo de la Distancia

# Declaracion de la variable
velocidad,tiempo=0.0,0.0

# Calculadora
velocidad=30
tiempo=15
distancia=velocidad*tiempo

#mostrar datos
print("velocidad = ", velocidad)
print("tiempo = ", tiempo)
print("distancia = ", distancia)

#verificador
distancia_recorrida=(distancia>200)

print("la distancia recorrida es mayor a 200 metros?",  distancia_recorrida)
