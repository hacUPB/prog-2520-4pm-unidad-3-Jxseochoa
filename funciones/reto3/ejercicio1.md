# Ejercicio 1: Estabilidad del avión en turbulencia

## Enunciado
Un avión en vuelo se enfrenta a una turbulencia que dura 8 segundos.  
Durante este tiempo, el **piloto debe decidir en cada segundo** si aumentar, disminuir o mantener:  

- El **ángulo de ataque (AoA)**, que afecta el **coeficiente de sustentación (Cl)**.  
- La **velocidad del avión (V)**.  

El programa simula los efectos de estas decisiones sobre la sustentación y evalúa si el avión logra mantenerse en vuelo o entra en pérdida.  

El usuario no ingresa datos numéricos, sino que selecciona uno de tres aviones predefinidos **(Cessna 172, Airbus A320 o Boeing 747-8)**, cada uno con su peso, área alar, velocidad inicial, coeficiente de sustentación base y un ángulo de ataque inicial.

---

## Aviones predefinidos

| Avión               | Peso (N) | Área alar (m²) | Velocidad inicial (m/s) | Cl base | AoA inicial (°) |
|----------------------|----------|----------------|--------------------------|---------|-----------------|
| Cessna 172 Skyhawk  | 10,000   | 16.2           | 65                       | 0.4     | 5               |
| Airbus A320         | 600,000  | 122.6          | 130                      | 0.5     | 5               |
| Boeing 747-8        | 3,500,000| 554            | 250                      | 0.6     | 5               |

---

## Tabla de variables

| Tipo       | Variable      | Descripción                                      | Tipo de dato |
|------------|---------------|--------------------------------------------------|--------------|
| Entrada    | avion         | Selección del avión (1, 2 o 3)                   | int          |
| Entrada    | aoa           | Ángulo de ataque actual (°)                      | int          |
| Entrada    | decision_aoa  | Decisión sobre el ángulo: aumentar, disminuir o mantener | str  |
| Entrada    | v             | Velocidad (m/s)                                  | float        |
| Entrada    | decision_v    | Decisión sobre la velocidad: aumentar, disminuir o mantener | str |
| Constante  | rho           | Densidad del aire (1.225 kg/m³)                  | float        |
| Constante  | cl_base       | Cl inicial del avión en el AoA base              | float        |
| Constante  | aoa_inicial   | Ángulo de ataque de referencia para Cl base      | int          |
| Salida     | cl_actual     | Coeficiente de sustentación ajustado por AoA     | float        |
| Salida     | sustentacion  | Sustentación (N) en cada segundo                 | float        |
| Salida     | estado        | Estado de vuelo (Estable, Crítico o Pérdida)     | str          |
| Control    | segundo       | Contador de tiempo (1 a 8)                       | int          |
| Control    | estado_final  | Resultado final de la simulación (Exitoso o Pérdida) | str      |

---

## Constantes utilizadas

- **Densidad del aire a nivel del mar:**  
  ρ = 1.225 kg/m³  

- **Relación simplificada entre Cl y AoA:**  
 Cl_actual = Cl_base + 0.1 x (AoA - AoA_inicial)

## Ecuación principal
L = 0.5 x \rho x V^2 x Cl x A

Donde:  
- **L** = Sustentación (N)  
- **ρ** = Densidad del aire (kg/m³)  
- **V** = Velocidad (m/s)  
- **Cl** = Coeficiente de sustentación  
- **A** = Área alar (m²)  


## Estados definidos

- **Estable:** Sustentación ≥ Peso.  
- **Crítico:** 0.5 × Peso ≤ Sustentación < 0.8 × Peso.  
- **Pérdida:** Sustentación < 0.5 × Peso → fin de simulación.  

## Bucle de simulación

- El ciclo se ejecuta por **8 segundos**.  
- En cada segundo:  
  1. Se muestra el **AoA actual** y el usuario decide aumentarlo, disminuirlo o mantenerlo.  
  2. Se recalcula el **Cl** y la **sustentación**.  
  3. Se muestra el **estado del vuelo** (Estable, Crítico o Pérdida).  
  4. Se muestra la **velocidad actual** y el usuario decide aumentarla, disminuirla o mantenerla.  

## Finalización del programa

- **Fracaso:** si ocurre pérdida antes de los 8 segundos.  
- **Éxito:** si se completan los 8 segundos sin pérdida.  

## Resultados posibles

- **Éxito:**  
  El avión logró atravesar la turbulencia con éxito.

- **Fracaso:**  
  El avión no logró superar la turbulencia.
