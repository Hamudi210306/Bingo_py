import random
import time
import os

def limpiar_pantalla():
    # Limpia la pantalla en Windows ('cls') o Unix ('clear')
    os.system('cls' if os.name == 'nt' else 'clear')

def generar_carton():
    carton = []
    while len(carton) < 25:
        numero = random.randint(1, 75)
        if numero not in carton:
            carton.append(numero)
    return carton

def mostrar_carton(carton):
    print("\n=== TU CARTÓN DE BINGO ===")
    print("B  I  N  G  O")
    for i in range(5):
        for j in range(5):
            print(f"{carton[i*5 + j]:2}", end=" ")
        print()
    print("\nPresiona 'q' en cualquier momento para salir al menú principal")

def mostrar_menu():
    limpiar_pantalla()
    print("\n=== BINGO GAME ===")
    print("1. Jugar")
    print("2. Cómo jugar")
    print("3. Salir")
    return input("\nSeleccione una opción (1-3): ")

def mostrar_instrucciones():
    limpiar_pantalla()
    print("\n=== CÓMO JUGAR ===")
    print("1. Se te asignará un cartón con 25 números aleatorios")
    print("2. En cada turno se sacará un número al azar")
    print("3. Si tienes el número en tu cartón, se marcará con una X")
    print("4. Para ganar, debes completar todo tu cartón")
    input("\nPresiona Enter para volver al menú principal...")

def main():
    while True:
        opcion = mostrar_menu()
        
        if opcion.lower() == 'q':
            limpiar_pantalla()
            print("\n¡Volviendo al menú principal!")
            time.sleep(1)
            continue
            
        if opcion == "1":
            limpiar_pantalla()
            nombre = input("\nPor favor, ingresa tu nombre: ")
            if nombre.lower() == 'q':
                continue
                
            limpiar_pantalla()
            print(f"\n¡Bienvenido/a {nombre} al Bingo!")
            print("Preparando tu cartón...")
            time.sleep(1)
            
            carton_jugador = generar_carton()
            numeros_sacados = []
            limpiar_pantalla()
            mostrar_carton(carton_jugador)
            
            while True:
                accion = input("\nPresiona Enter para sacar un número...")
                if accion.lower() == 'q':
                    limpiar_pantalla()
                    print("\n¡Volviendo al menú principal!")
                    time.sleep(1)
                    break
                    
                limpiar_pantalla()
                
                while True:
                    numero = random.randint(1, 75)
                    if numero not in numeros_sacados:
                        numeros_sacados.append(numero)
                        break
                
                print(f"\n¡Ha salido el número {numero}!")
                
                if numero in carton_jugador:
                    print("¡Tienes ese número en tu cartón!")
                    carton_jugador[carton_jugador.index(numero)] = "X"
                    mostrar_carton(carton_jugador)
                    
                    if carton_jugador.count("X") == 25:
                        print("\n¡¡¡BINGO!!!")
                        print("¡Has ganado!")
                        time.sleep(2)
                        break
                else:
                    print("No tienes ese número en tu cartón")
                    mostrar_carton(carton_jugador)
                
                time.sleep(1)
        
        elif opcion == "2":
            mostrar_instrucciones()
        
        elif opcion == "3":
            limpiar_pantalla()
            print("\n¡Gracias por jugar! ¡Hasta pronto!")
            time.sleep(2)
            break
        
        else:
            print("\nOpción no válida. Por favor, seleccione 1, 2 o 3.")
            time.sleep(1)

if __name__ == "__main__":
    main()
    
