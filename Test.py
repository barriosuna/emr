#Good Guy Santos se levanta temprano y arregla el codigo 
from datetime import datetime
class tarjeta:
  def __init__(self):
    self.money=0
    self.colant=0 
    hora="01/01/0001 0:00"
    self.tiempoant=datetime.strptime(hora,"%d/%m/%Y %H:%M") #hora del bondi anterior
    self.valido=False #rue, se puede, false no
    self.vieja = viaje()
    self.viaje=[]
      
  def pay(self,colectivo,horario):
    horario1 = datetime.strptime(horario,"%d/%m/%Y %H:%M")    
    if self.transbordo(colectivo,horario1)==True:
      if self.money>=1.90:
        self.money=self.money-1,90
        self.valido=False
        self.colant=0
        hour="01/01/0001 0:00"
        self.tiempoant= datetime.strptime(hour, "%d/%m/%Y %H:%M") #hora del bondi anterior
        self.vieja.tour(horario1,1.9,colectivo.linea,colectivo.interno,colectivo.empresa)
        self.viaje.append (self.vieja)
        #self,horario1,monto,cole,interno,company
        return True
      else:
        print ("Saldo insuficiente")
        return False
    elif self.money>=5.75:
      self.money=self.money-5.75
      if self.valido==False:
        self.valido=True
        self.tiempoant=horario1
        self.colant=colectivo.linea
        self.vieja.tour(horario1,5.75,colectivo.linea,colectivo.interno,colectivo.empresa)
        self.viaje.append (self.vieja)
        return True
    else:
      print ("Saldo insuficiente")
      return False
      #
    #horario = datetime.strptime(horario1,"%d/%m/%Y %H:%M")
    #delta=(horario - self.Viaje[0].horario)

      
  def transbordo(self,colectivo,horario):
    
    delta = (horario-self.tiempoant)
    if self.colant!=colectivo.linea and self.valido==True and delta.seconds<3600:
      return True
    else:
      return False 

  
  def recarga(self,cant):
    self.cant=cant
    if self.cant==196:
      self.money=self.money+230
    elif self.cant==368:
      self.money=self.money+460
    else:
      self.money=self.money+self.cant
  def saldo(self):
    print (str(self.money))
    return self.money
  
  def vrel(self):
    for i in self.viaje:
      print (str(i.hora) + " - " + str(i.monto) + " - " + str(i.empresa) + " - " + (str(i.colectivo)) + " - " + (str(i.interno)))
  
  
  
  
class medio(tarjeta):

  def pay(self,colectivo,horario):
    horario1 = datetime.strptime(horario, "%d/%m/%Y %H:%M")  
    if horario.hour<6:
     self.pay2()
    elif self.transbordo(colectivo,horario1)==True:
      if self.money>=0.96:
        self.money=self.money-0.96
        self.valido=False
        self.colant=0
        self.tiempoant=0
        self.vieja.tour(horario1, 0.96 ,colectivo.linea,colectivo.interno,colectivo.empresa)
        self.viaje.append (self.vieja)
        #self,horario1,monto,cole,interno,company
        return True
      else:
        print("Saldo insuficiente")
        return False
    elif self.money>=2.9:
      self.money=self.money-2.9
      if self.valido==False:
        self.valido=True
        self.tiempoant=horario1
        self.colant=colectivo.linea
        self.vieja.tour(horario1,2.9,colectivo.linea,colectivo.interno,colectivo.empresa)
        self.viaje.append (self.vieja)
        return True
    else:
      print("Saldo insuficiente")
      return False

      
def pay2(self,colectivo,horario):
    from datetime import datetime
    horario1 = datetime.strptime(horario, "%d/%m/%Y %H:%M")    
    if self.transbordo(colectivo,horario1)==True:
      if self.money>=1.90:
        self.money=self.money-1.90
        self.valido=False
        self.colant=0
        horita="01/01/0001 0:00"
        self.tiempoant=datetime.strptime(horita, "%d/%m/%Y %H:%M") #hora del bondi anterior
        self.vieja.tour(horario1,1.9,colectivo.linea,colectivo.interno,colectivo.empresa)
        self.viaje.append (self.vieja)
        #self,horario1,monto,cole,interno,company
        return True
    elif self.money>=5.75:
      self.money=self.money-5.75
      if self.valido==False:
        self.valido=True
        self.tiempoant=horario1
        self.colant=colectivo.linea
        self.vieja.tour(horario1,5.75,colectivo.linea,colectivo.interno,colectivo.empresa)
        self.viaje.append (self.vieja)
        return True
    else:
      return False


class colectivo:
  def __init__(self,empresa,linea,interno):
    self.interno=interno
    self.linea=linea
    self.empresa=empresa
    
class viaje:
  def __init__(self):
    self.monto=0
    self.hora="01/01/0001 0:00"
    self.empresa=""
    self.colectivo=0
    self.interno=0
  def tour(self,horario,monto,colectivo,interno,empresa):
    self.hora=horario
    self.monto=monto
    self.colectivo=colectivo
    self.interno=interno
    self.empresa=empresa


t=tarjeta()
t.saldo()
t.recarga(368)
t.saldo()
C136=colectivo(15,136,2)
t.pay(C136,"05/11/1996 0:04")
t.saldo()
t.vrel()

tarje=tarjeta()
media=medio()
tarje.recarga(368)
media.recarga(368)
bondi1=colectivo("pepe",136,12)
bondi2=colectivo("papa",137,13)

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
def test3():
	if  tarje.vrel():
		pi==true
	else:
		false
	assert pi==true








