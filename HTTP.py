from Utils import *

http_methods = ["GET", "HEAD","POST","PUT","DELETE"]

class HTTPMessage:
    def __init__(self, length_TCP):
        self.offset = length_TCP
        first_line = self.readline().rstrip("0d0a")
        self.word1, self.word2, self.word3 = first_line.split()[:3]
      
    def get_method(self):
        return self.word1

    def get_versionRes(self):
        return self.word1
    
    def get_url(self):
        return self.word2
    
    def get_code(self):
        return self.word2

    def get_versionReq(self):
        return self.word3

    def get_message(self):
        return self.word3
    
  
    def is_newline(c):
      return c in "0d0a"

    def readline(in_):
        c = in_.read(1)
        line = str()
        while (len (c) > 0):
            if (is_newline (c)):
                line += c
                break
            line += c
            c = in_.read(1)
        return line

    def is_request(first_line):
        try:
            first_word = first_line.split()[0]
            return first_word in http_methods
        except:
            return False

    def is_response(first_line):
        try:
            first_word = first_line.split()[0]
            return first_word.startswith("HTTP/")
        except:
            return False

    def toString(self, first_line):
        res = "HTTP:\n"
        if(is_request(first_line)):
          res += "Request\n\t Methode : {}\n\t URL : {}\n\t Version : {}\n". get_method(self), get_url(self), get_versionReq(self)
        else:
          res += "Response\n\t Version : {}\n\t Code : {}\n\t Message : {}\n". get_versionRes(self), get_code(self), get_message(self)
        return res

    def toDict(self, first_line):
        if(is_request(first_line)):
            dictStr = '"HTTP Request":{{"Methode": "{}", "URL": "{}", "Version":"{}"'.get_method(self), get_url(self), get_versionReq(self)
        else:
            dictStr = '"HTTP Response":{{"Version": "{}", "Code": "{}", "Message":"{}",'.get_versionRes(self), get_code(self), get_message(self)
        return dictStr
