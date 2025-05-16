# ?? Validaci�n de Entradas en Python

Este proyecto contiene funciones reutilizables para validar entradas del usuario en la consola, asegurando que los datos introducidos correspondan al tipo esperado (por ejemplo, `int` o `float`). Ideal para proyectos peque�os, scripts interactivos o como base para futuros m�dulos.

## ?? Contenido

- `obtainValueLoop(prompt, converter)`: Solicita una entrada y la convierte con la funci�n especificada (como `int` o `float`).
- `obtainInt(prompt)`: Solicita un n�mero entero.
- `obtainFloat(prompt)`: Solicita un n�mero decimal (float).

## ?? Ejemplo de uso

```python
from input_utils import obtainInt, obtainFloat

edad = obtainInt("Introduce tu edad:")
precio = obtainFloat("Introduce el precio:")
print(f"Tienes {edad} a�os y el precio es {precio}�.")

