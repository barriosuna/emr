#ARREGLAR TIEMPO PRIMERO QUE NADA

#Carga de Saldo
def test1():
   tarj=tarjeta()
   tarj.recarga(196)
   assert tarj._Saldo == 230

def test2():
	tarja=tarjeta()
	tarja.recarga(368)
	assert tarj.saldo==460
#Pago en tarjeta comun sin transbordo por haberlo usado anteriormente
def test3():
	tarje=tarjeta()
	C136=colectivo(15,136,2)
	tarje.recarga(368)
	tarje.pagar(C136,1000)
	assert tarje.saldo()==363.25
#Pago comun con transbordo anulado por mismo bondi

def test4():
	tarje=tarjeta()
	C136=colectivo(15,136,2)
	tarje.recarga(368)
	tarje.pagar(C136,1000)
	tarje.pagar(C136,1500)
	assert tarje.saldo()==357.5
#Pago comun con transbordo anulado por tiempo
#Primero hay que arreglar el tiempo
def test5():
	tarje=tarjeta()
	C136=colectivo(15,136,2)
	C137=colectivo(15,137,5)
	tarje.recarga(368)
	tarje.pagar(C136,1000)
	tarje.pagar(C137,1500)
	assert tarje.saldo()==357.5
	

#Pago comun con transbordo
def test6():
	tarje=tarjeta()
	C136=colectivo(15,138,2)
	tarje.recarga(368)
	tarje.pagar(C136,1000)
	tarje.pagar(C138,1500)
	assert tarje.saldo()==361.1

def testi():
	tarje=tarjeta
	C136=colectivo(15,136,2)
	tarje.recarga(368)
	tarje.pagar(C136,1000)
	tarje.pagar(C136,1500)

def testa():
	tarta=medio()
	tarta.recarga(368)
	tarta.pagar(C136,5)
	C136=colectivo(15,136,2)
def teste():
	tarte=tarjeta()
	C136=colectivo(15,136,2)
	tarte.recarga(368)
	tarje.pagar()
