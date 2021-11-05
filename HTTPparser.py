class HTTPReq():


    def __init__(self,raw) -> None:

        self.raw = raw
        self.headers = {}
        self.queryString = {}
        self.method = ""
        self.version = ""
        self.file = ""
        self.body = ""
        self.parse()
        pass


    def parse(self):
        splitLines = self.raw.split("\r\n")
        statusLine = splitLines[0]
        self.method,self.file,self.version = statusLine.split(" ")
        


        for i in range(1,len(splitLines)):
            line = splitLines[i]
            if line == "":
                break
            
            
            header,value = line.split(":",1)
            value = value[1:]


            if header == "cookie":
                

                splitval = value.split(";")
                cookies = {}
                for i in splitval:
                    name,val = i.split("=",1)
                    cookies[name]=value
                self.headers[header]=cookies

            else:

                value = value.split(",")
                value = [s.strip() for s in value]
                if len(value) == 1:
                    value = value[0]

                self.headers[header] = value


class HTTPresp():

    def __init__(self) -> None:
        self.raw = None
        self.headers = {}
        self.version = "HTTP/1.1"
        self.status = 200
        self.phrase = "OK"
        self.body = ""
        pass
    

    def build(self):
        if self.body:
            self.headers["content-length"] = len(self.body)

        statusLine = f"{self.version} {self.status} {self.phrase}"
        headers = ""

        for key in self.headers:
            val = self.headers[key]
            
            if type(val) == list:
                val = ",".join(val)



            headers += f"{key}: {val}\r\n"

        resp = f"{statusLine}\r\n{headers}{self.body}\r\n\r\n" 
        return(resp)
    

    def __bytes__(self):
        return(bytes(self.build(),'utf-8'))





    

