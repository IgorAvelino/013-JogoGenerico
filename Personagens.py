class Heroi:
    def __init__(self, h_vida, h_ataque, h_sorte, h_defesa, h_magia, h_nome) -> None:
        self.vida = h_vida
        self.ataque = h_ataque
        self.sorte = h_sorte
        self.defesa = h_defesa
        self.magia = h_magia
        self.nome = h_nome
        
        # GETTERS
        def getVida(): return self.vida
        def getAtaque():return self.ataque
        def getSorte(): return self.sorte
        def getDefesa(): return self.defesa
        def getMagia(): return self.magia
        def getNome(): return self.nome
        
        # SETTERS
        def setVida(self, pt_vida): self.vida = pt_vida
        
        