import time
import pygame


class Game(object):
    def __init__(self):
        self.run()

    def loop(self):
        self.kolej = "cross"
        self.zajete = []
        self.generator = []

        self.RUNNING = True    

        self.starting_screen()

        self.RUNNING = True

        while self.RUNNING:
            
            self.key = pygame.key.get_pressed()

            if self.key[pygame.K_c]:
                self.zajete.clear()
                self.generator.clear()
                
            self.background()
            self.text()

            self.generate_lines()
            
            self.checkingWhichField()
            try:
                self.generate_sym()
            except:
                pass

            try:
                self.create()
            except:
                pass

            if self.isWin():
                self.winning_screen()

            if self.checkIfDraw():
                self.ending_screen()

            pygame.display.flip()
            self.fps()

        pygame.quit()

    def text(self):
        width = self.screen.get_width()/2-300
        height = 0
        self.font = pygame.font.SysFont('comicsans', 50)
        self.label = self.font.render(f'  To clear table: click this text and c  ', 1, "white", "red")
        self.screen.blit(self.label, (width, height)) 

    def starting_screen(self):
        self.background()

        width = self.screen.get_width()/4     
        height = self.screen.get_height()/2

        self.font = pygame.font.SysFont('comicsans', 50)

        self.label = self.font.render(f'   Who starts    ', 1, "white", "red")
        self.label2 = self.font.render(f'Click q --> cross', 1, "white", "red")
        self.label3 = self.font.render(f'Click y --> circle', 1, "white", "red")

        x = 40
        self.screen.blit(self.label, (width+52, height-x)) 
        self.screen.blit(self.label2, (width+40, height+35-x)) 
        self.screen.blit(self.label3, (width+40, height+72-x)) 

        pygame.display.flip()

        while self.RUNNING:
            self.choice = pygame.key.get_pressed()
            
            for event in pygame.event.get():
                if self.choice[pygame.K_q]:
                    self.kolej = "cross"
                    self.RUNNING = False

                elif self.choice[pygame.K_y]:
                    self.kolej = "circle"
                    self.RUNNING = False

                elif self.choice[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                    pygame.quit()


    def winning_screen(self):
        width = self.screen.get_width()/4     
        height = self.screen.get_height()/2

        self.font = pygame.font.SysFont('comicsans', 50)

        self.label = self.font.render(f'    WON {self.winner}    ', 1, "white", "red")
        self.label2 = self.font.render(f'Click y to play again', 1, "white", "red")
        self.label3 = self.font.render(f'Click q to leave', 1, "white", "red")

        x = 40
        self.screen.blit(self.label, (width+50, height-x)) 
        self.screen.blit(self.label2, (width, height+35-x)) 
        self.screen.blit(self.label3, (width+50, height+72-x)) 

        pygame.display.flip()

        while self.RUNNING:
            self.choice = pygame.key.get_pressed()
            
            for event in pygame.event.get():
                if self.choice[pygame.K_y] or self.choice[pygame.K_KP_ENTER]:
                    self.zajete = []
                    self.generator = []
                    self.run()
                    self.loop()

                elif self.choice[pygame.K_n] or self.choice[pygame.K_ESCAPE] or self.choice[pygame.K_q] or event.type == pygame.QUIT:
                    pygame.quit()

    def isWin(self):
        wygrane = [["1","2","3"],["4","5","6"],["7","8","9"],["1","4","7"],["2","5","8"],["3","6","9"],["1","5","9"],["3","5","7"]]
        
        for x in range(len(wygrane)):
            try:
                index1 = self.zajete.index(wygrane[x][0])
                index2 = self.zajete.index(wygrane[x][1])
                index3 = self.zajete.index(wygrane[x][2])
                if self.generator[index1][1] == self.generator[index2][1] and self.generator[index1][1] == self.generator[index3][1]:
                    # print(self.generator[index1][1], self.generator[index2][1], self.generator[index3][1])
                    self.winner = self.generator[index1][1]
                    print(f"winner {self.winner}")
                    return True     #if found pattern return True
        
            except:
                pass

        return False #if not found pattern return False
        


    def create(self):
        for x in range(len(self.generator)):
            if self.generator[x][1] == "circle":
                self.generate_circle(self.generator[x][0])
            elif self.generator[x][1] == "cross":
                self.generate_xyz(self.generator[x][0])

    def checkIfDraw(self):
        if len(self.generator) == 9:
            return True
        return False

    def ending_screen(self):
        self.background()

        width = self.screen.get_width()/4     
        height = self.screen.get_height()/2

        self.font = pygame.font.SysFont('comicsans', 50)

        self.label = self.font.render(f'     DRAW       ', 1, "black", "white")
        self.label2 = self.font.render(f'Click y to play again', 1, "black", "white")
        self.label3 = self.font.render(f'Click q to leave', 1, "black", "white")

        x = 40
        self.screen.blit(self.label, (width+50, height-x)) 
        self.screen.blit(self.label2, (width, height+35-x)) 
        self.screen.blit(self.label3, (width+25, height+72-x)) 

        pygame.display.flip()

        while self.RUNNING:
            self.choice = pygame.key.get_pressed()
            
            for event in pygame.event.get():
                if self.choice[pygame.K_y] or self.choice[pygame.K_KP_ENTER]:
                    self.zajete = []
                    self.generator = []
                    self.run()
                    self.loop()

                elif self.choice[pygame.K_n] or self.choice[pygame.K_ESCAPE] or self.choice[pygame.K_q] or event.type == pygame.QUIT:
                    pygame.quit()
                


    def generate_sym(self):
            if self.x >= 50 and self.x <= 190 and self.y <= 190 and self.y >= 50:
                self.zajete.append("1")
            elif self.x >= 200 and self.x <= 390 and self.y <= 190 and self.y >= 50:
                self.zajete.append("2")
            elif self.x >= 400 and self.x <= 550 and self.y <= 190 and self.y >= 50:
                self.zajete.append("3")
            elif self.x >= 50 and self.x <= 190 and self.y >= 210 and self.y <= 390:
                self.zajete.append("4")
            elif self.x >= 200 and self.x <= 390 and self.y >= 210 and self.y <= 390:
                self.zajete.append("5")
            elif self.x >= 400 and self.x <= 550 and self.y >= 210 and self.y <= 390:
                self.zajete.append("6")
            elif self.x >= 50 and self.x <= 190 and self.y >= 410 and self.y <= 550:
                self.zajete.append("7")
            elif self.x >= 200 and self.x <= 390 and self.y >= 410 and self.y <= 550:
                self.zajete.append("8")
            elif self.x >= 400 and self.x <= 550 and self.y >= 410 and self.y <= 550:
                self.zajete.append("9")
            else:
                print("Incorrect place, click the correct cell")
                return
            
            if self.zajete.count(self.zajete[-1]) > 1:
                del self.zajete[-1]
                print("zajete")
            elif self.zajete.count(self.zajete[-1]) == 1:
                self.generator.append((self.zajete[-1],self.kolej))

                if self.kolej == "circle":
                    self.kolej = "cross"
                    self.generate_circle(self.zajete[-1])
                    
                elif self.kolej == "cross":
                    self.kolej = "circle"
                    self.generate_xyz(self.zajete[-1])
  

    def generate_circle(self,wlasnosc):
        if wlasnosc=="1":
            pygame.draw.circle(self.screen, "black", [118,115], 45)
        elif wlasnosc=="2":
            pygame.draw.circle(self.screen, "black", [300,115], 45) 
        elif wlasnosc=="3":
            pygame.draw.circle(self.screen, "black", [485,115], 45)
        elif wlasnosc=="4":
            pygame.draw.circle(self.screen, "black", [118,300],45)
        elif wlasnosc=="5":
            pygame.draw.circle(self.screen, "black", [300,300],45)
        elif wlasnosc=="6":
            pygame.draw.circle(self.screen, "black", [485,300],45)
        elif wlasnosc=="7":
            pygame.draw.circle(self.screen, "black", [118,485],45)
        elif wlasnosc=="8":
            pygame.draw.circle(self.screen, "black", [300,485],45)
        elif wlasnosc=="9":
            pygame.draw.circle(self.screen, "black", [485,485],45)    

    def generate_xyz(self,wlasnosc):
        x = 50
        y = 50
        if wlasnosc=="1":
            pygame.draw.rect(self.screen, "black",pygame.Rect(118-x,115-y, 100,100))
        elif wlasnosc=="2":
            pygame.draw.rect(self.screen, "black",pygame.Rect(300-x,115-y, 100,100)) 
        elif wlasnosc=="3":
            pygame.draw.rect(self.screen, "black",pygame.Rect(485-x,115-y, 100,100))
        elif wlasnosc=="4":
            pygame.draw.rect(self.screen, "black",pygame.Rect(118-x,300-y, 100,100))
        elif wlasnosc=="5":
            pygame.draw.rect(self.screen, "black",pygame.Rect(300-x,300-y, 100,100))
        elif wlasnosc=="6":
            pygame.draw.rect(self.screen, "black",pygame.Rect(485-x,300-y, 100,100))
        elif wlasnosc=="7":
            pygame.draw.rect(self.screen, "black",pygame.Rect(118-x,485-y, 100,100))
        elif wlasnosc=="8":
            pygame.draw.rect(self.screen, "black",pygame.Rect(300-x,485-y, 100,100))
        elif wlasnosc=="9":
            pygame.draw.rect(self.screen, "black",pygame.Rect(485-x,485-y, 100,100))    

    def checkingWhichField(self):
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    print(f"x -> {event.pos[0]}") #x
                    print(f"y -> {event.pos[1]}") #y

                    self.x = event.pos[0]
                    self.y = event.pos[1]
                    time.sleep(0.05)
                    
                elif event.type == pygame.QUIT or self.key[pygame.K_ESCAPE]:
                    self.RUNNING = False

    def leaving(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT or self.key[pygame.K_ESCAPE]:
                    self.RUNNING = False

    def generate_lines(self):
        x = self.screen.get_width()/3
        y = self.screen.get_height()/3-150
        jump = 0

        for i in range(0,2):
            pygame.draw.line(self.screen, "black",[x+jump,y],[x+jump,y+500],20)
            jump += 200
        
        x = self.screen.get_width()/3-150
        y = self.screen.get_height()/3
        jump = 0 
        
        for i in range(0,2):
            pygame.draw.line(self.screen, "black",[x,y+jump],[x+500,y+jump],20)
            jump += 200

        

    def background(self):
        self.screen.fill("white")

    def run(self):
        pygame.init() #initialize application
        self.screen = pygame.display.set_mode((600, 600)) #setting resolution
        self.clock = pygame.time.Clock() #starting clock
        
        # pygame.display.toggle_fullscreen() # turning on the fullscreen
        pygame.display.set_caption("Tic Tac Toe") #setting the title of app
        # pygame.display.set_icon(pygame.image.load("pobrane.png")) #changing the icon

    def fps(self):
        self.clock.tick(45)/10000 #configurating frame rate

    def exit(self):
        pygame.quit()

App = Game()
App.loop()
