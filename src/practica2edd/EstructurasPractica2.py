from flask import Flask, request, Response
from graphviz import Digraph
app = Flask('EDD_PRACTICA2')
#clase nodo de la lista simple :3
class nodoLista:
	def __init__(self, palabra,correlativo):
		self.id = correlativo
		self.palabra = palabra
		self.siguiente = None

#clase lista simple y sus metodos
class Lista:

	def __init__(self):
		self.primero = None
		self.contador=0

#metodo para incertar en la lista simple
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

# metodo que imprime en consola todos los nodos de la lista simple
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

#metodo que extrae por id nodos de la lista simple
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


# metodo que debuelve el id referente al nodo solicitado
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

# metodo que genera el archivo.dot de la lista y lugo lo compila generando un pdf
	def graficarLista(self):
		dot = Digraph(comment='GraficaListaSimple')
		dot  #doctest: +ELLIPSIS
		aux = self.primero
		if aux==None:
			print"lista vacia"
		else:
			if (aux.siguiente == None):
				print aux.id
				print aux.palabra
				dot.node(str(aux.id), aux.palabra)
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
			dot.render('test-output/ImagenListaSimple.dot', view=False)

#**************************************************************************************************************************
# clase nodo de la cola
class nodoCola:
	def __init__(self, digito,correlativo):
		self.id = correlativo
		self.numero = digito
		self.siguiente = None


class Cola:

	def __init__(self):
		self.primero=None
		self.contador=0

#metodo que ingresa un nuevo numero a la cola
	def queue(self,parametro):
		nodo = nodoCola(parametro, self.contador)
		print "se encolarpa: ", nodo.numero
		if self.primero == None:
			self.primero = nodo
			self.graficarCola()
		else:
			aux = self.primero
			while True:
				if aux.siguiente == None:
					aux.siguiente=nodo
					self.graficarCola()
					break
				else:
					aux = aux.siguiente
		self.contador = self.contador + 1

#metodo que elimina el elemento mas antiguo de la cola
	def dequeue(self):
		deTurno = ""
		if self.primero == None:
			return"la cola está vacia"
		else:
			deTurno=str(self.primero.numero)
			aux = self.primero.siguiente
			self.primero=aux
			self.graficarCola()
			return "atendiendo al elemento: ",deTurno

#metodo que imprime todos los elementos contenidos actualmente en la cola
	def consultarCola(self):
		aux = self.primero
		if aux==None:
			print"Cola vacia"
		else:
			print aux.id
			print aux.numero

			while aux.siguiente!= None:
				aux = aux.siguiente
				print aux.id
				print aux.numero

#metodo que grafica la cola
	def graficarCola(self):
		dot = Digraph(comment='GraficaCola')
		dot  #doctest: +ELLIPSIS
		aux = self.primero
		if aux==None:
			print"Cola vacia"
		else:
			if (aux.siguiente == None):
				dot.node(str(aux.id), aux.numero)
			else:
				while aux.siguiente!= None:
					dot.node(str(aux.id), aux.numero)
					dot.node(str(aux.siguiente.id), aux.siguiente.numero)
					dot.edge(str(aux.id), str(aux.siguiente.id), constraint='false')
					aux = aux.siguiente
			print(dot.source)
			dot.render('test-output/ImagenCola.dot', view=False)
#****************************************************************************************************************************
#metodos de la pila

class nodoPila:
	def __init__(self, digito,correlativo):
		self.id = correlativo
		self.numero = digito
		self.siguiente = None


class pila:

	def __init__(self):
		self.primero=None
		self.contador=0

#metodo que ingresa un nuevo numero a la pila
	def push(self,parametro):
		nodo = nodoCola(parametro, self.contador)
		print "se apilara: ", nodo.numero
		if self.primero == None:
			self.primero = nodo
			self.graficarPila()
		else:
			aux = self.primero
			self.primero = nodo
			self.primero.siguiente = aux
			self.graficarPila()
		self.contador = self.contador + 1

#metodo que elimina el elemento mas antiguo de la pila
	def pop(self):
		deTurno = ""
		if self.primero == None:
			return"la pila está vacia"
		else:
			deTurno=str(self.primero.numero)
			aux = self.primero.siguiente
			self.primero=aux
			self.graficarPila()
			return "atendiendo al elemento: ",deTurno

#metodo que imprime todos los elementos contenidos actualmente en la pila
	def consultarPila(self):
		aux = self.primero
		if aux==None:
			print"Pila vacia"
		else:
			print aux.id
			print aux.numero

			while aux.siguiente!= None:
				aux = aux.siguiente
				print aux.id
				print aux.numero

#metodo que grafica la pila
	def graficarPila(self):
		dot = Digraph(comment='GraficaPila')
		dot  #doctest: +ELLIPSIS
		aux = self.primero
		if aux==None:
			print"Pila vacia"
		else:
			if aux.siguiente == None :
				dot.node(str(aux.id), aux.numero)
			else:
				while aux.siguiente!= None:
					dot.node(str(aux.id), aux.numero)
					dot.node(str(aux.siguiente.id), aux.siguiente.numero)
					dot.edge(str(aux.id), str(aux.siguiente.id), constraint='false')
					aux = aux.siguiente
			print(dot.source)
			dot.render('test-output/ImagenPila.dot', view=False)

#****************************************************************************************************************************

#declaración de instancia de la lista
miLista = Lista()
#declaracion de la cola
miCola = Cola()
#declaracion de la instancia de la pila
miPila = pila()
#***************************************************************************************************************************
#metodos web de la lista
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

#**************************************************************************************************************************
#metodos web de la cola
@app.route('/insertarCola',methods=['POST'])
def insertarCola():
	print"insertando en Cola"
	parametro= str(request.form['dato'])
	print parametro
	miCola.queue(str(parametro))
	miCola.consultarCola()
	return "ok insertar Cola"

@app.route('/sacarCola',methods=['POST'])
def sacardeCola():
	print"sacando de Cola"
	parametro= str(request.form['dato'])
	print "se eliminará un parametro ",parametro
	retorno = miCola.dequeue()
	miCola.consultarCola()
	return str(retorno)

#**************************************************************************************************************************
#metodos web de la pila
@app.route('/insertarPila',methods=['POST'])
def insertarPila():
	print"insertando en pila"
	parametro= str(request.form['dato'])
	print parametro
	miPila.push(str(parametro))
	miPila.consultarPila()
	return "ok insertar Pila"

@app.route('/sacarPila',methods=['POST'])
def sacardePila():
	print"sacando de Pila"
	parametro= str(request.form['dato'])
	print "se eliminará un parametro ",parametro
	retorno = miPila.pop()
	miPila.consultarPila()
	return str(retorno)

#**************************************************************************************************************************
if __name__ == "__main__":
	print"servicio corriendo"
	app.run(debug = True, host = '0.0.0.0')