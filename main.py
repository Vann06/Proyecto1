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

def main():
    sets = []
    while True:
        try:
            opcion = int(menu())
        except ValueError:
            print("ERROR: Ingrese algo valido")
            continue
        if opcion == 1:
            conjunto = construir_con()
            sets.append(conjunto)
        elif opcion == 2:
            #Error si no hay suficientes opciones
            if len(sets) < 2:
                print("ERROR: Necesitas al menos 2 conjuntos para operar")
            #Si existe mas opciones, dar a elegir
            elif len(sets) > 2:
                print("Listas de opciones: ")
                for i, s in enumerate(sets):
                    print(f"SET {i+1}: {s}")
                try:
                    con1 = int(input("Ingrese el primer conjunto \n>"))-1
                    con2 = int(input("Ingrese el segundo conjunto \n>"))-1
                    #Verificar que ambos pertenezcan a la lista de conjuntos
                    if con1 < 0 or con1 >= len(sets) or con2 < 0 or con2 >= len(sets):
                        print("ERROR: Uno de los conjuntos esta fuera del rango")
                        continue
                    operar_con(sets[con1],sets[con2])
                except ValueError:
                    print("ERROR: Ingrese algo valido")
                    continue
            #Si solo son dos conjuntos se envian los conjuntos de una vez
            else:
                operar_con(sets[0], sets[1])
        elif opcion == 3:
            print("Saliendo del programa...")
            break
        else:
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


main()
