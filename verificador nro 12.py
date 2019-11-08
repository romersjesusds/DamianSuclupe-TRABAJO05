#CALCULADORA nro 12
# Esta calculadora realiza el calculo de la Velocidad Angular

# Declaracion de la variable
angulo,tiempo,velocidad_angular=0.0,0.0,0.0

# Calculadora
angulo=45
tiempo=14
velocidad_angular=angulo/tiempo

#mostrar datos
print("angulo = ", angulo)
print("tiempo = ", tiempo)
print("velocidad_angular = ", velocidad_angular)

#verificador
velocidad_angular_elevada=(velocidad_angular>100)
print("la velocidad angular es mayor a 100 rad/s?",  velocidad_angular_elevada)
