
import Utils
import csv
PATHREFERENCES = "./referances/"
OUTPUTPATH = "./output/"


with open(PATHREFERENCES+"methodshttp.csv", "r")as httpOp:
    reader=csv.reader(httpOp, delimiter=',')
    httpMethods = []
    for ligne in reader:
        httpMethods.append(ligne[0])

httpOp.close()
HTTPMETHODS=httpMethods

"""
with open(PATHREFERENCES+"http-status-codes-1.csv", "r")as status:
    reader=csv.DictReader(status, delimiter=',')
    statushttp = []
    for ligne in reader:
        statushttp.append((ligne))

status.close()
TCPOPTIONSTYPE=tcpOptions
"""

class Http:
    def __init__(self, data):
        self.data = data.upper()
        self.info1, self.info2, self.info3 = "","",""
        self.erronee=False
        self.message=""
        self.lignesEntete =self.analyse(self.data)
        
    
    def analyse(self,data):
        lignes=data.split("0D0A")

        if len(lignes)==0:
            self.erronee=True
        
        first_line = lignes[0].split("20")
        if len(first_line)==3: 
            self.info1=Utils.asciiToString(first_line[0])
            self.info2=Utils.asciiToString(first_line[1])
            self.info3=Utils.asciiToString(first_line[2])
        elif len(first_line)==2:
            self.info1=Utils.asciiToString(first_line[0])
            self.info2=Utils.asciiToString(first_line[1])
        elif len(first_line)==1: 
            self.info1=first_line[0]
        else:
            self.erronee=True
        
        dict={}

        if not self.erronee: 
            lignes=lignes[1:]
            #if len(lignes)!=0: lignes.pop()
            for i in range(len(lignes)):
                if(len(lignes[i])==0):#pour le message , car si on a un "" c'est qu il "etait entre 2 0a0d successifs
                    if(i+1<len(ligne)-1):
                        str=''.join(lignes[i+1:])
                        self.message=Utils.asciiToString(str)
                else:    
                    ligneSplitted=lignes[i].split("20")
                    if(len(ligneSplitted)%2!=0): #Si on a un nom de champs sans sa valeur en effet les 0x20
                                                # separent chaque champs avec sa valeur donc il doit y'avoir 
                                                #un nombre pair de val(cle,val)
                        self.erronee=True
                        break
                    else:
                        i=0
                        while(i+1<=len(ligneSplitted)-1):
                            if(len(ligneSplitted[i])>0):
                                key=Utils.asciiToString(ligneSplitted[i])
                                value=Utils.asciiToString(ligneSplitted[i+1])
                                dict[key]=value
                            else:
                                self.erronee=True
                                break
                            
                            i+=2
        return dict

    def get_method(self):
        return self.info1

    def get_versionRes(self):
        return self.info1
    
    def get_url(self):
        return self.info2
    
    def get_code(self):
        return self.info2

    def get_versionReq(self):
        return self.info3

    def get_message(self):
        return self.info3

    def is_request(self,isReq):
        
        if not  isReq in HTTPMETHODS:
            self.erronee=True
            return False
        return True

    def is_response(isRes):
        try:
            return isRes.startswith("HTTP/")
        except:
            return False

    def toString(self):
        res = "\nHTTP:"
        if not self.erronee:
            if(self.is_request(self.info1)):
                res += "\n\tRequest\n\t\t Methode : {}\n\t\t URL : {}\n\t\t Version : {}\n". format(self.info1, self.info2,self.info3)
            else:
                res += "\n\tResponse\n\t\t Version : {}\n\t\t Code : {}\n\t\t Message : {}\n".format(self.info1, self.info2,self.info3)
            
            for key in self.lignesEntete.keys():
                res+="\n\t\t{} : {} ".format(key,self.lignesEntete.get(key))
        else:
            res+=" Erreur de format au niveau de la COUCHE7 ----> on arrete l'analyse"
        return res
    
    def getMessage(self):
        return " {} {} {} ". format(self.info1, self.info2,self.info3)


""""
http =Http("474554202f7e737061746869732f20485454502f312e310d0a486f73743a207777772d6e70612e6c6970362e66720d0a436f6e6e656374696f6e3a206b6565702d616c6976650d0a557067726164652d496e7365637572652d52657175657374733a20310d0a557365722d4167656e743a204d6f7a696c6c612f352e3020284d6163696e746f73683b20496e74656c204d6163204f5320582031305f31345f3634330d0a0d0a")
print(http.toString())
print(http.getMessage())
"""