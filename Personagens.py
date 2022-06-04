import math
import random
import time
import pprint


class Heroi:
    def __init__(self, h_vida, h_ataquef, h_sorte, h_defesa, h_magia, h_arma, h_nome) -> None:
        self.vida = h_vida
        self.ataquef = h_ataquef
        self.sorte = h_sorte
        self.defesa = h_defesa
        self.magia = h_magia
        self.arma = h_arma
        self.nome = h_nome
        
    # GETTERS
    def get_vida(self): return self.vida
    def get_ataquef(self):return self.ataquef
    def get_sorte(self): return self.sorte
    def get_defesa(self): return self.defesa
    def get_magia(self): return self.magia
    def get_nome(self): return self.nome
    
    # SETTERS
    def set_vida(self, h_vida): self.vida = h_vida
    def set_ataquef(self, h_ataque): self.ataquef = h_ataque
    def set_sorte(self, h_sorte): self.sorte = h_sorte
    def set_defesa(self, h_defesa): self.defesa = h_defesa
    def set_magia(self, h_magia): self.magia = h_magia
    def set_nome(self, h_nome): self.nome = h_nome


def criar_heroi():
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
    
    print('\nVamos ver sua sorte...Jogue um dado, o número será a quantidade de sorte do jogador...')
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
[C] Cajado de Magia\n""")
    op = str(input('[>>] Digite Aqui: ')).upper()
    
    while op != 'E' and op != 'A' and op != 'M' and op != 'C':
        print('<<< Opção Inválida >>>')
        op = str(input('\n[>>] Digite aqui: ')).upper()
    
    if op == 'M':
        ataque_heroi += 100
        magia_heroi = 50
        arma_heroi = 'Machado'
    
    elif op == 'E':
        ataque_heroi += 100
        magia_heroi = 50
        arma_heroi = 'Espada'
    
    elif op == 'A':
        ataque_heroi += 100
        magia_heroi = 50
        arma_heroi = 'Arco'
    
    elif op == 'C':
        ataque_heroi += 50
        magia_heroi = 200
        arma_heroi = 'Cajado'
    
    print('\n')
    print('--------' * 10)
    print('Qual o seu nome heroi?')
    nome_heroi = str(input('[>>] Digite seu nome: '))
    
    print(f'Bem vindo ao meu jogo {nome_heroi}!! Espero que aproveite!')
    
    return (ataque_heroi, sorte, defesa_heroi, magia_heroi, arma_heroi, nome_heroi)


# INIMIGO
class Inimigo:
    def __init__(self, i_vida, i_ataque, i_especial, i_chance, i_nome) -> None:
        self.vida = i_vida
        self.ataque = i_ataque
        self.especial = i_especial
        self.chance = i_chance
        self.nome = i_nome
        
    # GETTERS
    def get_vida(self): return self.vida
    def get_ataque(self): return self.ataque
    def get_especial(self): return self.especial
    def get_chance(self): return self.chance
    def get_nome(self): return self.nome
    
    # SETTERS
    def set_vida(self, i_vida): self.vida = i_vida
    def set_ataque(self, i_ataque): self.ataque = i_ataque
    def set_especial(self, i_especial): self.especial = i_especial
    def set_chance(self, i_chance): self.chance = i_chance
    def set_nome(self, i_nome): self.nome = i_nome
    
    
class Boss(Inimigo):
    def __init__(self, i_vida, i_ataque, i_especial, i_chance, i_nome, i_super) -> None:
        super().__init__(i_vida, i_ataque, i_especial, i_chance, i_nome)
        
        self.super = i_super
    
    # GETERS
    def get_super(self): return self.super
    
    # SETERS
    def set_super(self, i_super): self.super = i_super


def gerar_inimigo(lv_boss=bool):
    arquivo = open("adjetivos.txt","r")
    linhas = arquivo.readlines()
    adjetivo = linhas[random.randint(0, len(linhas)-1)][:-1]
    arquivo.close
    
    arquivo = open("animais.txt","r")
    linhas = arquivo.readlines()
    animal = linhas[random.randint(0, len(linhas)-1)][:-1]
    arquivo.close
    
    if lv_boss == False:
        i_vida = random.randint(50, 100)
        i_ataque = random.randint(1, 10)
        i_especial = random.randint(10, 20)
        i_chance = random.randint(1, 10)
        
        return Inimigo(i_vida, i_ataque, i_especial, i_chance, animal+" "+adjetivo)

    else:
        b_vida = random.randint(150, 200)
        b_ataque = random.randint(20, 40)
        b_especial = random.randint(50, 60)
        b_chance = random.randint(1, 8)
        b_super = random.randint(100, 200)
        
        return Boss(b_vida, b_ataque, b_especial, b_chance, animal+" "+adjetivo, b_super)


def ataque_inimigo(chance_acerto, valor_ataque, nome, defesa):
    print(f'\n<<<{nome} está se preparando para atacar!>>>')
    acerto = random.randint(0, 10)
    
    if chance_acerto >= acerto:
        print(f'\n<<<{nome} te acerta um golpe!>>>')
        perda = valor_ataque - defesa
        print(f'\n<<<Você perde {perda} pontos de vida deste ataque!>>>')
        return math.ceil(perda)
    
    else:
        print(f'\n<<<{nome} erra o golpe!>>>')
        return 0


def chance_acerto(sorte):
    acerto = random.randint(0,4)
    if sorte < acerto:
        print('\n<<<Você erra o ataque!>>>')
        return False

    else:
        print('\n<<<Você acerta o inimigo>>>')
        return True


def esta_morto(vida):
    if vida < 1: return True
    else: return False

