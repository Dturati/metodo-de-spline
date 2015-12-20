#Python 3
#David Turati
#Implelentaão da forma de Spline

# _*_ coding:latin 1 _*_
class Spline():
	dominio = []
	imagem = []
	equacao = []
	#Contrutor
	def __init__(self,tm):
		self.__tamanho = tm

	
	def getTamanho(self):
		return self.__tamanho

	#property
	tamanho = property(fget = getTamanho)

	def vetorDominio(self):
		for i in range(self.tamanho):
			print("Digite um valor pra X{:d}".format(i))
			self.dominio.append(int(input()))

	def vetorImagem(self):
		for i in range(self.tamanho):
			print("Digite um valor pra F(x){:d}".format(i))
			self.imagem.append(int(input()))
	
	def imprime(self):
		print(self.dominio)
		print(" ")
		print(self.imagem)

	def calcula_equacao(self):
		for i in range(1,self.tamanho):
			self.equacao.append( str(self.imagem[i-1])+"*"+str(self.dominio[i]) + "-" + "x" + "/" + str(self.dominio[i] - self.dominio[i-1]) 
			+ " " + "+" + str(self.imagem[i]) + "*" +"x"+"-"+ str(self.dominio[i-1]) + "/" + str(self.dominio[i]-self.dominio[i-1]))

	def imprime(self):
		print(" ")
		print("As equações são")
		for i in range(self.tamanho-1):
			print('s{:d}{}'.format(i,self.equacao[i]))
			print(" ")

print("Digite o tamanho do dominio e da imagem:")
s = Spline(int(input()))

s.vetorDominio()

s.vetorImagem()

s.calcula_equacao()

s.imprime()