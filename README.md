# PyKemon Battle - Aplicación de Consola

## Descripción General
**PyKemon Battle** es una aplicación de consola desarrollada en Python utilizando los principios de Programación Orientada a Objetos (POO). Simula combates por turnos entre un Pokémon controlado por el jugador y otro por la máquina (IA), incorporando mecánicas como efectividad de tipos, cálculo de daño basado en estadísticas y una selección de 150 Pokémon de la primera generación. El proyecto está diseñado para ser modular, escalable y fácil de mantener, con una clara separación de responsabilidades entre sus componentes.

---

## Características
- **Combate por Turnos**: El jugador y la IA eligen movimientos alternadamente, con el orden de ataque determinado por la velocidad de los Pokémon.
- **Efectividad de Tipos**: Incluye una tabla de efectividad simplificada (ej. Fuego > Planta, Agua > Fuego) con multiplicadores de daño (x2, x0.5, x1).
- **Selección de Pokémon**: El jugador elige entre 150 Pokémon disponibles, mientras que la IA selecciona uno aleatoriamente.
- **Estadísticas y Daño**: Cada Pokémon tiene HP, Ataque, Defensa y Velocidad, usados en una fórmula de daño: `(Potencia * Ataque / Defensa) * Multiplicador`.
- **Interfaz en Consola**: Mensajes dinámicos (ej. "¡Es súper efectivo!") y diseño claro para una experiencia inmersiva.
- **Rejugabilidad**: Opción de volver a jugar tras cada combate.

---

## Requisitos
- **Python 3.x**: Asegúrate de tener instalado Python 3 (no se requieren librerías externas).

---

## Estructura del Proyecto

```
pykemon_battle/
│
├── main.py                  # Punto de entrada del programa
│
├── core/                    # Lógica principal del juego
│   ├── game.py              # Clase Game (controlador principal)
│   ├── battle.py            # Clase Battle (gestión del combate)
│   ├── player.py            # Clase Player (jugador y máquina)
│   └── interface.py         # Clase Interface (visualización en consola)
│
├── entities/                # Entidades del juego
│   ├── pokemon.py           # Clase Pokemon (base para todos los Pokémon)
│   ├── move.py              # Clase Move (movimientos)
│   └── type.py              # Clase Type (gestión de tipos y efectividad)
│
├── data/                    # Datos estáticos
│   ├── pokemon_data.py      # Datos de los 150 Pokémon (stats, movimientos)
│   └── type_chart.py        # Tabla de efectividad de tipos
│
└── utils/                   # Utilidades generales
    ├── constants.py         # Constantes (tipos, mensajes)
    └── helpers.py           # Funciones auxiliares (validación, aleatoriedad)
```

### Descripción de Componentes
- **`main.py`**: Inicia la aplicación creando una instancia de `Game`.
- **`core/game.py`**: Controla el flujo del juego (menú, selección de Pokémon, inicio de combates).
- **`core/battle.py`**: Gestiona la lógica de los combates (turnos, daño, ganador).
- **`core/player.py`**: Representa al jugador y la IA, con métodos para elegir movimientos.
- **`core/interface.py`**: Maneja la salida en consola y la entrada del usuario.
- **`entities/pokemon.py`**: Clase base para todos los Pokémon, con atributos como HP y métodos como recibir daño.
- **`entities/move.py`**: Define los movimientos (nombre, tipo, potencia).
- **`entities/type.py`**: Gestiona la efectividad entre tipos.
- **`data/pokemon_data.py`**: Contiene los datos de los 150 Pokémon (ej. Pikachu: HP 35, Ataque 55, Movimientos [Impactrueno, Ataque Rápido]).
- **`data/type_chart.py`**: Tabla de efectividad (ej. Fuego > Planta: x2).
- **`utils/constants.py`**: Constantes como nombres de tipos o mensajes predefinidos.
- **`utils/helpers.py`**: Funciones de apoyo (validación, selección aleatoria).

---

## Cómo Funciona
1. **Inicio**:
   - Ejecuta `main.py` para iniciar el juego.
   - Se muestra un menú: "Jugar", "Ver Reglas", "Salir".
2. **Selección de Pokémon**:
   - El jugador elige un Pokémon de los 150 disponibles (mostrados por `interface.py` desde `pokemon_data.py`).
   - La IA selecciona un Pokémon aleatorio.
3. **Combate**:
   - Se inicia un combate (`battle.py`) con los dos Pokémon.
   - Por turno:
     - El jugador elige un movimiento de su Pokémon.
     - La IA elige un movimiento aleatorio.
     - El orden se basa en la velocidad.
     - Se calcula el daño y se actualiza el HP.
     - Se muestran mensajes como "¡Pikachu usa Impactrueno! Hace 25 de daño."
   - Termina cuando el HP de un Pokémon llega a 0.
4. **Resultado**:
   - Se declara un ganador ("¡Has ganado!" o "Has perdido...").
   - Opción de jugar de nuevo.

---

## Instalación y Ejecución

1. Clona o descarga el repositorio:
   
   Para HTTPS:
   ```
   git clone https://github.com/robertcanoe/PyKemon-Battle.git
   ```
   Para SSH:
   ```
   git clone git@github.com:robertcanoe/PyKemon-Battle.git
   ```

2. Navega al directorio:
   ```
   cd pykemon-battle
   ```
3. Ejecuta el juego:
   ```
   python main.py
   ```

---

## Ejemplo de Uso
```
¡Bienvenido a PyKemon Battle!
1. Jugar
2. Ver Reglas
3. Salir
> 1

Elige tu Pokémon:
1. Pikachu (Eléctrico) - HP: 35
2. Charmander (Fuego) - HP: 39
3. Bulbasaur (Planta) - HP: 45
> 1

¡Pikachu vs Squirtle! ¡Que comience el combate!
Pikachu: 35/35 HP | Squirtle: 40/40 HP
Elige un movimiento:
1. Impactrueno (40)
2. Ataque Rápido (30)
> 1

Pikachu usa Impactrueno. ¡Es súper efectivo! Hace 30 de daño.
Squirtle usa Placaje. Hace 10 de daño.
Pikachu: 25/35 HP | Squirtle: 10/40 HP
...
```

---

## Detalles Técnicos
- **Paradigma**: POO con encapsulamiento (atributos privados), herencia (clases abstractas) y modularidad.
- **Datos**: Los 150 Pokémon están definidos en `pokemon_data.py` para facilitar su edición.
- **Tipos**: Actualmente incluye Fuego, Agua, Planta y Eléctrico, pero es ampliable en `type_chart.py`.
- **Validación**: Entradas del usuario validadas en `interface.py`.

---

## Posibles Mejoras
- Agregar efectos de estado (quemadura, parálisis).
- Implementar más tipos y movimientos.
- Guardar estadísticas o puntuación del jugador.
- Mejorar la interfaz con colores en la consola.

---

## Autor
Desarrollado por *Roberto Cano Estévez y Fernando Sánchez Sánchez* como proyecto de práctica en Python para final de primer año de DAW
