"""
UNIVERSIDAD DEL VALLE DE GUATEMALA
Matematica Discreta

Proyecto 1
Descripcion: Construir y almacenar conjuntos
             Realizar operaciones de conjuntos

Autores: Vianka Castro 23201
         Ricardo Godinez 23247
Fecha:   Agosto 17, 2024.
"""

# Constantes
ELEMENTOS_VALIDOS = 'abcdefghijklmnopqrstuvwxyz0123456789'

def char_to_bin(c):
    """Convierte un carácter en su correspondiente índice binario"""
    return 1 << ELEMENTOS_VALIDOS.index(c)

def conjunto_to_bin(conjunto):
    """Convierte una lista de caracteres a su representación binaria"""
    binario = 0
    for char in conjunto:
        binario |= char_to_bin(char)
    return binario

def bin_to_conjunto(binario):
    """Convierte una representación binaria a una lista de caracteres"""
    conjunto = []
    for i, c in enumerate(ELEMENTOS_VALIDOS):
        if binario & (1 << i):
            conjunto.append(c)
    return conjunto

def construir_con():
    """Función para construir un conjunto a partir de la entrada del usuario"""
    print("*** Construcción de Conjuntos ***")
    elemento = input(
        "Ingrese los elementos del conjunto que desea agregar:\n"
        "OPCIONES: letras (A-Z) y números (0-9)\n >"
    ).lower()
    
    conjunto = []

    for e in elemento.strip():
        if e in ELEMENTOS_VALIDOS and e not in conjunto:
            conjunto.append(e)
        elif e not in ELEMENTOS_VALIDOS:
            print(f"ERROR: {e} NO pertenece a las opciones permitidas.")
            return None

    conjunto_bin = conjunto_to_bin(conjunto)
    print(f"Conjunto construido: {conjunto}")
    return conjunto_bin

def operar_con(conjunto_bin1, conjunto_bin2):
    """Función para realizar operaciones entre dos conjuntos de forma manual"""
    while True:
        print("*** Operaciones con Conjuntos ***")
        print(
            "Opciones Disponibles:\n"
            "1: Complemento\n"
            "2: Unión\n"
            "3: Intersección\n"
            "4: Diferencia\n"
            "5: Diferencia Simétrica\n"
            "6: Regresar a menú principal"
        )
        try:
            opcion = int(input("Ingrese alguna de las opciones\n> "))
        except ValueError:
            print("ERROR: Ingrese algo válido")
            continue

        conjunto_resultado = 0

        if opcion == 1:
            print("*COMPLEMENTO*")
            for i in range(36):
                if not (conjunto_bin1 & (1 << i)):
                    conjunto_resultado |= (1 << i)

        elif opcion == 2:
            print("*UNIÓN*")
            for i in range(36):
                if (conjunto_bin1 & (1 << i)) or (conjunto_bin2 & (1 << i)):
                    conjunto_resultado |= (1 << i)

        elif opcion == 3:
            print("*INTERSECCIÓN*")
            for i in range(36):
                if (conjunto_bin1 & (1 << i)) and (conjunto_bin2 & (1 << i)):
                    conjunto_resultado |= (1 << i)

        elif opcion == 4:
            print("*DIFERENCIA*")
            for i in range(36):
                if (conjunto_bin1 & (1 << i)) and not (conjunto_bin2 & (1 << i)):
                    conjunto_resultado |= (1 << i)

        elif opcion == 5:
            print("*DIFERENCIA SIMÉTRICA*")
            for i in range(36):
                if (conjunto_bin1 & (1 << i)) != (conjunto_bin2 & (1 << i)):
                    conjunto_resultado |= (1 << i)

        elif opcion == 6:
            return

        else:
            print("ERROR: Opción inválida")
            continue

        if conjunto_resultado != 0:
            print("Resultado:", bin_to_conjunto(conjunto_resultado))
        else:
            print("Resultado: Conjunto vacío")

def menu():
    """Función que muestra el menú principal y devuelve la opción seleccionada"""
    print("********* Bienvenido a Operaciones con Conjuntos **********\n")
    print("Menú Principal")
    opcion = input(
        "1: Construir conjuntos\n"
        "2: Operar conjuntos\n"
        "3: Finalizar Programa\n"
        "Por favor ingrese su opción\n> "
    )
    return opcion

def main():
    """Función principal que coordina el flujo del programa"""
    conjuntos_bin = []

    while True:
        try:
            opcion = int(menu())
        except ValueError:
            print("ERROR: Ingrese algo válido")
            continue

        if opcion == 1:
            conjunto_bin = construir_con()
            if conjunto_bin is not None:
                conjuntos_bin.append(conjunto_bin)

        elif opcion == 2:
            if len(conjuntos_bin) < 2:
                print("ERROR: Necesitas al menos 2 conjuntos para operar")
            elif len(conjuntos_bin) > 2:
                print("Listas de opciones: ")
                for i, s in enumerate(conjuntos_bin):
                    print(f"SET {i+1}: {bin_to_conjunto(s)}")
                try:
                    con1 = int(input("Ingrese el primer conjunto \n> ")) - 1
                    con2 = int(input("Ingrese el segundo conjunto \n> ")) - 1
                    if con1 < 0 or con1 >= len(conjuntos_bin) or con2 < 0 or con2 >= len(conjuntos_bin):
                        print("ERROR: Uno de los conjuntos está fuera del rango")
                        continue
                    operar_con(conjuntos_bin[con1], conjuntos_bin[con2])
                except ValueError:
                    print("ERROR: Ingrese algo válido")
                    continue
            else:
                operar_con(conjuntos_bin[0], conjuntos_bin[1])

        elif opcion == 3:
            print("Saliendo del programa...")
            break

        else:
            print("ERROR: Ingrese alguna de las opciones disponibles")

main()
