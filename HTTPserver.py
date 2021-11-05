import socket
import basicHTTP.consts
import basicHTTP.clientHandler


class HTTPServer():
    def __init__(self,ip="127.0.0.1",port=8080,handler=None,debug=False) -> None:
        self.ip = ip
        self.port = port
        self.debug = debug
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientHandler = handler
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.socket.bind((self.ip,self.port))
        self.socket.listen()
        print(f"Server started on: http://{ip}:{port}")
        pass
    
    def receive(self):
        buffer = ""
        conn, addr = self.socket.accept()



        if conn:
            client = basicHTTP.clientHandler.HTTPClient(conn)
            if self.clientHandler:
                self.clientHandler(client)

            if self.debug:
                print(client)

            #print(client.HTTP.headers)

            return()



        
    
    


        



    

    














