# PyKemon


## Lógica de la aplicación de consola


pokemon_battle/
│
├── main.py                  # Punto de entrada del programa
│
├── core/                    # Lógica principal del juego
│   ├── game.py              # Clase Game (controlador principal)
│   ├── battle.py            # Clase Battle (gestión del combate)
│   ├── player.py            # Clase Player (jugador y máquina)
│   └── interface.py         # Clase Interface (visualización en consola)
│
├── entities/                # Entidades del juego (Pokémon, movimientos, tipos)
│   ├── pokemon.py           # Clase Pokemon (base para todos los Pokémon)
│   ├── move.py              # Clase Move (movimientos)
│   └── type.py              # Clase Type (gestión de tipos y efectividad)
│
├── data/                    # Datos estáticos o iniciales
│   ├── pokemon_data.py      # Definición de los 150 Pokémon (stats, movimientos)
│   └── type_chart.py        # Tabla de efectividad de tipos
│
└── utils/                   # Utilidades generales
    ├── constants.py         # Constantes como tipos o mensajes
    └── helpers.py           # Funciones auxiliares (validación, random, etc.)