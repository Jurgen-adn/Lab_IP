#solicitar el total de la cuenta en un restaurante
total = float(input("ingrese el total de la cuenta a pagar:"))
personas = int (input("numero de personas en la mesa :"))
propina = float (input("ingrese el porcentaje de propina que desea dejar:"))
total = total + (total * propina / 100)
pago_por_persona = total / personas
print(f"el pago por persona es: {pago_por_persona}")