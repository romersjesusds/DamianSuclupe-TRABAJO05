#CALCULADORA nro9
# Esta calculadora realiza el calculo de la Energia Potencial Gravitatoria

# Declaracion de la variable
masa,gravedad,altura,energia_potencial_gravitatoria=0.0,0.0,0.0,0.0

# Calculadora
masa=20
gravedad=9.8
altura=12
energia_potencial_gravitatoria=masa*gravedad*altura

#mostrar datos
print("masa = ", masa)
print("gravedad = ", gravedad)
print("altura = ", altura)
print("energia_potencial_gravitatoria = ", energia_potencial_gravitatoria)

#verificador
energia_elevada=(energia_potencial_gravitatoria>100)

print("la energia potencial gravitatoria es mayor a 100 joules?",  energia_elevada)
