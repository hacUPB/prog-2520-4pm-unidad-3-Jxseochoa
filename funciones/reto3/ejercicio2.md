# Ejercicio 2: Planeo de emergencia sin motores

## Contexto
Un avión sufre una falla total de motores durante el vuelo y debe planear hasta tocar el suelo.  
El desempeño del planeo depende de la relación de planeo (L/D), que indica cuántos metros avanza horizontalmente por cada metro que pierde en altitud.  

Durante la simulación, el piloto debe decidir en cada segundo si:  
- Aumentar el ángulo de picado → gana velocidad, pero la eficiencia (L/D) disminuye.  
- Disminuir el ángulo de picado → pierde velocidad, pero la eficiencia (L/D) mejora.  
- Mantener → conserva la eficiencia base.  

El objetivo es recorrer la mayor distancia horizontal posible antes de llegar al suelo.  

## Aviones predefinidos y duración del planeo

| Avión                | Altura inicial (m) | Pérdida por segundo (m) | Duración aprox. (s) | Relación L/D base |
|-----------------------|--------------------|--------------------------|----------------------|-------------------|
| Piper PA-28 Cherokee | 600                | 100                      | 6                    | 10:1              |
| Embraer E190         | 1200               | 150                      | 8                    | 14:1              |
| Concorde             | 2000               | 250                      | 8                    | 7:1               |

## Tabla de variables

| Tipo       | Variable      | Descripción                                                   | Tipo de dato |
|------------|---------------|---------------------------------------------------------------|--------------|
| Entrada    | avion         | Selección del avión (1, 2 o 3)                                | int          |
| Entrada    | decision      | Elección del usuario: aumentar, disminuir o mantener ángulo   | str          |
| Constante  | rho           | Densidad del aire (1.225 kg/m³)                               | float        |
| Constante  | L_D_base      | Relación de planeo base del avión (L/D)                       | float        |
| Constante  | h_inicial     | Altura inicial asignada según el avión                        | float        |
| Constante  | delta_h       | Pérdida de altura por segundo (depende del avión)             | float        |
| Salida     | h_actual      | Altura restante en cada segundo (m)                           | float        |
| Salida     | distancia     | Distancia horizontal acumulada (m)                            | float        |
| Salida     | estado        | Estado del vuelo (En planeo, Crítico o Aterrizado)            | str          |
| Control    | segundo       | Contador de tiempo (segundos de simulación)                   | int          |

## Constantes utilizadas

- ρ = 1.225 kg/m³ (densidad del aire a nivel del mar, ISA).  
- Δh: pérdida de altura por segundo según el avión:  
  - Piper PA-28 Cherokee → 100 m/seg  
  - Embraer E190 → 150 m/seg  
  - Concorde → 250 m/seg  
- Relación L/D ajustada según decisión del piloto:  
  - Aumentar ángulo → L/D - 2  
  - Disminuir ángulo → L/D + 2  
  - Mantener → L/D sin cambios  

## Ecuaciones principales

1. Pérdida de altura por segundo:  
   Δh = valor definido por el avión  

2. Distancia horizontal recorrida por segundo:  
   Δx = (L/D) x Δh  

3. Actualización de altura y distancia:  
   h_nuevo = h_anterior - Δh  
   x_nuevo = x_anterior + Δx  

## Estados definidos

- En planeo: mientras h > 0 y L/D ≥ 5.  
- Crítico: si L/D < 5 (planeo ineficiente, riesgo de caída brusca).  
- Aterrizado: cuando h ≤ 0.  

## Bucle de simulación

1. El usuario selecciona un avión.  
2. Se asigna la altura inicial, el L/D base y la pérdida de altura por segundo (Δh).  
3. Se establece: segundo = 1, distancia = 0, estado = “planeo”.  
4. Mientras la altura sea mayor a 0:  
   - Mostrar la altura y la distancia recorrida.  
   - Preguntar al usuario si desea aumentar, disminuir o mantener el ángulo.  
   - Ajustar el valor de L/D según la decisión.  
   - Calcular la distancia horizontal de ese segundo y restar Δh de altura.  
   - Evaluar el estado (planeo normal, crítico o aterrizado).  
   - Incrementar el contador de segundos.  
5. El bucle termina cuando el avión llega al suelo. 

## Resultados posibles

- **Éxito completo:** el avión logra recorrer la máxima distancia posible según su L/D base.  
- **Éxito parcial:** el avión recorre una distancia considerable, aunque con decisiones subóptimas.  
- **Fracaso:** el avión baja demasiado el L/D (<5) y pierde eficiencia, aterrizando de forma crítica.

