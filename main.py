import random

class Pet():
    cores = ('branco', 'preto', 'preto e branco', 'cinza', 'marrom', 'tricolor', 'difereciado')
    def __init__(self):                                        
        self.nome = input('Qual o nome do seu Pet? - ')
        x = random.randint(0, 6)
        self.cor = self.cores[x]
        self.fome = 100
        self.sono = 100
        self.humor = 70
        self.saude = 100
        self.dimas = 0

    def comer(self, comida):                                      
        if comida in self.comida_preferida:
            self.fome += 20
        elif comida in self.comida_envenenada:
            self.fome += 5
            self.saude -= 25
        else:
            self.fome += 10
        if self.fome > 100:
            self.fome = 100
            self.saude -= 5
        self.sono -= 10
        self.humor -= 10

    def dormir(self):                                       
        if self.sono == 100:
            self.humor -= 30
        self.sono = 100
        self.fome -= 20
        self.humor -= 15
        if self.saude < 100:
            self.saude += 5

    def jogar(self, jogo):                                      
        if jogo in self.jogo_preferido:
            self.humor += 20
            self.dimas += 1
            if self.dimas == 5:
                print('Voce ganhou !!! UUHUUUL')
            breakpoint
        else:
            self.humor += 10
        if self.humor > 100:
            self.humor = 100
            self.sono -= 25
        self.sono -= 10
        self.fome -= 15

    def Pet_morrendo(self):                                    
        if self.sono <= 0 or self.fome <= 0 or self.saude <= 0 or self.humor <= 0:
            return True
        else:
            return False

    def preferencias_Pet(self):                                    
        print('A/O {} prefere comer {} e jogar com {}, mas tome cuidado - ele pode morrer por causa de {}.'.format(
            self.nome, ', '.join(self.comida_preferida), ', '.join(self.jogo_preferido), ', '.join(self.comida_envenenada)))

    def print_status(self):                                    
        print('Como {} se sente:\n fome: {}\n sono: {}\n humor: {}\n saude: {}\n diamantes:{}'.format(
            self.nome, self.fome, self.sono, self.humor, self.saude, self.dimas))

class Gato(Pet):                                                
    comida_preferida = ['peixe', 'carne', 'leite']                   
    comida_envenenada = ['chocolate', 'lixo', 'cenoura', 'doce']
    jogo_preferido = ['ratinho de pelucia', 'laser']

class Cachorro(Pet):
    comida_preferida = ['carne', 'bone']                            
    comida_envenenada = ['chocolate', 'leite', 'cenoura', 'doce']
    jogo_preferido = ['bola', 'sapatos do dono']

class Coelho(Pet):                                             
    comida_preferida = ['lixo', 'cenoura']
    comida_envenenada = ['peixe', 'carne', 'doce']
    jogo_preferido = ['abraco', 'historinha no ouvido']

p = ''
pets_possiveis = ['gato', 'cachorro', 'coelho']                       
acoes = ['comer', 'dormir', 'jogar']                            
jogos = ['ratinho de pelucia', 'laser', 'bola', 'sapatos do dono', 'abraco', 'historinha no ouvido']
foods = ['peixe', 'carne', 'leite', 'bone', 'lixo', 'cenoura']  

while p == '' or p.lower() not in pets_possiveis:               
    p = input('Qual o tipo de Pet q voce quer? (gato, cachorro, coelho): ')

if p.lower() == 'gato':                                         
    pet = Gato()
elif p.lower() == 'cachorro':
    pet = Cachorro()
else:
    pet = Coelho()

print('Show! Voce tem um {} chamado {}! Que tem a cor {}!:)'.format(p.lower(), pet.nome, pet.cor))
pet.preferencias_Pet()

while True:
    try:
        if not pet.Pet_morrendo():                              
            
            answ = int(input('Voce quer jogar mais?\n 1 - sim\n 2 - nao\n'))
            if answ == 1:
                pet.print_status()

                
                acao = int(input('Por favor, escolha uma acao (precisa digitar um numero):\n 1 - {}\n 2 - {}\n 3 - {}\n'.format(
                    acoes[0], acoes[1], acoes[2])))

                if 1 <= acao <= 3:
                    acao = acoes[acao - 1]
                    
                    if acao == acoes[0]:
                        comida = int(input(
                            'Por favor, escolha a comida (precisa digitar um numero):\n 1 - {}\n 2 - {}\n 3 - {}\n 4 - {}\n 5 - {}\n 6 - {}\n'.format(
                                foods[0], foods[1], foods[2], foods[3], foods[4], foods[5])))

                        if 1 <= comida <= 6:
                            comida = foods[comida - 1]
                            pet.comer(comida)
                        else:
                            print('Perdao, mas voce tem que escolher entre 1 e 6, talvez  ele coma mais tarde. ;(')

                    elif acao == acoes[1]:
                        pet.dormir()

                    else:
                        jogo = int(input(
                            'Por favor, escolha o  jogo (precisa digitar um numero):\n 1 - {}\n 2 - {}\n 3 - {}\n 4 - {}\n 5 - {}\n 6 - {}\n'.format(
                                jogos[0], jogos[1], jogos[2], jogos[3], jogos[4], jogos[5])))

                        if 1 <= jogo <= 6:
                            jogo = jogos[jogo - 1]
                            pet.jogar(jogo)

                        else:
                            print('Perdao, mas voce tem que escolher entre 1 e 6, talvez  ele coma mais tarde. ;(')
                else:
                    print('Perdao, mas voce tem que escolher entre 1 e 3! ')
            elif answ == 2:
                break
        else:
            print('NAAAAO, TU MATOU O MENÒÒÒ!!! A/O {} ta no ceu agora, descanse em paz!;(\n Por favor, NAO faca isso com animais de verdade! '.format(pet.nome))
            break

    except ValueError as err:                                  
        print('Valor inserido nao valido!')