from tp.py import*
tarje=tarjeta()
media=medio()
tarje.recarga(368)
media.recarga(368)
bondi1=colectivo(pepe,136,12)
bondi2=colectivo(papa,137,13)

#viaje comun
tarje.pay(bondi1,"12/12/1998 12:30 ")
#Con transbordo
tarje.pay(bondi2,"12/12/1998 12 40")

#Medio comun
media.pay(bondi1,"12/12/1999 14:10 ")
#Medio con transbordo
media.pay(bondi2,"12/12/1999 14:30 ")
#Media fuera de horario escolar
media.pay(bondi1,"12/12/1999 05:00 ")
#Media fuera de horario escolar y con transbordo
#media.pay(bondi2,"12/12/1999 05:20")

def test1():
	assert tarje.saldo()==452.35
def test2():
	assert media.saldo()==448.49
def test3:
	if  tarje.vrel():
		pi==true
	else:
		false
	assert pi==true








