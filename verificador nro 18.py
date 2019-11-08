#CALCULADORA nro 18
 # Esta calculadora realiza el calculo de la Aceleracion_tangencial

# Declaracion de la variable
aceleracion_angular,radio,aceleracion_tangencial=0.0,0.0,0.0

# Calculadora
aceleracion_angular=19
radio=20
aceleracion_tangencial=aceleracion_angular*radio

#mostrar datos
print("aceleracion_angular = ", aceleracion_angular)
print("radio = ", radio)
print("aceleracion_tangencial = ", aceleracion_tangencial)

#verificador
aceleracion_tangencial_elevada=(aceleracion_tangencial>50)

print("la aceleracion tangencial es mayor a 50 m/s**2?",  aceleracion_tangencial_elevada)
