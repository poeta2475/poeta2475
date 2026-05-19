import time
import random

LIMITE_INFERIOR = 1
LIMITE_SUPERIOR = 30
MAX_INTENTOS    = 5


def obtener_numero(prompt: str):
    try:
        return int(input(prompt))
    except ValueError:
        return None


def mostrar_pista(intento: int, diferencia: str) -> None:
    restantes = MAX_INTENTOS - intento
    if diferencia == "mayor":
        print("   Es Un Número Menor Al Que Elegiste.")
    else:
        print("   Intenta Con Un Número Más Grande.")
    if restantes > 0:
        plural = "Intentos" if restantes > 1 else "Intento"
        print(f"   Te Quedan {restantes} {plural} Más.\n")


def jugar() -> None:
    num_secreto = random.randint(LIMITE_INFERIOR, LIMITE_SUPERIOR)

    nombre = input("¿Nombre Del Jugador? ").strip() or "Jugador"
    time.sleep(1)
    print(f"\n   Hola {nombre.title()}, ¿Cómo Estás?\n")
    time.sleep(1)
    print(f"   Tendrás {MAX_INTENTOS} Intentos Para Adivinar Un Número Entre "
          f"{LIMITE_INFERIOR} Y {LIMITE_SUPERIOR}.\n")
    time.sleep(1)

    for intento in range(1, MAX_INTENTOS + 1):
        numero = obtener_numero(f"   Intento {intento}/{MAX_INTENTOS} — Ingresa Un Número: ")

        if numero is None:
            print("   Por Favor Ingresa Solo Números Enteros.\n")
            continue

        if numero == num_secreto:
            time.sleep(0.5)
            label = "Intento" if intento == 1 else "Intentos"
            print(f"\n   ¡Ganaste, {nombre.title()}! Adivinaste En {intento} {label}. 🎉\n")
            return

        mostrar_pista(intento, "mayor" if numero > num_secreto else "menor")
        time.sleep(0.5)

    print(f"\n   ¡Perdiste! El Número Era {num_secreto}. ¡Mejor Suerte La Próxima Vez!\n")


if __name__ == "__main__":
    jugar()
