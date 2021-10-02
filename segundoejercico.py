#Para pagar impuesto un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos superiores a 1000 € mensuales.
 #Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no

edad = int(input("¿Cuál es tu edad? "))
sueldo = float(input("¿Cuales son tus ingresos mensuales?"))
if edad > 18 and sueldo >= 300:
    print("Tienes que pagar impuestos")
else:
    print("No tienes que pagar impuestos")