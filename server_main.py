# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Reflects the requests from HTTP methods GET, POST, PUT, and DELETE
# Written by Nathan Hamiel (2010)

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser
from NeuroPy import NeuroPy
import serial
import MySQLdb
import datetime
from time import sleep
import threading



########################################################


def send_datas(datas_user,signals):
    API_BASE = "https://api.myjson.com/"
    # TODO: Aqui os dados serão enviados para serem salvos no banco
    print("DADOS ENVIADOS",signals)
    return True


########################################################
neuropy = NeuroPy("COM4")  # type: NeuroPy
neuropy.start()
print("start neuro")
porta = 'COM6'
velocidade = 9600

conexao = serial.Serial(porta, velocidade);

def start_capture(datas_user,start_time,session_id,movie_name,value):

    while True:
        #sleep(1)
        #current_time = datetime.datetime().now()
        leitura1 = conexao.readline()
        leitura2 = conexao.readline()
        #send_datas(datas_user,neuropy.attention)
        datas_send = {"datas_user":datas_user,
            "start_time":start_time,
            "session_id":session_id,
            "movie_name": movie_name,
            "neuropy.attention":neuropy.attention,
            "neuropy.meditation":neuropy.meditation,
            "neuropy.rawValue":neuropy.rawValue,
            "neuropy.delta": neuropy.delta,
            "neuropy.theta":neuropy.theta,
            "neuropy.lowAlpha": neuropy.lowAlpha,
            "neuropy.highAlpha": neuropy.highAlpha,
            "neuropy.lowBeta": neuropy.lowBeta,
            "neuropy.highBeta": neuropy.highBeta,
            "neuropy.lowGamma":neuropy.lowGamma,
            "neuropy.midGamma":neuropy.midGamma,
            "neuropy.poorSignal":neuropy.poorSignal,
            "neuropy.blinkStrength":neuropy.blinkStrength,
            "leitura1":leitura1,
            "leitura2": leitura2}



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



        ######################################################
        user = request_headers.getheaders('user')
        start_time = request_headers.getheaders('start_time')
        movie_name = request_headers.getheaders('movie_name')
        session_id = request_headers.getheaders('session_id')
        start_capture(user, start_time, movie_name, session_id, True)

        ######################################################



        length = int(content_length[0]) if content_length else 0
        
        #print(request_headers)
        #print(user)
        #print(self.rfile.read(length))

        print("<----- Request End -----\n")
        
        self.send_response(200)
        #start_capture(user,start_time,session_id,movie_name)
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