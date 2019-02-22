#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 2 - lock_stub.py
Grupo:ad032
Números de aluno: 44312
"""

# Zona para fazer importação
import net_client
import pickle

#class to connect/disconnect to server and handle other commands
class lock_stub:
    
    def __init__(self, address, port):
        self.con = net_client.server(address,port)
        self.con.connect()
        
    def close(self):
        #Fecha a ligação conn_sock
        self.con.close()

    def lock(self, cmd):
        #msg enviado[10, client_id, n_recurso
        #resposta [11,True] ou [11,False] ou [11,NONE]
        print "entrou lock", cmd
        if cmd[2] == '10':
            resposta = pickle.dumps(cmd, -1) #most recent protocol
            #self.con.send_receive(resposta)
            #pickle.loads(resposta)
            return self.con.send_receive(resposta)
        else:
            print 'wrong value'
        
    def release(self, cmd):
        #msg enviado[20, client_id, n_recurso
        #resposta [21,True] ou [21,False] ou [21,NONE]
        if cmd[2] == '20':
            resposta = pickle.dumps(cmd, -1) #most recent protocol
            return self.con.send_receive(resposta)
        else :
            print "wrong value"

    def test(self, cmd):
        #msg enviado[30, n_recurso
        #resposta [31,True] ou [31,False] ou [31,Disable] ou [31,NONE]
        if cmd[2] == '30':
            resposta = pickle.dumps(cmd, -1) #most recent protocol
            return self.con.send_receive(resposta)
        else :
            print "wrong value"

    def stats(self, cmd):
        #msg enviado[40, n_recurso
        #resposta [41,n de bloqueios] ou [41,NONE]
        if cmd[2] == '40':
            resposta = pickle.dumps(cmd, -1) #most recent protocol
            return self.con.send_receive(resposta)
        else :
            print "wrong value"

    def stats_y(self, cmd):
        #msg enviado[50]
        #resposta [51,n_recurso bloqueados em y]
        if cmd[2] == '50':
            resposta = pickle.dumps(cmd, -1) #most recent protocol
            return self.con.send_receive(resposta)
        else :
            print "wrong value"
        
    def stats_n(self,cmd):
        if cmd[2] == '60':
            resposta = pickle.dumps(cmd, -1) #most recent protocol
            return self.con.send_receive(resposta)
        else :
            print "wrong value"
        
