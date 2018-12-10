# -*- coding: utf-8 -*-

class Objetivo:
	def __init__(self, nombre, acciones):
		self.nombre = str(nombre)
		self.acciones = dict(acciones)

	def interactuar(self, interaccion):
		try:
			resultados = self.acciones[interaccion].split(":")
			try:
				return resultados[0], int(resultados[1])
			except IndexError:
				return resultados[0], -1
		except KeyError:
			return "¿Por qué haría eso?", -1

def separarOracion(oracion):
	palabras = oracion.split(" ")
	try:
		return palabras[0], palabras[1], palabras[2:]
	except IndexError:
		return palabras[0], "", ""

def leerArchivo(nombre):
	texto = []
	with open(nombre, "r", encoding="utf-8") as archivo:
		for linea in archivo:
			linea = linea.strip()
			if len(linea) > 0:
				texto.append(linea)

	objetos = []
	i = 0
	while i in range(len(texto)):
		if texto[i] == "[Objetos]":
			i += 1
			while texto[i][0] == '=':
				nombre = texto[i][1:]
				acciones = {}
				i += 1
				while(texto[i][0] == '*'):
					entrada = texto[i][1:].split("-")
					acciones[entrada[0]] = entrada[1]
					i += 1

				objetos.append(Objetivo(nombre, acciones))
		if texto[i] == "[Banderas]":
			banderas = []
			i += 1
			while texto[i][1] == ".":
				banderas.append(bool(texto[i][2]))
				i += 1
		i += 1
	return objetos, banderas

objetos, banderas = leerArchivo(input("Escribe el nombre del archivo: "))

while True:
	print("="*25)
	oracion = input()
	accion, objetivo, extras = separarOracion(oracion)

	for indice in range (len(objetos)):
		if objetos[indice].nombre.lower() == objetivo:
			break

	if len(oracion) > 0:
		if len(objetivo) > 0:
			texto, bandera = objetos[indice].interactuar(accion)
			print(texto)
			if bandera >= 0:
				banderas[bandera] = not banderas[bandera]
		else:
			print("¿{} qué?".format(accion))

	if banderas[0]:
		print("La cama no está rota")
	else:
		print("La cama está rota")

	if banderas[1]:
		print("A la mesa no le pasa nada")
	else:
		print("La mesa está de cabeza")