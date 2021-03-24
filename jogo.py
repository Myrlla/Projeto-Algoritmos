import pygame
from random import randrange

vermelho=(255,0,0)
preto=(0,0,0)
branco=(255,255,255)
verde=(0,255,0)
azul=(0,0,255)
verdeEscuro= (0,100,0)
cinza = (105 ,105 ,105)

pygame.init()

tam=10
largura=640
altura=520 #a altura antes era 480
placar=40


relo=pygame.time.Clock() #definir o fps
fundo=pygame.display.set_mode((largura,altura)) #fundo do jogo
pygame.display.set_caption("SNAKE") #definir o nome do jogo



    

def texto3 (m,cor,t,x,y):
    font=pygame.font.Font('fonte/fonte.ttf',t )
    texto1= font.render(m, True, cor)
    fundo.blit(texto1, [x,y])




def texto2 (m,cor,t,x,y):
    font=pygame.font.Font('fonte/Minecraft.ttf',25 )
    
    texto1= font.render(m, True, cor)
    fundo.blit(texto1, [x,y])


def texto (m,cor,t,x,y):
    font=pygame.font.Font('fonte/Minecraft.ttf',t ) #30
    
    texto1= font.render(m, True, cor)
    fundo.blit(texto1, [x,y])


def cobrinha(cobra_l): #cobra_l é a lista
    for v in cobra_l:
        pygame.draw.rect(fundo,preto,[v[0],v[1],tam,tam])

def fruta(fruta_x,fruta_y):
    pygame.draw.rect(fundo,vermelho,[fruta_x,fruta_y,tam,tam])
            


#menu
    
pygame.mixer.music.load('musica/musicaMenu.mp3')
    
pygame.mixer.music.play(-1)
    
imagemFundoMenu=pygame.image.load('imagem/tela.jpeg')
    
    
    
fimdejogo=False
sairmenu= True
maior=0

