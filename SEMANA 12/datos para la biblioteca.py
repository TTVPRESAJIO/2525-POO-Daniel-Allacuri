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
