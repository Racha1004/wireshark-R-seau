from Utils import *

class Segment:
    def __init__(self, segment):
        self.segment = segment
        self.srcPort = self.segment[0:4]
        self.dstPort = self.segment[4:8]
        self.seqNum = self.segment[8:16]
        self.ackNum = self.segment[16:24]
        self.offsetReservedFlags = self.segment[24:28]

        binary = hexToBin(self.offsetReservedFlags)
        self.thl = self.binary[0:4]
        self.reserved = self.binary[4:10]
        self.urg = self.binary[10:11]
        self.ack = self.binary[11:12]
        self.psh = self.binary[12:13]
        self.rst = self.binary[13:14]
        self.syn = self.binary[14:15]
        self.fin = self.binary[15:16]

        self.window = self.segment[28:32]
        self.checksum = self.segment[32:36]
        self.urgentPointer = self.segment[36:40]
        self.data = self.datagramme[40:]
        self.bool = False

        if int("0x"+self.srcPort, 16) == 53 or int("0x" + self.dstPort, 16) == 53 :
            self.data =  DNS(self.data)
            self.bool = True
        else:
            pass

    def toString(self):
        res = "TCP:\n"
        res += "\tPort Source: {}\n\tPort Destination {}\n\tNumero Sequence: {}\n\tNumero ACK : {}\n\tTHL : {}\n\tReserved : {}\n\tURG : {}\n\tACK : {}\n\tPSH : {}\n\t RST : {}\n\tSYN : {}\n\tFIN : {}\n\tWindow : {}\n\tChecksum: {}\n\tUrgent Pointer : {}\n".format(int(
            "0x"+self.srcPort, 16), int("0x"+self.dstPort, 16), int("0x"+self.seqNum, 16), int("0x"+self.ackNum, 16), binToDec(self.thl), binToDec(self.reserved), binToDec(self.urg), binToDec(self.ack), binToDec(self.psh), binToDec(self.rst), binToDec(self.syn), binToDec(self.fin), "0x"+self.window, "0x"+self.checksum, "0x"+self.urgentPointer)
        return res + self.data.toString()

    def toDict(self):
        if(self.bool):
            dictStr = '"TCP":{{"Port Source": "{}", "Port Destination": "{}", "Numero Sequence":"{}", "Numero ACK":"{}", "THL":"{}", "Reserved":"{}", "URG":"{}", "ACK":"{}", "PSH":"{}", "RST":"{}", "SYN":"{}", "FIN":"{}", "Window":"{}", "Checksum":"{}", "Urgent Pointer":"{}"}},'.format(int(
            "0x"+self.srcPort, 16), int("0x"+self.dstPort, 16), int("0x"+self.seqNum, 16), int("0x"+self.ackNum, 16), binToDec(self.thl), binToDec(self.reserved), binToDec(self.urg), binToDec(self.ack), binToDec(self.psh), binToDec(self.rst), binToDec(self.syn), binToDec(self.fin), "0x"+self.window, "0x"+self.checksum, "0x"+self.urgentPointer)+self.data.toDict()
        else:
            dictStr = '"TCP":{{"Port Source": "{}", "Port Destination": "{}", "Numero Sequence":"{}", "Numero ACK":"{}", "THL":"{}", "Reserved":"{}", "URG":"{}", "ACK":"{}", "PSH":"{}", "RST":"{}", "SYN":"{}", "FIN":"{}", "Window":"{}", "Checksum":"{}", "Urgent Pointer":"{}"}},'.format(int(
            "0x"+self.srcPort, 16), int("0x"+self.dstPort, 16), int("0x"+self.seqNum, 16), int("0x"+self.ackNum, 16), binToDec(self.thl), binToDec(self.reserved), binToDec(self.urg), binToDec(self.ack), binToDec(self.psh), binToDec(self.rst), binToDec(self.syn), binToDec(self.fin), "0x"+self.window, "0x"+self.checksum, "0x"+self.urgentPointer)
        return dictStr
