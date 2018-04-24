# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Reflects the requests from HTTP methods GET, POST, PUT, and DELETE
# Written by Nathan Hamiel (2010)

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser
from NeuroPy import NeuroPy
from time import sleep
import threading



########################################################


def send_datas(datas_user,signals):
    API_BASE = "https://api.myjson.com/"
    # TODO: Aqui os dados serão enviados para serem salvos no banco
    print("DADOS ENVIADOS",neuropy.attention)
    return True


########################################################

def start_capture(datas_user):    
    neuropy.start()
    while True:
        sleep(1)

        send_datas(datas_user,neuropy)

        #print( neuropy.attention,
        #    neuropy.meditation,
        #    neuropy.rawValue,
        #    neuropy.delta,
        #    neuropy.theta,
        #    neuropy.lowAlpha,
        #    neuropy.highAlpha,
        #    neuropy.lowBeta,
        #    neuropy.highBeta,
        #    neuropy.lowGamma,
        #    neuropy.midGamma,
        #    neuropy.poorSignal,
        #    neuropy.blinkStrength)



########################################################
class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        #request_path = self.path
        
        #print("\n----- Request Start ----->\n")
        #print(request_path)
        #print(self.headers)
        #print("<----- Request End -----\n")
        
        self.send_response(200)
        self.send_header("Set-Cookie", "foo=bar")                
        
    def do_POST(self):        
        request_path = self.path
        
        print("\n----- Request Start ----->\n")
        print(request_path)
        
        request_headers = self.headers
        content_length = request_headers.getheaders('content-length')
        user = request_headers.getheaders('user')
        length = int(content_length[0]) if content_length else 0
        
        #print(request_headers)
        #print(user)
        #print(self.rfile.read(length))
        start_capture(user)
        print("<----- Request End -----\n")
        
        self.send_response(200)
    
    do_PUT = do_POST
    do_DELETE = do_GET
        
def main():
    port = 8080
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()

        
if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = ("Creates an http-server that will echo out any GET or POST parameters\n"
                    "Run:\n\n"
                    "   reflect")
    (options, args) = parser.parse_args()
    
    main()