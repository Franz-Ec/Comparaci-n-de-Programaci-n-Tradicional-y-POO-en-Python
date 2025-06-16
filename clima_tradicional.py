1. Código de Programación Tradicional (clima_tradicional.py)
# clima_tradicional.py

def obtener_temperaturas_diarias():
    """
    Solicita al usuario las temperaturas para cada día de la semana.
    Realiza una validación de entrada básica para asegurar que sean números.
    Retorna una lista de temperaturas flotantes.
    """
    temperaturas = []
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    print("\n--- Ingreso de Temperaturas (Programación Tradicional) ---")
    for dia in dias_semana:
        while True:
            try:
                temp_str = input(f"Ingresa la temperatura para el {dia}°C: ")
                temp = float(temp_str)
                temperaturas.append(temp)
                break  # Sale del bucle si la entrada es un número válido
            except ValueError:
                print("¡Error! Por favor, ingresa un valor numérico para la temperatura.")
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    """
    Calcula el promedio de una lista dada de temperaturas.
    Retorna el promedio como un flotante. Si la lista está vacía, retorna 0.
    """
    if not temperaturas:
        return 0.0  # Retorna 0.0 para indicar que no hay temperaturas para promediar
    suma_temperaturas = sum(temperaturas)
    promedio = suma_temperaturas / len(temperaturas)
    return promedio

def mostrar_resultados_tradicional(temperaturas, promedio):
    """
    Muestra las temperaturas ingresadas y el promedio semanal calculado.
    """
    print("\n--- Resultados (Programación Tradicional) ---")
    if temperaturas:
        print(f"Temperaturas ingresadas para la semana: {temperaturas}")
        print(f"El promedio semanal de la temperatura es: {promedio:.2f}°C")
    else:
        print("No se ingresaron temperaturas para calcular el promedio.")

def main_tradicional():
    """
    Función principal que orquesta la ejecución del programa
    en el enfoque de programación tradicional.
    """
    temperaturas_semana = obtener_temperaturas_diarias()
    promedio_semanal = calcular_promedio_semanal(temperaturas_semana)
    mostrar_resultados_tradicional(temperaturas_semana, promedio_semanal)

if __name__ == "__main__":
    main_tradicional()
