from random import random

class personagem:
    def __init__(self):
        self.nome = ''
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0
    
    def __str__(self):
        return(
            f'Nome: {self.nome}\n'
            f'Força: {self.forca}\n'
            f'Destreza: {self.destreza}\n'
            f'Constituição: {self.constituicao}\n'
            f'Inteligência: {self.inteligencia}\n'
            f'Sabedoria: {self.sabedoria}\n'
            f'Carisma: {self.carisma}\n'
        )

class criador_personagem(personagem):
    def __init__(self):
        super().__init__()

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