#CALCULADORA nro 11
# Esta calculadora realiza el calculo de Cantidad de Movimiento

# Declaracion de la variable
masa,velocidad,Cantidad_de_Movimiento=0.0,0.0,0.0

# Calculadora
masa=14
velocidad=18
Cantidad_de_Movimiento=masa*velocidad

#mostrar datos
print("masa = ", masa)
print("velocidad = ", velocidad)
print("Cantidad_de_Movimiento = ", Cantidad_de_Movimiento)

#verificador
cantidad_elevada=(Cantidad_de_Movimiento>200)

print("la cantidad de movimento, es mayor que 200 kg.m/s?", cantidad_elevada)
