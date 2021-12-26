#DEBER_ELABORADO_POR_JUAN_INGUILLAY
#Tipos de datos y acciones elementales
#Ejercicio_1
#“Hola Mundo" -> string o cadena de carácter
#Verdadero -> Tipo bool 
#"1" -> string o cadena de carácter
# "c" -> string o cadena de carácter
# 256 -> Tipo int 
# 8>19 -> Tipo bool
# Ejercicio_2
operacion_1=(5+3*2)+9 > 3*5*14 % 3
print(operacion_1)#Tipo de dato "True" -> bool
operacion_2= 2*(4-10+8)/2*36*(1/2)
print(operacion_2)#Tipo de dato "36.0"-> float
operacion_3=260 / 12 + 54%3-85 % 7
print(operacion_3)#Tipo de dato "20.66666" -> float
operacion_4= (48 < 2 * 3) or (2 * 7 < 12)
print(operacion_4)#Tipo de dato "False" -> bool
operacion_5=((8 > 2) or (932 < 23) ) and 4 == 2
print(operacion_5)#Tipo de dato "False" -> bool
#Ejercicio_4
num1=int(input("Ingrese un número: "))
num2=int(input("Ingrese otro número: "))
suma= num1 + num2
resta= num1- num2
multiplicacion= num1*num2
division = num1/num2
modulo = num1%num2
print(suma)
print(resta)
print(division)
print(modulo)
#Ejercicio_5
a=int(input("Ingrese un número: "))
b=int(input("Ingrese otro número: "))
c=int(input("Ingrese otro número: "))
resolvente_1= (-b+((b**2-(4*a*c))**(1/2)))/(2*a)
resolvente_2= (-b-((b**2-(4*a*c))**(1/2)))/(2*a)
print("El resultado es {} {}".format(resolvente_1,resolvente_2))
#Ejercicio_6
lado1=float(input("Ingrese el primer lado: "))
lado2=float(input("Ingrese el segundo lado: "))
hipotenusa= (lado1**2 + lado2**2)**(1/2)
print("La hipotenusa es: {}".format(hipotenusa))
#Ejercicio_7
num1=int(input("Ingresar un número: "))
if (num1%2==0):
    print("0")
else:
    print("1")
#Ejercicio_9
#Método 1 -> función count
numer_bin=input("Ingrese un número binario de 4 dígitos: ")
cantidad=numer_bin.count("1")
if (cantidad%3==0):
    print("1")
else:
    print("0")
#Método 2 -> utilizando for
numer_bin=input("Ingrese un número binario de 4 dígitos: ")
contador=0
for numero1 in numer_bin:
    if (numero1=="1"):
        contador+=1
    else:
        contador+=0
if (contador%3==0):
    print("1")
else:
    print("0")
#Ejercicio_10
#Método_1 -> usando indexación
numer_bin=input("Ingrese un número binario de 4 dígitos: ")
valor1=numer_bin[0]       
valor2=numer_bin[1]       
valor3=numer_bin[2]       
valor4=numer_bin[3]       
total=0
if (valor1=="1"):
    total+=(2**3)
if (valor2=="1"):
    total+=(2**2)
if (valor3=="1"):
    total+=(2**1)    
if (valor4=="1"):
    total+=(2**0)
print("El valor del número binario {} es: {} ".format(numer_bin,total))
#Método_2 -> usando for
numer_bin=input("Ingrese un número binario de 4 dígitos: ")
exponente=3
total=0
for numero1 in numer_bin:
    if (numero1=="1"):
        total+=(2**exponente)
    exponente-=1
