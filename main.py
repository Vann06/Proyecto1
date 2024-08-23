"""
UNIVERSIDAD DEL VALLE DE GUATEMALA
Matematica Discreta

Proyecto 1
Descripcion: Construir y almacenar conjuntos
             Realizar operaciones de conjuntos
             por medio de cadenas binarias

Autores: Vianka Castro 23201
         Ricardo Godinez 23247
         
Fecha inicio:   Agosto 17, 2024
Fecha fin:      Agosto 22, 2024
"""

# Constantes
caracter = 'abcdefghijklmnopqrstuvwxyz0123456789'


# Función principal que coordina el flujo del programa
def main():
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
            # Validar que exista por lo menos dos conjuntos
            if len(conjuntos_bin) < 2:
                print("ERROR: Necesitas al menos 2 conjuntos para operar")
            # Si existen mas de dos conjuntos en el progama le pide al usuario
            # con cuales quiere trabajar
            elif len(conjuntos_bin) > 2:
                print("Listas de opciones: ")
                for i, s in enumerate(conjuntos_bin):
                    print(f"SET {i + 1}: {bin_to_conjunto(s)}")
                try:
                    con1 = int(input("Ingrese el primer conjunto \n> ")) - 1
                    con2 = int(input("Ingrese el segundo conjunto \n> ")) - 1
                    # Validacion del rango de los conjuntos
                    if con1 < 0 or con1 >= len(conjuntos_bin) or con2 < 0 or con2 >= len(conjuntos_bin):
                        print("ERROR: Uno de los conjuntos está fuera del rango")
                        continue
                    # Se lleva a operar
                    operar_con(conjuntos_bin[con1], conjuntos_bin[con2])
                except ValueError:
                    print("ERROR: Ingrese algo válido")
                    continue
            # Si solo son dos conjuntos se envian los conjuntos de una vez
            else:
                operar_con(conjuntos_bin[0], conjuntos_bin[1])

        elif opcion == 3:
            print("Saliendo del programa...")
            break
        else:
            print("ERROR: Ingrese algunas de las opciones disponibles")
            menu()


# Función que muestra el menú principal y devuelve la opción seleccionada
def menu():
    print("********* Bienvenido a Operaciones con Conjuntos **********\n")
    print("Menú Principal")
    opcion = input(
        "1: Construir conjuntos\n"
        "2: Operar conjuntos\n"
        "3: Finalizar Programa\n"
        "Por favor ingrese su opción\n> "
    )
    return opcion


# Convierte un carácter a su representacion bianria
# utilizando un desplazamiento de bits
def caracter_a_binario(c):
    return 1 << caracter.index(c)


# Convierte una lista de caracteres en un solo número
# binario utilizando la operación OR bit a bit
def conjunto_to_binario(conjunto):
    binario = 0
    # Si existe el caracter en
    for char in conjunto:
        # Combinacion de bits
        binario |= caracter_a_binario(char)
    return binario


# Convierte un número binario de vuelta a una lista de caracteres
def bin_to_conjunto(binario):
    conjunto = []
    for i, c in enumerate(caracter):
        if binario & (1 << i):
            conjunto.append(c)
    return conjunto


# Función para construir un conjunto a partir de la entrada del usuario
def construir_con():
    print("*** Construcción de Conjuntos ***")
    elemento = input(
        "Ingrese los elementos del conjunto que desea agregar:\n"
        "OPCIONES: letras (A-Z) y números (0-9)\n >").lower()

    conjunto = []

    for e in elemento.strip():
        # Valida si esta en caracteres y no esta repetido
        if e == " ":
            continue

        elif e in caracter and e not in conjunto:
            conjunto.append(e)
        # Si ingresa algo erroneo no se guarda el conjunto

        elif e not in caracter:
            print(f"ERROR: {e} NO pertenece a las opciones permitidas.")
            return None
    # Regresa el conjunto a binario
    conjunto_bin = conjunto_to_binario(conjunto)
    print(f"Conjunto construido: {conjunto}")
    return conjunto_bin


# Función para realizar operaciones entre conjuntos
def operar_con(conjunto_bin1, conjunto_bin2):
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

        # Resultado de cualquier operacion se guardara aqui
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


main()
