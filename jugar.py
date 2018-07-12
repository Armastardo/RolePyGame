import juego


mensaje = "¡Bienvenido a la primera versión del motor de juegos de texto!\n"
mensaje += "Este programa está en una versión muy temprana de desarrollo y\n"
mensaje += "no hay mucho que mostrar, pero aún así espero que lo disfrutes. :)"

print(mensaje)
ruta = input("Introduce el nombre del archivo que contiene el juego (con extensión): ")
juego.jugar(ruta)