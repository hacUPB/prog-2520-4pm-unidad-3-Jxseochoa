# Ejercicio 3: Consumo de combustible

## Contexto
Un Airbus A320 inicia un vuelo con una cierta cantidad de combustible.  
El vuelo se divide en tres fases:  

1. **Ascenso** → consumo elevado: 75 litros/minuto.  
2. **Crucero** → consumo moderado: 50 litros/minuto.  
3. **Descenso** → consumo reducido: 37.5 litros/minuto.  

El usuario debe ingresar:  
- La cantidad inicial de combustible disponible.
- La duración de cada fase (ascenso, crucero y descenso) en minutos.  

Durante la simulación, el sistema calcula cada **5 minutos**:  
- El combustible restante.  
- Verifica si el vuelo entra en estado de normalidad, emergencia o falla.  
- Informa si el vuelo finaliza con éxito o en emergencia.  

## Objetivos del ejercicio
- Simular el consumo progresivo de combustible en las fases de vuelo.  
- Mostrar cómo las diferentes fases afectan directamente el gasto de combustible.  
- Destacar la importancia de mantener siempre la reserva mínima de seguridad (1500 L).  

## Estados posibles durante la simulación

- **Normal:** combustible > 1500 litros.  
- **Emergencia:** combustible ≤ 1500 litros (aunque no llegue a 0).  
- **Sin combustible:** combustible = 0 antes de completar todas las fases.  
- **Vuelo exitoso:** se completan todas las fases con combustible ≥ 1500 litros (reserva reglamentaria).  


## Tabla de variables

| Tipo       | Variable          | Descripción                                                  | Tipo de dato |
|------------|------------------|--------------------------------------------------------------|--------------|
| Entrada    | combustible_ini  | Combustible inicial del avión (litros)                       | float        |
| Entrada    | t_ascenso        | Duración de la fase de ascenso (minutos)                     | int          |
| Entrada    | t_crucero        | Duración de la fase de crucero (minutos)                     | int          |
| Entrada    | t_descenso       | Duración de la fase de descenso (minutos)                    | int          |
| Constante  | consumo_ascenso  | 75 L/min                                                     | float        |
| Constante  | consumo_crucero  | 50 L/min                                                     | float        |
| Constante  | consumo_descenso | 37.5 L/min                                                   | float        |
| Constante  | intervalo        | Intervalo de reporte: cada 5 min                             | int          |
| Constante  | min_seguridad    | Nivel mínimo de seguridad: 1500 L                            | float        |
| Salida     | combustible_act  | Combustible restante después de cada intervalo               | float        |
| Salida     | estado           | Estado del vuelo (Normal, Emergencia, Sin combustible, Éxito)| str          |
| Control    | tiempo_total     | Suma de los minutos simulados                                | int          |
| Control    | fase             | Indica la fase actual (ascenso, crucero o descenso)          | str          |


## Constantes utilizadas
- Consumos de combustible por fase: 
  - Ascenso: 75 L/min.  
  - Crucero: 50 L/min.  
  - Descenso: 37.5 L/min.  
- Intervalo de control: cada 5 minutos.  
- Mínimo de seguridad: 1500 L.  


## Ecuaciones principales

## Ecuaciones principales

1. Combustible consumido en un intervalo de 5 minutos:  
   Δcombustible = consumo_fase × intervalo  

2. Combustible restante tras cada intervalo:  
   combustible_act = combustible_ant − Δcombustible  

3. Estado del vuelo:  
   - Si combustible_act = 0 → "Sin combustible"  
   - Si 0 < combustible_act ≤ 1500 → "Emergencia"  
   - Si combustible_act > 1500 → "Normal"  
 


## Bucle de simulación

1. **Inicialización:** establecer combustible inicial y duración de fases.  
2. **Fase ascenso:**  
- Por cada 5 min: consumir combustible y verificar estado.  
- Si combustible = 0 → detener simulación.  
3. **Fase crucero:** repetir el proceso con consumo de 50 L/min.  
4. **Fase descenso:** repetir el proceso con consumo de 37.5 L/min.  
5. **Finalización:**  
- Si termina con combustible ≥ 1500 L → **Vuelo exitoso**.  
- Si termina con combustible > 0 pero < 1500 L → **Vuelo en emergencia**.  
- Si combustible llega a 0 antes del final → **Vuelo fallido**.  


## Resultados posibles

- **Vuelo exitoso:** el avión completa todas las fases con al menos 1500 L de combustible, cumpliendo la reserva mínima.  
- **Vuelo en emergencia:** el avión completa el plan, pero aterriza con menos de 1500 L.  
- **Vuelo fallido:** el avión se queda sin combustible antes de terminar alguna fase.  
