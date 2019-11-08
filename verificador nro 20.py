#CALCULADORA nro 20
# Esta calculadora realiza el calculo de la Presion Hidrostatica

# Declaracion de la variable
densidad_liquido,gravedad,altura,presion_hidrostatica=0.0,0.0,0.0,0.0

# Calculadora
densidad_liquido=1000
gravedad=9.8
altura=5
presion_hidrostatica=densidad_liquido*gravedad*altura

#mostrar datos
print("densidad_liquido = ", densidad_liquido)
print("gravedad = ", gravedad)
print("altura = ", altura)
print("presion_hidrostatica = ", presion_hidrostatica)

#verificador
verificador=(presion_hidrostatica<300)

print("la presion hidrotatica es menor a 300 pascales?", verificador)
