# sistema gestion biblioteca

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla inmutable (titulo, autor)
        self.datos = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"[{self.isbn}] {self.datos[0]} de {self.datos[1]} | Categoría: {self.categoria}"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros(self):
        if not self.libros_prestados:
            print(f"{self.nombre} no tiene libros prestados.")
        else:
            print(f"Libros prestados a {self.nombre}:")
            for libro in self.libros_prestados:
                print(" -", libro)


class Biblioteca:
    def __init__(self):
        self.libros = {}      # Diccionario: ISBN → Libro
        self.usuarios = {}    # Diccionario: ID → Usuario
        self.ids_usuarios = set()  # Conjunto de IDs únicos

    #libros
    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print("✗ Ya existe un libro con ese ISBN.")
        else:
            self.libros[libro.isbn] = libro
            print(f"✓ Libro añadido: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            eliminado = self.libros.pop(isbn)
            print(f"✓ Libro eliminado: {eliminado}")
        else:
            print("✗ No existe un libro con ese ISBN.")

    #usuarios
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print("✗ Ya existe un usuario con ese ID.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"✓ Usuario registrado: {usuario.nombre}")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.ids_usuarios:
            eliminado = self.usuarios.pop(id_usuario)
            self.ids_usuarios.remove(id_usuario)
            print(f"✓ Usuario dado de baja: {eliminado.nombre}")
        else:
            print("✗ No existe un usuario con ese ID.")

    #préstamos
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("✗ Usuario no encontrado.")
            return
        if isbn not in self.libros:
            print("✗ Libro no encontrado.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros.pop(isbn)  # Lo quitamos de la biblioteca
        usuario.prestar_libro(libro)
        print(f"✓ {libro.datos[0]} prestado a {usuario.nombre}")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("✗ Usuario no encontrado.")
            return

        usuario = self.usuarios[id_usuario]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.devolver_libro(libro)
                self.libros[isbn] = libro  # Regresa al catálogo
                print(f"✓ {libro.datos[0]} devuelto por {usuario.nombre}")
                return
        print("✗ Ese libro no estaba prestado a este usuario.")

    #busquedas
    def buscar_libro(self, texto):
        texto = texto.lower()
        resultados = [
            libro for libro in self.libros.values()
            if texto in libro.datos[0].lower()
            or texto in libro.datos[1].lower()
            or texto in libro.categoria.lower()
        ]
        if resultados:
            print("Resultados de la búsqueda:")
            for libro in resultados:
                print(" -", libro)
        else:
            print("✗ No se encontraron coincidencias.")

    # listar
    def mostrar_catalogo(self):
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            print("Catálogo de libros disponibles:")
            for libro in self.libros.values():
                print(" -", libro)


def menu():
    biblio = Biblioteca()

    while True:
        print("\n===== MENÚ BIBLIOTECA =====")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Mostrar catálogo")
        print("9. Listar libros prestados por usuario")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblio.añadir_libro(libro)

        elif opcion == "2":
            isbn = input("ISBN del libro a quitar: ")
            biblio.quitar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            id_usuario = int(input("ID de usuario: "))
            usuario = Usuario(nombre, id_usuario)
            biblio.registrar_usuario(usuario)

        elif opcion == "4":
            id_usuario = int(input("ID del usuario a dar de baja: "))
            biblio.dar_baja_usuario(id_usuario)

        elif opcion == "5":
            id_usuario = int(input("ID del usuario: "))
            isbn = input("ISBN del libro: ")
            biblio.prestar_libro(id_usuario, isbn)

        elif opcion == "6":
            id_usuario = int(input("ID del usuario: "))
            isbn = input("ISBN del libro: ")
            biblio.devolver_libro(id_usuario, isbn)

        elif opcion == "7":
            texto = input("Texto de búsqueda (título, autor o categoría): ")
            biblio.buscar_libro(texto)

        elif opcion == "8":
            biblio.mostrar_catalogo()

        elif opcion == "9":
            id_usuario = int(input("ID del usuario: "))
            if id_usuario in biblio.usuarios:
                biblio.usuarios[id_usuario].listar_libros()
            else:
                print("✗ Usuario no encontrado.")

        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("✗ Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()


#crear la biblioteca
biblio = Biblioteca()

#añadir libros
l1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "12345")
l2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Infantil", "67890")
biblio.añadir_libro(l1)
biblio.añadir_libro(l2)

#registrar usuarios
u1 = Usuario("Daniel", 1)
u2 = Usuario("María", 2)
biblio.registrar_usuario(u1)
biblio.registrar_usuario(u2)

#mostrar catálogo
biblio.mostrar_catalogo()

#prestar y devolver
biblio.prestar_libro(1, "12345")
u1.listar_libros()
biblio.mostrar_catalogo()

biblio.devolver_libro(1, "12345")
biblio.mostrar_catalogo()

#buscar
biblio.buscar_libro("principito")
