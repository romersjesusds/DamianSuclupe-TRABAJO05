#CALCULADORA nro 17
# Esta calculadora realiza el calculo del area lateral de un prisma

# Declaracion de la variable
prerimetro_base,altura,area_lateral_prisma=0.0,0.0,0.0

# Calculadora
prerimetro_base= 120
altura=13
area_lateral_prisma=prerimetro_base*altura

#mostrar datos
print("prerimetro_base = ", prerimetro_base)
print("altura = ", altura)
print("area_lateral_prisma = ", area_lateral_prisma)

#verificador
area_lateral_prisma_elevada=(area_lateral_prisma>10)
print("el prisma tiene un area lateral mayor a 10 m**2?", area_lateral_prisma)
