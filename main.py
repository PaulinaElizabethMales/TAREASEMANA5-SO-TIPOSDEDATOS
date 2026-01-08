# El programa solicita al usuario el ancho y el alto de un rectángulo,
# calcula el área y muestra el resultado. Se utilizan diferentes tipos de datos:

def calcular_area_rectangulo(ancho: float, alto: float) -> float:
    """
    Función que calcula el área de un rectángulo.
    Parámetros:
        ancho (float): ancho del rectángulo
        alto (float): alto del rectángulo
    Retorna:
        float: área del rectángulo
    """
    return ancho * alto


# Solicitar datos al usuario
nombre_usuario: str = input("Ingrese su nombre: ")
ancho_rectangulo: float = float(input("Ingrese el ancho del rectángulo: "))
alto_rectangulo: float = float(input("Ingrese el alto del rectángulo: "))

# Calcular área
area: float = calcular_area_rectangulo(ancho_rectangulo, alto_rectangulo)

# Verificar si el área es mayor a 50 (ejemplo de uso de boolean)
es_grande: bool = area > 50

# Mostrar resultados
print(f"Hola {nombre_usuario}, el área del rectángulo es: {area}")
print(f"¿El rectángulo es grande? {es_grande}")