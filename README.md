3. Texto Comparativo para README.md
Este es el contenido que deberías usar para tu archivo README.md en el repositorio de GitHub.
# Tarea Práctica: Comparación de Programación Tradicional y POO en Python

Este repositorio contiene dos implementaciones en Python para determinar el promedio semanal del clima, demostrando los paradigmas de **Programación Tradicional** (basada en funciones) y **Programación Orientada a Objetos (POO)**.

## 1. Implementación con Programación Tradicional (`clima_tradicional.py`)

### Descripción
Esta solución se enfoca en la **división del problema en funciones independientes**. Cada función tiene una tarea específica: una para la entrada de datos, otra para el cálculo, y una tercera para mostrar los resultados. Los datos (la lista de temperaturas) se pasan explícitamente entre estas funciones.

### Estructura
* `obtener_temperaturas_diarias()`: Se encarga de solicitar las temperaturas al usuario y validar que sean números.
* `calcular_promedio_semanal(temperaturas)`: Recibe una lista de temperaturas y retorna su promedio.
* `mostrar_resultados_tradicional(temperaturas, promedio)`: Presenta las temperaturas y el promedio final.
* `main_tradicional()`: La función principal que coordina la ejecución de las otras funciones.

### Ventajas
* **Simplicidad para tareas pequeñas:** El código es directo y fácil de entender para problemas que no involucran una gran complejidad de datos o comportamientos.
* **Modularidad funcional:** Las funciones son unidades lógicas y reutilizables, aunque la gestión de datos puede requerir pasar argumentos constantemente.

### Desventajas
* **Acoplamiento de datos y lógica:** Los datos se manejan de forma separada de las operaciones, lo que puede llevar a que una función modifique datos que no le corresponden directamente o a un exceso de paso de parámetros.
* **Dificultad de escalabilidad:** En aplicaciones más grandes, la gestión de un estado global o el paso constante de datos entre múltiples funciones puede volverse complejo y propenso a errores.
* **Menor encapsulamiento:** No hay una forma inherente de proteger los datos de ser accedidos o modificados de maneras no deseadas desde cualquier parte del código.

## 2. Implementación con Programación Orientada a Objetos (POO) (`clima_poo.py`)

### Descripción
Esta solución modela el concepto del "clima semanal" como un **objeto**. Se define una clase `ClimaSemanal` que no solo almacena las temperaturas (datos) sino que también incluye los métodos (operaciones) para interactuar con ellas, como ingresarlas y calcular su promedio.

### Conceptos POO Aplicados
* **Clase (`ClimaSemanal`):** Es la plantilla o el "plano" para crear objetos de tipo clima semanal.
* **Objeto:** Una instancia de la clase `ClimaSemanal` (e.g., `mi_clima_semanal`), que contiene sus propios datos y métodos.
* **Atributos:** `self.__temperaturas` es un atributo (datos) que almacena la lista de temperaturas. El uso de `__` denota un atributo privado, reforzando el **encapsulamiento**.
* **Métodos:**
    * `__init__()`: El constructor, que se llama automáticamente al crear un objeto para inicializar sus atributos.
    * `ingresar_temperaturas()`: Un método que permite al objeto obtener y almacenar sus propias temperaturas.
    * `calcular_promedio()`: Un método que permite al objeto calcular el promedio de *sus propias* temperaturas.
    * `mostrar_temperaturas()` y `mostrar_resultados_poo()`: Métodos para presentar la información contenida en el objeto.
* **Encapsulamiento:** Los datos (`__temperaturas`) están "ocultos" dentro del objeto y solo se pueden modificar o acceder a través de los métodos públicos definidos en la clase. Esto protege la integridad de los datos.

### Ventajas
* **Mayor Cohesión:** Los datos y las funciones que operan sobre esos datos están agrupados lógicamente dentro de una misma entidad (el objeto), lo que facilita la comprensión y el mantenimiento.
* **Reutilización de Código:** Las clases y objetos son componentes autocontenidos que pueden ser reutilizados fácilmente en diferentes partes del mismo programa o en otros proyectos.
* **Escalabilidad:** Facilita la expansión y la adición de nuevas funcionalidades. Si se necesitara manejar otro tipo de datos climáticos, se podrían crear nuevas clases o extender la actual mediante herencia.
* **Modelado del Mundo Real:** Permite representar conceptos del mundo real de una manera más intuitiva y organizada.
* **Mantenibilidad:** Los cambios en un objeto o clase suelen tener un impacto limitado en otras partes del sistema, lo que simplifica la depuración y las actualizaciones.

### Desventajas
* **Curva de Aprendizaje:** Puede ser inicialmente más compleja de entender e implementar para desarrolladores nuevos en el paradigma.
* **"Overhead" para Problemas Simples:** Para tareas muy pequeñas y sencillas, la estructura de clases y objetos puede parecer excesiva en comparación con un enfoque funcional directo.

## Comparación y Conclusión

Ambos enfoques, el tradicional y el POO, son válidos para resolver el problema de calcular el promedio semanal del clima. La elección entre uno u otro depende en gran medida de la **escala** y la **complejidad** del proyecto, así como de las preferencias de diseño y mantenimiento a largo plazo.

| Característica         | Programación Tradicional (Funcional)          | Programación Orientada a Objetos (POO)            |
| :--------------------- | :-------------------------------------------- | :------------------------------------------------ |
| **Enfoque Principal** | Qué hacer (funciones/procedimientos)          | Quién es y qué puede hacer (objetos)              |
| **Organización** | Funciones modulares, datos pasados entre ellas | Datos y operaciones encapsulados en clases/objetos |
| **Reusabilidad** | Funciones reutilizables                         | Objetos/Clases altamente reutilizables y extensibles |
| **Manejo de Estado** | Variables globales o paso de parámetros        | Estado contenido y gestionado dentro del objeto    |
| **Escalabilidad** | Puede volverse difícil de manejar en proyectos grandes | Ideal para proyectos grandes y complejos          |
| **Mantenibilidad** | Depende de la modularidad y disciplina          | Generalmente más fácil de mantener y depurar      |
| **Acoplamiento** | Mayor acoplamiento entre funciones y datos      | Menor acoplamiento (gracias al encapsulamiento)   |

En resumen, para una tarea pequeña como esta, la programación tradicional es funcional y rápida. Sin embargo, si este programa fuera parte de un sistema meteorológico más grande con más tipos de datos (humedad, presión, etc.) y funcionalidades (pronósticos, alertas), el enfoque de **Programación Orientada a Objetos** ofrecería una estructura mucho más robusta, organizada y fácil de mantener y escalar. La POO fomenta un diseño de software más **modular** y **cohesivo**, alineándose mejor con la forma en que los sistemas complejos del mundo real son percibidos y modelados.
