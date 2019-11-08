#CALCULADORA nro4
# Esta calculadora realiza el calculo de la Densidad en kg/m*m*m

# Declaracion de la variable
masa2,volumen,densidad=0.0,0.0,0.0

# Calculadora
masa2=190
volumen=19
densidad=masa2/volumen

#mostrar datos
print("masa2 = ", masa2)
print("volumen = ", volumen)
print("densidad = ", densidad)

#verificador
densidad_elevada=(densidad>500)

print("la densidad es mayor a 500 kg/m**3 ?",  densidad_elevada)
