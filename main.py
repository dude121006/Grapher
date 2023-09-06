import pygame
import math
import string


pygame.init()

width, height = 900, 600
extraWidth = 300
totalWidth = width + extraWidth
oriX, oriY = width / 2, height / 2


pixPerGrid = 50
font = pygame.font.SysFont("Verdana", 16)
font2 = pygame.font.SysFont("Serif", 24)

white = (150, 145, 181)
blue = (81, 66, 179)
black = (0, 0, 0)
pink = (147, 80, 171)
green = (76, 168, 100)
transparent = (0, 0, 0)


# Creating windows and surfaces
win = pygame.display.set_mode(
    (width + extraWidth, height),
)
pygame.display.set_caption("My advanced grapher")
win.fill(white)

graph = pygame.Surface((width, height))
graph.fill(white)


def Eval(eqn):

    #if 'x' in eqn:
        for x in range(-width, math.floor(width), 1):

            try:
                y = eval(eqn)
                print("x: ", x, "  y: ", y)
                rect = ((x + width/2, -y + height/2), (2, 2))
                pygame.draw.rect(graph, green, rect)

            except Exception as e:
                print("Eval exception: ", e)
                
        


def DrawLine(coord, slope, color=green, thickness=3):
    if slope.lower() == "v":
        pygame.draw.line(graph, color, (coord, 0), (coord, height), thickness)

    elif slope.lower() == "h":
        pygame.draw.line(graph, color, (0, coord), (totalWidth, coord), thickness)


def DrawGraph(k):
    # makes the mentioned space editable
    win.set_clip(0, 0, width, height)

    # displaying the graph paper
    for i in range(math.floor(width / k)):
        gridX = k * i
        gridY = k * i
        pygame.draw.line(win, blue, (gridX, 0), (gridX, height), 1)  # Vertical lines
        pygame.draw.line(win, blue, (0, gridY), (width, gridY), 1)

    # x and y axes
    midX, midY = width / (2), height / (2)

    pygame.draw.line(win, black, (midX, 0), (midX, height), 3)
    pygame.draw.line(win, black, (0, midY), (width, midY), 3)
    # DrawLine(oriX, 'v', black, 3)
    # DrawLine(oriY, 'h', black, 3)

    # border splitting the two sections
    pygame.draw.line(win, black, (width - 1, 0), (width - 1, height), 1)

    win.set_clip(None)


def RenderEquations(equations):
    # updating screen
    win.set_clip(width + 10, height - 50, width + extraWidth, height)
    win.fill(white)

    # Join eqn array without commams
    eqn = "".join(equations)
    # eqn = str.replace(eqn, " ", "")

    # rendering the equations
    eqnshow = font.render(" y = " + eqn, 1, black)
    win.blit(eqnshow, (width + 30, height - 50))

    win.set_clip(None)

    return eqn


def RenderInstructions():
    # Instructions
    title = font2.render("Grapher", 1, pink)
    win.blit(title, (width + 10, 20))

    instruct = font.render("Enter the equation: ", 1, black)
    win.blit(instruct, (width + 15, 70))


def main():
    active = True
    done = False

    RenderInstructions()

    # Equations
    equations = []

    # Active loop
    while active:
        # update loop
        pygame.display.update()

        win.blit(graph, (0, 0))

        eqn = RenderEquations(equations)
        DrawGraph(pixPerGrid)
 
        graph.fill(white)

        # Handling events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False

            elif event.type == pygame.KEYDOWN:
                # number keys
                if event.key == pygame.K_KP_0 or event.key == pygame.K_0:
                    equations.append("0")
                elif event.key == pygame.K_KP_1 or event.key == pygame.K_1:
                    equations.append("1")
                elif event.key == pygame.K_KP_2 or event.key == pygame.K_2:
                    equations.append("2")
                elif event.key == pygame.K_KP_3 or event.key == pygame.K_3:
                    equations.append("3")
                elif event.key == pygame.K_KP_4 or event.key == pygame.K_4:
                    equations.append("4")
                elif event.key == pygame.K_KP_5 or event.key == pygame.K_5:
                    equations.append("5")
                elif event.key == pygame.K_KP_6 or event.key == pygame.K_6:
                    equations.append("6")
                elif event.key == pygame.K_KP_7 or event.key == pygame.K_7:
                    equations.append("7")
                elif event.key == pygame.K_KP_8 or event.key == pygame.K_8:
                    equations.append("8")
                elif event.key == pygame.K_KP_9 or event.key == pygame.K_9:
                    equations.append("9")
                elif event.key == pygame.K_BACKSPACE:
                    equations.pop()

                # unicode keys
                if event.key == pygame.K_KP_MULTIPLY or event.key == pygame.K_QUOTE:
                    equations.append("*")
                if event.key == pygame.K_KP_PLUS or event.key == pygame.K_EQUALS:
                    equations.append("+")
                if event.key == pygame.K_KP_MINUS or event.key == pygame.K_MINUS:
                    equations.append("-")
                if event.key == pygame.K_KP_DIVIDE or event.key == pygame.K_SLASH:
                    equations.append("/")
                if event.key == pygame.K_KP_PERIOD or event.key == pygame.K_PERIOD:
                    equations.append(".")
                if event.key == pygame.K_LEFTBRACKET:
                    equations.append("(")
                if event.key == pygame.K_RIGHTBRACKET:
                    equations.append(")")
                if event.key == pygame.K_CARET:
                    equations.append("**")

                # variable keys
                if event.key == pygame.K_x:
                    equations.append("x")

                elif event.key == pygame.K_RETURN:
                    active = False

        pygame.display.flip()

        try:
            #result = eval(eqn)
            Eval(eqn)
            #DrawLine(result, "h")
        except Exception as e:
            print(e)

    if done:
        # Quitting pygame
        pygame.quit()
    else:
        win.set_clip()


main()


