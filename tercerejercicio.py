#Una empresa necesita saber cuándo aplicar los descuentos 25% si el monto es mayor o igual que $300 20% si el monto es mayor que 150
# y menor que $300. No se le aplicaria descuento si el monto es menor a $150
print("10. DADO UN MONTO, CALCULAR EL DESCUENTO.")
monto = float(input("Ingrese Monto : "))
if monto > 300:
    descuento = monto * 0.25
    print("El Descuento es : ", descuento)
elif (monto > 150) and (monto < 300):
    descuento = monto * 0.02
    print("El Descuento es : ", descuento)
else:
     print("No Hay Descuento")