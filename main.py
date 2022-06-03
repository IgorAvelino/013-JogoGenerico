from pprint import pprint
import Personagens


dados = Personagens.criar_classe()
personagem = Personagens.Heroi(100, dados[0], dados[1], dados[2], dados[3], dados[4], dados[5])

print('\nSeus status: ')
pprint(vars(personagem))
