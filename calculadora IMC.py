
nombre = (input("Por favor introduce tu nombre ") )

aPaterno= str (input ("Por favor introduce apellido paterno ")) 

aMaterno = str (input ("Por favor introduce apellido materno "))

edad =  int (input ("por favor ingrese su edad en años: "))

peso = float (input ("Por favor introduce tu peso ")) 

estatura = float (input ("Por favor introduce tu estatura "))
indice = peso / estatura ** 2

print (f"Su indice de masa corporal es de: {indice}")