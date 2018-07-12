from gameClasses import Bandera, Opcion, Habitacion

def crearOpcion(cadena):
	temp = cadena.split("]")
	req = temp[0][1:].split(",")
	text = temp[1].split("[")[0]
	con = temp[1].split("[")[1]#.split(",")
	temp = temp[2].split(":")
	textE = temp[0]
	dest = temp[1]

	return Opcion(req, text, con, textE, dest)

def crearBandera(cadena):
	text = cadena.split(":")[1].split("_")
	if len(text) < 3:
		text.append(0)
	return Bandera(text[0], text[1], int(text[2]))

def leerArchivo(ruta):
	data = []
	banderas = dict()
	habitaciones = dict()
	error = False
	try:
		with open(ruta, "r", encoding="utf-8") as archivo:
			for i, linea in enumerate(archivo):
				linea = linea.strip()
				linea = linea.split("#")[0].lstrip().rstrip()
				valor = linea.count("[") - linea.count("]")
				if linea.count("[") - linea.count("]") != 0:
					error = True
					print("¡Error en la línea {0}! ".format(i+1),end='')
					if valor > 0:
						print("Faltó cerrar una llave")
					elif valor < 0:
						print("Hay una llave abierta que necesita cerrarse")
				data.append(linea)

		for i in range (len(data)):
			if data[i] == "[Banderas]":
				i += 1
				while data[i]:
					key = data[i].split(":")[0]
					banderas[key] = crearBandera(data[i])
					i += 1
				break

		data = data[i+1:]

		i = 0

		while i<(len(data)):
			key = data[i][1:-1]
			i += 1
			dialog = data[i]
			i += 1
			opciones = []
			try:
				while data[i]:
					opciones.append(crearOpcion(data[i]))
					i += 1
			except IndexError:
				pass
				i += 1
			i += 1
			habitaciones[key] = Habitacion(dialog, opciones)

		if error:
			return error, None, None
		else:
			return error, banderas, habitaciones
	except FileNotFoundError:
		print("No se ha encontrado ningún archivo con ese nombre.")
		return True, None, None