while sairmenu:
    cred=True
    regra=True




    fundo.blit(imagemFundoMenu, (0,0))

    texto("SNAKE", cinza, 30,260,30)
    texto("SNAKE", branco, 30,261,30)
        
    texto("MENU", cinza,30,265,110)
    texto("MENU", branco,30,266,110)
    pygame.draw.rect(fundo,preto, [190,250, 110,35])
    texto("Iniciar",branco,30,195,255)
    pygame.draw.rect(fundo,preto, [330,250,110,35])
    texto("Sair",branco,30,350,255) #Ajeitar tamanho
    pygame.draw.rect(fundo,preto, [250,320, 130,35])
    texto("Creditos",branco,30,255,325)

    pygame.draw.rect(fundo,preto, [250,370, 130,35])
    texto("Regras",branco,30,255,375)
        

        
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.mixer.music.stop()
                sairmenu=False


            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x= pygame.mouse.get_pos()[0]
                    y= pygame.mouse.get_pos()[1]
                    if x> 190 and y>250 and x< 300 and y< 285:


                        #AQUI COMEÇA O JOGO


                        
                        pygame.mixer.music.stop()

                        pygame.mixer.music.load('musica/musicaJogo.mp3')
                        pygame.mixer.music.play(-1)
                        sair= True
                        fimdejogo=False
                        imagemFundo=pygame.image.load('imagem/grama1.png')
                        
                        imagemGameOver=pygame.image.load('imagem/gameover.jpg')
                        pos_x=randrange(0,largura-tam,10)
                        pos_y=randrange(0,altura-tam-placar,10)
                        fruta_x=randrange(0,largura-tam,10)
                        fruta_y=randrange(0,altura-tam-placar,10)

                        vel_x=0
                        vel_y=0
                        cobra_l=[]
                        cobra_cres=1
                        pontos=0
                        while sair: #loop principal do jogo
                            
                   

                            
                            while fimdejogo:
                                pygame.mixer.music.stop( )
                                if pontos>maior:
                                    maior=pontos
                                
                                
                                for event in pygame.event.get():
                                    if event.type==pygame.QUIT:
                                        sairmenu=False
                                        sair=False
                                        fimdejogo=False
                                        pygame.mixer.music.stop()
                    
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        x= pygame.mouse.get_pos()[0]
                                        y= pygame.mouse.get_pos()[1]
                                        if x> 200 and y>180 and x< 310 and y< 215:
                                            sair= True
                                            fimdejogo=False
                                            pos_x=randrange(0,largura-tam,10)
                                            pos_y=randrange(0,altura-tam-placar,10)
                                            fruta_x=randrange(0,largura-tam,10)
                                            fruta_y=randrange(0,altura-tam-placar,10)

                                            vel_x=0
                                            vel_y=0
                                            cobra_l=[]
                                            cobra_cres=1
                                            
                                            pontos=0
                                            pygame.mixer.music.play( ) 
                                            
                                        elif x>350 and y>180 and x<460 and y<215:
                                            sair=False
                                            fimdejogo=False
                                            pygame.mixer.music.pause()
                                            
                                            
                                    
                                
                                fundo.blit(imagemGameOver, (0,0))
                                
                                texto("GAME OVER", branco,30,225,30)
                                texto("Score: "+str(pontos),branco,25,255,90)
                                texto("Recorde: "+str(maior),branco,25,235,130)
                                pygame.draw.rect(fundo,preto, [150,180, 150,35])
                                texto("Continuar",branco,30,155,185)
                                pygame.draw.rect(fundo,preto, [350,180,110,35])
                                texto("Menu",branco,30,370,185) #Ajeitar tamanho
                                pygame.display.update()
                                            
                                    
                            for event in pygame.event.get():
                                if event.type==pygame.QUIT:
                                    pygame.mixer.music.stop( )
                                    sairmenu=False
                                    sair= False
                                    
                                if event.type==pygame.KEYDOWN:
                                    if event.key==pygame.K_LEFT and vel_x != tam:
                                        vel_y=0
                                        vel_x=-tam
                                    if event.key==pygame.K_RIGHT and vel_x != -tam:
                                        vel_y=0
                                        vel_x=tam
                                    if event.key==pygame.K_UP and vel_y != tam:
                                        vel_y=-tam
                                        vel_x=0
                                    
                                    if event.key==pygame.K_DOWN and vel_y != - tam:
                                        vel_y=tam
                                        vel_x=0
                            if sair:

                                                

                            
                                fundo.blit(imagemFundo, (0,0))
                                pos_x+=vel_x
                                pos_y+=vel_y

                                if pontos<2:


                                    if pos_x == fruta_x and pos_y==fruta_y: #quando a cobra comer a maçã a maçã mudar de posição
                                        fruta_x=randrange(30,largura-tam-10,10)
                                        fruta_y=randrange(30,altura-tam-placar,10)
                                        cobra_cres+=3
                                        pontos+=1

                                if pontos==2:#and pontos<10
                                    

                                    

                                    if pos_x == fruta_x and pos_y==fruta_y: #quando a cobra comer a maçã a maçã mudar de posição
                                        fruta_x=randrange(10,largura-40,10)
                                        fruta_y=randrange(10,altura-60,10)
                                        
                                        cobra_cres+=5
                                        pontos+=1

                                    
                                    porta=pygame.draw.rect(fundo,cinza,[630,1,tam,520])
                                    parede=pygame.draw.rect(fundo,cinza,[0,1,tam,520])
                                    

                                   
                                    
                                    if pos_x >= 620 and pos_y>=1 or pos_x<=10 and pos_y>=1: #quando a cobra bater na parede
                                        fimdejogo=True


                                if pontos>=3 and pontos<5:# and pontos<15:
                                    

                                    if pos_x == fruta_x and pos_y==fruta_y: #quando a cobra comer a maçã a maçã mudar de posição
                                        fruta_x=randrange(30,largura-tam-30,10)
                                        fruta_y=randrange(30,altura-tam-placar-30,10)
                                        cobra_cres+=5
                                        pontos+=1

                                        
                                    porta=pygame.draw.rect(fundo,cinza,[630,1,tam,520])
                                    parede=pygame.draw.rect(fundo,cinza,[0,1,tam,520])
                                    porta1=pygame.draw.rect(fundo,cinza,[1,470,640,tam])
                                    porta1=pygame.draw.rect(fundo,cinza,[1,0,640,tam])
                                    

                                    if pos_x >= 620 and pos_y>=1 or pos_x<=10 and pos_y>=1 or pos_x>=1 and pos_y>=460 or pos_x>=1 and pos_y<=10: #quando a cobra bater na parede
                                            fimdejogo=True




                                if pontos>=5:
                                    

                                    if pos_x == fruta_x and pos_y==fruta_y: #quando a cobra comer a maçã a maçã mudar de posição
                                        fruta_x=randrange(40,largura-tam-40,10)
                                        fruta_y=randrange(40,altura-tam-placar-40,10)
                                        cobra_cres+=5
                                        pontos+=1

                                        
                                    porta=pygame.draw.rect(fundo,cinza,[610,1,30,520])
                                    parede=pygame.draw.rect(fundo,cinza,[0,1,30,520])
                                    porta1=pygame.draw.rect(fundo,cinza,[1,450,640,30])
                                    porta1=pygame.draw.rect(fundo,cinza,[1,0,640,30])
                                    

                                    if pos_x >= 600 and pos_y>=1 or pos_x<=30 and pos_y>=1 or pos_x>=1 and pos_y>=440 or pos_x>=1 and pos_y<=30: #quando a cobra bater na parede
                                        fimdejogo=True
                                        

                                

                                

                                
                                if pos_x + tam >largura:
                                    pos_x=0
                                if pos_x<0:
                                    pos_x=largura-tam
                                if pos_y + tam>altura-placar:
                                    pos_y=0
                                if pos_y<0:
                                    pos_y=altura-tam-placar
                                
                                
                                cobra_cabeca=[]
                                cobra_cabeca.append(pos_x) 
                                cobra_cabeca.append(pos_y)
                                cobra_l.append(cobra_cabeca)
                                if len(cobra_l)>cobra_cres:
                                    del cobra_l[0]

                                if any(bloco==cobra_cabeca for bloco in cobra_l[:-1]):
                                       fimdejogo = True

                                pygame.draw.rect(fundo,preto,[0,altura-placar,largura,placar])
                                texto("Pontos: "+str(pontos), branco, 20, 10,altura-30)
                               

                                
                                
                                cobrinha(cobra_l)
                                    
                                    
                                    
                                fruta(fruta_x,fruta_y)

                            
                                if pontos<5:
                                    relo.tick(12)
                                elif pontos>=5 and pontos<10:
                                    relo.tick(15)
                                
                                    
                                elif pontos>=10 and pontos<15:
                                    relo.tick(17)

                                elif pontos>=15 and pontos<20:
                                    relo.tick(20)
                                elif pontos>=20:
                                    relo.tick(25)
                                
                            
                            
                            
                                pygame.display.update()









                        
                        
                        pygame.mixer.music.load('musica/musicaMenu.mp3')
                        pygame.mixer.music.play(-1)


                    elif x>250 and y>320 and x<380 and y<355:


                        #AQUI OS CREDITOS

                        

                        imagemCreditos=pygame.image.load('imagem/creditos.jpg')

                        while cred:

                            fundo.blit(imagemCreditos, (0,0))


                            
                            texto3("Programadora: Myrlla Lucas Pereira", branco,25, 101, 50)
                            
                            texto3("Disciplina: Algoritmos e Programação", branco,25, 101, 100)
                            
                            texto3("Versao Python: 3.6 ", branco,25, 101, 150)
                            
                            pygame.draw.rect(fundo,preto, [50,470, 80,35])
                            texto2("Menu", branco,25, 55, 475)

                            for event in pygame.event.get():
                                if event.type==pygame.QUIT:
                                        sairmenu=False
                                        cred=False
                                        
                                    
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                    x= pygame.mouse.get_pos()[0]
                                    y= pygame.mouse.get_pos()[1]
                                    if x> 50 and y>470 and x< 140 and y<505:
                                        
                                        cred=False



        



                            pygame.display.update()
                        
                            

                    elif x>250 and y>370 and x<380 and y<405:

                        #AQUI AS REGRAS
                        

                        imagemRegra=pygame.image.load('imagem/regra.jpg')

                        while regra:

                            for event in pygame.event.get():
                                if event.type==pygame.QUIT:
                                    sairmenu=False
                                    regra=False
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                    x= pygame.mouse.get_pos()[0]
                                    y= pygame.mouse.get_pos()[1]
                                    if x> 50 and y>470 and x< 140 and y<505:
                                        
                                        regra=False


                            fundo.blit(imagemRegra, (0,0))

                            texto3("REGRAS", branco,30, 150, 20)

                            
                            texto3("1- Se a cobra encostar nela mesma, você perde o jogo", branco,15, 20, 110)
                            texto3("2- A medida que sua pontuação for aumentando, obstaculos irão surgir", branco,15, 20, 150)
                            texto3("3- Não encoste nas bordas que irão aparecer, será fatal", branco,15, 20, 190)
                            texto3("4- Sua pontuação subiu? Sua cobra ficará mais veloz", branco,15, 20, 230)
                            
                            
                            pygame.draw.rect(fundo,preto, [50,470, 80,35])
                            texto2("Menu", branco,20, 55, 475)

                            pygame.display.update()

                               
                    elif x>350 and y>250 and x<460 and y<285:
                        pygame.mixer.music.stop()
                        sairmenu=False
                        


                        


        
    
        



    pygame.display.update()


        
      
pygame.quit()
  

