# This program is the game rock,paper, and scisors
import random
import pygame
import math

pygame.init()

screen = pygame.display.set_mode((640,480))
running = True
pygame.display.set_caption("Rock, Paper, Scissors!")

hand1 = pygame.image.load('rock.png')
hand1_dimensions = hand1.get_rect()
hand1_x = 0
hand1_y = 200

hand1_paper = pygame.image.load('paper.png')
hand1_dimensions = hand1_paper.get_rect()
hand1_x = 0
hand1_y = 200

hand1_scissors = pygame.image.load('scissors.png')
hand1_dimensions = hand1_scissors.get_rect()
hand1_x = 0
hand1_y = 200

hand2_nonflipped = pygame.image.load('rock.png')
hand2 = pygame.transform.flip(hand2_nonflipped,True,False)
hand2_dimensions = hand2.get_rect()
hand2_x = 560
hand2_y = 200

hand2_nonflipped = pygame.image.load('paper.png')
hand2_paper = pygame.transform.flip(hand2_nonflipped,True,False)
hand2_dimensions = hand2_paper.get_rect()
hand2_x = 560
hand2_y = 200

hand2_nonflipped = pygame.image.load('scissors.png')
hand2_scissors = pygame.transform.flip(hand2_nonflipped,True,False)
hand2_dimensions = hand2_scissors.get_rect()
hand2_x = 560
hand2_y = 200

points = 0
possible_states = ["Rock", "Paper", "Scissors"]
def logic(a):
    global points
    comp_state = possible_states[random.randint(0,2)]    

    if a == "Rock" and comp_state == "Scissors":
        hand1_rotated = pygame.transform.rotate(hand1, 270.0)
        hand1_enlarged = pygame.transform.scale(hand1_rotated,((hand1_dimensions.width * 2.5), (hand1_dimensions.height*2.5)))
        screen.blit(hand1_enlarged, (hand1_x, hand1_y))
        hand2_rotated = pygame.transform.rotate(hand2_scissors, 360.0)
        hand2_enlarged = pygame.transform.scale(hand2_rotated,((hand2_dimensions.width * 2.5), (hand2_dimensions.height*2.5)))
        screen.blit(hand2_enlarged, (hand2_x, hand2_y))

        font= pygame.font.SysFont("Calibri", 25)
        text4 = font.render('Congratulations!', True, (0, 0, 0))
        screen.blit(text4, (250, 240))
        points+=1

    elif a == "Scissors" and comp_state == "Paper":
        hand1_rotated = pygame.transform.rotate(hand1_scissors, 0.0)
        hand1_enlarged = pygame.transform.scale(hand1_rotated,((hand1_dimensions.width * 2.5), (hand1_dimensions.height*2.5)))
        screen.blit(hand1_enlarged, (hand1_x, hand1_y))
        hand2_rotated = pygame.transform.rotate(hand2_paper, 90.0)
        hand2_enlarged = pygame.transform.scale(hand2_rotated,((hand2_dimensions.width * 2.5), (hand2_dimensions.height*2.5)))
        screen.blit(hand2_enlarged, (hand2_x, hand2_y))

        font= pygame.font.SysFont("Calibri", 25)
        text4 = font.render('Congratulations!', True, (0, 0, 0))
        screen.blit(text4, (250, 240))
        points+=1

    elif a == "Paper" and comp_state == "Rock":
        hand1_rotated = pygame.transform.rotate(hand1_paper, 270.0)
        hand1_enlarged = pygame.transform.scale(hand1_rotated,((hand1_dimensions.width * 2.5), (hand1_dimensions.height*2.5)))
        screen.blit(hand1_enlarged, (hand1_x, hand1_y))
        hand2_rotated = pygame.transform.rotate(hand2, 90.0)
        hand2_enlarged = pygame.transform.scale(hand2_rotated,((hand2_dimensions.width * 2.5), (hand2_dimensions.height*2.5)))
        screen.blit(hand2_enlarged, (hand2_x, hand2_y))

        font= pygame.font.SysFont("Calibri", 25)
        text4 = font.render('Congratulations!', True, (0, 0, 0))
        screen.blit(text4, (250, 240))
        points+=1
    else:
        font= pygame.font.SysFont("Calibri", 25)
        text4 = font.render('Uh oh!', True, (0, 0, 0))
        screen.blit(text4, (290, 240))

        if a == "Rock":
            hand1_rotated = pygame.transform.rotate(hand1, 270.0)
            hand1_enlarged = pygame.transform.scale(hand1_rotated,((hand1_dimensions.width * 2.5), (hand1_dimensions.height*2.5)))
            screen.blit(hand1_enlarged, (hand1_x, hand1_y))
        elif a == "Paper":
            hand1_rotated = pygame.transform.rotate(hand1_paper, 270.0)
            hand1_enlarged = pygame.transform.scale(hand1_rotated,((hand1_dimensions.width * 2.5), (hand1_dimensions.height*2.5)))
            screen.blit(hand1_enlarged, (hand1_x, hand1_y))
        elif a == "Scissors":
            hand1_rotated = pygame.transform.rotate(hand1_scissors, 0.0)
            hand1_enlarged = pygame.transform.scale(hand1_rotated,((hand1_dimensions.width * 2.5), (hand1_dimensions.height*2.5)))
            screen.blit(hand1_enlarged, (hand1_x, hand1_y))

        if comp_state == "Rock":
            hand2_rotated = pygame.transform.rotate(hand2, 90.0)
            hand2_enlarged = pygame.transform.scale(hand2_rotated,((hand2_dimensions.width * 2.5), (hand2_dimensions.height*2.5)))
            screen.blit(hand2_enlarged, (hand2_x, hand2_y))
        elif comp_state == "Paper":
            hand2_rotated = pygame.transform.rotate(hand2_paper, 90.0)
            hand2_enlarged = pygame.transform.scale(hand2_rotated,((hand2_dimensions.width * 2.5), (hand2_dimensions.height*2.5)))
            screen.blit(hand2_enlarged, (hand2_x, hand2_y))
        elif comp_state == "Scissors":
            hand2_rotated = pygame.transform.rotate(hand2_scissors, 360.0)
            hand2_enlarged = pygame.transform.scale(hand2_rotated,((hand2_dimensions.width * 2.5), (hand2_dimensions.height*2.5)))
            screen.blit(hand2_enlarged, (hand2_x, hand2_y))


