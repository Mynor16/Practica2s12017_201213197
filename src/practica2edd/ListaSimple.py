from flask import Flask, request, Response
from graphviz import Digraph
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
			self.graficarLista()
		else:
			aux = self.primero
			while True:
				if aux.siguiente == None:
					aux.siguiente=nodo
					self.graficarLista()
					break
				else:
					aux = aux.siguiente
		self.contador = self.contador + 1

	def consultar(self):
		aux = self.primero
		if aux==None:
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
		if aux == None:
			print "no hay elementos en la lista"
		else:

			if aux.id == elemento:
				if aux.siguiente == None:
					self.primero = nodoLista(self,"",None)
					self.graficarLista()
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
						self.graficarLista()
						aux = None
						t = False
						break
					aux2 = aux2.siguiente
				if t==True:
					print "ID no encontrado"


	def buscar(self,elemento):
		aux = self.primero
		retorno=""
		if aux == None:
			return "lisra vacia"
		else:

			if aux.palabra == elemento:
				print"el elemento ",aux.palabra," es igual al primer elemento: ", elemento
				return "Elemento encontrado en la posicion: ",aux.id
			else:
				t = True
				while aux.siguiente != None and t:
					aux = aux.siguiente
					if aux.palabra == elemento:
						print"el elemento ",aux.palabra," es igual a ", elemento
						t = False
						return "Elemento encontrado en la posicion: ",aux.id
				if t==True:
					print "ID no encontrado"
					return "No se encontro el dato :("

	def graficarLista(self):
		dot = Digraph(comment='GraficaListaSimple')
		dot  #doctest: +ELLIPSIS
		aux = self.primero
		if aux==None:
			print"lista vacia"
		else:
			print aux.id
			print aux.palabra
			while aux.siguiente!= None:
				dot.node(str(aux.id), aux.palabra)
				dot.node(str(aux.siguiente.id), aux.siguiente.palabra)
				dot.edge(str(aux.id), str(aux.siguiente.id), constraint='false')
				aux = aux.siguiente
				print aux.id
				print aux.palabra
			print(dot.source)
			dot.render('test-output/ListaSimple.dot', view=False)

miLista = Lista()

@app.route('/insertarLista',methods=['POST'])
def insertarLista():
	print"insertando en lista"
	parametro= str(request.form['dato'])
	miLista.insertar(str(parametro))
	miLista.consultar()
	return "ok insertar"

@app.route('/eliminarLista',methods=['POST'])
def eliminarLista():
	print"eliminando de lista"
	parametro = str(request.form['dato'])
	miLista.eliminar(int(parametro))
	miLista.consultar()
	return "ok eliminar"

@app.route('/buscaLista',methods=['POST'])
def buscarLista():
	print"buscando en lista"
	parametro = str(request.form['dato'])
	return str(miLista.buscar(str(parametro)))



if __name__ == "__main__":
	print"servicio corriendo"
	app.run(debug = True, host = '0.0.0.0')