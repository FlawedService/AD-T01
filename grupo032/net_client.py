# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - net_client.py
Grupo:ad032
Números de aluno: 44312
"""

# zona para fazer importação

import sock_utils as s
import pickle

# definição da classe server

class server:
    """
    Classe para abstrair uma ligação a um servidor TCP. Implementa métodos
    para estabelecer a ligação, para envio de um comando e receção da resposta,
    e para terminar a ligação
    """

    #ADDRESS = '127.0.0.1'
    #PORT = 9999

    def __init__(self, address, port):
        """
        Inicializa a classe com parâmetros para funcionamento futuro.
        """
        self.address = address
        self.port = port
        self.conn_sock = s.create_tcp_client_socket()
        # self.conn_sock = s.socket(s.AF_INET, s.SOCK_STREAM)"

    def connect(self):
        """
        Estabelece a ligação ao servidor especificado na inicialização do
        objeto.
        """
        # try:
        #    self.conn_sock.connect((HOST, PORT))
        # except:
        #  return 0

        #self.socket = create_tcp_client_socket(self.address, self.port)
        self.conn_sock.connect((self.address, self.port))
        
    def send_receive(self, data):
        """
        Envia os dados contidos em data para a socket da ligação, e retorna a
        resposta recebida pela mesma socket.
        """

        d = pickle.dumps(data, -1)
        self.conn_sock.send(d)

        msg = self.conn_sock.recv(2048)
        l = pickle.loads(msg)
        return l

    def close(self):
        """
        Termina a ligação ao servidor.
        """
        self.conn_sock.close()
