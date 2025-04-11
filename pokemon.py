from typeguard import typechecked
from random import randint, choice
import time
from species import pokemon_implementados
import json
from funciones import *

equipo_entrenador = []

@typechecked
class Pokemon:
    def __init__(self, nombre_pokemon: str, Entrenador: str = "Jugador", nivel: int = 100):
        self.OT = Entrenador
        with open(f'data/pokemon/{nombre_pokemon}.json') as f:
            pokemon = json.load(f)
        self.pokemon_name = nombre_pokemon
        self.pokedex_number = pokemon['pokedex']
        self.nivel = nivel
        self.shiny = randint(0, 200)
        if self.shiny == 1:
            self.pokemon_name = self.pokemon_name + "🌟"

        self.quemado = False
        self.paralizado = False
        self.envenenado = False
        self.dormido = False
        self.congelado = False

        self.IVS = {
            "Vida": randint(1, 31),
            "Ataque": randint(1, 31),
            "Defensa": randint(1, 31),
            "AtaqueEspecial": randint(1, 31),
            "DefensaEspecial": randint(1, 31),
            "Velocidad": randint(1, 31),
        }
        self.estadisticas = {
            "Vida": ((2 * pokemon["hp"] + self.IVS["Vida"]) * self.nivel) // 100 + self.nivel + 10,
            "Ataque": ((2 * pokemon["attack"] + self.IVS["Ataque"]) * self.nivel) // 100 + 5,
            "Defensa": ((2 * pokemon["defense"] + self.IVS["Defensa"]) * self.nivel) // 100 + 5,
            "AtaqueEspecial": ((2 * pokemon["special attack"] + self.IVS["AtaqueEspecial"]) * self.nivel) // 100 + 5,
            "DefensaEspecial": ((2 * pokemon["special defense"] + self.IVS["DefensaEspecial"]) * self.nivel) // 100 + 5,
            "Velocidad": ((2 * pokemon["speed"] + self.IVS["Velocidad"]) * self.nivel) // 100 + 5
        }

    def recalcular_estadisticas(self):
        self.estadisticas = {
            "Vida": ((2 * pokemon["hp"] + self.IVS["Vida"]) * self.nivel) // 100 + self.nivel + 10,
            "Ataque": ((2 * pokemon["attack"] + self.IVS["Ataque"]) * self.nivel) // 100 + 5,
            "Defensa": ((2 * pokemon["defense"] + self.IVS["Defensa"]) * self.nivel) // 100 + 5,
            "AtaqueEspecial": ((2 * pokemon["special attack"] + self.IVS["AtaqueEspecial"]) * self.nivel) // 100 + 5,
            "DefensaEspecial": ((2 * pokemon["special defense"] + self.IVS["DefensaEspecial"]) * self.nivel) // 100 + 5,
            "Velocidad": ((2 * pokemon["speed"] + self.IVS["Velocidad"]) * self.nivel) // 100 + 5
        }

    def __str__(self):
        return f"{self.OT}´s {self.pokemon_name}"
    def __repr__(self):
        return f"{self.pokemon_name.capitalize()} lvl.{self.nivel}"

def combate():
    turno = 0
    pokemon_enemigo = Pokemon(choice(pokemon_implementados), "Enemigo")
    pokemon_aliado = Pokemon(choice(pokemon_implementados))
    equipo_entrenador.append(pokemon_aliado)

    while True:
        print(f"{pokemon_enemigo.pokemon_name.capitalize()} lvl.{pokemon_enemigo.nivel} | {pokemon_enemigo.estadisticas["Vida"]} HP")
        print()
        print("       vs")
        print()
        print(f"{pokemon_aliado.pokemon_name.capitalize()} lvl.{pokemon_aliado.nivel} | {pokemon_aliado.estadisticas["Vida"]} HP")
        option = input("(Atacar / Pokemon / Huir): ")

        if option.lower() == "atacar":
            slow_print(f"{pokemon_aliado.pokemon_name.capitalize()} ha usado placaje!")
            slow_print(f"{pokemon_enemigo.pokemon_name.capitalize()} ha usado placaje!")

        elif option.lower() == "pokemon":
            print(equipo_entrenador)

        elif option.lower() == "huir":
            valor_escape = ((pokemon_aliado.estadisticas["Velocidad"] * 128) // pokemon_enemigo.estadisticas[
                "Velocidad"] + 30 * turno) % 256
            if randint(0, 255) < valor_escape:
                slow_print("Escapaste correctamente!")
                break
            else:
                slow_print("No has podido escapar!")
                turno += 1

if __name__ == "__main__":
    combate()