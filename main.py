import pygame
import math
import string


pygame.init()

width, height = 900, 600
extraWidth = 300

font = pygame.font.SysFont('Verdana', 16)
font2 = pygame.font.SysFont('Serif', 24)

white = (150, 145, 181)
blue = (81, 66, 179)
black = (0, 0, 0)
pink = (147, 80, 171)

win = pygame.display.set_mode((width + extraWidth, height))
pygame.display.set_caption("My advanced grapher")
win.fill(white)


def GraphPaper(k):
    #makes the mentioned space editable
    win.set_clip(0, 0, width + extraWidth, height)

    #displaying the graph paper
    for i in range(math.floor(width / k)):
        gridX = k * i
        gridY = k * i
        pygame.draw.line(win, blue, (gridX, 0), (gridX, height), 1) #Vertical lines
        pygame.draw.line(win, blue, (0, gridY), (width, gridY), 1)

    #x and y axes
    midX, midY = width/(2), height/(2)
    pygame.draw.line(win, black, (midX, 0), (midX, height), 3)
    pygame.draw.line(win, black, (0, midY), (width, midY), 3)

    #border splitting the two sections
    pygame.draw.line(win, black, (width-1, 0), (width-1, height), 1 ) 


    win.set_clip(None)

def main():
    active = True

    # Pixels per grid
    pixPerGrid = 25
    GraphPaper(pixPerGrid)

    #Instructions
    title = font2.render("Grapher", 1, pink)
    win.blit(title, (width + 10, 20))

    instruct = font.render("Enter the equation: ", 1, black)
    win.blit(instruct, (width + 15, 70))

    #Equations
    equations = []

    #Active loop
    while active:
        #update loop
        pygame.display.update()
 
        #updating screen
        win.set_clip(width + 10, height - 50, width + extraWidth, height)
        win.fill(white)

        #Join eqn array without commams
        eqn = ''
        eqn = eqn.join(equations)
        eqn = str.replace(eqn, " ", "")

        #rendering the equations
        eqnshow = font.render(" y = " + eqn, 1, black)
        win.blit(eqnshow, (width + 30, height - 50))

        # Handling events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False

    # Quitting pygame
    pygame.quit()


main()
