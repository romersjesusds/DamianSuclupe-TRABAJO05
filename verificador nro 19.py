#CALCULADORA nro 19
# Esta calculadora realiza el calculo del area del trapezio

# Declaracion de la variable
base_mayor,base_menor,altura,area_trapezio=0.0,0.0,0.0,0.0

# Calculadora
base_mayor=120
base_menor=90
altura=20
area_trapezio=(base_mayor + base_menor)*altura/2

#mostrar datos
print("base_mayor = ", base_mayor)
print("base_menor = ", base_menor)
print("altura = ", altura)
print("area_trapezio = ", area_trapezio)

#verificador
area_trapezio_elevada=(area_trapezio>100)

print("el area del trapecio es mayor a 100 m**2?",  area_trapezio_elevada)
