import textParser
import textwrap
from gameClasses import Bandera, Habitacion, Opcion
from os import system, name

def cumplenRequerimentos(banderas, opcion):
	for requerimento in opcion.requerimentos:
		if requerimento:
			if requerimento[0] == "-":
				if not banderas[requerimento[1:]].estado:
					return True
			elif banderas[requerimento].estado:
				return True
		else:
			return True
	return False

def leerOpcion():
	try:
		opc = int(input())
		return opc, False
	except ValueError:
		print("¡Error! Escribe un número")
		return -1, True

def jugar(ruta):
	error, banderas, habitaciones = textParser.leerArchivo(ruta)

	if not error:
		if name == 'nt':
			_ = system('cls')
		else:
			_ = system('clear')
		
		habActual = habitaciones["Inicio"] 

		w = textwrap.TextWrapper(replace_whitespace=False)

		while True:
			print("="*30)
			print(w.fill(habActual.dialogo))
			#print(habActual.dialogo)

			opc = 0
			disponibles = []
			print("")
			for opcion in habActual.opciones:
				if cumplenRequerimentos(banderas, opcion):
					disponibles.append(opcion)
					print(str(opc+1) +") "+ str(opcion))
					opc += 1
			print("Elige una opción: ", end='')

			eleccion, error = leerOpcion()

			while error or eleccion > len(disponibles) or eleccion < 1:
				if not error:
					print("Por favor, elige una opción que esté disponible.")
				eleccion, error = leerOpcion()

			decision = disponibles[eleccion-1]
			
			if decision.textoE:
				print(decision.textoE+"\n")
			
			if decision.consecuencias:
				banderas[decision.consecuencias].toggle()

			if decision.destino == "Fin":
				print("\n"+habitaciones[decision.destino].dialogo)
				break
			else:
				habActual = habitaciones[decision.destino]