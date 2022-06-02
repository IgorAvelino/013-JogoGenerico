from pprint import pprint
import Personagens


dados = Personagens.criarClasse()
personagem = Personagens.Heroi(100, dados[0], dados[1], dados[2], dados[3], dados[4])

print('\nSeus status: ')
pprint(vars(personagem))
