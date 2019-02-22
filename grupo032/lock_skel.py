#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 2 - lock_stub.py
Grupo:ad032
Números de aluno: 44312
"""

# Zona para fazer importação
import pickle
import lock_pool as lp
import time as t
#class that handles severall server commands

class lock_skel:

    def __init__(self, rs, maxl, maxsiml, timel):

        self.rs = rs
        self.maxl = maxl
        self.maxsiml = maxsiml
        self.timel = timel
        self.l = lp.lock_pool(rs,maxl, maxsiml, timel)
        self.r = lp.resource_lock()
        self.servicoLista = []
        #should have a handler

    def processMessage(self, msg_bytes) :
        
        pedido = pickle.loads(msg_bytes)
        resposta = []
        print "pedido", pedido
        if pedido == None or len(pedido) == 0 :
            resposta.append("INVALID MESSAGE")

        else :
            if pedido[2] == "10" and len(pedido) > 1 :
                if self.l.lock(pedido[4], pedido[3], self.timel) == True and pedido[1] == int(pedido[3]) :
                    self.servicoLista.append(msg_bytes[2]) #ver isto
                    resposta.append("11")
                    resposta.append("True")
                    print "LOCKED!"
                    return resposta

                elif self.l.lock(pedido[4], pedido[3], self.timel) == False  and pedido[1] == int(pedido[3]):
                    self.servicoLista.append(msg_bytes[2])
                    resposta.append("11")
                    resposta.append("False")
                    return resposta
                    
                else:
                    resposta.append("11")
                    resposta.append("None")
                    return resposta

            elif pedido[2] == "20" and len(pedido) > 1:
                if self.l.release(pedido[4], pedido[3]) == True:
                    resposta.append(str(self.servicoLista))
                    resposta.append("21")
                    resposta.append("true")
                    print "UNLOCKED!"
                    return resposta

                elif self.l.release(pedido[4], pedido[3]) == False:
                    resposta.append(str(self.servicoLista))
                    resposta.append("21")
                    resposta.append("False")
                    return resposta

                else:
                    resposta.append("21")
                    resposta.append("None")
                    return resposta

            elif pedido[2] == "30" and len(pedido) > 1:
                if int(pedido[3]) == pedido[1] and self.l.test(pedido[4]) == True:
                    resposta.append(str(self.servicoLista))
                    resposta.append("31")
                    resposta.append("True")
                    return resposta

                elif int(pedido[3]) == pedido[1] and self.l.test(pedido[4]) == False:
                    resposta.append(str(self.servicoLista))
                    resposta.append("31")
                    resposta.append("False")
                    return resposta
                    
                elif self.l.test(pedido[3]) == 0: # 0 == disable
                    resposta.append(str(self.servicoLista))
                    resposta.append("31")
                    resposta.append("Disable")
                    return resposta

                else:
                    resposta.append("31")
                    resposta.append("None")
                    return resposta

            elif pedido[2] == "40" and len(pedido) > 1:
                if self.l.stats(pedido[3]) == True and int(pedido[3]) == pedido[1]:
                    resposta.append(str(self.servicoLista))
                    resposta.append("41")
                    resposta.append(lp.resource_lock.stats(self.r))
                    return resposta

                else:
                    resposta.append("41")
                    resposta.append("None")
                    return resposta

            elif pedido[2] == "50" and len(pedido) > 1:
                resposta.append(str(self.servicoLista))
                resposta.append("51")
                resposta.append(lp.lock_pool.stats_y(self.l))
                return resposta
                
            elif pedido[2] == "60" and len(pedido) > 1:
                resposta.append(str(self.servicoLista))
                resposta.append("61")
                resposta.append(lp.lock_pool.stats_n(self.l))
                return resposta

            else :
                resposta.append("INVALID MESSAGE")
                return resposta

        pickle.dumps(resposta)
        return resposta
