from lista_enlazada import ListaEnlazada

class Playlist:
    def __init__(self):
        self.playlist = ListaEnlazada()

    def agregar_cancion(self, cancion):
        self.playlist.agregar(cancion)
        print(f"'{cancion}' ha sido agregada a la playlist.")

    def eliminar_cancion(self, cancion):
        if self.playlist.eliminar(cancion):
            print(f"'{cancion}' ha sido eliminada de la playlist.")
        else:
            print(f"'{cancion}' no se encontró en la playlist.")

    def mostrar_playlist(self):
        canciones = self.playlist.mostrar()
        if canciones:
            print("Playlist actual:")
            for cancion in canciones:
                print(f"- {cancion}")
        else:
            print("La playlist está vacía.")

    def buscar_cancion(self, cancion):
        if self.playlist.buscar(cancion):
            print(f"'{cancion}' está en la playlist.")
        else:
            print(f"'{cancion}' no se encuentra en la playlist.")


def menu():
    playlist = Playlist()
    while True:
        print("\nGestión de Playlist de Música")
        print("1. Agregar canción")
        print("2. Eliminar canción")
        print("3. Mostrar playlist")
        print("4. Buscar canción")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cancion = input("Ingrese el nombre de la canción: ")
            playlist.agregar_cancion(cancion)
        elif opcion == "2":
            cancion = input("Ingrese el nombre de la canción a eliminar: ")
            playlist.eliminar_cancion(cancion)
        elif opcion == "3":
            playlist.mostrar_playlist()
        elif opcion == "4":
            cancion = input("Ingrese el nombre de la canción a buscar: ")
            playlist.buscar_cancion(canc
