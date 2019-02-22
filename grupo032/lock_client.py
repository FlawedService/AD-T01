#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_client.py
Grupo:ad032
Números de aluno: 44312
"""
# Zona para fazer imports
import sys
import lock_stub as ls

# Programa principal
if len(sys.argv) > 3:
    addr = sys.argv[1]  # ip do servidor
    port = int(sys.argv[2])  # porta tcp
    client_id = int(sys.argv[3])  # id unico do cliente
    n_recurso = int(sys.argv[4]) # n de recursos
    cont = 0
    dados = []
    while cont < len(sys.argv):
        dados.append(sys.argv[cont])
        cont += 1
    print "dados", dados
    print "connected"
    
    lscon = ls.lock_stub(addr, port)
    
    while True:
        try:
            cmd = raw_input("commands -> : ")
            cmd = cmd.split(" ")
            #cmd += str(sys.argv[3])  # o cliente id
            cmd.insert(1, client_id)
            msg = ''
            print "Command: ", cmd
            if cmd[0].upper() == "EXIT":  # upper_case just in case bad typing
                print "bazei"
                exit()
            elif cmd[0].upper() == "LOCK":
                msg = lscon.lock(cmd)
                
            elif cmd[0].upper() == "RELEASE":
                msg = lscon.release(cmd)

            elif cmd[0].upper() == "TEST":
                msg = lscon.test(cmd)

            elif cmd[0].upper() == "STATS":
                msg = lscon.stats(cmd)
            elif cmd[0].upper() == "STATS-Y":
                msg = lscon.stats_y(cmd)

            elif cmd[0].upper() == "STATS-N":
                msg = lscon.stats_n(cmd)

            else:
                print "UNKNOWN COMMAND"
                
            print "recebi:", msg 
            
        except Exception, e:
            print" sai pelo except"
            print e
            lscon.close()
            exit()