import Personagens


if __name__ == "__main__":
    
    print('\n')
    print('Você está em busca de aventuras e entra em uma caverna misteriosa, o clima assustador e desafiante te anima a\nentrar e descobrir o que você pode encontar...')

    dados = Personagens.criar_heroi()
    personagem = Personagens.Heroi(100, dados[0], dados[1], dados[2], dados[3], dados[4], dados[5])
    
    print()
    print(f"""[S] Seus status:
[+] Nome: {personagem.get_nome()}
[+] Vida: {personagem.get_vida()}
[+] Arma: {personagem.get_arma()}
[+] Ataque: {personagem.get_ataque()}
[+] Sorte: {personagem.get_sorte()}
[+] Defesa: {personagem.get_defesa()}
[+] Magia: {personagem.get_magia()}""")
 
    input('[ENTER]')
    
    print('\n--------- <<< LEVEL 1 >>> ---------')
    Personagens.gerar_level(personagem, 1)
    
    print('\n--------- <<< LEVEL 2 >>> ---------')
    Personagens.gerar_level(personagem, 2)
    
    print('\n --------- <<< LEVEL FINAL >>> ---------')
    Personagens.gerar_level(personagem, 3)
    
    print('\n')
    print('======================================================')
    print(f'================= VOCÊ VENCEU O JOGO =================')
    print('======================================================')

    input('[ENTER]')
