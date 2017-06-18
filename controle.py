from pessoa import Pessoa
from lista import Lista
import os
#import sys, termios, tty

def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(fd)
		ch = sys.stdin.read(1)
		sys.stdin.seek(2)
		#termios.tcflush(sys.stdin, termios.TCIFLUSH)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

# Essa funcao recebe dois objetos do tipo Pessoa
# e retorna qual pessoa deve vir antes de acordo com
# o nome e sobrenome.
# A funcao deve retornar:
# -1 -- se p1 < p2
# 0  -- se p1 == p2
# +1 -- se p1 > p2
# Voce deve implementa-la
def cmp(p1, p2):
        if p1.getNome() < p2.getNome(): return -1
        elif p1.getNome() > p2.getNome(): return 1
        elif p1.getSobrenome() < p2.getSobrenome(): return -1
        elif p1.getSobrenome() > p2.getSobrenome(): return 1
        return 0

class Controle:
	
	def __init__(self, arquivo):
		self.__lista = Lista()
		self.__arquivo = arquivo
		self.__carregarDados()
	
	def __carregarDados(self):
		with open(self.__arquivo) as f:
			for linha in f:
				self.__lista.inserirOrdenado(Pessoa(*(linha.strip().split('\t'))), cmp)
	
	def __cadastrar(self, p):
		self.__lista.inserirOrdenado(p, cmp)
	
	def __remover(self, p):
		self.__lista.remover(p)
	
	def __salvar(self):
		with open(self.__arquivo,'w') as f:
			f.write(self.__lista.toCSV('\t'))
	
	def __exibir(self):
		print(self.__lista)
	
	def __buscar(self,p):
		return self.__lista.buscar(p)
	
	def __menuCadastrar(self):
		while True:
			os.system('cls' if os.name == 'nt' else 'clear')
			nome = input('Nome do cliente:')
			sobrenome = input('Sobrenome:')
			rg = input('RG:')
			cpf = input('CPF:')
			tel = input('Telefone:')
			cel = input('Celular:')
			end = input('Endereco:')
			self.__cadastrar(Pessoa(nome,sobrenome,rg,cpf,tel,cel,end))
			
			continuar = input('Deseja cadastrar outro cliente? (S/N)')
			if continuar.upper() != 'S': break
		
	def __menuExcluir(self):
		while True:
			os.system('cls' if os.name == 'nt' else 'clear')
			cpf = input('Entre com o CPF do cliente que seja excluir:')
			self.__remover(Pessoa(cpf=cpf))
			
			continuar = input('Deseja excluir outro cliente? (S/N)')
			if continuar.upper() != 'S': break

	def __menuSalvar(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		self.__salvar()
		print('Dados armazenados em arquivo')
		print('Pressione uma tecla para continuar')
		getch()
		

	def __menuListar(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		self.__exibir()
		print('Pressione uma tecla para continuar')
		getch()
		
	def __menuSair(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		sys.exit(0)
	
	def menu(self):
		interface='''
*******************************************************************************
                              GESTAO DE CLIENTES                               
*******************************************************************************

Escolha a operacao que deseja executar:

1 - Cadastrar novos clientes
2 - Excluir cliente
3 - Salvar base de dados
4 - Listar clientes
5 - SAIR

Opcao:\b
'''
		while True:
			os.system('cls' if os.name == 'nt' else 'clear')
			opcao = int(input(interface))
			menu = [self.__menuCadastrar,self.__menuExcluir,self.__menuSalvar,self.__menuListar,self.__menuSair]
			acao = menu[opcao-1]
			acao()
