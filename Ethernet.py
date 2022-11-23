import Utils
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


class Ethernet:
	def __init__(self,trame):
		if(len(trame)>28):
			self.ethernet = trame.upper()
			self.entete = self.ethernet[0:28]
			self.adresseDest = self.ethernet[0:12]
			self.adresseSource = self.ethernet[12:24]
			self.type = { "Hexadecimal": self.entete[24:28], "Definition": TYPES[self.entete[24:28]]}
			self.data = self.ethernet[28:]
	

	def toString(self):
		return "Ethernet:\n\tAdresse MAC Destination: {}\n\tAdresse MAC Source: {}\n\tType (Ox{}): {}".format( 
			Utils.formatMACAdress(self.adresseDest), Utils.formatMACAdress(self.adresseSource), self.type["Hexadecimal"], self.type["Definition"])

	"""
	def analyser(self):
		if(self.type["Hexadecimal"]=="0800"):
			ip=IPv4(self.data)
			return ip.analyer()
		else:
			return None

	"""
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