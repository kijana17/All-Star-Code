from random import *
gamestart = 0 #boolean variable for startscreen and play
score = 0 #variable for score value
ufox = 75 #X axis of UFO base and head
ufoy = 100 #Y axis coordinate of UFO base and head
bullets = [] #list for bullets
ufo1y = ufoy #Ufo Y coordinate for UFO 1 and so on
ufo2y = ufoy
ufo3y = ufoy
ufo4y = ufoy
ufo5y = ufoy
ufo6y = ufoy
gameover = score

def setup():
    size(700,700)
    background(0,0,0)
    for i in range(4000): #star generator for start screen
            fill(255, 255, 255)
            rect(randint(0, 700), randint(0, 700), 2.75, 2.75)
    
def draw():
    global gamestart
    global score
    global ufox
    global ufoy
    global bullets
    global ufo1y
    global ufo2y
    global ufo3y
    global ufo4y
    global ufo5y
    global ufo6y
    global gameover
    shotY = mouseY-55
    if gamestart == 0:
        #texts and buttons for start screen
        font = loadFont("Arial-BoldMT-48.vlw")
        textFont(font, 50)
        fill(39, 174, 96)
        text("Space Invaders!", 170, 300)
        textFont(font, 25)
        text("Kill all of the aliens!", 250, 350)
        fill(randint(0,255), randint(0,255), randint(0, 255))
        rect(265, 400, 200, 75)
        fill(39, 174, 96)
        textFont(font, 50)
        text("Play!", 305, 455)
        
        #Clicking play button activates game start via if statement
        if mousePressed and mouseX < 465 and mouseX > 265 and mouseY > 400 and mouseY < 475:
            shots = 0
            gamestart = 1
            
    if gamestart == 1:
        background(0, 0, 0)
        for i in range(500): #star generator for game
            fill(255, 255, 255)
            rect(randint(0, 700), randint(0, 700), 1.75, 1.75)
            
        #info bar
        fill(189, 195, 199)
        noStroke()
        infobar = rect(0, 0, 700, 50)
        font = loadFont("Arial-BoldMT-48.vlw")
        textFont(font, 25)
        fill(39, 174, 96)
        text("Score: " + str(score), 15, 35)
        fill(randint(0,255), randint(0,255), randint(0, 255))
        text("Space Invaders!", 250, 35)
        noStroke() 

        #FINAL ROCKET
    
        #top triangle
        fill(189, 195, 199)
        triangle(mouseX - 15, mouseY - 18, mouseX, mouseY - 38, mouseX + 15, mouseY - 18)
        #wide triangle
        fill(231, 76, 60)
        triangle(mouseX - 29, mouseY + 30, mouseX, mouseY + 10, mouseX + 27, mouseY + 30)
        #bottom fire triangle
        fill(243, 156, 18)
        triangle(mouseX - 9, mouseY + 30, mouseX, mouseY + 75, mouseX + 7, mouseY + 30)
        #rectangle base
        fill(255, 0, 0)
        rect(mouseX - 15, mouseY - 20,30,40)
        
        #Adds a bullet every frame for when the mouse is pressed
        if mousePressed:
            bullets.append([mouseX-2.5, shotY])
            
        #Creates a bullet for every list within the bullets list
        for i in range(0, len(bullets)):
            bullets[i][1] -= 5
            fill(236, 240, 241)
            rect(bullets[i][0], bullets[i][1], 5, 20)
    
        #Dev Check systems
        if bullets[i][1] > ufoy - 2.5 and bullets[i][1] < ufoy + 2.5:
            print("good")
            score += (1)
            gameover = score
        else:
            print("bad")
            
        #UFO 1
        if bullets[i][1] > ufoy and bullets [i][1] < ufoy + 25 and ufox <= bullets[i][0] <= ufox + 45:
            print("destroyed")
            ufo1y = 900
        else:
            fill(39, 174, 96)
            ellipse(ufox+22, ufo1y,25,25)
            rect(ufox, ufo1y,45,25,7)
        
        #UFO 2
        if bullets[i][1] > ufoy and bullets [i][1] < ufoy + 25 and ufox + 100 <= bullets[i][0] <= ufox + 145:
            print("destroyed")
            ufo2y = 900
        else:
            fill(39, 174, 96)
            ellipse(ufox+122, ufo2y,25,25)
            rect(ufox + 100, ufo2y,45,25,7)
        
        #UFO 3
        if bullets[i][1] > ufoy and bullets [i][1] < ufoy + 25 and ufox + 200 <= bullets[i][0] <= ufox + 245:
            print("destroyed")
            ufo3y = 900
        else:
            fill(39, 174, 96)
            ellipse(ufox+222, ufo3y,25,25)
            rect(ufox + 200, ufo3y,45,25,7)
        
        #UFO 4
        if bullets[i][1] > ufoy and bullets [i][1] < ufoy + 25 and ufox + 300 <= bullets[i][0] <= ufox + 345:
            print("destroyed")
            ufo4y = 900
        else:
            fill(39, 174, 96)
            ellipse(ufox+322, ufo4y,25,25)
            rect(ufox + 300, ufo4y,45,25,7)
        
        #UFO 5
        if bullets[i][1] > ufoy and bullets [i][1] < ufoy + 25 and ufox + 400 <= bullets[i][0] <= ufox + 445:
            print("destroyed")
            ufo5y = 900
        else:
            fill(39, 174, 96)
            ellipse(ufox+422, ufo5y,25,25)
            rect(ufox + 400, ufo5y,45,25,7)
        
        #UFO 6
        if bullets[i][1] > ufoy and bullets [i][1] < ufoy + 25 and ufox + 500 <= bullets[i][0] <= ufox + 545:
            print("destroyed")
            ufo6y = 900
        else:
            fill(39, 174, 96)
            ellipse(ufox+522, ufo6y,25,25)
            rect(ufox + 500, ufo6y,45,25,7)
        
        #UFO Movement
        for i in range(4):
            ufoy += 0.2
            ufo1y += 0.2
            ufo2y += 0.2
            ufo3y += 0.2
            ufo4y += 0.2
            ufo5y += 0.2
            ufo6y += 0.2
        
       #gameover screen 
    if gameover == 6:
        #gamestart = 0
        background(0,0,0)
        #texts and buttons for start screen
        font = loadFont("Arial-BoldMT-48.vlw")
        textFont(font, 50)
        fill(39, 174, 96)
        text("Game Over!", 220, 310)
        textFont(font, 25)
        text("Score: " + str(score), 295, 355)
        fill(randint(0,255), randint(0,255), randint(0, 255))
        rect(265, 400, 200, 75)
        fill(39, 174, 96)
        textFont(font, 30)
        text("Play Again!", 285, 445)
        
        #Clicking play button activates game start via if statement
        if mousePressed and mouseX < 465 and mouseX > 265 and mouseY > 400 and mouseY < 475:
            gameover = 0
            shots = 0
            gamestart = 1
            
        