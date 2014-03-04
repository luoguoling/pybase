__author__ = 'Administrator'
import time
from SocketServer import TCPServer,ThreadingMixIn,StreamRequestHandler
class Server(ThreadingMixIn,TCPServer):
    pass
class Handler(StreamRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(2048)
            if not data:
                break
            result = 0
            for i in range(1,int(data)+1):
                result = result + reduce(lambda x,y:x*y,range(1,i+1))
            self.request.send('the result is %i'% result)
a = time.time()
server = Server(('localhost',2007),Handler)

server.serve_forever()
print time.time() - a


