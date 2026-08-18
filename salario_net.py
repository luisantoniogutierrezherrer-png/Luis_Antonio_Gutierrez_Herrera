# Programa para calcular el salario neto #

salario_bruto = float(input("Introduce el salario bruto: "))
porcentaje_impuestos = float(input("Introduce el porcentaje de impuestos (ejemplo: 16): "))
deducciones = float(input("Introduce el monto total de otras deducciones: "))

retencion_impuestos = salario_bruto * (porcentaje_impuestos / 100)

salario_neto = salario_bruto - retencion_impuestos - deducciones

print(f"El salario neto final es: {salario_neto:.2f}")