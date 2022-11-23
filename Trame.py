from Utils import *
import IPv4
PATHREFERENCES = "./referances/"
OUTPUTPATH = "./output/"

with open(PATHREFERENCES+"typeEthernet.txt", "r")as typeEthe:
    typeEthe.readline()
    types = []
    for line in typeEthe:
        split = line.split(" ",1)
        types.append((split[0], split[1].rstrip()))
typeEthe.close()
TYPES = dict(types)


class Trame:
	id = 1
	def __init__(self,trame):
		if(len(trame)>28):
			self.trame = trame.lower()
			self.entete = trame[0:28]
			self.id = Trame.id
			self.adresseDest = trame[0:12]
			self.adresseSource = trame[12:24]
			self.type = { "Hexadecimal": self.entete[24:28], "Definition": TYPES[self.entete[24:28]]}
			self.data = trame[28:]
			if(self.type["Hexadecimal"]=="0800"):
				self.paquet = IPv4.IPv4(self.data)
			Trame.id += 1

	def analyser(self):
		if(self.type["Hexadecimal"]=="0800"):
			ip=IPv4(self.data)
			return ip.analyer()
		else:
			return None
	def toString(self):
		return "Trame numero {}:\nEthernet:\n\tAdresse MAC Destination: {}\n\tAdresse MAC Source: {}\n\tType (Ox{}): {}".format(self.id, self.adresseDest, self.adresseSource, self.type["Hexadecimal"], self.type["Definition"])
"""
	def toDict(self):
        dictStr = '"Trame numero {}":'.format(self.id)
        dictStr += '{"Ethernet":'
        dictStr += '{{"Adresse MAC Destination":"{}","Adresse Mac Source":"{}","Type":{{"hexa":"{}","Definition":"{}"}}}},'.format(
            self.destMac, self.srcMac, "0x"+self.type["Hexadecimal"], self.type["Definition"])
        dictStr += self.paquet.toDict()
        dictStr += '}'
        return dictSt

"""