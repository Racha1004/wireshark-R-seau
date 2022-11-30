from Utils import * 
import Trame
class Trace:
	def __init__(self,data):
		self.listeDeTrames=[]#Liste d'objets trame , ayant tous les champs initialisés
		for trame in data:
			self.listeDeTrames.append(Trame.Trame(trame))

	def analyse(self):
		resuletat=""
		for trame in self.listeDeTrames:
			resuletat+=trame.analyse()
			resuletat+="\n"
		resuletat=resuletat[:-1]
		return resuletat