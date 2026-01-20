from modelos.rectangulo import Rectangulo

class CalculadoraArea:
    """Servicio que utiliza las clases de modelos para calcular áreas"""

    @staticmethod
    def evaluar_rectangulo(ancho: float, alto: float) -> dict:
        rect = Rectangulo(ancho, alto)
        area = rect.calcular_area()
        es_grande = area > 50

        return {
            "area": area,
            "es_grande": es_grande
        }