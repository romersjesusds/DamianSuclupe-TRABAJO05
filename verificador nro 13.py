#CALCULADORA nro 13
# Esta calculadora realiza el calculo de la Velocidad Tangencial

# Declaracion de la variable
longitud_arco,tiempo,velocidad_tangencial=0.0,0.0,0.0

# Calculadora
longitud_arco=3200
tiempo=32
velocidad_tangencial=longitud_arco/tiempo

#mostrar datos
print("longitud_arco = ", longitud_arco)
print("tiempo =", tiempo)
print("velocidad_tangencial = ", velocidad_tangencial)

#verificador
velocidad_tangencial_reducida=(velocidad_tangencial<80)
print("la velocidad tangencial es menor que 80 m/s?", velocidad_tangencial_reducida)
