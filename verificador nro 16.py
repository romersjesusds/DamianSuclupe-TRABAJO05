#CALCULADORA nro 16
# Esta calculadora realiza el calculo del volumen del cubo

# Declaracion de la variable
arista,volumen_cubo=0.0,0.0

# Calculadora
arista=30
volumen_cubo=arista*arista*arista

#mostrar datos
print("arista = ", arista)
print("volumen_cubo = ", volumen_cubo)

#verificador
volumen_elevado=(volumen_cubo>150)
print("el valor del volumen del cubo es mayor que 150 m**3?", volumen_elevado)
