from priority_manager import PriorityManager

def main():
    manager = PriorityManager()

    while True:
        print("\nGestión de Prioridades con AVL")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Salir")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            task_id = input("Ingrese la ID de la tarea: ")
            priority = int(input("Ingrese la prioridad: "))
            manager.add_task(task_id, priority)
        elif choice == "2":
            print("\nLista de Tareas:")
            manager.display_tasks(manager.root)
        elif choice == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
