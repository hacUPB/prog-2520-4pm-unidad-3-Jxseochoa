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


# Pseudocódigo
```
Inicio

ρ = 1.225    // densidad del aire (kg/m³)

Definir aviones:
    1 → Cessna 172 Skyhawk: peso=10000, área=16.2, v=65, Cl_base=0.4, AoA_inicial=5
    2 → Airbus A320: peso=600000, área=122.6, v=130, Cl_base=0.5, AoA_inicial=5
    3 → Boeing 747-8: peso=3500000, área=554, v=250, Cl_base=0.6, AoA_inicial=5

Mostrar "Seleccione un avión:"
Leer opcion

Si opcion no está en {1,2,3} Entonces
    Mostrar "Opción inválida. Debe seleccionar 1, 2 o 3."
    Fin
Fin Si

peso = valor_peso_del_avion
área = valor_area_del_avion
v = valor_velocidad_inicial
Cl_base = valor_Cl_base
AoA_inicial = valor_AoA_inicial

AoA = AoA_inicial
estado_final = "Exitoso"

Para segundo desde 1 hasta 8 Hacer
    Mostrar "Segundo", segundo
    Mostrar "Ángulo de ataque actual =", AoA

    Mostrar "¿Ángulo de ataque: (a)umentar, (d)isminuir o (m)antener?"
    Leer decision_AoA

    Si decision_AoA = "a" Entonces
        AoA = AoA + 1
        Mostrar "Ángulo de ataque aumentó a", AoA
    Sino Si decision_AoA = "d" Entonces
        AoA = AoA - 1
        Mostrar "Ángulo de ataque disminuyó a", AoA
    Sino Si decision_AoA = "m" Entonces
        Mostrar "Ángulo de ataque se mantiene en", AoA
    Sino
        Mostrar "Opción inválida → se mantiene ángulo"
    Fin Si

    Cl_actual = Cl_base + 0.1 × (AoA - AoA_inicial)
    sustentación = 0.5 × ρ × v² × Cl_actual × área
    Mostrar "Velocidad =", v, "| Cl =", Cl_actual, "| Sustentación =", sustentación

    Si sustentación ≥ peso Entonces
        Mostrar "Estado: Estable"
    Sino Si sustentación < 0.5 × peso Entonces
        Mostrar "Estado: Pérdida - Fin de simulación"
        estado_final = "Pérdida"
        Salir del bucle
    Sino Si sustentación < 0.8 × peso Entonces
        Mostrar "Estado: Crítico"
    Fin Si

    Mostrar "Velocidad actual =", v
    Mostrar "¿Velocidad: (a)umentar, (d)isminuir, (m)antener?"
    Leer decision_v

    Si decision_v = "a" Entonces
        v = v + 10
        Mostrar "Velocidad aumentó a", v
    Sino Si decision_v = "d" Entonces
        v = v - 10
        Mostrar "Velocidad disminuyó a", v
    Sino Si decision_v = "m" Entonces
        Mostrar "Velocidad se mantiene en", v
    Sino
        Mostrar "Opción inválida → velocidad se mantiene"
    Fin Si

Fin Para

Si estado_final = "Exitoso" Entonces
    Mostrar "El avión logró atravesar la turbulencia con éxito."
Sino
    Mostrar "El avión no logró superar la turbulencia."
Fin Si

Fin
```
