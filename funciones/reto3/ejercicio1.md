# Ejercicio 1 

Un avión en vuelo se enfrenta a una turbulencia que modifica su ángulo de ataque durante 8 segundos.
El programa simula cómo cambia la sustentación y determina si el vuelo se mantiene estable, crítico o si entra en pérdida.

El usuario no ingresa datos manualmente, sino que selecciona uno de tres aviones predefinidos **(Cessna 172, Airbus A320 o Boeing 747-8)**, cada uno con su peso, área alar, velocidad inicial y coeficiente de sustentación base. El usuario solamente cambia el ángulo de ataque, el cual, altera el Cl.

| Tipo    | Variable       | Descripción                                      |Tipo de dato|
| ------- | -------------- | -------------------------------------------------| -----------|
| Entrada | avion        | Selección del avión (1, 2 o 3)                     | int        |
| Entrada | peso         | Peso del avión (N)                                 | float      |
| Entrada | area         | Área alar (m²)                                     | float      |
| Entrada | v            | Velocidad inicial (m/s)                            | float      |
| Entrada | cl_base      | Coeficiente de sustentación base                   | float      |
| Salida  | sustentacion | Valor de sustentación en cada segundo (N)          | float      |
| Salida  | estado       | Mensaje del estado (Estable, Crítico o Pérdida)    | str        |
| Control | segundo      | Contador de tiempo (1 a 8)                         | int        |
| Control | AoA          | Ángulo de ataque simulado mediante cambio en Cl    | float      |
| Control | decision     | Opción del usuario (aumentar o mantener velocidad) | str        |
|Constante|p             | Densidad del aire (kg/m³)   
# Análisis del ejercicio

## Contexto del ejercicio
Se quiere analizar la sustentación de un avión durante turbulencia, considerando cómo cambios en el ángulo de ataque alteran el coeficiente de sustentación (Cl).

## Constantes utilizadas:
### Densidad del aire a nivel del mar: 
- p = 1.225 kg/m³.
### Ecuación principal:
- L=0.5⋅p⋅V²⋅Cl⋅A

Donde:
- L = Sustentación (N)
- p = Densidad del aire (kg/m³)
- V = Velocidad (m/s)
- Cl = Coeficiente de sustentación
- A = Área alar (m²)

## Estados definidos:
- Estable: Sustentación ≥ Peso.
- Crítico: Sustentación < 80% del Peso.
- Pérdida: Sustentación < 50% del Peso (fin de simulación).

## Bucle:
- Se ejecuta un bucle de 8 segundos.
- En cada segundo se altera el coeficiente de sustentación (Cl ± 0.05) para simular turbulencia.
- Se recalcula la sustentación y se determina el estado del vuelo.

## Decisiones del usuario (condicionales):

### En cada segundo el usuario puede:
- Aumentar velocidad: se incrementa +10 m/s.
- Mantener velocidad: se conserva igual.

## Finalización del programa:
- Si ocurre pérdida antes de los 8 segundos → la simulación termina.
- Si completa los 8 segundos sin pérdida → éxito del vuelo.