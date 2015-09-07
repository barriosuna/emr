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
      
  def pagar(self,colectivo,horario):
    self.pay(colectivo,horario)
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

  def pagar(self,colectivo,horario):
    horario1 = datetime.strptime(horario,"%d/%m/%Y %H:%M")
    if (horario1.hour<6):
      self.pay(colectivo,horario)
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
