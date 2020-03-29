###############################################
## Exercicio Programa 1 - Design de Software ##
##                                           ##
## author: @lhfaguiar                        ##
## author: @gabriellakz                      ##
###############################################

import random


def main():
    random.seed()
    game = ''
    
    while((game!=True) and (game!=False)):
        game = str(input('Vamos jogar craps? Digite S para sim e N para não: '))
        if (game=='S'):
            game = True
            continue
        elif(game=='N'):
            print('Até logo.')
            game = False
            return False
        else:
            print('Entrada inválida. Digite S para sim e N para não.')
 
    fichas = int(input('Quanto você quer apostar? Digite um número válido. '))
    
    if(fichas > 0):
        print('Você está começando com {} fichas.'.format(fichas))
        
    else:
        print('Valor inválido para aposta.')
        game = False
        
    while game:
        if (fichas == 0):
            print('Acabaram as suas fichas.')
            
        else:
            continuar = ''
            while((continuar != True) and (continuar != False)):
                print('Para apostar, digite A, para sair, digite S.')
                continuar = str(input('Apostar (A) ou sair(S)? '))
    
                if(continuar=='A'):
                    continuar = True
                    continue
                elif(continuar=='S'):
                    continuar = False
                    continue
                else:
                    print('Resposta inválida.\nDigite A ou S')
            
            if(continuar == True):
                print('Fase de Come out.')
                dado0, dado1 = lancamento_dados()
                soma = dado0 + dado1
                
                comeout = ComeOut(soma, fichas)
                
                if(comeout == 'point'):
                    point = Point(soma)
                    
                else:
                    fichas = fichas + comeout
                    
                
            else: 
                print('sair')
                
            game = False
            
            
            #come out
            
            
            #point
    main()

def ComeOut(soma, fichas):
    escolha = int(input('O que você deseja fazer? Digite o número correspondente. \n1) Pass Line Bet \n2) Field \n3) Any Craps \n4) Twelve \n5) Saldo \n6) Sair do Jogo \nValor: '))
    
    if(escolha == 1):
        print('Pass Line Bet')

        aposta = int(input('Quanto você quer apostar? '))
        
        if(aposta>0):
            if(aposta>=fichas):
                PassLineBet = pass_line_bet(soma, aposta)
                return PassLineBet
            else:
                print('Saldo insuficiente.')
                
        elif(aposta == 0):
            print('Você precisa apostar mais que zero')
        else:
            print('Valor inválido')
            
    elif(escolha == 2):
        print('Field')
        field = field()
        print('2')
        
    elif(escolha == 3):
        print('Any Craps')
        anycraps = any_craps()
        print('3')
        
    elif(escolha==4):
        print('4')

    elif(escolha == 5):
        print('5')
        
    elif(escolha==6):
        print('Saindo')
        
    else:
        print('Valor inválido.')


def Point(soma, fichas):
    
    passa_point = True
    
    while passa_point:
        novo_lancamento = lancamento_dados()
        
        if(novo_lancamento == 7):
            aposta=0
            print('Perdeu tudo no point com soma 7.')
            passa_point = False
            fichas = fichas - aposta
            
            comeout = ComeOut(novo_lancamento, aposta)
            return aposta
            
        elif(novo_lancamento == soma):
            print('venceu')
            passa_point = False
            fichas = fichas + aposta
            
            comeout = ComeOut(novo_lancamento, aposta)
            return aposta

    
def pass_line_bet(soma, aposta):
    
    if (soma==7) or (soma==11):
        print('Venceu Pass Line Bet com soma {}'.format(soma))
        aposta = aposta*2
        
    elif (soma==2) or (soma==3) or (soma==12):
        print('Perdeu com Pass Line Bet com soma {}'.format(soma))
        aposta = 0
        
    else:
        point = Point(aposta)
        return point
    
    return aposta

       
def field():
    
    print('field')


def any_craps(aposta):
    print('Any Craps')
    soma = lancamento_dados()
    
    if((soma==2) or (soma==3) or (soma==12)):
        print('Você ganhou any craps!!!')
        fichas = fichas + 7*aposta
        return fichas
    
    else:
        print('Você perdeu Any Craps')
        fichas = fichas - aposta
        return fichas
    

def twelve():
    print('Twelve')
    soma = lancamento_dados()
    
    if(soma==12):
        print('Você ganhou Twelve!!!')
        fichas = fichas + 30*aposta
        return fichas
    
    else:
        print('Você perdeu Twelve.')
        fichas = fichas - aposta
        return fichas
    
    
def lancamento_dados():
    random.seed()
    
    dado0 = random.randrange(1, 7, 1)
    dado1 = random.randrange(1, 7, 1)
    
    return dado0, dado1

main()