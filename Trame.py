
import Ethernet
import IPv4
import Tcp
import Http
from Utils import hexToDec
class Trame:
	id=1
	def __init__(self, ligne):
		self.trame=ligne.upper()
		self.erronee=False
		self.id = Trame.id
		self.ethernet=None
		self.ipv4=None
		self.tcp=None
		self.http=None
		Trame.id += 1



	def analyse(self):
		resuletatString=""
		if(self.id!=1):
			resuletatString+="\n\n\n"

		resuletatString+="********************Trame numero {}********************\n".format(self.id)
		suite=""
		if (len(self.trame)>=28):

			self.ethernet=Ethernet.Ethernet(self.trame)
			suite+=self.ethernet.toString()
			if( not self.ethernet.erronee and self.ethernet.type["Hexadecimal"]=="0800"):
				if(len(self.ethernet.data)>=40):
					self.ipv4=IPv4.IPv4(self.ethernet.data)
					suite+=self.ipv4.toString()

					if  not self.ipv4.erronee:
						if hexToDec(self.ipv4.protocol)==6 :
							if len(self.ipv4.data)>=40:
								self.tcp=Tcp.Tcp(self.ipv4.data)
								suite+=self.tcp.toString()
								if(not self.tcp.erronee and hexToDec(self.tcp.dstPort)==65453 or hexToDec(self.tcp.srcPort)==65453 and len(self.tcp.data)>0): #Remplacer 80
									self.http =Http.Http(self.tcp.data)
									suite+=self.http.toString()

									if self.http.erronee:
										self.erronee=True

								elif self.tcp.erronee:
									self.erronee=True
							else:
								self.erronee=True
						else:
							#self.erronee=True
							suite+="\nProtocole encapsulé dans le paquest ip non traité ---->( Pas d'analyse au niveau de la COUCHE 4)"
					else:
						self.erronee=True
				else:	
					self.erronee=True
					suite+="\nLa taille du paquet ip est trop petite ---->( Pas d'analyse au niveau de la COUCHE 3)"
			else:
				if self.ethernet.erronee:
					self.erronee=True
				else:
					suite+="\nProtocole encapsulé  dans la trame ethernet non traité ---->( Pas d'analyse au niveau de la COUCHE 3)"
		else:
			self.erronee=True
			suite+="\n Trame de longeur insuffisante ---->( Pas d'analyse au niveau de la COUCHE2 )"

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
				if self.http!=None:
					result+=self.http.toString()

		result=result[:-1]
		return result


	def getMsgGraphe(self):
		message=""
		if not self.erronee:
			if self.http!=None:
				message=self.http.getMessage()
			elif self.tcp!=None:
				message=self.tcp.getMessage()
		return message

	def getMsgTerminal(self):
		message=[]

		if self.http!=None and not self.http.erronee:
			message.append("HTTP")
			message.append(self.ipv4.sourceAdress)
			message.append(self.tcp.srcPort)
			message.append(self.http.getMessage())
			message.append(self.ipv4.destinationAdress)
			message.append(self.tcp.dstPort)
		elif self.tcp!=None and not self.tcp.erronee:
			message.append("TCP")
			message.append(self.ipv4.sourceAdress)
			message.append(self.tcp.srcPort)
			message.append(self.tcp.getMessage())
			message.append(self.ipv4.destinationAdress)
			message.append(self.tcp.dstPort)
			
		elif self.ipv4!=None and not self.ipv4.erronee:
			message.append("IPV4")
			message.append(self.ipv4.sourceAdress)
			message.append(self.ipv4.getMessage())
			message.append(self.ipv4.destinationAdress)
			if self.erronee:
				message.append("(Trame erronée au niveau TCP))")
			else:
				message.append("(Protocol non supporté)")
		elif self.ethernet!=None and not self.ethernet.erronee:
			message.append("ETHERNET")
			message.append(self.ethernet.adresseSource)
			message.append(self.ethernet.getMessage())
			message.append(self.ethernet.adresseDest)
			if self.erronee:
				message.append("(Trame erronée au niveau IP)")
			else:
				message.append("(Protocol non supporté)")


			
		return message
		
""""
	def affiche(self):
		elif self.ipv4!=None:
				message+="IP Protocol : (Protocol encaplsulé pas IP non supporté)"
			elif self.ethernet!=None:
				message="(Protocol encaplsulé non supporté)"

trame=Trame("08002087b04408001108c06308004500007c3f860000fb0649afc0219f0684e33d05ffad13895c3e066a00000000a00240009c2e0000020405a0010303000101080a009e7bc400000000474554202f7e737061746869732f20485454502f312e310d0a486f73743a207777772d6e70612e6c6970362e66720d0a436f6e6e656374696f6e3a206b6565702d616c6976650d0a557067726164652d496e7365637572652d52657175657374733a20310d0a557365722d4167656e743a204d6f7a696c6c612f352e3020284d6163696e746f73683b20496e74656c204d6163204f5320582031305f31345f3634330d0a0d0a")
r1=trame.analyse()
print("{}".format(r1))
"""
