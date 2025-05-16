# Validación de Entradas en Python

Este proyecto contiene funciones reutilizables para validar entradas del usuario en la consola, asegurando que los datos introducidos correspondan al tipo esperado (por ejemplo, `int` o `float`). Ideal para proyectos pequeños, scripts interactivos o como base para futuros módulos.

## Contenido

- `obtainValueLoop(prompt, converter)`: Solicita una entrada y la convierte con la función especificada (como `int` o `float`).
- `obtainInt(prompt)`: Solicita un número entero.
- `obtainFloat(prompt)`: Solicita un número decimal (float).

## Ejemplo de uso

```python
from input_utils import obtainInt, obtainFloat

edad = obtainInt("Introduce tu edad:")
precio = obtainFloat("Introduce el precio:")
print(f"Tienes {edad} años y el precio es {precio}€.")

