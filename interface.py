import personagens
import os
import json

class interface:
    def __init__(self):
        self.info = []
        self.caracters = []
        self.opção = {
            1 : self.criar_personagem,
            2 : self.mostrar_ficha,
            3 : self.salvar_personagens,
            4 : self.exit
        }

    def load(self):
        if os.path.exists('personagens.json'):
            try:
                with open('personagens.json', 'r') as arquivo:
                    dados = json.load(arquivo)
                
                for escolhido in dados:
                    personagem = personagens.criador_personagem()
                    personagem.nome = escolhido['Nome']
                    personagem.forca = escolhido['Força']
                    personagem.destreza = escolhido['Destreza']
                    personagem.constituicao = escolhido['Constituicao']
                    personagem.inteligencia = escolhido['Inteligencia']
                    personagem.sabedoria = escolhido['Sabedoria']
                    personagem.carisma = escolhido['Carisma']
                    self.caracters.append(personagem)
            except json.JSONDecodeError:
                print('Erro ao carregar os personagens')

    def transform(self):
        for escolhido in self.caracters:
            dados = {
                'Nome' : escolhido.nome,
                'Força' : escolhido.forca,
                'Destreza' : escolhido.destreza,
                'Constituicao' : escolhido.constituicao,
                'Inteligencia' : escolhido.inteligencia,
                'Sabedoria' : escolhido.sabedoria,
                'Carisma' : escolhido.carisma
            }
            self.info.append(dados)
        

    def salvar_personagens(self):
        self.transform()
        dados = self.info
        try :
            with open('personagens.json', 'w') as arquivo:
                json.dump(dados, arquivo, indent=4)
        except json.JSONDecodeError:
            print('Erro ao salvar os personagens')

    def exit(self):
        print('Até mais...')

    def retorno(self):
        input('Digite uma tecla para voltar ao menu...')
        self.iniciar()

    def mostrar_ficha(self):
        valor = int(input('Digite o valor do personagem para checagem (a partir do 0): '))
        print(self.caracters[valor])
        self.retorno()

    def criar_personagem(self):
        maker = personagens.criador_personagem()
        os.system('clear')
        print('Bem-vindo ao criador de personagem')
        print('-'*34)
        maker.definir_atributos()
        self.caracters.append(maker)
        self.retorno()

    def iniciar(self):
        os.system('clear')
        print('Seja bem vindo jogador!')
        print()
        print('Qual a opção desejada ?')
        print('1 - Criar personagem')
        print('2 - Ver fichas')
        print('3 - Salvar personagens')
        print('3 - Finalizar o programa')
        valor = int(input())
        valor = self.opção.get(valor)
        if valor:
            valor()
        else :
            print('opção invalida')
            interface.iniciar()


frame = interface()

if __name__ == "__main__":
    frame.load()
    frame.iniciar()