print("El valor del número binario {} es: {} ".format(numer_bin,total))
#Ejercicio_11
numero = int(input("Ingrese un numero entero de 4 digitos: "))
umil = numero / 1000
tmp = numero % 1000
centenas = tmp / 100
tmp = tmp % 100
decenas = tmp / 10
unidades = tmp % 10
print("Mil: %i" % umil)
print("Centenas: %i" % centenas)
print("Decenas: %i" % decenas)
print("Unidades: %i" % unidades)
#Estructuras de Control de Flujo de Datos
#Ejercicio_1 
fecha=int(input("Ingrese la fecha: "))
año=int((str(fecha)[4:]))
if ((año%400==0 or año%4==0) and año%100!=0 ):
    print("El año {} es bisiesto.".format(año))
else:
    print("El año {} no es bisiesto.".format(año))
#Ejercicio_2
numero=input("Ingrese un número de 5 dígitos: ")
num_alreves=numero[::-1]
if (numero==num_alreves):
    print("El número {} es capicúa.".format(numero))
else:
    print("El número {} no es capicúa.".format(numero))
#Ejercicio_3
hora=int(input("Ingrese las horas: "))
minutos=int(input("Ingrese los minutos: "))
resultado= hora*(3600) + minutos*(60)
print("El equivalente de segundos es: ",resultado)
#Ejercicio_4
valor=int(input("Ingrese un entero positivo: "))
while(valor<0):
    valor=int(input("Ingrese un entero positivo: "))
minutos=int(valor*(1/60))
horas=int(minutos*(1/60))
dias=int(horas*(1/24))
print("El equivalente en minutos es {}, en horas es {} y en días es {}".format(minutos,horas,dias))
#Ejercicio_5
A=int(input("Valor de A: "))
B=int(input("Valor de B: "))
C=int(input("Valor de C: "))
while(A<0 or B<0 or C<0):
    print("¡Ingrese valores positivos!")
    A=int(input("Valor de A: "))
    B=int(input("Valor de B: "))
    C=int(input("Valor de C: "))
if(A>B and A>C):
    if(B>C):
        print("A es el mayor y B es el segundo mayor")
    else:
        print("A es el mayor y C es el segundo mayor")
if(B>A and B>C):
    if(A>C):
        print("B es el mayor y A es el segundo mayor")
    else:
        print("B es el mayor y C es el segundo mayor")
if(C>A and C>B):
    if(A>B):
        print("C es el mayor y A es el segundo mayor")
    else:
        print("C es el mayor y B es el segundo mayor")
#Ejercicio_6
hora_entrada=int(input("Ingrese la hora de entrada(formnato 12 horas): "))
while(hora_entrada>12 or hora_entrada<0):
    print("¡Ingrese una hora de entrada correcta!")
    hora_entrada=int(input("Ingrese la hora de entrada: "))
minutos_entrada=int(input("Ingrese los minutos de la hora de entrada: "))
while(minutos_entrada>60 or minutos_entrada<0):
    print("¡Ingrese minutos correctos!")
    minutos_entrada=int(input("Ingrese los minutos de la hora de entrada: "))
Am_Pm=input("Ingrese el horario de entrada: ")
while(Am_Pm!="A" and Am_Pm!="P"):
    print("¡Ingrese un horario correcto!")
    Am_Pm=input("Ingrese el horario de entrada: ")
hora_salida=int(input("Ingrese la hora de salida(formato 12 hora): "))
while(hora_salida>12 or hora_salida<0):
    print("¡Ingrese una hora de salida correcta!")
    hora_salida=int(input("Ingrese la hora de salida: "))
minutos_salida=int(input("Ingrese los minutos de la hora de salida: "))
while(minutos_salida>60 or minutos_salida<0):
    print("¡Ingrese minutos correctos!")
    minutos_salida=int(input("Ingrese los minutos de la hora de salida: "))
Am_Pm2=input("Ingrese el horario de salida: ")
while(Am_Pm2!="A" and Am_Pm2!="P"):
    print("¡Ingrese un horario correcto!")
    Am_Pm2=input("Ingrese el horario de salida: ")
