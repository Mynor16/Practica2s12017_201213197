from flask import Flask, request, Response
app = Flask('EDD_PRACTICA2')

class nodoLista:
	def __init__(self, palabra,correlativo):
		self.id = correlativo
		self.palabra = palabra
		self.siguiente = None


class Lista:

	def __init__(self):
		self.primero = None
		self.contador=0

	def insertar(self,parametro):
		nodo = nodoLista(parametro, self.contador)
		print "se insertara la palabra: ", nodo.palabra
		if self.primero == None:
			self.primero = nodo
		else:
			aux = self.primero
			while True:
				if aux.siguiente == None:
					aux.siguiente=nodo
					break
				else:
					aux = aux.siguiente
		self.contador = self.contador + 1

	def consultar(self):
		aux = self.primero
		if aux.palabra==None:
			print"lista vacia"
		else:
			print aux.id
			print aux.palabra

			while aux.siguiente!= None:
				aux = aux.siguiente
				print aux.id
				print aux.palabra

	def eliminar(self,elemento):
		aux = self.primero
		aux2 = self.primero
		if aux.id == None:
			print "no hay elementos en la lista"
		else:

			if aux.id == elemento:
				if aux.siguiente == None:
					self.primero = nodo()
				else:
					self.primero = aux.siguiente
			else:
				t = True
				while aux.siguiente != None and t:
					aux = aux.siguiente
					print"comparando elemento: ",aux.id," con el id a eliminar: ", elemento
					if aux.id == elemento:
						print"el elemento ",aux.id," es igual a ", elemento
						aux2.siguiente=aux.siguiente
						aux = None
						t = False
						break
					aux2 = aux2.siguiente
				if t==True:
					print "ID no encontrado"


	def buscar(self,elemento):
		aux = self.primero
		if aux.palabra == None:
			return None
		else:

			if aux.palabra == elemento:
				return aux.id
			else:
				t = True
				while aux.siguiente != None and t:
					aux = aux.siguiente
					if aux.palabra == elemento:
						print"el elemento ",aux.palabra," es igual a ", elemento
						t = False
						return aux.id
				if t==True:
					print "ID no encontrado"

"""miLista = Lista()
@app.route('/insertarLista',methods=['POST'])
def insertarLista():
	parametro= str(request.form['dato'])
	miLista.insertar(srt(parametro))
	miLista.consultar()
	return 'ok'


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')"""


		


class principal:


	lista = Lista()
	lista.contador=0
	while True:
		print "***Menu***"
		print "1) insertar"
		print "2) consultar"
		print "3) eliminar"
		print "4) buscar"
		print "5) salir"
		try:
			option = input("elige tu opcion: ")
			if option == 1:
				palabra = raw_input("escribe tu palabra: ")
				print "se almacenara la palabra : ",palabra, "con id: ",lista.contador
				lista.insertar(palabra)
			elif option == 2:
				lista.consultar()
			elif option == 3:
				elemento = input("escribe el id del elemento a eliminar: ")
				print "se eliminara el elemento con id: ", elemento
				lista.eliminar(elemento)
			elif option == 4:
				elemento = raw_input("escrie el nombre a buscar: ")
				print "resultado encontrado en el id: "
				print lista.buscar(elemento)
			elif option == 5:
				break
		except Exception as e:
			print "ocurrio un error"
			print e