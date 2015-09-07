def test1():
   tarj=tarjeta()
   tarj.recarga(196)
   assert tarj._Saldo == 230

def test2():
	tarja=tarjeta()
	tarja.recarga(368)
	assert tarj.saldo==460

def test3():
	tarje=tarjeta()
	C136=colectivo(15,136,2)
	tarje.recarga(368)
	tarje.pagar(C136,1000)
	assert tarje.saldo()==367.1
def test():
	
	tarje=tarjeta()
	C136=colectivo(15,136,2)
	tarje.recarga(368)
	tarje.pagar(C136,1000)
	tarje.pagar(C136,1500)
	assert tarje.saldo()==355.75

def test():
	tarje=tarjeta

def test4():
	tarta=medio()
	tarta.recarga(368)
	tarta.pagar(C136,5)
	C136=colectivo(15,136,2)
def test5():
	tarte=tarjeta()
	C136=colectivo(15,136,2)
	tarte.recarga(368)
	tarje.pagar()
