from Utils import *
import csv
PATHREFERENCES = "./referances/"
OUTPUTPATH = "./output/"


with open(PATHREFERENCES+"tcpOptions.csv", "r")as tcpOpt:
    reader=csv.DictReader(tcpOpt, delimiter=',')
    tcpOptions = []
    for ligne in reader:
        tcpOptions.append((ligne))
tcpOpt.close()
TCPOPTIONSTYPE=tcpOptions


class Segment:
    def __init__(self, segment):
        self.segment = segment
        self.srcPort = self.segment[0:4]
        self.dstPort = self.segment[4:8]
        self.seqNum = self.segment[8:16]
        self.ackNum = self.segment[16:24]
        self.offsetReservedFlags = self.segment[24:28]

        binary = hexToBin(self.offsetReservedFlags)
        self.thl = binary[0:4]
        self.reserved = binary[4:10]
        self.urg = binary[10:11]
        self.ack = binary[11:12]
        self.psh = binary[12:13]
        self.rst = binary[13:14]
        self.syn = binary[14:15]
        self.fin = binary[15:16]
        

        self.window = self.segment[28:32]
        self.checksum = self.segment[32:36]
        self.urgentPointer = self.segment[36:40]

        if (int(self.thl,16)==5):
            self.data = self.segment[40:]
            self.option=[]
            self.padding=""
        else:
            #verfiier la taille des options!!
            options,padding=self.analyseOptions(self.segment[40:(int(self.thl,16)*4*2)])
            self.option=options
            self.padding=padding
            self.data = self.segment[(int(self.thl,16)*4*2):]



    def analyseOptions(self,data):
        offset=0
        options=[]
        padding=""
        erreur=False
        while(offset+2<=len(data) and not erreur):
            kind=int(data[offset:offset+2],16)
            infosOption=infoOption(TCPOPTIONSTYPE,kind)
            if infosOption != None:
                uneOption={"Option":infosOption["Meaning"],"Type":infosOption["Kind"]}

                if infosOption.get("Length")== "-":
                    offset+=2
                else:
                    uneOption.update({"Longueur ": infosOption["Length"]})
                    longueur=int(infosOption["Length"])
                    if longueur*2<=len(data[offset:]):
                        valeur=data[offset+4:offset+4+(longueur-2)*2]
                        if kind==2:
                            uneOption.update({"MSS": "0x"+valeur})
                        elif kind==3:
                            uneOption.update({"Shift": "0x"+valeur})
                        elif kind==8:
                            uneOption.update({"Time Stamp Value": "0x"+valeur[:8]})
                            uneOption.update({"Time Echo Value":"0x"+valeur[8:]})
                        else:
                            uneOption.update({"Valeur":"0x"+valeur})
                        offset+=longueur*2
                    else:
                        erreur=True
                if not erreur:
                    options.append(uneOption)
            else:
                erreur=True
        if(offset<len(data)):
            padding=data[offset:]
        return options,padding


    def optionsToString(self):
        result="\n\tOptions contenues:"+str(len(self.option))+" au total"
        cpt=1
        for op in self.option:
            for key, value in op.items():
                if(key=="Option"):
                    result+="\n\t\t"+key+" "+str(cpt)+": "+value 
                else:
                    result+="\n\t\t\t"+key+" : "+value 
                if key=="MSS":
                    result+=" ({})".format(hexToDec(value[2:]))

            cpt+=1
        return result
        
            
    def toString(self):
        res = "\nTCP:\n"

        res += "\tPort Source: {}({})\n\tPort Destination {} ({})\n\tNumero Sequence: {} ({})\n\tNumero ACK : {}({})\n\tTHL : {} ({} octets)\n\tReserved : {}".format(
            "0x"+self.srcPort,int("0x"+self.srcPort, 16),"0x"+self.dstPort, int("0x"+self.dstPort, 16),"0x"+self.seqNum, int("0x"+self.seqNum, 16),
            "0x"+self.ackNum, int("0x"+self.ackNum, 16), "0x"+binToHex(self.thl),binToDec(self.thl)*4, binToDec(self.reserved)
        )
        
        res+="\n\tURG : {}\n\tACK : {}\n\tPSH : {}\n\tRST : {}\n\tSYN : {}\n\tFIN : {}".format(
            self.urg,self.ack,self.psh,self.rst,self.syn,self.fin,
        )
        
        res+="\n\tWindow : {}\n\tChecksum: {}\n\tUrgent Pointer : {}\n".format(
            "0x"+self.window, "0x"+self.checksum, "0x"+self.urgentPointer
        )
       
        return res + self.optionsToString()
"""
data="ffad13895c3e066a00000000a00240009c2e0000020405a0010303000101080a009e7bc400000000"
tst=Segment(data)
print(tst.toString())
"""