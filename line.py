def line():
    coef_a = float(input("Ingrese el coeficiente A: "))
    coef_b = float(input("Ingrese el coeficiente B: "))
    coef_x_1 = float(input("Ingrese el coeficiente X1: "))
    coef_x_2 = float(input("Ingrese el coeficiente X2: "))

    print(f"El coeficiente A de su ecuación de la recta es: {coef_a}")
    print(f"El coeficiente B de su ecuación de la recta es: {coef_b}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {coef_x_1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {coef_x_2}")
    print("")
    print("Para la siguiente ecuación:")
    print(f"\tY = {coef_a}X + {coef_b}")
    print("")
    coef_y_1 = coef_a * coef_x_1 + coef_b
    coef_y_2 = coef_a * coef_x_2 + coef_b
    print("Dados los siguientes puntos:")
    print(f"\tP1 ({coef_x_1}, {coef_y_1})")
    print(f"\tP2 ({coef_x_2}, {coef_y_2})")
    print("")
    distancia_puntos = ((coef_x_2 - coef_x_1)**2 + (coef_y_2 - coef_y_1)**2)**0.5
    print(f"La distancia entre ellos es: {distancia_puntos}")
