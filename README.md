### Hi there 👋

<!--
**poeta2475/poeta2475** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->

import time
import random

num_adivinar = random.randint(1,30)

nombre_player = input("¿nombre del jugador? ".title())
time.sleep(1)
print(f"hola {nombre_player} como estas\n".title())
time.sleep(1)
print("tendras 5 opciones para adivinar el numero correcto:".title())
time.sleep(1)
imgresar_numero = int(input("ingresa un numero por favor: "))



if imgresar_numero == num_adivinar:
    print("ganaste".title())

else:
    if imgresar_numero > num_adivinar:
     print("es un numero menor al elegido".title())

    else:
        print("intenta un numero mas grande.".title())
        print("a proposito te quedadan solo cuatro intentos mas".title())

    print("\n te quedan cuatro intentos".title())
    ingresar_numero = input("intenta otra vez.".title())
    if imgresar_numero == num_adivinar:
        print("ganaste".title())

    else:
        if imgresar_numero > num_adivinar:
            print("es un numero menor al elegido".title())

        else:
            print("intenta un numero mas grande.".title())
            print("a proposito te quedadan solo tres intentos mas".title())

        print("\n te queda tres intentos".title())
        ingresar_numero = input("intenta otra vez.".title())
        if imgresar_numero == num_adivinar:
            print("ganaste".title())

        else:
            if imgresar_numero > num_adivinar:
                print("es un numero menor al elegido".title())

            else:
                print("intenta un numero mas grande.".title())
                print("a proposito te quedadan solo dos intentos mas".title())

            print("\n te queda dos intentos".title())
            ingresar_numero = input("intenta otra vez.".title())
            if imgresar_numero == num_adivinar:
                print("ganaste".title())

            else:
                if imgresar_numero > num_adivinar:
                    print("es un numero menor al elegido".title())

                else:
                    print("intenta un numero mas grande.".title())
                    print("a proposito te quedadan solo un intentos mas".title())

                print("\n te queda solo un intento mas.".title())
                ingresar_numero = input("intenta otra vez.".title())

                if imgresar_numero > num_adivinar:
                    print("Ganaste")
                else:
                    print("Perdiste")
