
import Ethernet
import IPv4
import Tcp
from Utils import hexToDec
class Trame:
	id=1
	def __init__(self, ligne):
		self.trame=ligne.upper()
		self.id = Trame.id
		self.ethernet=None
		self.ipv4=None
		self.tcp=None
		Trame.id += 1



	def analyse(self):
		resuletatString="Trame numero {}:\n".format(self.id)
		suite=""
		print(len(self.trame))
		if (len(self.trame)>14):
			self.ethernet=Ethernet.Ethernet(self.trame)
			suite+=self.ethernet.toString()

			if(self.ethernet.type["Hexadecimal"]=="0800"):
				if(len(self.ethernet.data)>20):
					self.ipv4=IPv4.IPv4(self.ethernet.data)
					suite+=self.ipv4.toString()
					if(hexToDec(self.ipv4.protocol)==6):
						#self.tcp=Tcp(self.ipv4.data)
						print("Fin :{}".format(self.ipv4.data))
					else:
						suite="Protocole encapsulé dans le paquest ip non traité(couche3)"
				else:	
					suite="Taille du paquet ip trop petite(couche3)"
			else:
				suite="Protocole encapsulé  dans la trame ethernet non traité(couche2)"
		else:
			suite="Trame de longeur insuffisante(couche2)"

		resuletatString+=suite
		return (resuletatString)


trame=Trame("08002087b04408001108c06308004500004849ba00001e06698dc13733f6c1373304177096d4397f84c2bf3a21fd5018111c99bc00000e00313f02c0001100003ec100000011000000022828a7b08029eafc81589070")
r1=trame.analyse()
print("{}".format(r1))