print("ejemplos de condicionales")

def evaluar_clima(temperatura, humedad, viento):
    if (temperatura > 30 and humedad > 70) or viento > 50:
        return "Condiciones extremas"
    elif 25 <= temperatura <= 30 and 40 <= humedad <= 60:
        return "Condiciones ideales"
    elif temperatura < 10 or (temperatura < 15 and humedad > 80):
        return "Clima frío y húmedo"
    else:
        return "Condiciones normales"

print(evaluar_clima(32, 75, 10))  # "Condiciones extremas"