#CALCULADORA nro 14
# Esta calculadora realiza el calculo de la LONGITUD DE ARCO de una circunferencia

# Declaracion de la variable
angulo,radio,longitud_arco=0.0,0.0,0.0

# Calculadora
angulo=37
radio=10
longitud_arco=angulo*radio

#mostrar datos
print("angulo = ", angulo)
print("radio = ", radio)
print("longitud_arco = ", longitud_arco)

#verificador
longitud_arco_elevado=(longitud_arco>90)
print("la longitud de arco es mayor que 90 m?",  longitud_arco_elevado)
