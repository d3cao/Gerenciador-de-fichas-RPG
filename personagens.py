from random import random

class personagem:
    def __init__(self):
        self.nome = ''
        self.pericias = [
            ['Atletismo', 0],
            ['Acrobacia', 0],
            ['Furtividade', 0],
            ['Prestigitação', 0],
            ['Arcanismo', 0],
            ['Historia', 0],
            ['Investigação', 0],
            ['Natureza', 0],
            ['Religião', 0],
            ['Adestrar Animais', 0],
            ['Intuição', 0],
            ['Medicina', 0],
            ['Percepção', 0],
            ['Sobrevivência', 0],
            ['Atuação', 0],
            ['Enganação', 0],
            ['Intimidação', 0],
            ['Persuação', 0]
        ]
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0

    def __str__(self):
        texto = (
            f'Nome: {self.nome}\n'
            f'Força: {self.forca}\n'
            f'Destreza: {self.destreza}\n'
            f'Constituição: {self.constituicao}\n'
            f'Inteligência: {self.inteligencia}\n'
            f'Sabedoria: {self.sabedoria}\n'
            f'Carisma: {self.carisma}\n'
        )
        return texto

class criador_personagem(personagem):
    def __init__(self):
        super().__init__()
        self.racas = {
            'Humano' : self.humano
        }

    def __str__(self):
        return super().__str__()

    def definir_atributos(self):
        valores = self.roll()
        print(f'Os valores disponiveis são:', end=' ')
        print(', '.join(f'{num}' for num in valores))
        self.nome = input('Nome: ')
        self.forca = int(input('Força: '))
        self.destreza = int(input('Destreza: '))
        self.constituicao = int(input('Constituição: '))
        self.inteligencia = int(input('Inteligência: '))
        self.sabedoria = int(input('Sabedoria: '))
        self.carisma = int(input('Carisma: '))

    def roll(self):
        valores = []
        for _ in range(6):
            lista = []
            for _ in range(4):
                lista.append(int((random()*6)+1))
            lista = sorted(lista)
            lista.remove(lista[0])
            valores.append(sum(lista))
        return valores
    
    def humano(self):
        self.forca += 1; self.destreza += 1; self.constituicao += 1; self.inteligencia += 1; self.sabedoria += 1; self.carisma += 1