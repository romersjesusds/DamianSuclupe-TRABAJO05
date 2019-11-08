#CALCULADORA nro7
# Esta calculadora realiza el calculo de la Frecuencia en

# Declaracion de la variable
revoluciones,tiempo,frecuencia=0.0,0.0,0.0

# Calculadora
revoluciones=300
tiempo=15
frecuencia=revoluciones/tiempo

#mostrar datos
print("revoluciones = ", revoluciones)
print("tiempo = ", tiempo)
print("frecuencia = ", frecuencia)

#verificador
frecuencia_elevada=(frecuencia>200)
print("la frecuencia es mayor a 200?",  frecuencia_elevada )
