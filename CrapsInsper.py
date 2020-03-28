###############################################
## Exercicio Programa 1 - Design de Software ##
##                                           ##
## author: @lhfaguiar                        ##
## author: @gabriellakz                      ##
###############################################

import random


def main():
    random.seed()
    print('Começa o jogo')
    game = True
    
    fichas = 9
    
    while game:
        if (fichas == 0):
            print('Acabaram as suas fichas. \nSair')
            
        else:
            continuar = 'F'
            
            while((continuar != True) and (continuar != False)):
                print('Para apostar, digite A, para sair, digite S.')
                continuar = input('Apostar (A) ou sair(S)?')
                if(continuar=='A'):
                    continuar = True
                    continue
                elif(continuar=='S'):
                    continuar = False
                    continue
                else:
                    print('Resposta inválida.\nDigite A ou S')
            
            
            
            if(continuar == True):
                print('Fase de Come out. \njogo')
                comeout = come_out()
                
                if(comeout == 'point'):
                    
                    
                    point = Point()
                
            else: 
                print('sair')
                
            game = False
            
            
            #come out
            
            
            #point


def come_out():
    print('comeout')
    

def Point():
    print('point')

    
def pass_line_bet(soma):
    
    if (soma==7) or (soma==11):
        print('Venceu')
        
    elif (soma==2) or (soma==3) or (soma==12):
        print('Perdeu')
        
    else:
        print('Point')

       
def field():
    
    print('field')


def any_craps():
    
    print('any_craps')
    

def twelve():
    
    print('twelve')
    
def lancamento_dados():
    random.seed()
    
    dado0 = random.randrange(1, 7, 1)
    dado1 = random.randrange(1, 7, 1)
    
    return dado0, dado1

main()