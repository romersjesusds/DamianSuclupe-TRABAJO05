#CALCULADORA nro5
# Esta calculadora realiza el calculo de la Energia

# Declaracion de la variable
masa3,velocidad_luz,energia=0.0,0.0,0.0

# Calculadora
masa3=100
velocidad_luz=300000000
energia=masa3*velocidad_luz*velocidad_luz

#mostrar datos
print("masa3 = ", masa3)
print("velocidad_luz = ", velocidad_luz)
print("energia = ", energia)

#verificador
velocidad=(velocidad_luz<100000)

print("el valor de la velocidad de la luz, es menor a 100000 m/s?", velocidad)
