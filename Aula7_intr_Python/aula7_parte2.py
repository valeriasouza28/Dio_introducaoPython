# vamos criar uma classe chamada televisão
# E essa classe vai implementar os métodos
class Televisao:
        
        def __init__(self):
          
          #sempre que instanciamos uma tV ela vai estar desligada
          self.ligada = False
          self.canal = 5



          #Agora vamos criar um método de fazer a ação de ligar a televisão
          # vamos usar o pawer de botão de liga e desliga da nossa tv
          #se a TV estiver ligada
        def power(self):
          if self.ligada :
            self.ligada = False 
          
          else:
            self.ligada = True
            
            
        def proximo_canal(self):
            if self.ligada:
              self.canal += 1
            
        def anterior_canal(self):
            if self.ligada:
              self.canal -= 1
                
#vamos instanciar a classe televisão
televisao = Televisao()
print('Televisão está ligada: {}'.format(televisao.ligada))
televisao.power()
print('Televiasao está ligada {}'.format(televisao.ligada))
televisao.power()
print('Televisão está ligada: {}'.format(televisao.ligada))
print('Canal: {}'.format(televisao.canal))
televisao.power()
print('Televiasao está ligada {}'.format(televisao.ligada))
televisao.proximo_canal()
televisao.proximo_canal()
print('Canal: {}'.format(televisao.canal))
televisao.anterior_canal()
print('Canal: {}'.format(televisao.canal))