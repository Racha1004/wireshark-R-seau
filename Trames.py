class Trames:
	def __init__(self,trame):
		self.trame=trame.lower()
		self.adresseDest=trame[0:12]
		self.adresseSource=trame[12:24]
		self.type=trame[24:28]
		self.data=trame[28:]


	