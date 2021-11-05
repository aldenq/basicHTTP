import basicHTTP.HTTPparser
class HTTPClient():

    def __init__(self,socket) -> None:
        self.socket = socket
        self.raw = ""
        self.HTTP = None


        while True:
            data = self.socket.recv(1).decode("utf-8")
            self.raw += data
            if data == "\n":
                if len(self.raw) >= 4:
                    if self.raw[-4:] == "\r\n\r\n":
                        break
            
        
        self.HTTP = basicHTTP.HTTPparser.HTTPReq(self.raw)




        pass

    def __repr__(self) -> str:
        return(self.raw)


    def send(self,data):
        self.socket.send(data)
        self.socket.close()

