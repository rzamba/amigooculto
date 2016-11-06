# -*- coding: utf-8 -*-
import argparse
import os
from random import randint

# cLass para objetos participante
class Participante:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
 
    def __str__(self):
        return "%s - %s" % (str(self.nome), str(self.email))

# class para objetos resultado do sorteio
class Resultado:
    def __init__(self, participante, amigo):
        self.participante = participante
        self.amigo = amigo
 
    def __str__(self):
        return "%s - %s" % (str(self.participante), str(self.amigo))

def sorteio_modo_aleatorio(lista_participantes,lista_amigos):
	print "Executando sorteio aleatorio"
	lista_resultado = []
	for participante in lista_participantes:
		amigo = ""
		while True:
			i = randint(0,len(lista_amigos)-1)
			amigo = lista_amigos[i]
			# validando se participamte nao sorteou ele mesmo
			if participante.nome != amigo.nome:
				break
			# trata casa do ultimo participante tirar ele mesmo
			elif participante == lista_participantes[len(lista_participantes)-1]:
				amigo_trocado = amigo
				amigo = lista_resultado[0].amigo 
				lista_resultado[0].amigo = amigo_trocado
				break
		# armazenando lista de resultado
		lista_resultado.append(Resultado(participante,amigo))
		# retirando amigo sorteado
		if participante != lista_participantes[len(lista_participantes)-1]:
			lista_amigos.remove(amigo)
	return lista_resultado


def sorteio_modo_semquebra(lista_amigos):
	print "Executando sorteio sem quebra"
	lista_resultado = []
	participante = lista_amigos[0]
	while len(lista_amigos) > 0:
		amigo = ""
		while True:
			i = randint(0,len(lista_amigos)-1)
			amigo = lista_amigos[i]
			# validando se participamte nao sorteou ele mesmo
			if participante.nome != amigo.nome:
				amigo_ja_participou = False
				for resultado in lista_resultado:
					if (amigo.nome == resultado.participante.nome) and len(lista_amigos) > 1:
						amigo_ja_participou = True
				if not amigo_ja_participou:
					break
		
		# armazenando lista de resultado
		lista_resultado.append(Resultado(participante,amigo))
		# amigo sorteado agora e participante e escolhe proximo amigo
		participante = amigo
		# retirando amigo sorteado
		lista_amigos.remove(amigo)
	return lista_resultado


def prepara_sorteio_gera_saida(args):
	
	arquivo_de_participantes = args.arq
	mode = args.mode
	print u"Executando leitura do arquivo de participantes "+ arquivo_de_participantes
	
	try:
		f = open(arquivo_de_participantes, 'r')
	except:
		print "Erro na abertura do arquivo " + arquivo_de_participantes
		sys.exit(-1)
		
	# carregando lista de participantes
	lista_participantes = []
	for line in f:
		nome,email = line.split(",")
		email = email.replace("\n", "")
		lista_participantes.append(Participante(nome,email))
	f.close()

	# gerando list de amigos
	lista_amigos = list(lista_participantes)

	os.system("rm -rf resultado_sorteio")
	try:
		os.mkdir ("resultado_sorteio")
	except:
		pass
	

	lista_resultado = []
	if mode != "sem_quebra":
		lista_resultado = sorteio_modo_aleatorio(lista_participantes,lista_amigos)
	else:
		lista_resultado = sorteio_modo_semquebra(lista_amigos)

	
	for resultado in lista_resultado:
		# print resultado.participante.nome + " seu amigo oculto é " + resultado.amigo.nome
		# print "---------------------------------------------------------------------------------------------------------"

		# gravando arquivo de resultado
		saida = open("./resultado_sorteio/"+resultado.participante.email+".txt", "w")
		saida.write(resultado.participante.nome + " seu amigo oculto é " + resultado.amigo.nome)
		saida.close()

	print u"Final de execução - sorteio realizado"

def main():
	parser = argparse.ArgumentParser(description='Sorteio de amigo oculto')
	parser.add_argument('-a', '--arq', required=True, help='Arquivo de participantes no formato nome,email')
	parser.add_argument('-m', '--mode', required=False, default="sem_restricoes", help='São permitidos dois tipos de sorteio: totalmente aleatorio -m sem_restricoes (default) ou lista circular sem quebras -m sem_quebra')
	args = parser.parse_args()
	prepara_sorteio_gera_saida(args)

if __name__ == '__main__':
	main()