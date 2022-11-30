
import Ethernet
import IPv4
import Segment
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
		if (len(self.trame)>14):
			self.ethernet=Ethernet.Ethernet(self.trame)
			suite+=self.ethernet.toString()

			if(self.ethernet.type["Hexadecimal"]=="0800"):
				if(len(self.ethernet.data)>=40):
					self.ipv4=IPv4.IPv4(self.ethernet.data)
					suite+=self.ipv4.toString()
					if(hexToDec(self.ipv4.protocol)==6 and len(self.ipv4.data)>=40):
						self.tcp=Segment.Segment(self.ipv4.data)
						suite+=self.tcp.toString()
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

	def toString(self):
		result="Trame numero {}:\n".format(self.id)
		if Ethernet!=None:
			result+=self.ethernet.toString()
			result+="\n"
			if self.ipv4!=None:
				result+=self.ipv4.toString()
				result+="\n"
				if self.tcp!=None:
					result+=self.tcp.toString()
					result+="\n"

		result=result[:-1]
		return result
		
		

trame=Trame("08002087b04408001108c06308004500007c3f860000fb0649afc0219f0684e33d05ffad13895c3e066a00000000a00240009c2e0000020405a0010303000101080a009e7bc400000000")
r1=trame.analyse()
print("{}".format(r1))

