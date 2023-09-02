import pygame
import math
import string


pygame.init()

width, height = 900, 600
extraWidth = 300
totalWidth = width + extraWidth
oriX, oriY = width/2, height/2


font = pygame.font.SysFont('Verdana', 16)
font2 = pygame.font.SysFont('Serif', 24)

white = (150, 145, 181)
blue = (81, 66, 179)
black = (0, 0, 0)
pink = (147, 80, 171)
green = (76, 168, 100)


#Creating windows and surfaces
win = pygame.display.set_mode((width + extraWidth, height))
pygame.display.set_caption("My advanced grapher")
win.fill(black)

graph = pygame.Surface((width, height))
graph.fill(white)

def DrawLine(coord, orientation, color = green, thickness = 2):
    if orientation.lower() == 'v':
        pygame.draw.line(graph, color, (coord, 0), (coord, height), thickness)
    elif orientation.lower() == 'h':
        pygame.draw.line(graph, color, (0, coord), (totalWidth, coord), thickness)



def GraphPaper(k):
    #makes the mentioned space editable
    graph.set_clip(0, 0, width, height)

    #displaying the graph paper
    for i in range(math.floor(width / k)):
        gridX = k * i
        gridY = k * i
        pygame.draw.line(graph, blue, (gridX, 0), (gridX, height), 1) #Vertical lines
        pygame.draw.line(graph, blue, (0, gridY), (width, gridY), 1)

    #x and y axes
    midX, midY = width/(2), height/(2)
    # pygame.draw.line(win, black, (midX, 0), (midX, height), 3)
    # pygame.draw.line(win, black, (0, midY), (width, midY), 3)
    DrawLine(oriX, 'v', black, 3)
    DrawLine(oriY, 'h', black, 3)

    #border splitting the two sections
    pygame.draw.line(win, black, (width-1, 0), (width-1, height), 1 ) 


    graph.set_clip(None)



def main():
    active = True
    done = False

    # Pixels per grid
    pixPerGrid = 25
    GraphPaper(pixPerGrid)

    #Instructions
    win.blit(graph, (0,0))

    title = font2.render("Grapher", 1, pink)
    win.blit(title, (width + 10, 20))
 
    instruct = font.render("Enter the equation: ", 1, black)
    win.blit(instruct, (width + 15, 70))

    #Equations
    equations = []

    DrawLine(25, 'v')
    DrawLine(250, 'h')    

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

            elif event.type == pygame.KEYDOWN:
                
                #number keys
                if event.key == pygame.K_0:
                    equations.append("0")
                elif event.key == pygame.K_1:
                    equations.append("1")
                elif event.key == pygame.K_2:
                    equations.append("2")
                elif event.key == pygame.K_3:
                    equations.append("3")
                elif event.key == pygame.K_4:
                    equations.append("4")
                elif event.key == pygame.K_5:
                    equations.append("5")
                elif event.key == pygame.K_6:
                    equations.append("6")
                elif event.key == pygame.K_7:
                    equations.append("7")
                elif event.key == pygame.K_8:
                    equations.append("8")
                elif event.key == pygame.K_9:
                    equations.append("9")

                #unicode keys
                if event.unicode == u'*':
                    equations.append("*")
                if event.unicode == u'+':
                    equations.append("+")
                if event.unicode == u'-':
                    equations.append("-")
                if event.unicode == u'/':
                    equations.append("/")
                if event.unicode == u'.':
                    equations.append(".")
                if event.unicode == u'(':
                    equations.append("(")
                if event.unicode == u')':
                    equations.append(")")
                if event.unicode == u'^':
                    equations.append("**")

                #variable keys
                if event.key == pygame.K_x:
                    equations.append('x')

                elif event.key == pygame.K_RETURN:
                    active = False




    if done:
        # Quitting pygame
        pygame.quit()
    else:
        win.set_clip()


main()
