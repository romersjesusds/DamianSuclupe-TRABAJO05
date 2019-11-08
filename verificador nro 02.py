 #CALCULADORA nro 02
# Esta calculadora realiza el calculo de la fuerza

# Declaracion de la variable
masa,aceleracion,fuerza=0.0,0.0,0.0

# Calculadora
masa=16
aceleracion=10
fuerza=masa*aceleracion

#mostrar datos
print("masa = ", masa)
print("aceleracion = ", aceleracion)
print("fuerza = ", fuerza)

#verificador
fuerza_elevada=(fuerza>100)
 print("la fuerza realizada es mayor a 100 newton?", fuerza_elevada)