if Am_Pm == "A" and Am_Pm2 == "A" or Am_Pm == "P" and Am_Pm2 == "P":
    resta_Horas = hora_entrada - hora_salida
    Total_Horas = resta_Horas * 4
    resta_Minutos = minutos_entrada - minutos_salida
    Total_Minutos = resta_Minutos/30
    Total_M_2 = 0
    if Total_Minutos < 0 :
        Total_M_2 = 2.50
        Total_Tiempo = Total_Horas + Total_M_2
        print("El Total a cancelar es: Bs ", Total_Tiempo)
elif Am_Pm == "A" and Am_Pm2 == "P":
    hora_salida+=12
    resta_Horas = hora_entrada - hora_salida
    Total_Horas = resta_Horas * 4
    resta_Minutos = minutos_entrada - minutos_salida
    Total_Minutos = resta_Minutos/30
    Total_M_2 = 0
    if Total_Minutos < 0 :
        Total_M_2 = 2.50
        Total_Tiempo = Total_Horas + Total_M_2
        print("El Total a cancelar es: Bs ", Total_Tiempo)
#Ejercicio_7
libra=float(input("Ingrese su peso en libras: "))
centimetros=float(input("Ingrese su estatura en centímetros: "))
peso=libra*0.453592
estatura=centimetros/100
MC=peso/(estatura)**2
if(MC<16):
    print("Criterio de ingreso.")
elif(16<=MC<=16.9):
    print("Infra peso.")
elif(17<=MC<=18.4):
    print("Bajo peso.")
elif(18.5<=MC<=24.9):
    print("Peso normal.")
elif(25<=MC<=29.9):
    print("Sobrepeso.")
elif(30<=MC<=34.9):
    print("Obesidad pre-mórbida.")
elif(40<=MC<=45):
    print("Obesidad mórbida.")
elif(MC>45):
    print("Obesidad híper-mórbida.")
#Ejercicio_8
dia= int(input("Ingrese un dia: "))
while(dia<=0 or dia>31) :
    print("¡Ingrese un día correcto!")
    dia= int(input("Ingrese un dia: "))
mes= int(input("Ingrese un mes: "))
while(mes<=0 or mes>12):
    print("¡Ingrese un mes correcto!")
    mes= int(input("Ingrese un mes: "))
diasMes_bisiesto = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
i=0
acumulador = 0
total=0
while (i<=mes-1):
    acumulador = acumulador + diasMes_bisiesto[i]
    i = i + 1
    total = acumulador + dia
print("EL total de dias que han transcurrido es: ", total)
#Ejercicio_9
meses=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
mes=int(input("Ingrese el número de mes a encontrar: "))
print("Su mes ingresado es {}".format(meses[mes-1]))
#Ejericio_10
monto_a_pagar=int(input("Ingrese el valor total de compra: "))
if(monto_a_pagar>1000):
    monto_desc=monto_a_pagar*0.20
    print("El total a pagar es: ",monto_a_pagar-monto_desc)
else:
    print("El total a pagar es: ",monto_a_pagar)
#Estructuras Iterativas
#Ejercicio_1
numero=input("Ingrese un número entero: ")
digitos=0
for i in range(len(numero)):
    digitos+=1
print("El total de dígitos es: ",digitos)
#Ejercicio_2
numero=input("Ingrese un número: ")
capicua=numero[::-1]
comprobacion=0
for i in range(len(numero)):
    if numero[i] == capicua[i]:
        comprobacion+=1
if comprobacion==len(numero):
    print("El número es capicúa")
else:
    print("El número no es capicúa")
#Ejercicio_3
numero=int(input("Ingrese un número: "))
valor= range(2,numero)
contador = 0
for n in valor:
  if numero % n == 0:
    contador +=1
if contador > 0 :
  print("El número no es primo" )
else:
  print("El nÚmero es primo")
#Ejercicio_4
numero=int(input("Ingrese el número para calcular el factorial: "))
factorial_total = 1
while (numero>1):
    factorial_total *= numero
    numero-= 1
