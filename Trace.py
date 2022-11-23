from Utils import * 
class Trace:
	def __init__(self,data):
		self.listeDeTrames=[]
		for trame in data:
			print(trame)
			self.listeDeTrames.append(parseTrame(trame))

	def affiche(self):
		i=0
		for trame in self.listeDeTrames:
			print("Trame {} : {} \n".format(i,trame))
			i+=1
