# Clase base con encapsulación y herencia

class FiguraGeometrica:
    """Clase base para figuras geométricas"""
    def calcular_area(self) -> float:
        raise NotImplementedError("Este método debe ser sobrescrito en la clase derivada")


class Rectangulo(FiguraGeometrica):
    """Clase derivada que representa un rectángulo"""

    def __init__(self, ancho: float, alto: float):
        # Encapsulación: atributos privados
        self.__ancho = ancho
        self.__alto = alto

    # Métodos getter y setter para acceder a los atributos encapsulados
    def get_ancho(self) -> float:
        return self.__ancho

    def set_ancho(self, ancho: float):
        self.__ancho = ancho

    def get_alto(self) -> float:
        return self.__alto

    def set_alto(self, alto: float):
        self.__alto = alto

    # Polimorfismo: sobrescribimos el metodo de la clase base
    def calcular_area(self) -> float:
        return self.__ancho * self.__alto