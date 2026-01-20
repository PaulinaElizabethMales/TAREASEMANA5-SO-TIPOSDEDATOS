from servicios.calculadora_area import CalculadoraArea

def main():
    # Solicitar datos al usuario
    nombre_usuario: str = input("Ingrese su nombre: ")
    ancho_rectangulo: float = float(input("Ingrese el ancho del rectángulo: "))
    alto_rectangulo: float = float(input("Ingrese el alto del rectángulo: "))

    # Usar el servicio para calcular área
    resultado = CalculadoraArea.evaluar_rectangulo(ancho_rectangulo, alto_rectangulo)

    # Mostrar resultados
    print(f"Hola {nombre_usuario}, el área del rectángulo es: {resultado['area']}")
    print(f"¿El rectángulo es grande? {resultado['es_grande']}")

if __name__ == "__main__":
    main()