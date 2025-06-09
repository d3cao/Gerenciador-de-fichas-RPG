class ficha_interativa:
    def __init__(self, personagem):
        self.personagem = personagem
    
    def mostrar_fic(self):
        def status(termo, status):
            print('|' + f'{termo} : {status}'.ljust(33) + '|')
            print('-'*35)
        
        def atributos(atributos):
            for item in atributos:
                print('|'+ f'{item[0]} : {item[1]}'.ljust(33) +'|')

        print('-'*35)
        status('Nome', self.personagem.nome)
        status('Força', self.personagem.forca)
        status('Destreza', self.personagem.destreza)
        status('Constituição', self.personagem.constituicao)
        status('Inteligência', self.personagem.inteligencia)
        status('Sabedoria', self.personagem.sabedoria)
        status('Carisma', self.personagem.carisma)
        atributos(self.personagem.pericias)
        print('-'*35)