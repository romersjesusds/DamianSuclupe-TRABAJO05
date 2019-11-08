#CALCULADORA nro 10
# Esta calculadora realiza el calculo de la Presion

# Declaracion de la variable
fuerza,area,presion=0.0,0.0,0.0

# Calculadora
fuerza=1200
area=41
presion=fuerza/area

#mostrar datos
print("fuerza = ", fuerza)
print("area = ", area)
print("presion = ", presion)

#verificador
presion_elevada=(presion>200)

print("la presion que se ejerce supera  200 pascales ?", presion_elevada)