clock = pygame.time.Clock()
clicked = False

while running:
    screen.fill("white")
    if clicked == False:
        button0_dim = pygame.Rect(250,240,100,50)
        pygame.draw.rect(screen, (255, 255, 255), button0_dim)
        pygame.draw.rect(screen, (0,0,0), button0_dim, 2)
        font= pygame.font.SysFont("Calibri", 35)
        text = font.render('START', True, (0, 0, 0))
        screen.blit(text, (255,255))
    
    else:
        font= pygame.font.SysFont("Calibri", 35)
        text0 = font.render("Points: " + str(points), True, (0,0,0))
        screen.blit(text0, (275, 0))

        button1_dim = pygame.Rect(100,400,100,50)
        pygame.draw.rect(screen, (255, 255, 255), button1_dim)
        pygame.draw.rect(screen, (0,0,0), button1_dim, 2)
        font= pygame.font.SysFont("Calibri", 35)
        text1 = font.render('Rock', True, (0, 0, 0))
        screen.blit(text1, (120,410))

        button2_dim = pygame.Rect(300,400,100,50)
        pygame.draw.rect(screen, (255, 255, 255), button2_dim)
        pygame.draw.rect(screen, (0,0,0), button2_dim, 2)
        font= pygame.font.SysFont("Calibri", 35)
        text2 = font.render('Paper', True, (0, 0, 0))
        screen.blit(text2, (310,410))

        button3_dim = pygame.Rect(500,400,100,50)
        pygame.draw.rect(screen, (255, 255, 255), button3_dim)
        pygame.draw.rect(screen, (0,0,0), button3_dim, 2)
        font= pygame.font.SysFont("Calibri", 30)
        text3 = font.render('Scissors', True, (0, 0, 0))
        screen.blit(text3, (503,410))
    
    clock.tick(2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not clicked:
                if button0_dim.collidepoint(event.pos):
                    clicked = True
            else:
                if button1_dim.collidepoint(event.pos):
                    logic("Rock")
                elif button2_dim.collidepoint(event.pos):
                    logic("Paper")
                elif button3_dim.collidepoint(event.pos):
                    logic("Scissors")

    pygame.display.flip()