###############################################
## Exercicio Programa 1 - Design de Software ##
##                                           ##
## author: @lhfaguiar                        ##
## author: @gabriellakz                      ##
###############################################

import random

def main():
    #Sorteia o aleatorio
    random.seed()
    game = ''
    
    #Comeca o jogo
    while((game!=True) and (game!=False)):
        game = str(input('Vamos jogar craps? Digite S para sim e N para não: '))
        if (game=='S'):
            game = True
            continue
        elif(game=='N'):
            #Saindo do jogo
            print('Até logo.')
            game = False
            return False
        else:
            #Verifica se entrada valida
            print('Entrada inválida. Digite S para sim e N para não.')
 
    fichas = int(input('Quanto você quer apostar? Digite um número válido. '))
    #com quantas fichas comecamos?
    
    if(fichas > 0):
        print('Você está começando com {} fichas.'.format(fichas))
        
    else:
        print('Valor inválido para aposta.')
        game = False
        
    while game:
        #Comeca o jogo
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
                #Comeca o jogo no come out
                print('Fase de Come out.')
                #sorteio dos dados
                soma = lancamento_dados()
                
                comeout = ComeOut(soma, fichas)
                
                if(comeout == 'point'):
                    point = Point(soma)
                    
                else:
                    fichas = fichas + comeout
            else: 
                print('Saindo')
                
            game = False

    main()

def ComeOut(soma, fichas):
    #implementacao das regras do come out
    jogo = True
    while(jogo):
        escolha = int(input('O que você deseja fazer? Digite o número\
             correspondente. \n1) Pass Line Bet \n2) Field \n3) Any Craps\
                  \n4) Twelve \n5) Saldo \n6) Sair do Jogo \nValor: '))
        
        if(escolha == 1):
            print('Pass Line Bet')
            valido = False
            
            while not(valido):
                aposta = int(input('Quanto você quer apostar? '))
                if(aposta > 0):
                    if(aposta >= fichas):
                        PassLineBet = pass_line_bet(soma, aposta)
                        valido = True
                        return PassLineBet
                    else:
                        print('Saldo insuficiente.')
                        
                elif(aposta == 0):
                    print('Você precisa apostar mais que zero')
                else:
                    print('Valor inválido')
                
        elif(escolha == 2):
            print('Field')
            field = field(aposta, fichas)
            
        elif(escolha == 3):
            print('Any Craps')
            anycraps = any_craps(aposta, fichas)
            
        elif(escolha==4):
            print('Twelve')
            twelve = twelve(aposta, fichas)

        elif(escolha == 5):
            print('Seu saldo é {} fichas.'.format(fichas))
            
        elif(escolha==6):
            print('Saindo')
            
        else:
            print('Valor inválido.')


    def Point(soma, fichas):
        #regras do point
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
    #implementacao pass line
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

       
def field(aposta, fichas):
    #implementacao field
    print('Field')
    soma = lancamento_dados()
    
    if (soma ==  3) or (soma == 4) or (soma == 9) or (soma == 10) or (soma == 11):
        print ('Você ganhou Field!')
        fichas = fichas + aposta
        return fichas
    elif (soma == 2):
        print ('Você ganhou Field em dobro!!')
        fichas = fichas + 2*aposta
        return fichas
    elis (soma == 12):
        print ('Você ganhou Field em triplo!!!')
        fichas = fichas + 3*aposta
        return fichas
    else:
        print ('Você perdeu Field')
        fichas = fichas - aposta
        return fichas
    


def any_craps(aposta, fichas):
    #implementa any craps
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
    

def twelve(aposta, fichas):
    #implementa twelve
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
    #sorteio dos dados
    random.seed()
    dado0 = random.randrange(1, 7, 1)
    dado1 = random.randrange(1, 7, 1)
    soma = dado0 + dado1
    return soma


main()
