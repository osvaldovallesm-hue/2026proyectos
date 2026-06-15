def revisar_presupuesto(presupuesto, gasto_real):
diferencia = presupuesto - gasto_real
porcentaje = (diferencia / presupuesto) * 100

print(f"Presupuesto: ${presupuesto:,.2f}")
print(f"Gasto real: ${gasto_real:,.2f}")
print(f"Diferencia: ${diferencia:,.2f}")
print(f"Variación: {porcentaje:.2f}%")

if gasto_real > presupuesto:
print("⚠️ Se excedió el presupuesto.")
else:
print("✅ El gasto está dentro del presupuesto.")

def main():
presupuesto = 1200000
gasto_real = 1150000

revisar_presupuesto(presupuesto, gasto_real)

if __name__ == "__main__":
main()