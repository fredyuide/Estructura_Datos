class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if self.is_empty():
            # Primera inserción, el nodo se apunta a sí mismo
            new_node.next = new_node.prev = new_node
            self.head = new_node
        else:
            temp = self.head
            if position == 0:
                # Insertar al inicio
                new_node.next = self.head
                new_node.prev = self.head.prev
                self.head.prev.next = new_node
                self.head.prev = new_node
                self.head = new_node
            else:
                # Insertar en una posición específica
                for _ in range(position - 1):
                    temp = temp.next
                    if temp == self.head:  # Si llegamos al final, romper el bucle
                        break
                new_node.next = temp.next
                new_node.prev = temp
                temp.next.prev = new_node
                temp.next = new_node

    def delete_first(self):
        if self.is_empty():
            print("La lista está vacía.")
        elif self.head.next == self.head:
            # Solo hay un elemento
            self.head = None
        else:
            self.head.prev.next = self.head.next
            self.head.next.prev = self.head.prev
            self.head = self.head.next

    def delete_last(self):
        if self.is_empty():
            print("La lista está vacía.")
        elif self.head.next == self.head:
            # Solo hay un elemento
            self.head = None
        else:
            last = self.head.prev
            last.prev.next = self.head
            self.head.prev = last.prev

    def display_forward(self):
        if self.is_empty():
            print("La lista está vacía.")
            return
        temp = self.head
        print("Lista en dirección hacia adelante:")
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()

    def display_backward(self):
        if self.is_empty():
            print("La lista está vacía.")
            return
        temp = self.head.prev
        print("Lista en dirección hacia atrás:")
        while True:
            print(temp.data, end=" ")
            temp = temp.prev
            if temp.next == self.head:
                break
        print()


# Menú interactivo
def menu():
    cdll = CircularDoublyLinkedList()
    while True:
        print("\n--- Menú ---")
        print("1. Insertar un elemento en una posición específica")
        print("2. Eliminar el primer elemento")
        print("3. Eliminar el último elemento")
        print("4. Mostrar elementos hacia adelante")
        print("5. Mostrar elementos hacia atrás")
        print("6. Salir")
        choice = int(input("Seleccione una opción: "))

        if choice == 1:
            data = int(input("Ingrese el dato a insertar: "))
            position = int(input("Ingrese la posición (0 para inicio): "))
            cdll.insert_at_position(data, position)
        elif choice == 2:
            cdll.delete_first()
        elif choice == 3:
            cdll.delete_last()
        elif choice == 4:
            cdll.display_forward()
        elif choice == 5:
            cdll.display_backward()
        elif choice == 6:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
