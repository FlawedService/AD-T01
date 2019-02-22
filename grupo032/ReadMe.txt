Projeto de Aplicações Distribuídas do Grupo 032
——Segunda entrega ——

Inicializar primeiro Servidor:
 -> python lock_server 127.0.0.1 9999 10 60 #(Host, Port, n de recursos, tempo)

Inicializar clientes:
 -> python lock_client 127.0.0.1 9999 1 5 #(Host, Port, client_id, n de recurso)
 -> python lock_client 127.0.0.1 9999 2 4

Comandos:
	Exit
	Lock 10 1 2
	Release 20 1 2
	Test 30 3
	Stats 40 3
	Stats-y 50
	Stats-n 60
	
Melhoramentos:
	Do projeto 1 para o projeto 2 foi refeita a base da ligação do cliente  ao servidor pois este não aceitava múltiplas ligações.
	Refeito também as funções base como LOCK, RELEASE (…)


Limitações do Projecto:
	Devido a má interpretação do enunciado, os comandos que o cliente tem 	de introduzir seguem um padrão de [Comando] [inteiro correspondente 	ao comando] [Client_Id] [numero do recurso], para o LOCK e RELEASE

	Cliente fecha a ligação após cada comando,

	Funcionalidades dos Comandos TEST, STATS, STATS-Y, STATS-N estão i	mplementadas mas não estão implementadas corretamente
	

