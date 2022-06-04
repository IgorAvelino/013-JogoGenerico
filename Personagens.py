import math
import random
import time


class Heroi:
    def __init__(self, h_vida, h_ataque, h_sorte, h_defesa, h_magia, h_arma, h_nome) -> None:
        self.vida = h_vida
        self.ataque = h_ataque
        self.sorte = h_sorte
        self.defesa = h_defesa
        self.magia = h_magia
        self.arma = h_arma
        self.nome = h_nome
        
    # GETTERS
    def get_vida(self): return self.vida
    def get_ataque(self):return self.ataque
    def get_sorte(self): return self.sorte
    def get_defesa(self): return self.defesa
    def get_magia(self): return self.magia
    def get_arma(self): return self.arma
    def get_nome(self): return self.nome
    
    # SETTERS
    def set_vida(self, h_vida): self.vida = h_vida
    def set_ataque(self, h_ataque): self.ataque = h_ataque
    def set_sorte(self, h_sorte): self.sorte = h_sorte
    def set_defesa(self, h_defesa): self.defesa = h_defesa
    def set_magia(self, h_magia): self.magia = h_magia
    def set_arma(self, h_arma): self.arma = h_arma
    def set_nome(self, h_nome): self.nome = h_nome


def criar_heroi():
    print('--------' * 10)
    print('Com qual modo de jogo você se identifica mais?')
    time.sleep(.5)
    print('[E] Estratégico\n[L] Lutador')
    time.sleep(.5)
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
    
    time.sleep(.5)
    print('\nVamos ver sua sorte...Jogue um dado, o número será a quantidade de sorte do jogador...')
    time.sleep(.5)
    input('[Enter] -> Rolar dado')
    print('\nRolando...')
    time.sleep(2)
    sorte = random.randint(1, 10)
    print(f'\n<<< Sua sorte é {sorte} de um total de 10! >>>')

    time.sleep(.5)
    print('\n')
    print('--------' * 10)
    print('Qual arma você prefere usar?', end='')
    time.sleep(.5)
    print("""
[M] Machado
[E] Espada
[A] Arco e Flecha
[C] Cajado de Magia\n""")
    time.sleep(.5)
    op = str(input('[>>] Digite Aqui: ')).upper()
    
    while op != 'E' and op != 'A' and op != 'M' and op != 'C':
        print('<<< Opção Inválida >>>')
        op = str(input('\n[>>] Digite aqui: ')).upper()
    
    if op == 'M':
        ataque_heroi += 100
        magia_heroi = 50
        arma_heroi = 'machado'
    
    elif op == 'E':
        ataque_heroi += 100
        magia_heroi = 50
        arma_heroi = 'espada'
    
    elif op == 'A':
        ataque_heroi += 100
        magia_heroi = 50
        arma_heroi = 'arco'
    
    elif op == 'C':
        ataque_heroi += 50
        magia_heroi = 200
        arma_heroi = 'cajado'
    
    time.sleep(.5)
    print('\n')
    print('--------' * 10)
    print('Qual o seu nome heroi?')
    time.sleep(.5)
    nome_heroi = str(input('[>>] Digite seu nome: '))
    
    time.sleep(.5)
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
        i_vida = random.randint(100, 350)
        i_ataque = random.randint(30, 120)
        i_especial = random.randint(50, 170)
        i_chance = random.randint(1, 10)
        
        return Inimigo(i_vida, i_ataque, i_especial, i_chance, animal+" "+adjetivo)

    else:
        b_vida = random.randint(200, 450)
        b_ataque = random.randint(50, 200)
        b_especial = random.randint(100, 230)
        b_chance = random.randint(1, 8)
        b_super = random.randint(100, 300)
        
        return Boss(b_vida, b_ataque, b_especial, b_chance, animal+" "+adjetivo, b_super)


def ataque_inimigo(chance_acerto, valor_ataque, nome, defesa):
    time.sleep(2)
    print(f'\n<<<{nome} está se preparando para atacar!>>>')
    acerto = random.randint(0, 10)
    
    if chance_acerto >= acerto:
        time.sleep(2)
        print(f'\n<<<{nome} te acerta um golpe!>>>')
        
        if valor_ataque <= defesa:
            perda = 0
        
        else: perda = valor_ataque - defesa
        
        time.sleep(2)
        print(f'\n<<<Você perde {perda} pontos de vida deste ataque!>>>')
        return math.ceil(perda)
    
    else:
        time.sleep(2)
        print(f'\n<<<{nome} erra o golpe!>>>')
        return 0


def chance_acerto(sorte):
    acerto = random.randint(0,5)
    if sorte < acerto:
        time.sleep(2)
        return False

    else:
        time.sleep(2)
        print('\n<<< Você acerta o inimigo >>>')
        return True


def esta_morto(vida):
    if vida < 1: return True
    else: return False


