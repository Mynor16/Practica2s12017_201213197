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

class nodoMatriz:
	def __init__(self, nombre,alfa,dominio,lista)
		self.nombre = nombre
		self.dominio = dominio
		self.alfa = alfa
		self.lista = lista
		self.arriba = None
		self.abajo= None
		self.izquierda = None
		self.derecha = None
		self. atras = None

class matrizDispersa:
	def __init__(self):
		self.inicio = None
		self.dominioFinal = None
		self.alfaFinal = None

	def matrizVacia(self):
		if self.inicio == None
		return True

	def agregar(self, nombre, dominio, lDoble):
		if self.matrizVacia() == True:
			nodoM = nuevoNodo.nodoMatriz("base","base","base","",lDoble)
			self.inicio = nodoM
			self.dominioFinal = nodoM
			self.alfaFinal = nodoM
		self.crearDominio(dominio)
		self.crearAlfa()(nombre[0])
		aux = self.dominio(dominio)
		aux2 = self.abecedario(nombre[0])
		izquierda = ""
		derecha = ""
		if(aux.derecha != None):
			derecha = aux.derecha.dominio
		if(aux.izquierda != None):
			izquierda = aux.izquierda.dominio
		email = nombre+dominio
		if(aux.abajo == None and aux2.derecha == None):
			nodoM = nuevoNodo.nodoMatriz(email,nombre[0],dominio,lDoble)
			print("ingresado nuevo correo ",email)
			aux.abajo = nodoM
			nodoM.arriba = aux
			aux2.derecha = nodoM
			nuevo.izquierda = aux2
		else:
			dominioAux = aux
			nodoM = nuevoNodo.nodoMatriz(email,nombre[0],dominio,lDoble)
			print("ingresado nuevo correo",email)
			validar = False
			if(self.posicion(dominio,nombre[0]) != True)
				while (dominioAux != None):
					if(dominioAux.abajo != None):
						if(nodoM.alfa < dominioAux.abajo.alfa):
							nodoM.arriba = dominioAux
							nodoM.abajo = dominioAux.abajo
							dominioAux.abajo.arriba = nodoM
							dominioAux.abajo = nodoM
							aux_dominio = None
						else:
							dominioAux = dominioAux.abajo
					elif(dominioAux.abajo == None):
						nodoM.arriba = dominioAux
						dominioAux.abajo = nodoM
						dominioAux = None
					else:
						dominioAux = dominioAux.abajo
				self.nodoMedio(aux2, nuevo, izquierda,derecha,aux.izquierda,aux.derecha)
			else:
				aux3 = self.nodoX(dominio,nombre[0])
				if(aux3.atras == None):
					aux3.atras = nodoM
				else:
					while (aux3 != None):
						if(aux3.atras == None):
							aux3.atras = nodoM
						else:
							aux3 = aux3 = aux3.atras
	return "ok agregar matriz"

	def crearDominio(self,dominio):
		if(self.inicio.derecha == None):
			nuevoD = nuevoNodo.nodoMatriz("base","base",dominio,"","")
			nuevo.izquierda = self.dominioFinal
			self.dominioFinal.derecha = nuevoD
			self.dominioFinal = nuevoD
		else:
			aux = self.inicio
			validar = False
			while (aux != None):
				if (aux.dominio == dominio):
					validar = True
					aux = None
				else:
					aux=aux.derecha
				if(validar != True):
					nuevoD = nuevoNodo.nodoMatriz("base","base",dominio,"","")
					nuevoD.izquierda = self.dominioFinal
					self.dominioFinal.siguiente=nuevoD
					self.dominioFinal = nuevoD

	def crearAlfa(self,alfa):
		if(self.inicio.abajo == None):
			nuevoA = nuevoNodo.nodoMatriz("base",alfa,"base","","")
			nuevoA.arriba = self.alfaFinal
			self.alfaFinal.abajo = nuevoA
			self.alfaFinal=nuevoA
		else:
			aux = self.inicio
			validar = False
			while (aux != None):
				if(aux.alfa == alfa):
					validar = True
					aux = None
				else:
					aux = aux.abajo
			if(validar != True):
				nuevoA = nuevoNodo.nodoMatriz("base",alfa,"base","","")
				aux = self.inicio
				while(aux != None):
					if(aux.abajo != None):
						if(alfa < aux.abajo.alfa):
							aux2 = aux.abajo
							nuevoA.arriba = aux
							aux.abajo = nuevoA
							nuevoa.abajo = aux2
							aux2.arriba = nuevoA
							aux = None
						else:
							aux = aux.abajo
					elif(aux.abajo == None):
						nuevoA.arriba = self.alfaFinal
						self.alfaFinal.abajo=nuevoA
						self.alfaFinal = nuevoA
						aux = None
					else
						aux = aux.abajo

	def dominio(self, dominio):
		aux = self.inicio
		validar = True
		NodoD = None
		while(aux != None and validar !=False):
			if(aux.dominio == dominio):
				validar = False
				nodoD = aux
			else:
				aux = aux.siguiente
				validar = True
		return NodoD

	def alfa(self,alfa):
		aux = self.inicio
		validar = True
		nodoA = None
		while(aux != None and validar != False):
			if(aux.alfa == alfa):
				validar = False
				nodoA = aux
			else:
				aux = aux.abajo
				validar = True
		return nodoA

		def posicion(self, dominio,alfa):
			aux = self.inicio.derecha
			validar = False
			while (aux !=None):
				if(aux.dominio == dominio):
					aux2 = aux
					while (aux2 != None):
						if(aux2.alfa == alfa):
							aux2 = None
							validar = True
						else:
							aux2 = aux2.abajo
					aux = None
				else:
					aux = aux.derecha
			return validar

	def nodoX(self,dominio,letra):
		aux = self.inicio
		nodoN= None
		while(aux != None):
			if (aux.dominio == dominio):
				aux2 = aux
				while(aux2 != None):
					if (aux2.alfa == alfa):
						nodoN = aux2
						return nodoN
						aux2 = None
					else:
						aux2 = aux2.abajo
				aux = None
			else:
				aux = aux.siguiente
				

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