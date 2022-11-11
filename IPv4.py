from Utils import * 
class IPv4:
	def __init__(self,data):
		self.version=data[0:1]
		self.ihl=data[1:2]
		self.tos=data[2:4]
		self.totalLength=data[4:8]
		self.identification=data[8:12]
		self.flagsAndFragOffset=data[12:16]
		self.ttl=data[16:18]
		self.protocol=data[18:20]
		self.headerChecksum=data[20:24]
		self.sourceAdress=data[24:32]
		self.destinationAdress=data[32:40]
		#SI on a pas d'option 
		if(int(self.ihl,base=16)==5):
			self.options=""
			self.padding=""
			self.data=data[40:]
		#40 octets d'options
		else:
			self.options=data[40:118]#todo padding combien
			self.padding=data[118:120]
		self.data=data[120:]
		

	def analyser(self):
		if(int(self.protocol,base=16)==6):
			tcp=Tcp(self.data)
			return tcp.analyser()
		else:
			return None


	def flagsInformation(test):
		binaire=hexToBin(test)
		binaire=binaire.zfill(16)
		R=binaire[0:1]
		DF=binaire[1:2]
		MF=binaire[2:3]
		fragOffset=binToDec(binaire[3:16])

		return "\n \t\tReserved bit: {}\n\t\tDon't fragment: {}\n\t\tMore fragments: {}\n\tFragment offset: {}\n".format(
			R,DF,MF,fragOffset)

	def formatIPAdress(self,adressIP):
		return "{}.{}.{}.{}".format(hexToDec(adressIP[0:2]),
									hexToDec(adressIP[2:4]),
									hexToDec(adressIP[4:6]),
									hexToDec(adressIP[6:8]))

	def protocolInformation(protocol):
		#todo .... 
		return "\n"

	def getInformationStringFormat(self):
		info=""
		info+="Internet Protocol:\n\tVersion: {}\n\tHeader Length: {} bytes ({})\n".format(
			self.version,hexToDec(self.ihl)*4,hexToDec(self.ihl))
		info+="\tDifferentiated Services Filed: {}\n".format("0x"+self.tos)
		info+="\tTotal Length: {}\n".format(hexToDec(self.totalLength))
		info+="\tIdentification: {} ({})\n".format("0x"+self.identification,hexToDec(self.identification))
		info+="\tFlags: {}".format("0x"+self.flagsAndFragOffset)+IPv4.flagsInformation(self.flagsAndFragOffset)
		info+="\tTime to live: {}\n".format(hexToDec(self.ttl))
		info+="\tProtocol: "+IPv4.protocolInformation(self.protocol)
		info+="\tHeader checksum: {}\n".format("0x"+self.headerChecksum)
		info+="\tSource: {}\n".format(self.formatIPAdress(self.sourceAdress))
		info+="\tDestination: {}\n".format(self.formatIPAdress(self.destinationAdress))
		return info



ipv4=IPv4("4f00007c3f860000fb0149afc0219f0684e33d0507272884e33c20c02c4112c0464705c0219f02c0219f06c0464706c02c411a84e33c1e84e33d87000000aa562f00000029368c410003862b08090a0b0c0de0f101112131415161718191a1b1c1d1e1f20212223242526272829a2b2c2d2e2f3031323334353637")
print(ipv4.getInformationStringFormat())