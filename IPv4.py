class IPv4:
	def __init__(self,data):
		self.version=data[0:4]
		self.ihl=data[4:8]
		self.tos=data[8:16]
		self.totalLength=data[16:32]
		self.identification=data[32:48]
		self.flags=data[48:51]
		self.fragmentOffset=data[51:64]
		self.ttl=data[64:72]
		self.protocol=data[72:80]
		self.headerChecksum=data[80:96]
		self.sourceAdress=data[96:128]
		self.destinationAdress=data[128:160]
		#Ici c'est selon le champs IHL
		if(valDecimale(self.ihl)>20):
			self.options=data[160:464]
		self.padding=data[464:480]
		self.data=data[480:]


	