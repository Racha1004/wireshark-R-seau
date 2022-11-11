def hexToBin(test):
	entier=int("0x"+test,base=16)
	binaire=bin(entier)
	return binaire[2:]

def hexToDec(test):
	return int("0x"+test,base=16)

def binToDec(test):
	return int("0b"+test,base=2)

def parseTrame(liste):
	stringValeurs=""
	stringValeurs+=''.join(liste)
	stringValeurs=stringValeurs.replace('\n','')
	return stringValeurs