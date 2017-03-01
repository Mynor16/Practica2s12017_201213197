class nodoLista:
	def __init__(self):
		self.palabra = None
		self.siguiente = None


class Lista:

	def __init__(self):
		self.primero = nodoLista()

	def insertar(self,nodo):
		if self.primero.palabra == None:
			self.primero = nodo
		else:
			aux = self.primero
			while True:
				if aux.siguiente == None:
					aux.siguiente=nodo
					break
				else:
					aux = aux.siguiente

	def consultar(self):
		aux = self.primero
		if aux.palabra==None:
			print"lista vacia"
		else:
			print aux.palabra

			while aux.siguiente!= None:
				aux = aux.siguiente
				print aux.palabra


class principal:
	lista = Lista()
	while True:
		print "***Menu***"
		print "1) insertar"
		print "2) consultar"
		print "3) salir"
		try:
			option = input("elige tu opcion: ")
			if option == 1:
				print "opcion 1 elegida"
				nodo = nodoLista()
				nodo.palabra = raw_input("escribe tu palabra: ")
				print "se guardo la palabra : ",nodo.palabra
				lista.insertar(nodo)
			elif option == 2:
				lista.consultar()
			elif option == 3:
				break
		except Exception as e:
			print "ocurrio un error"
			print e






	def vacia(self):
		if self.primero== None:
			return True
		else:
			return False

