
import Trame
import IPv4
import Tcp
class Trame2:
	def __init__(self, ligne):
		self.ligne=ligne
		self.trame=Trame.Trame(ligne)
		self.ipv4=None
		self.tcp=None


	def analyse(self):
		resuletatString=""

		resuletatString+=self.trame.toString()

		if(self.trame.type["Hexadecimal"]=="0800"):
			self.ipv4=IPv4.IPv4(self.trame.data)
			resuletatString+=self.ipv4.getInformationStringFormat()
			try:
				if(int(self.protocol,base=16)==6):
					#self.tcp=Tcp(self.ipv4.data)
					print("Fin :{}".format(self.ipv4.data))
				else:
					print("Protocole encapsulé dans le paquest ip non traité")
			except:	
				print("Impossible")
		else:
			print("Protocole encapsulé  dans la trame ethernet non traité")
		
		return (resuletatString)


trame2=Trame2("08002087b04408001108c06308004500004849ba00001e06698dc13733f6c1373304177096d4397f84c2bf3a21fd5018111c99bc00000e00313f02c0001100003ec100000011000000022828a7b08029eafc81589070")
r1=trame2.analyse()
print("{}".format(r1))
