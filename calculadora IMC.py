
nombre = str (input("Por favor introduce tu  nombre "))

while nombre == "":
    print ("No se puede dejar en blanco")
    nombre = input ("por Introduce tu nombre ")  

aPaterno= str (input ("Por favor introduce apellido paterno ")) 

while aPaterno == "":
    print ("No se puede dejar en blanco")
    aPaterno = input ("Por Introduce tu apellido paterno ") 

aMaterno = str (input ("Por favor introduce apellido materno "))

while aMaterno == "":
    print ("No se puede dejar en blanco")
    aMaterno = input ("por Introduce apellido materno ")

edad = (input ("Por favor ingrese su edad en años "))

peso = float(input ("Por favor introduce tu peso "))

estatura = float(input ("Por favor introduce tu estatura "))

indice = peso / estatura ** 2

print (f"Su indice de masa corporal es de: {indice}")