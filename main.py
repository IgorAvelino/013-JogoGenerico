from time import sleep
from pprint import pprint
import Personagens


dados = Personagens.criar_heroi()
personagem = Personagens.Heroi(100, dados[0], dados[1], dados[2], dados[3], dados[4], dados[5])
print('Seus status')
pprint(vars(personagem))

sleep(.5)
print('\n<<< Vamos Gerar um inimigo aleatório para voce >>>')

inimigo1 = Personagens.gerar_inimigo(False)

print('\nStatus Inimigo: ')
pprint(vars(inimigo1))
