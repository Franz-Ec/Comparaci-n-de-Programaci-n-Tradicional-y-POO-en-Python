2. Código de Programación Orientada a Objetos (POO) (clima_poo.py)
Este archivo implementa la solución utilizando una clase y objetos, siguiendo el paradigma de la Programación Orientada a Objetos.
# clima_poo.py

class ClimaSemanal:
    """
    Representa el registro del clima para una semana, encapsulando
    las temperaturas diarias y los métodos para operarlas.
    """
    def __init__(self):
        """
        Constructor de la clase. Inicializa la lista de temperaturas como vacía
        y define los días de la semana.
        """
        self.__temperaturas = []  # Atributo privado para encapsulamiento
        self.dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        print("Objeto 'ClimaSemanal' inicializado.")

    def ingresar_temperaturas(self):
        """
        Permite al usuario ingresar las temperaturas diarias para la semana.
        Valida la entrada para asegurar que sean números.
        """
        self.__temperaturas = []  # Limpia la lista antes de un nuevo ingreso
        print("\n--- Ingreso de Temperaturas (POO) ---")
        for dia in self.dias_semana:
            while True:
                try:
                    temp_str = input(f"Ingresa la temperatura para el {dia}°C: ")
                    temp = float(temp_str)
                    self.__temperaturas.append(temp)
                    break
                except ValueError:
                    print("¡Error! Por favor, ingresa un valor numérico para la temperatura.")
        print("Temperaturas semanales registradas en el objeto.")

    def calcular_promedio(self):
        """
        Calcula el promedio de las temperaturas almacenadas en esta instancia.
        Retorna el promedio o 0.0 si no hay temperaturas.
        """
        if not self.__temperaturas:
            return 0.0
        suma_temperaturas = sum(self.__temperaturas)
        promedio = suma_temperaturas / len(self.__temperaturas)
        return promedio

    def mostrar_temperaturas(self):
        """
        Muestra las temperaturas diarias almacenadas en la instancia.
        """
        if self.__temperaturas:
            print(f"Temperaturas registradas en el objeto: {self.__temperaturas}")
        else:
            print("No hay temperaturas registradas en este objeto 'ClimaSemanal' aún.")

    def mostrar_resultados_poo(self):
        """
        Muestra los resultados completos de las temperaturas y su promedio.
        """
        promedio = self.calcular_promedio()
        print("\n--- Resultados (POO) ---")
        self.mostrar_temperaturas()
        if self.__temperaturas: # Solo muestra el promedio si hay temperaturas
            print(f"El promedio semanal de la temperatura es: {promedio:.2f}°C")
        else:
            print("No se pudo calcular el promedio, no hay temperaturas ingresadas.")


def main_poo():
    """
    Función principal que orquesta la ejecución del programa
    en el enfoque de programación orientada a objetos.
    """
    # Creamos una instancia (objeto) de la clase ClimaSemanal
    mi_clima_semanal = ClimaSemanal()

    # Utilizamos los métodos del objeto para realizar las operaciones
    mi_clima_semanal.ingresar_temperaturas()
    mi_clima_semanal.mostrar_resultados_poo()


if __name__ == "__main__":
    main_poo()
