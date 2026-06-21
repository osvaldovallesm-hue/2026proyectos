def revisar_presupuesto(presupuesto, gasto_real, avance_periodo):
    """
    presupuesto: presupuesto total aprobado
    gasto_real: gasto acumulado a la fecha
    avance_periodo: porcentaje transcurrido del período (0-100)
    """

    if presupuesto <= 0:
        raise ValueError("El presupuesto debe ser mayor que cero.")

    if not 0 < avance_periodo <= 100:
        raise ValueError("El avance del período debe estar entre 0 y 100.")

    # Métricas actuales
    disponible = presupuesto - gasto_real
    porcentaje_utilizado = (gasto_real / presupuesto) * 100

    print("=" * 50)
    print("REVISIÓN PRESUPUESTARIA")
    print("=" * 50)
    print(f"Presupuesto aprobado : ${presupuesto:,.2f}")
    print(f"Gasto acumulado      : ${gasto_real:,.2f}")
    print(f"Disponible           : ${disponible:,.2f}")
    print(f"Uso del presupuesto  : {porcentaje_utilizado:.2f}%")

    # Alertas tempranas
    if porcentaje_utilizado > 100:
        exceso = gasto_real - presupuesto
        print(f"🔴 Presupuesto excedido por ${exceso:,.2f}")
    elif porcentaje_utilizado >= 95:
        print("🟠 Riesgo crítico: presupuesto casi agotado.")
    elif porcentaje_utilizado >= 85:
        print("🟡 Alerta preventiva: consumo elevado.")
    else:
        print("🟢 Presupuesto bajo control.")

    # Comparación contra lo esperado
    gasto_esperado = presupuesto * (avance_periodo / 100)

    print("\n--- Seguimiento del período ---")
    print(f"Avance del período   : {avance_periodo:.1f}%")
    print(f"Gasto esperado       : ${gasto_esperado:,.2f}")

    if gasto_real > gasto_esperado:
        desviacion = gasto_real - gasto_esperado
        print(f"⚠️ Desviación positiva: +${desviacion:,.2f}")
    else:
        ahorro = gasto_esperado - gasto_real
        print(f"✅ Por debajo de lo esperado: ${ahorro:,.2f}")

    # Proyección de cierre
    gasto_proyectado = gasto_real / (avance_periodo / 100)
    diferencia_proyectada = presupuesto - gasto_proyectado

    print("\n--- Proyección de cierre ---")
    print(f"Gasto proyectado     : ${gasto_proyectado:,.2f}")

    if gasto_proyectado > presupuesto:
        sobrecosto = gasto_proyectado - presupuesto
        print(f"🔴 Proyección de sobrecosto: ${sobrecosto:,.2f}")
    else:
        remanente = presupuesto - gasto_proyectado
        print(f"🟢 Remanente proyectado: ${remanente:,.2f}")


def main():
    presupuesto = 1_200_000
    gasto_real = 990_000
    avance_periodo = 50  # 50% del año/mes/proyecto transcurrido

    revisar_presupuesto(
        presupuesto,
        gasto_real,
        avance_periodo
    )


if __name__ == "__main__":
    main()