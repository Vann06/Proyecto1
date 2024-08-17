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
import sys


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
            else:
                operar_con(sets[0], sets[1])
        elif opcion == 3:
            print("Saliendo del programa...")
            sys.exit()
        else:
            print("ERROR: Ingrese algunas de las opciones disponibles")
            menu()

#MENU principal
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
                      "OPCIONES: letras (A-Z) y numeros (0-9)\n >")).upper()
    elementos_validos = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    conjunto_user = set()

    for e in elemento.strip():
        # Ignorar espacios
        if e == ' ':
            continue
        # Agregar al conjunto si pertenece a las opciones
        elif e in elementos_validos:
            conjunto_user.add(e)
        else:
            print(f"ERROR: {e} NO pertenece a las opciones permitidas.")
            return menu()

    #Verificar que el conjunto no este vacio
    if conjunto_user:
        print(f"Conjunto construido: {conjunto_user}")
    else:
        print("No se agregaron elementos válidos al conjunto.")
        return menu()

    return conjunto_user


# MENU de operaciones a realizar
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

        if opcion == 1:
            print("*COMPLEMENTO*")
        elif opcion == 2:
            print("*UNION*")
        elif opcion == 3:
            print("*INTERSECCION*")
        elif opcion == 4:
            print("*DIFERENCIA*")
        elif opcion == 5:
            print("*SIMETRICA*")
        elif opcion == 6:
            return
        else:
            print("ERROR: Opcion invalida")


main()
