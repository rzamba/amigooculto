# -*- coding: utf-8 -*-
import unittest
from amigooculto.amigo_oculto import *

class Mockparticipantes:
    def carregaParticipantes(self):
    	lista_participantes = []
    	lista_participantes.append(Participante("paulo","paulo@amigo.com"))
    	lista_participantes.append(Participante("maria","maria@amigo.com"))
    	lista_participantes.append(Participante("joao","joao@amigo.com"))
        lista_participantes.append(Participante("jorge","jorge@amigo.com"))
        lista_participantes.append(Participante("antonio","antonio@amigo.com"))
        lista_participantes.append(Participante("pedro","pedro@amigo.com"))
        lista_participantes.append(Participante("flavio","flavio@amigo.com"))
        lista_participantes.append(Participante("luiz","luiz@amigo.com"))
        lista_participantes.append(Participante("fabiana","fabiana@amigo.com"))
        lista_participantes.append(Participante("mauro","mauro@amigo.com"))
    	return lista_participantes

class test_sorteio_modo_aleatorio(unittest.TestCase):
    def test_modo_aleatorio(self):
    	obj = Mockparticipantes()
    	lista_participantes= obj.carregaParticipantes()
    	lista_amigos = list(lista_participantes)
    	lista_resultado = sorteio_modo_aleatorio(lista_participantes,lista_amigos)
        # verifica se o tamanho da lista de resultado e igual ao tamanho da lista de amigos
    	self.assertTrue(len(lista_participantes) == len(lista_resultado))
        # verifica se cada participante não tem ele mesmo como amigo
    	for resultado in lista_resultado:
			self.assertFalse(resultado.participante.nome == resultado.amigo.nome)

class test_sorteio_modo_sem_quebra(unittest.TestCase):
    def test_modo_sem_quebra(self):
        obj = Mockparticipantes()
        lista_participantes= obj.carregaParticipantes()
        lista_amigos = list(lista_participantes)
        lista_resultado = sorteio_modo_semquebra(lista_participantes)
        # verifica se o tamanho da lista de resultado e igual ao tamanho da lista de amigos
        self.assertTrue(len(lista_amigos) == len(lista_resultado))
        primeiroparticipante = lista_resultado[len(lista_resultado)-1].participante
        resultado = lista_resultado[len(lista_resultado)-1]
        # verifica se cada participante não tem ele mesmo como amigo e se nao tem quebra
        while len(lista_resultado) > 0:
            # verifica se cada participante não tem ele mesmo como amigo
            self.assertFalse(resultado.participante.nome == resultado.amigo.nome)
            amigoeparticipante = resultado.amigo
            lista_resultado.remove(resultado)
            tem_amigo_como_participante = False
            for resultadoaux in lista_resultado:
                if resultadoaux.participante == amigoeparticipante:
                    tem_amigo_como_participante = True
                    resultado = resultadoaux

            if len(lista_resultado) > 0:
                self.assertTrue(tem_amigo_como_participante)
            else:
                self.assertTrue(primeiroparticipante.nome == amigoeparticipante.nome)

        
if __name__ == '__main__':
    unittest.main()