import random
import time
import pprint


class Heroi:
    def __init__(self, h_vida, h_ataquef, h_sorte, h_defesa, h_magia, h_nome) -> None:
        self.vida = h_vida
        self.ataquef = h_ataquef
        self.sorte = h_sorte
        self.defesa = h_defesa
        self.magia = h_magia
        self.nome = h_nome
        
        # GETTERS
        def getVida(): return self.vida
        def getAtaquef():return self.ataquef
        def getSorte(): return self.sorte
        def getDefesa(): return self.defesa
        def getMagia(): return self.magia
        def getNome(): return self.nome
        
        # SETTERS
        def setVida(self, h_vida): self.vida = h_vida
        def setAtaquef(self, h_ataque): self.ataquef = h_ataque
        def setSorte(self, h_sorte): self.sorte = h_sorte
        def setDefesa(self, h_defesa): self.defesa = h_defesa
        def setMagia(self, h_magia): self.magia = h_magia
        def setNome(self, h_nome): self.nome = h_nome


def criarClasse():
    print('--------' * 10)
    print('Com qual modo de jogo você se identifica mais?')
    print('[E] Estratégico\n[L] Lutador')
    op = str(input('\n[>>] Digite aqui: ')).upper()

    while op != 'E' and op != 'L':
        print('<<< Opção Inválida >>>')
        op = str(input('\n[>>] Digite aqui: ')).upper()
    
    if op == "E":
        ataque_heroi = 50
        defesa_heroi = 100
    
    elif op == "L":
        ataque_heroi = 100
        defesa_heroi = 50
    
    print('\nVamos ver sua sorte...\nJogue um dado, o número será a quantidade de sorte do jogador...')
    input('[Enter] -> Rolar dado')
    print('\nRolando...')
    time.sleep(.5)
    sorte = random.randint(1, 10)
    print(f'\n<<< Sua sorte é {sorte} de um total de 10! >>>')

    print('\n')
    print('--------' * 10)
    print('Qual arma você prefere usar?', end='')
    print("""
    [M] Machado
    [E] Espada
    [A] Arco e Flecha
    [C] Cajado de Magia""")
    op = str(input('[>>] Digite Aqui: ')).upper()
    
    while op != 'E' and op != 'A' and op != 'M' and op != 'C':
        print('<<< Opção Inválida >>>')
        op = str(input('\n[>>] Digite aqui: ')).upper()
    
    if op == 'M' or op == 'E' or op == 'A':
        ataque_heroi += 100
        magia_heroi = 50
    
    elif op == 'C':
        ataque_heroi += 50
        magia_heroi = 200
    
    print('\n')
    print('--------' * 10)
    print('Qual o seu nome heroi?')
    nome_heroi = str(input('[>>] Digite seu nome: '))
    
    print(f'Bem vindo ao meu jogo {nome_heroi}!! Espero que aproveite!')
    
    return (ataque_heroi, sorte, defesa_heroi, magia_heroi, nome_heroi)
    