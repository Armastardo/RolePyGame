class Bandera:
	def __init__(self, apagada, encendida, estado):
		self.estado = bool(estado)
		self.apagada = str(apagada)
		self.encendida = str(encendida)

	def toggle(self):
		self.estado = not self.estado

	def __str__(self):
		if self.estado:
			return self.encendida
		else:
			return self.apagada

class Habitacion:
	def __init__(self, dialogo, opciones):
		self.dialogo = dialogo
		self.opciones = list(opciones)


class Opcion:
	def __init__(self, requerimentos, textoOpcion,\
	 consecuencias, textoE, destino):
		self.requerimentos = requerimentos
		self.consecuencias = consecuencias
		self.textoOpcion = textoOpcion
		self.textoE = textoE
		self.destino = destino
		
	def __str__(self):
		return self.textoOpcion