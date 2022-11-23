import Utils

PATHREFERENCES = "./referances/"
OUTPUTPATH = "./output/"
with open(PATHREFERENCES+"ipProtocoles.txt", "r")as typeProto:
    typeProto.readline()
    types = []
    for line in typeProto:
        split = line.split(" ",1)
        types.append((split[0], split[1].rstrip()))
typeProto.close()

TYPES = dict(types)

class IPv4:
	def __init__(self,data):

		self.ip=data.upper()
		self.version=self.ip[0:1]
		self.ihl=self.ip[1:2]
		self.tos=self.ip[2:4]
		self.totalLength=self.ip[4:8]
		self.identification=self.ip[8:12]
		self.flagsAndFragOffset=self.ip[12:16]

		binaire=Utils.hexToBin(self.flagsAndFragOffset)
		binaire=binaire.zfill(16)
		self.R=binaire[0:1]
		self.DF=binaire[1:2]
		self.MF=binaire[2:3]
		self.fragOffset=Utils.binToDec(binaire[3:16])

		self.ttl=self.ip[16:18]
		self.protocol=self.ip[18:20]
		self.headerChecksum=self.ip[20:24]
		self.sourceAdress=self.ip[24:32]
		self.destinationAdress=self.ip[32:40]
		#SI on a pas d'option 
		if(int(self.ihl,base=16)==5):
			self.options=""
			self.padding=""
			self.data=self.ip[40:]
		#40 octets d'options
		else:
			self.options=self.ip[40:118]#todo padding combien
			self.padding=self.ip[118:120]
		self.data=self.ip[120:]
		


	def toString(self):
		info=""
		info+="\nInternet Protocol:\n\tVersion: {}\n\tHeader Length: {} bytes ({})\n".format(
			self.version,Utils.hexToDec(self.ihl)*4,self.ihl)
		info+="\tDifferentiated Services Filed: {}\n".format("0x"+self.tos)
		info+="\tTotal Length: {}\n".format(Utils.hexToDec(self.totalLength))
		info+="\tIdentification: {} ({})\n".format("0x"+self.identification,Utils.hexToDec(self.identification))
		info+="\tFlags: {} \n \t\tReserved bit: {}\n\t\tDon't fragment: {}\n\t\tMore fragments: {}\n\tFragment offset: {}\n".format("0x"+self.flagsAndFragOffset,self.R,self.DF,self.MF,self.fragOffset)
		info+="\tTime to live: {}\n".format(Utils.hexToDec(self.ttl))
		info+="\tProtocol: {} ({})\n".format(Utils.hexToDec(self.protocol),TYPES[self.protocol])
		info+="\tHeader checksum: {}\n".format("0x"+self.headerChecksum)
		info+="\tSource: {}\n".format(Utils.formatIPAdress(self.sourceAdress))
		info+="\tDestination: {}\n".format(Utils.formatIPAdress(self.destinationAdress))
		return info




















	"""
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

	def toDict(self):
		dictStr='"IP":'
		dictStr+='{{"Version":"{}","Header Length":{{"hexa":"{}","octet":"({} octets)"}},"TOS":{{"hexa":"{}","octet":"({})"}}'.format(
        	self.version,"0x"+self.ihl,Utils.hexToDec(self.ihl)*4,"0x"+self.tos,Utils.hexToDec(self.tos))
		dictStr+=',"Total Length":{{"hexa":"{}","octet":"({} octets)"}},"Identification": {{"hexa":"{}","octet":"({})"}}'.format(
        	"0x"+self.totalLength, Utils.hexToDec(self.totalLength), "0x"+self.identification, Utils.hexToDec(self.identification))
		frag="Fragmentation: "+self.flagsAndFragOffset+" (Reserve: {} - Don't Fragment: {} - More Fragments: {} - Fragment Offset: {})\n".format(
        	self.R,self.DF,self.MF,self.fragOffset)
		dictStr+=',"Fragmentation":"{}",'.format(frag)
		dictStr+='"Time to live":{{"hexa":"{}","octet":"({})"}},"Protocole":{{"hexa":"{}","valeur":"{}" }},"Checksum Entete":"{}",'.format(
        	"0x"+self.ttl, Utils.hexToDec(self.ttl), Utils.hexToDec(self.protocol), TYPES[self.protocol], "0x"+self.headerChecksum)
		dictStr+='"Adresse Ip Source":"{}", "Adresse Ip Destination":"{}"}},'.format(Utils.formatIPAdress(self.sourceAdress), Utils.formatIPAdress(self.destinationAdress))
		return dictStr
		
ipv4=IPv4("4f00007c3f860000fb0149afc0219f0684e33d0507272884e33c20c02c4112c0464705c0219f02c0219f06c0464706c02c411a84e33c1e84e33d87000000aa562f00000029368c410003862b08090a0b0c0de0f101112131415161718191a1b1c1d1e1f20212223242526272829a2b2c2d2e2f3031323334353637")
print(ipv4.toDict()[0])

"""