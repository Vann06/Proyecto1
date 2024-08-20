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
            #Si solo son dos conjuntos se envian los conjuntos de una vez
            else:
                operar_con(conjuntos_bin[0], conjuntos_bin[1])

        elif opcion == 3:
            print("Saliendo del programa...")
            break

        else:
<<<<<<< HEAD
            print("ERROR: Ingrese alguna de las opciones disponibles")
=======
            print("ERROR: Ingrese algunas de las opciones disponibles")
            menu()

#MENU principal de opciones
def menu():
    print("********* Bienvenido a Operaciones con Conjuntos **********")
    print()
    print("Menu Principal")
    opcion = (input("1: Construir conjuntos "
                    "\n2: Operar conjuntos "
                    "\n3: Finalizar Programa "
                    "\nPorfavor ingrese su opcion\n>  "))
    return opcion


# Funcion para contruir un conjunto
def construir_con():
    print("*** Construccion de Conjuntos ***")
    elemento = input(("Ingrese los elementos del conjunto que desea agregar:\n"
                      "OPCIONES: letras (A-Z) y numeros (0-9)\n >")).lower()
    #Un set de los unicos elementos validos
    elementos_validos = set('abcdefghijklmnopqrstuvwxyz0123456789')
    conjunto_user = set()

    for e in elemento:
        # Ignorar espacios
        if e == ' ':
            continue
        # Agregar al conjunto si pertenece a las opciones validas
        elif e in elementos_validos:
            conjunto_user.add(e)
        else:
            print(f"ERROR: {e} NO pertenece a las opciones permitidas.")
            return menu()

    #Verificar que el conjunto no este vacio??
    if conjunto_user:
        print(f"Conjunto construido: {conjunto_user}")
    else:
        print("No se agregaron elementos válidos al conjunto.")
        return menu()

    return conjunto_user


# MENU de Operaciones
def operar_con(set1, set2):
    while True:
        print("*** Operaciones con Conjuntos ***")
        print("Opciones Disponibles:")
        print("1: Complemento\n2: Union\n3: Interseccion\n4: Diferencia\n"
              "5: Diferencia Simetrica\n6: Regresar a menu principal")
        try:
            opcion = int(input("Ingrese alguna de las opciones\n>"))
        except ValueError:
            print("ERROR: Ingrese algo valido")
            continue
        match opcion:
            case  1:
                #El complemento regresa lo que hay en el conjunto 2 pero no en el 1
                print("*COMPLEMENTO*")
                conjunto_resultado = set()
                for e in set2:
                    encontrado = False
                    for i in set1:
                        if e == i:
                            encontrado = True
                            break
                    if not encontrado:
                        conjunto_resultado.add(e)
                    print("Los conjuntos son iguales")
                else:
                    print("El complemento del conjunto 1 al conjunto 2 es \n", conjunto_resultado)
            case 2:
                #En la union se crea un nuevo conjunto de todos los valores de cada uno
                print("*UNION*")
                conjunto_resultado = set()
                for e in set1:
                    conjunto_resultado.add(e)

                for e in set2:
                    conjunto_resultado.add(e)

                print("El conjunto resultante de la union de los conjuntos ingresados es\n",conjunto_resultado)        
                    
            case 3:
                #Es un conjunto de los valores que estan en los dos
                print("*INTERSECCION*")
                conjunto_resultado = set()
                for e in set1:
                    for i in set2:
                        #si son iguales los agrega
                        if e == i:
                            conjunto_resultado.add(e)

                #Si no se guardo ninguno, no hay ninguno igual
                if len(conjunto_resultado) == 0:
                    print("No hay elemnetos en comun entre los conjuntos seleccionados")
                else:
                    print("La interseccion de los conjuntos es \n", conjunto_resultado)        

            case 4:
                #Que valores tienen de diferente del primero con el segundo
                print("*DIFERENCIA*")
                conjunto_resultado = set()
                for e in set1:
                    encontrado = False
                    for i in set2:
                        if e == i:
                            encontrado = True
                            break
                    if not encontrado:
                        conjunto_resultado.add(e)    
                if len(conjunto_resultado) == 0:
                    print("Los conjuntos son iguales")
                else:
                    print("La diferencia del conjunto 1 al conjunto 2 es \n", conjunto_resultado)        
            case 5:
                #Se crea un conjunto de lo que haya en ninguno de los dos
                print("*DIFERENCIA SIMETRICA*")
                conjunto_resultado = set()
                for e in set1:
                    encontrado = False
                    for i in set2:
                        if e == i:
                            encontrado = True
                            break
                    if not encontrado:
                        conjunto_resultado.add(e)    

                for e in set2:
                    encontrado = False
                    for i in set1:
                        if e == i:
                            encontrado = True
                            break
                    if not encontrado:
                        conjunto_resultado.add(e)

                if len(conjunto_resultado) == 0:
                    print("Los conjuntos son iguales")
                else:
                    print("La simetrica diferencia de los conjuntos es \n", conjunto_resultado)  

            case 6:
                return
            #Si hay un espacio
            case _:
                print("ERROR: Opcion invalida")

>>>>>>> 7381efa57f713b08cd0f8a8178cc371f0d2aa068

main()
