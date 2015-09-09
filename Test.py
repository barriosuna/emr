from tp import *
from datetime import datetime

#Tarjeta Comun

#Metodo Pagar
#Si el saldo es 0 no se puede viajar
#Descuento viaje comun
#Descuento un viaje transbordo
#Que arranque con saldo=0
#Inscriba el viaje en la lista

#Metodo transbordo
#Las tres razones por las que no puede funcionar
# Metodo recarga, que cargue valores normales y valores bonus
#Metodo saldo

#Metodo Vreal
#Que no este vacia
#Que si no se realiza el viaje no lo agregue
#Que agregue la cantidad de viajes realizados

#Tarjeta Medio
#En horario no escolar cobre boleto comun
#Transbordo y no transbordo

def testsaldo():
	#saldo inicial =0
	card=tarjeta()
	card2=medio()
	assert card.saldo()==0
	assert card2.saldo()==0

def testrecarga():
	#Cargue saldo comun y saldos bonificados
	card=tarjeta()
	card2=medio()
	card.recarga(196)
	assert card.saldo()==230
	card.recarga(368)
	assert card.saldo()==690
	card.recarga(20)
	assert card.saldo()==710

def testpagar():
	#Si no hay saldo no viajan
	#Viaje comun en normal y medio
	#Transbordo en ambas
	#Medio en horario no escolar
	card=tarjeta()
	card2=medio()
	bondi1=colectivo("pepe",136,12)
	bondi2=colectivo("papa",137,13)
	assert card.pay(bondi1,"12/12/1998 8:30")==False
	assert card2.pay(bondi1,"12/12/1998 8:30")==False
	card.recarga(100)
	card2.recarga(100)
	card.pagar(bondi1,"12/12/1998 8:30")
	card2.pagar(bondi1,"12/12/1998 8:30")
	assert round(card.saldo(),2)==round(94.25,2)
	assert round(card2.saldo(),2)==round(97.1,2)
	card.pagar(bondi2,"12/12/1998 8:40")
	card2.pagar(bondi2,"12/12/1998 8:40")
	assert round(card.saldo(),2)==round(92.35,2)
	assert round(card2.saldo(),2)==round(96.14,2)
	card2.pagar(bondi2,"13/12/1998 2:40")
	assert round(card2.saldo(),2)==round(90.39,2)

def testtransbordo():
	card=tarjeta()
	card2=medio()
	bondi1=colectivo("pepe",136,12)
	bondi2=colectivo("papa",137,13)
	#Sin transbordo luego de crearse
	hora="12/12/1998 2:40"
	horita=datetime.strptime(hora, "%d/%m/%Y %H:%M")
	
	assert card.transbordo(bondi1,horita)==False
	assert card2.transbordo(bondi1,horita)==False
	#self.tiempoant= datetime.strptime(hour, "%d/%m/%Y %H:%M") #hora del bondi anterior

	card.recarga(100)
	card2.recarga(100)
	card.pagar(bondi2,"12/12/1998 8:40")
	card2.pagar(bondi2,"12/12/1998 8:40")
	#Sin transbordo por mismo colectivo
	
	hora="12/12/1998 8:50"
	horita=datetime.strptime(hora, "%d/%m/%Y %H:%M")
	
	assert card.transbordo(bondi2,horita)==False
	assert card2.transbordo(bondi2,horita)==False
	#Sin transbordo por horario
	
	hora="12/12/1998 4:40"
	horita=datetime.strptime(hora, "%d/%m/%Y %H:%M")
	assert card.transbordo(bondi1,horita)==False
	assert card2.transbordo(bondi1,horita)==False
	#Si tomamos tres en una hora, un transbordo y dos normales
	
	card.pagar(bondi1,"12/12/1998 8:50")
	card2.pagar(bondi1,"12/12/1998 8:50")
	card.pagar(bondi2,"12/12/1998 9:00")
	
	card2.pagar(bondi2,"12/12/1998 9:00")
	
	assert round(card.saldo(),2)==round(86.6,2)
	assert round(card2.saldo(),2)==round(93.24,2)

def testvrel():
	card=tarjeta()
	card2=medio()
	bondi2=colectivo("papa",137,13)
	bondi1=colectivo("pepe",136,12)
	if not card.viajes:
		a=False
	else:
		a=True
		
	if not card2.viajes:
		a=False
	else:
		a=True
		
	assert a==False
	assert a==False
	card.recarga(100)
	card2.recarga(100)
	card.pagar(bondi2,"12/12/1998 8:50")
	card2.pagar(bondi2,"12/12/1998 8:50")
	assert len(card.viajes)==1
	assert card.viajes[0].interno==13
	assert card2.viajes[0].interno==13
	
	card.pagar(bondi2,"12/12/1998 9:40")
	card2.pagar(bondi2,"12/12/1998 9:40")
	assert len(card.viajes)==2
	
	assert len(card2.viajes)==2


#Test que no deberia andar
#def testnoanda():
#	assert 2==3


	




