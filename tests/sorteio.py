import unittest
from amigooculto.amigo_oculto import *

class Mockparticipantes:
    def carregaParticipantes(self):
    	lista_participantes = []
    	lista_participantes.append(Participante("paulo","paulo@amigo.com"))
    	lista_participantes.append(Participante("maria","maria@amigo.com"))
    	lista_participantes.append(Participante("joao","joao@amigo.com"))
    	return lista_participantes

class test_sorteio_modo_aleatorio(unittest.TestCase):
    def test_modo_aleatorio(self):
    	obj = Mockparticipantes()
    	lista_participantes= obj.carregaParticipantes()
    	lista_amigos = list(lista_participantes)
    	lista_resultado = sorteio_modo_aleatorio(lista_participantes,lista_amigos)
    	self.assertTrue(len(lista_participantes) == len(lista_resultado))
    	for resultado in lista_resultado:
			self.assertTrue(resultado.participante.nome != resultado.amigo.nome)

class test_sorteio_modo_sem_quebra(unittest.TestCase):
    def test_modo_sem_quebra(self):
        obj = Mockparticipantes()
        lista_participantes= obj.carregaParticipantes()
        lista_amigos = list(lista_participantes)
        lista_resultado = sorteio_modo_semquebra(lista_amigos)
        self.assertTrue(len(lista_participantes) == len(lista_resultado))
        for resultado in lista_resultado:
            self.assertTrue(resultado.participante.nome != resultado.amigo.nome)
        

if __name__ == '__main__':
    unittest.main()