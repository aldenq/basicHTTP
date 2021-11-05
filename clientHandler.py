import basicHTTP.HTTPparser,time
class HTTPClient():

    def __init__(self,socket,addr) -> None:

        self.start = time.time()
        self.socket = socket
        self.raw = ""
        self.HTTP = None
        self.addr = addr

        while True:
            data = self.socket.recv(1).decode("utf-8")
            self.raw += data
            if data == "\n":
                if len(self.raw) >= 4:
                    if self.raw[-4:] == "\r\n\r\n":
                        break
            
        
        self.HTTP = basicHTTP.HTTPparser.HTTPReq(self.raw)
        if "Content-Length" in self.HTTP.headers:
            self.HTTP.body = self.socket.recv(int(self.HTTP.headers["Content-Length"])).decode("utf-8")




        pass

    def __repr__(self) -> str:
        return(self.raw)


    def send(self,data):
        self.socket.send(data)
        self.socket.close()
        # print(f"time to handle: {time.time()-self.start}")