def loot(sorte, personagem):
    chance_drop = random.randint(0, 5)
    if sorte < chance_drop:
        print('\n>>> Você não encontra nenhum drop desse inimigo <<<')
    
    else:
        num_tabela = random.randint(0, 3)
        lista_drops = ['ataque', 'defesa', 'magia', 'itens']
        tipo_item = lista_drops[num_tabela]
        
        arquivo = open(f"{tipo_item}.txt","r")
        linhas = arquivo.readlines()
        
        
        print('\nO inimigo deixou cair no chão...')
        
        item = random.randint(0, len(linhas)-1)
        
        linha_item = linhas[item]
        
        separar_linha_item = linha_item.split(",")
        
        nome = separar_linha_item[0]
        valor = int(separar_linha_item[1])
        
        time.sleep(2)
        print(f'[Item]>>> {nome} <<<')
        
        if tipo_item == 'ataque':
            personagem.set_ataque(personagem.get_ataque()+valor)
            time.sleep(2)
            print(f'\n<<< Seu novo Ataque é {personagem.get_ataque()} >>>')
        
        elif tipo_item == 'defesa':
            personagem.set_defesa(personagem.get_defesa()+valor)
            time.sleep(2)
            print(f'\n<<< Sua nova defesa é {personagem.get_defesa()} >>>')
        
        elif tipo_item == 'magia':
            personagem.set_magia(personagem.get_magia()+valor)
            time.sleep(2)
            print(f'\n<<< Seu novo nível de magia é {personagem.get_magia()} >>>')
        
        else:
            if separar_linha_item[2] == 'sorte':
                personagem.set_sorte(personagem.get_sorte()+valor)
                time.sleep(2)
                print(f'\n<<< Sua nova sorte vale {personagem.get_sorte()} >>>')
            
            elif separar_linha_item[2] == 'vida':
                personagem.set_vida(personagem.get_vida()+valor)
                time.sleep(2)
                print(f'\n<<< Seus pontos de vida agora são {personagem.get_vida()} >>>')
                
            elif separar_linha_item[2] == 'magia':
                personagem.set_magia(personagem.get_magia()+valor)
                time.sleep(2)
                print(f'\n<<< Seu novo nível de magia é {personagem.get_magia()} >>>')
        

def batalha(inimigo, personagem):
    print()
    print('--------' * 10)
    time.sleep(2)
    print(f'<<< {inimigo.get_nome()} está se preparando para uma batalha!! >>>')
    print()
    print(f"""Status do Inimigo:
Nome: {inimigo.get_nome()}
Vida: {inimigo.get_vida()}
Ataque {inimigo.get_ataque()}
Especial: {inimigo.get_especial()}
Chance de acerto: {inimigo.get_chance()}
Super Golpe: """, end='')
    
    try:
        print(inimigo.get_super())
    except AttributeError:
        print('Não Possui')
    
    batalha = True
    
    while batalha:
        time.sleep(.5)
        print()
        print('--------' * 10)
        print('Escolha seu ataque:')
        time.sleep(.5)
        print('[A] Arma de combate\n[C] Cajado de Magia')
        time.sleep(.5)
        op = str(input('[>>] Digite aqui: ')).upper()
        
        while op != 'A' and op != 'C':
            print('----- Opção inválida -----')
            print('Escolha seu ataque:')
            time.sleep(.5)
            print('[A] Arma de combate\n[C] Cajado de Magia')
            time.sleep(.5)
            op = str(input('\n[>>] Digite aqui: ')).upper()
            
        if op == 'A':
            dano = personagem.get_ataque()
        
        elif op == 'C':
            dano = personagem.get_magia()
        
        print(f'\n>>> Você se prepara para um ataque contra {inimigo.get_nome()}!!<<<')
        acerto = chance_acerto(personagem.get_sorte())
        
        if acerto == True:
            inimigo.set_vida(inimigo.get_vida() - dano)
            time.sleep(2)
            print(f'\n>>> {inimigo.get_nome()} está com {inimigo.get_vida()} pontos de vida! <<<')
        
        
        else:
            time.sleep(2)
            print('\n>>> Você erra o ataque <<<')
        
        inimigo_morto = esta_morto(inimigo.get_vida())
        
        if inimigo_morto == False:
            personagem.set_vida(personagem.get_vida() - ataque_inimigo(inimigo.get_chance(), inimigo.get_ataque(), inimigo.get_nome(), personagem.get_defesa()))
            
            personagem_morto = esta_morto(personagem.get_vida())
            
            if personagem_morto:
                batalha = False
                return False

            else:
                time.sleep(2)
                print(f'\n>>> A vida restante de {personagem.get_nome()} é {personagem.get_vida()}!!<<<')

        else:
            batalha = False
            time.sleep(2)
            print('\n>>> ------ Parabéns, você derrotou esse inimigo !!! -------- <<<')
            input('[ENTER]')
            loot(personagem.get_sorte(), personagem)
            
            return True
            

def fim_de_jogo(inimigo_morto=bool):
    if inimigo_morto == True:
        time.sleep(1.5)
        print('\n<< Você segue em frente em sua jornada >>')
    
    else:
        time.sleep(.5)
        print('\n<< Você foi derrotado! >>')
        time.sleep(.5)
        print('\n========== FIM DE JOGO ==========')
        time.sleep(.5)
        exit()


def gerar_level(personagem, level):
    num_max_de_inimigos = math.ceil(level * 5)
    
    for i in range(0, num_max_de_inimigos):
        chance_boss = random.randint(1,10)
        if chance_boss > 7:
            lv_boss = True
        
        else: lv_boss = False
        
        luta = batalha(gerar_inimigo(lv_boss), personagem)
        fim_de_jogo(luta)
