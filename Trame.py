class Trame:
	d = 1
	def __init__(self,trame):
		self.trame = trame.lower()
		self.entete = trame[0:28]
		self.id = Trame.id
		self.adresseDest = trame[0:12]
		self.adresseSource = trame[12:24]
		self.type = self.entete[24:28]
		self.data = trame[28:]
		self.paquet = IPv4(self.data)
		Trame.id += 1


	def toString(self);
		return "Trame numero {}:\nEthernet:\n\tAdresse MAC Destination: {}\n\tAdresse MAC Source: {}\n\tType (Ox{}): {}".format(self.id, self.destMac, self.srcMac, self.type["Hexadecimal"], self.type["Definition"]) + self.paquet.toString()
