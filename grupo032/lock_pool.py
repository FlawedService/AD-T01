#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_server.py
Grupo:ad032
Números de aluno:
"""

# Zona para fazer importação
import time

###############################################################################

class resource_lock:
    def __init__(self):

        # self.resource_id = resource_id
        self.resource_id = 0
        self.client_id = 0
        self.is_lock = False
        self.is_inactive = False
        self.n_of_locks = 0
        self.starting_time = int(round(time.time() * 1000))  # start time in milliseconds
        self.ending_time = 0
        self.max_num_locks = 5

    def lock(self, client_id, time_limit):
        """
        Bloqueia o recurso se este não estiver bloqueado ou inativo, ou mantém o bloqueio
        se o recurso estiver bloqueado pelo cliente client_id. Neste caso renova
        o bloqueio do recurso até time_limit.
        Retorna True se bloqueou o recurso ou False caso contrário.
        """
        self.starting_time = int(round(time.time() * 1000))
        if(not self.is_lock and self.is_inactive == False): # if unblocked or inactive, block it till expected time
            self.client_id = client_id
            #self.starting_time = int(round(time.time() * 1000))
            self.ending_time = self.starting_time + time_limit
            self.is_lock = True
            self.n_of_locks += 1
            return True
        elif self.starting_time > self.ending_time:
            self.client_id = 0
            self.is_lock = False
            return False

    def urelease(self):
        """
        Liberta o recurso incondicionalmente, alterando os valores associados
        ao bloqueio.
        """
        self.is_lock = False
        self.ending_time = 0
        return True

    def release(self, client_id):
        """
        Liberta o recurso se este foi bloqueado pelo cliente client_id,
        retornando True nesse caso. Caso contrário retorna False.
        """
        if self.client_id == client_id:
            self.is_lock = False
            self.client_id = 0
            self.ending_time = 0
            return True
        else:
            return False

    def test(self):
        """
        Retorna o estado de bloqueio do recurso ou inativo, caso o recurso se
        encontre inativo.
        """
        if self.is_inactive:
            return 0  # returns this as inactive
        return self.is_lock

    def stats(self):
        """
        Retorna o número de vezes que este recurso já foi bloqueado em k.
        """
        return self.n_of_locks

    def disable(self):
        """
        Coloca o recurso inativo/indisponível incondicionalmente, alterando os
        valores associados à sua disponibilidade.
        """
        self.is_inactive = True

    def is_locked(self):
        return self.is_lock

    def get_resource_id(self):
        return self.resource_id

    def get_client_id(self):
        return self.client_id

    def get_ending_time(self):
        return self.ending_time



###############################################################################

class lock_pool:
    def __init__(self, N, K, Y, T):
        """
        Define um array com um conjunto de locks para N recursos. Os locks podem
        ser manipulados pelos métodos desta classe.
        Define K, o número máximo de bloqueios permitidos para cada recurso. Ao
        atingir K, o recurso fica indisponível/inativo.
        Define Y, o número máximo permitido de recursos bloqueados num dado
        momento. Ao atingir Y, não é possível realizar mais bloqueios até que um
        recurso seja libertado.
		Define T, o tempo máximo de concessão de bloqueio.
        """
        self.resources = []
        for i in range(N):
            self.resources.append(resource_lock())
        self.max_num_locks = K
        self.max_num_simultaneos_locks = Y
        self.num_current_locks = 0
        self.time_limit = T  # isto tem de vir em milisegundos se nao da mrd

    def clear_expired_locks(self):
        """
        Verifica se os recursos que estão bloqueados ainda estão dentro do tempo
        de concessão do bloqueio. Liberta os recursos caso o seu tempo de
        concessão tenha expirado.
        """
        #[resource.urelease() if int(round(time.time() * 1000)) > resource.ending_time for resource in self.resources]

        for resource in self.resources:
             if int(round(time.time() * 1000)) > resource.get_ending_time:
                resource.urelease()

    def lock(self, resource_id, client_id, time_limit):
        """
        Tenta bloquear o recurso resource_id pelo cliente client_id, até ao
        instante time_limit.
        O bloqueio do recurso só é possível se o recurso estiver ativo, não
        bloqueado ou bloqueado para o próprio requerente, e Y ainda não foi
        excedido. É aconselhável implementar um método __try_lock__ para
        verificar estas condições.
        Retorna True em caso de sucesso e False caso contrário.
        """

        return self.resources[int(resource_id)].lock(int(client_id), int(time_limit))

    def release(self, resource_id, client_id):
        """
        Liberta o bloqueio sobre o recurso resource_id pelo cliente client_id.
        True em caso de sucesso e False caso contrário.
        """
        if int(client_id) ==  0:
            return 0
        return self.resources[int(resource_id)].release(int(client_id))

    def test(self, resource_id):
        """
        Retorna True se o recurso resource_id estiver bloqueado e False caso
        esteja bloqueado ou inativo.
        """
        #state = self.resources[int(resource_id)].test()
        #if state == 0 or self.resources[resource_id].is_lock:
         #   return False
        #else:
         #   return True
        return self.resources[int(resource_id)].test()

    def stats(self, resource_id):
        """
        Retorna o número de vezes que o recurso resource_id já foi bloqueado, dos
        K bloqueios permitidos.
        """
        return self.resources[int(resource_id)].stats()

    def stats_y(self):
        """
        Retorna o número de recursos bloqueados num dado momento do Y permitidos.
        """
        return self.num_current_locks

    def stats_n(self):
        """
        Retorna o número de recursos disponíneis em N.
        """
        return (len(self.resources) - self.num_current_locks)

    def __repr__(self):
        """
        Representação da classe para a saída standard. A string devolvida por
        esta função é usada, por exemplo, se uma instância da classe for
        passada à função print.
        """
        output = ''
        for resource in self.resources:
            if resource.is_inactive == True:
                output += "recurso inativo", (resource.get_resource_id())
            elif resource.is_locked():
                output += "recurso %s bloqueado pelo cliente %s até %s" + resource.get_resource_id(), resource.get_client_id(), resource.get_ending_time()
            else:
                output += "recurso desbloqueado" + resource.get_resource_id()

    #
    # Acrescentar na output uma linha por cada recurso bloqueado, da forma:
    # recurso <número do recurso> bloqueado pelo cliente <id do cliente> até
    # <instante limite da concessão do bloqueio>
    #
    # Caso o recurso não esteja bloqueado a linha é simplesmente da forma:
    # recurso <número do recurso> desbloqueado
    # Caso o recurso não esteja inativo a linha é simplesmente da forma:
    # recurso <número do recurso> inativo
    #
        return output
