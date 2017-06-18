class Pessoa:
	
	def __init__(self, nome=None, sobrenome=None, rg=None, cpf=None, tel=None, cel=None, end=None):
		self.__nome = nome
		self.__sobrenome = sobrenome
		self.__rg = rg
		self.__cpf = cpf
		self.__tel = tel
		self.__cel = cel
		self.__end = end
	
	def getNome(self):
		return self.__nome

	def setNome(self, nome):
		self.__nome = nome

	def getSobrenome(self):
		return self.__sobrenome

	def setSobrenome(self,sobrenome):
		self.__sobrenome = sobrenome

	def getRG(self):
		return self.__rg

	def setRG(self, rg):
		self.__rg = rg
		
	def getCPF(self):
		return self.__cpf

	def getTel(self):
		return self.__tel

	def setTel(self, tel):
		self.__tel = tel

	def getCel(self):
		return self.__cel

	def setCel(self, cel):
		self.__cel = cel

	def getEnd(self):
		return self.__end

	def setEnd(self, end):
		self.__end = end
	
	def __repr__(self):
		return self.__str__()
	
	def __str__(self):
		return ','.join([self.__nome,self.__sobrenome,self.__rg,self.__cpf,self.__tel,self.__cel,self.__end])
	
	def __eq__(self, p):
		return self.__cpf == p.__cpf
	
