def hexToBin(test):
	entier=int("0x"+test,base=16)
	binaire=bin(entier)
	return binaire[2:]

def hexToDec(test):
	return int("0x"+test,base=16)

def binToDec(test):
	print("Bin to dec: ",test)
	return int("0b"+test,base=2)

def decToHex(test):
	hexa=hex(test)
	return hexa[2:]

def binToHex(test):
	hexa=hex(int("0b"+test,base=2))
	return hexa[2:]

def parseTrame(liste):
	stringValeurs=""
	stringValeurs+=''.join(liste)
	stringValeurs=stringValeurs.replace('\n','')
	return stringValeurs

def formatMACAdress(adressMAC):
	res = adressMAC[0:2] + ":" + adressMAC[2:4] + ":" + adressMAC[4:6] + \
		":" + adressMAC[6:8] + ":" + adressMAC[8:10] + ":" + adressMAC[10:12]
	return res

def formatIPAdress(adressIP):
	return "{}.{}.{}.{}".format(hexToDec(adressIP[0:2]),
								hexToDec(adressIP[2:4]),
								hexToDec(adressIP[4:6]),
								hexToDec(adressIP[6:8]))

def outPut (data,fileName):
	with open(fileName,"w") as output: 
		output.write(data)
	output.close()


def afficheTrame (trameParsée):
	trame=""
	hex=0
	for i in range(0,len(trameParsée),2):
		if i%32==0:
			if i!=0:
				trame=trame[:-1]
				trame+="\n"

			hex=decToHex(i//2)
			hex=hex.zfill(4)
			trame+=hex+"   "
		
		trame+=trameParsée[i:i+2]+" "

	trame=trame[:-1]
	print(trame)

def infoOption(liste,k):
	for d in liste:
		if d.get("Kind")==str(k):
			return d
	return None 

#afficheTrame("0812002087b008001108c063080045004849ba00001e06698dc13733f6c1373304177096d4397f84c2bf3a21fd5018111c99bc00000e00313f02c0001100003ec100000011000000022828a7b08029e5fc815890700812002087b008001108c063080045004849ba00001e06698dc13733f6c1373304177096d4397f84c2bf3a21fd5018111c99bc00000e00313f02c0001100003ec100000011000000022828a7b08029e5fc815890700812002087b008001108c063080045004849ba00001e06698dc13733f6c1373304177096d4397f84c2bf3a21fd5018111c99bc00000e00313f02c0001100003ec100000011000000022828a7b08029e5fc815890700812002087b008001108c063080045004849ba00001e06698dc13733f6c1373304177096d4397f84c2bf3a21fd5018111c99bc00000e00313f02c0001100003ec100000011000000022828a7b08029e5fc81589070")
