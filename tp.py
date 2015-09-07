class tarjeta:
  def __init__(self):
    self.money=0
    self.colant=0 #linea del bondi anterior
    self.tiempoant=0 #hora del bondi anterior
    self.valido=False #rue, se puede, false no
    self.vieja = viaje()
    self.viaje=[]
    
  
  def pay(self,colectivo,horario):
    if self.transbordo(colectivo,horario)==True:
      if self.money>=1.90:
        self.money=self.money-1,90
        self.valido=false
        self.colant=0
        self.tiempoant=0
        self.vieja.tour(horario,1.9,colectivo.linea,colectivo.interno,colectivo.empresa)
        self.viaje.append (self.vieja)
        #self,horario,monto,cole,interno,company
        return True
    elif self.money>=5.75:
      self.money=self.money-5.75
      if self.valido==False:
        self.valido=True
        self.tiempoant=horario
        self.colant=colectivo.linea
        self.vieja.tour(horario,5.75,colectivo.linea,colectivo.interno,colectivo.empresa)
        self.viaje.append (self.vieja)
        return True
    else:
      return False
      
  def transbordo(self,colectivo,horario):
    self.horario=horario
    self.pi= self.horario-self.tiempoant
    if self.colant!=colectivo.linea and self.valido==True and pi<60:
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
    print str(self.money)
    return self.money
  
  def vrel(self):
    for i in self.viaje:
      print (str(i.horario) + " - " + str(i.monto) + " - " + str(i.empresa) + " - " + (str(i.colectivo)) + " - " + (str(i.interno)))
  
  
  
  
class medio(tarjeta):

  def pay(self,colectivo,horario):
    if horario<6:
      self.pay
    elif self.transbordo(colectivo,horario)==True:
      if self.money>=0.96:
        self.money=self.money-0.96
        self.valido=false
        self.colant=0
        self.tiempoant=0
        self.vieja.tour(horario,0.96,colectivo.linea,colectivo.interno,colectivo.empresa)
        self.viaje.append (self.vieja)
        return true
    elif self.money>=2.9:
      self.money=self.money-2.9
      if (self.valido==False):
        self.valido=True
        self.tiempoant=horario
        self.colant=colectivo.line
        self.vieja.tour(horario,2.9,colectivo.linea,colectivo.interno,colectivo.empresa)
        self.viaje.append (self.vieja)
        return True
    else:
      return False
      
  # La onda es que si no esta en horario escolar vaya directamente a pay.    


class colectivo:
  def __init__(self,empresa,linea,interno):
    self.interno=interno
    self.linea=linea
    self.empresa=empresa
    
class viaje:
  def __init__(self):
    self.monto=0
    self.horario=0
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
t.pay(C136,1000)
t.saldo()
t.vrel()
