from pyswip import Prolog

prolog = Prolog()
prolog.consult("medicamento.pl")
from pyswip import Prolog
def mostrar_menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Consultar medicamento por nombre")
        print("2. Consultar medicamentos por forma")
        print("3. Agregar medicamento")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            consultar_medicamentos()
        elif opcion == '2':
            consultar_medicamentos_por_forma()
        elif opcion == '3':
            agregar_medicamento()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 4.")


def existe_medicamento(medicamento):
    formas = list(prolog.query(f"disponible(Forma, {medicamento})"))
    if formas:
        return formas[0]["Forma"]
    else:
        return None
def consultar_medicamentos():
    medicamento = input("Ingrese el nombre del medicamento: ")
    medicamento = medicamento.split("/")[-1].split("\\")[-1]
    
    forma_disponible = existe_medicamento(medicamento)
    if forma_disponible:
        print(f"El medicamento '{medicamento}' está disponible en forma de '{forma_disponible}'.")
    else:
        print(f"El medicamento '{medicamento}' no está disponible en el sistema.")
def consultar_medicamentos_por_forma():
    opciones = ["tableta", "pomada", "infusion", "jarabe"]
    
    print("Seleccione la forma en la que desea consultar la existencia del medicamento:")
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    
    while True:
        try:
            opcion_seleccionada = int(input("Ingrese el número correspondiente a la opción: "))
            if 1 <= opcion_seleccionada <= len(opciones):
                forma = opciones[opcion_seleccionada - 1]
                break
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    print(f"Medicamentos disponibles en forma de '{forma}':")
    medicamentos = list(prolog.query(f"disponible('{forma}', Medicamento)"))
    for med in medicamentos:
        print(med["Medicamento"])
def agregar_medicamento():
    formas_disponibles = ["pomada", "tableta", "ungüento", "jarabe"]

    print("Formas disponibles:")
    for i, forma in enumerate(formas_disponibles, 1):
        print(f"{i}. {forma}")

    opcion = int(input("Seleccione la forma del medicamento: "))
    
    if opcion < 1 or opcion > len(formas_disponibles):
        print("Opción inválida. Por favor seleccione una forma válida.")
        return
    
    forma_seleccionada = formas_disponibles[opcion - 1]
    nombre = input("Ingrese el nombre del medicamento: ")

    if list(prolog.query(f"disponible('{forma_seleccionada}', '{nombre}')")):
        print("El medicamento ya existe en la base de conocimientos.")
    else:
        prolog.assertz(f"disponible('{forma_seleccionada}', '{nombre}')")
        print(f"El medicamento '{nombre}' en forma de '{forma_seleccionada}' ha sido agregado correctamente.")
    consultar_medicamentos()

mostrar_menu()