from pprint import pprint
import Personagens


# dados = Personagens.criar_heroi()
# personagem = Personagens.Heroi(100, dados[0], dados[1], dados[2], dados[3], dados[4], dados[5])

inimigo1 = Personagens.gerar_inimigo(False)


print(f"""Seus status:
Nome: {inimigo1.nome}
Vida: {inimigo1.vida}""")
