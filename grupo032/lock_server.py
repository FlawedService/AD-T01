#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_server.py
Grupo: ad032
Números de aluno: 44312
"""

# Zona para fazer importação
import sys
import socket as s
import pickle
import select as sel
import lock_skel as skel

###############################################################################
# código do programa principal

print "Server is Online"
#python lock_server 127.0.0.1 9999 10 60
addr = ''
port = int(sys.argv[2]) #checkar isto
#client_id = int(sys.argv[3])
resource_number = int(sys.argv[3])
resource_time = int(sys.argv[4])
maxl = 10
maxsiml = 3
print "Porta: " + str(port)
print "address: " + str(addr)

lskel = skel.lock_skel(resource_number, maxl, maxsiml, resource_time)

sock = s.socket(s.AF_INET, s.SOCK_STREAM)
sock.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
sock.bind((addr, port))
sock.listen(3)
SocketList = [sock]

while True:
    try:
        R, W, X = sel.select(SocketList, [], []) #waits for sockets
        msg = ''
        for sckt in R:
            if sckt is sock:
                (conn_sock, addr) = sock.accept()
                addr, port = conn_sock.getpeername()
                print 'Novo cliente ligado desde %s:%d' % (addr, port)
                print 'Available Commands are: LOCK, RELEASE, TEST, STATS, STATS-Y, STATS-N'
                SocketList.append(conn_sock)
            else:
                temp = []
                getit = sckt.recv(1024)
                
                if getit == '':
                    print"Cliente" + str(sckt.getpeername()) + "Closed"
                    sckt.close()
                    SocketList.remove(sckt)
                else:
                    #takeit = sock_utils.receive_all(sckt, getit)
                    #resposta = pickle.loads(takeit)
                    temp = lskel.processMessage(pickle.loads(getit))
                    sckt.sendall(pickle.dumps(temp))
                    sckt.close()
                    SocketList.remove(sckt)
                    print 'Cliente fechou a ligacao %s:%d' % (addr, port)
    except KeyboardInterrupt :
        print " Interrupted by the user"
        #sckt.close()
        exit()