print("El resultado es: ",factorial_total)
#Ejercicio_5
contraseña=int(input("Ingrese una contraseña: "))
while(len(str(contraseña))<10):
    print("¡Contraseña insegura!")
    contraseña=int(input("Ingrese una contraseña de al menos 10 dígitos: "))
intento=int(input("Ingrese la contraseña: "))
while(intento!=contraseña or len(str(intento))<10):
    print("¡Contraseña Incorrecta!")
    intento=int(input("Ingrese la contraseña: "))
print("¡Contraseña Correcta!")
#Ejercicio_6
numeros=1
lista_numeros=[]
while(numeros!=0):
    numeros=int(input("Ingrese un número: "))
    if numeros!=0:
        lista_numeros.append(numeros)
mayor=max(lista_numeros)
menor=min(lista_numeros)
print("El número mayor es {} y el menor es {}".format(mayor,menor))
#Ejercicio_7
edad=1
peso=1
estatura=1
lista_edades=[]
lista_pesos=[]
lista_estaturas=[]
while(edad!=0 and peso!=0 and estatura!=0):
    edad=int(input("Ingrese una edad: "))
    peso=int(input("Ingrese un peso: "))
    estatura=int(input("Ingrese una estatura: "))
    if (edad!=0 and peso!=0 and estatura!=0):
        lista_edades.append(edad)
        lista_pesos.append(peso)
        lista_estaturas.append(estatura)
promedio_edad=sum(lista_edades)/len(lista_edades)
promedio_pesos=sum(lista_pesos)/len(lista_pesos)
promedio_estaturas=sum(lista_estaturas)/len(lista_estaturas)
lista_18y25=[]
lista_36=[]
peso_18y35=[]
for i in range(len(lista_edades)):
    if (18<=lista_edades[i]<=25):
        lista_18y25.append(lista_edades[i])
    elif (lista_edades[i]>36):
        lista_36.append(lista_edades[i])
    elif(18<=lista_edades[i]<=35):
        peso_18y35.append(lista_pesos[i])
promedio_peso18y35=sum(peso_18y35)/len(peso_18y35)
print("El promedio de edades en general es: ",promedio_edad)
print("El promedio de pesos en general: ",promedio_pesos)
print("El promedio de estaturas en general: ",promedio_estaturas)
print("Hay {} con edad entre los 18 y 25 años".format(len(lista_18y25)))
print("Hay {} con edad mayor a 36 años".format(len(lista_36)))
print("El promedio de pesos de las personas entre 18 y 35 años es: ",promedio_peso18y35)
#Ejercicio_8
for i in range(1, 10 + 1):
	print("Tabla de multiplicar del {}:".format(i)) 
	for j in range(1, 12 + 1):
		print("{} x {} = {}".format(i,j,i*j))
	print() 
#Ejercicio_9
lista_fichas=[]
for i in range(1,8):
    lista_fichas.append("0-{}".format(i-1))
for j in range(1,7):
    lista_fichas.append("1-{}".format(j))
for k in range(1,6):
    lista_fichas.append("2-{}".format(k+1))
for l in range(1,5):
    lista_fichas.append("3-{}".format(l+2))
for m in range(1,4):
    lista_fichas.append("4-{}".format(m+3))    
for n in range(1,3):
    lista_fichas.append("5-{}".format(n+4))
lista_fichas.append("6-{}".format(6))
print("---FICHAS DE DOMINO---")
for ficha in lista_fichas:
    print("Ficha: ",ficha)
#Ejercicio_10
numero=2
lista_numeros=[]
while(numero!=0):
    numero=int(input("Ingrese un número: "))    
    if numero==0:
        print("Programa terminado...")
    if numero>1:
        lista_numeros.append(numero)
    if numero<=1 and numero!=0:
        print("¡Ingrese números positivos mayores a 1!")
print("El promedio de la serie ingresada es: ",sum(lista_numeros)/len(lista_numeros))







































