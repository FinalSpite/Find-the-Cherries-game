from time import sleep
import pygame
from random import randrange
import initials
import Start
import time#noqa

def get_volume():
    with open("volume.txt", "r") as volume:
        read = volume.readlines(20)
        split = read[0].removeprefix("G: ")
        return float(split)/100

def things():

    def game():
        pygame.init()


        def getRandInt():
            value1 = randrange(0, 1000)
            if value1<865 and value1 > 50 and value1 != 475:
                return value1
            else:
                value1 = randrange(0,1000)
                if value1<865 or value1 > 50 or value1 != 475:
                    return value1
                else:
                    value1 = randrange(0,1000)
                    return value1


        def HRandInt():
            value2 = randrange(0, 750)
            if value2 > 30 and value2 != 375:
                return value2
            else:
                value2 = randrange(0,750)
                if value2 > 30 and value2 != 375:
                    return value2
                else:
                    value2 = randrange(0,750)
                    return value2

        SCREEN_WIDTH = 1000
        SCREEN_HEIGHT = 800
        DIFFUCULTTY = 10
        FPS = 60

        global img
        global rect
        global rect0
        global rect1
        global rect2
        global rect3
        global rect4
        global rect5
        global rect6
        global rect7
        global rect8
        global rect9
        global rect10
        global rect11
        global rect12
        global rect13
        global rect14
        global rect15
        global rect16
        global rect17
        global rect18
        global rect19
        global rect20
        global rect21
        global rect22
        global rect23
        global rect24
        global rect25
        global rect26
        global rect27
        global rect28
        global rect29
        global rect30

        img = pygame.image.load("/Users/nightacc/Documents/VSCode Projects/Python/pygameCHERRIES/cherry.png")
        rect = img.get_rect()
        rect.center = getRandInt(),HRandInt()

        global text_font
        global clock

        text_font = pygame.font.SysFont("Trattatello", 25, bold=True)
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()


        def draw_text(text, font, text_color, x, y):
            img = font.render(text, True, text_color)
            screen.blit(img, (x, y))
        rect0 = img.get_rect()
        rect0.center = getRandInt(), HRandInt()
        rect1 = img.get_rect()
        rect1.center = getRandInt(), HRandInt()
        rect2 = img.get_rect()
        rect2.center = getRandInt(), HRandInt()
        rect3 = img.get_rect()
        rect3.center = getRandInt(), HRandInt()
        rect4 = img.get_rect()
        rect4.center = getRandInt(), HRandInt()
        rect5 = img.get_rect()
        rect5.center = getRandInt(), HRandInt()
        rect6 = img.get_rect()
        rect6.center = getRandInt(), HRandInt()
        rect7 = img.get_rect()
        rect7.center = getRandInt(), HRandInt()
        rect8 = img.get_rect()
        rect8.center = getRandInt(), HRandInt()
        rect9 = img.get_rect()
        rect9.center = getRandInt(), HRandInt()
        rect10 = img.get_rect()
        rect10.center = getRandInt(), HRandInt()
        rect11 = img.get_rect()
        rect11.center = getRandInt(), HRandInt()
        rect12 = img.get_rect()
        rect12.center = getRandInt(), HRandInt()
        rect13 = img.get_rect()
        rect13.center = getRandInt(), HRandInt()
        rect14 = img.get_rect()
        rect14.center = getRandInt(), HRandInt()
        rect15 = img.get_rect()
        rect15.center = getRandInt(), HRandInt()
        rect16 = img.get_rect()
        rect16.center = getRandInt(), HRandInt()
        rect17 = img.get_rect()
        rect17.center = getRandInt(), HRandInt()
        rect18 = img.get_rect()
        rect18.center = getRandInt(), HRandInt()
        rect19 = img.get_rect()
        rect19.center = getRandInt(), HRandInt()
        rect20 = img.get_rect()
        rect20.center = getRandInt(), HRandInt()
        rect21 = img.get_rect()
        rect21.center = getRandInt(), HRandInt()
        rect22 = img.get_rect()
        rect22.center = getRandInt(), HRandInt()
        rect23 = img.get_rect()
        rect23.center = getRandInt(), HRandInt()
        rect24 = img.get_rect()
        rect24.center = getRandInt(), HRandInt()
        rect25 = img.get_rect()
        rect25.center = getRandInt(), HRandInt()
        rect26 = img.get_rect()
        rect26.center = getRandInt(), HRandInt()
        rect27 = img.get_rect()
        rect27.center = getRandInt(), HRandInt()
        rect28 = img.get_rect()
        rect28.center = getRandInt(), HRandInt()
        rect29 = img.get_rect()
        rect29.center = getRandInt(), HRandInt()
        rect30 = img.get_rect()
        rect30.center = getRandInt(), HRandInt()
        rect31 = img.get_rect()
        rect31.center = getRandInt(), HRandInt()


        global player
        player = pygame.Rect((475, 375, 45, 45))


        rect = (
            rect0,
            rect1,
            rect2,
            rect3,
            rect4,
            rect5,
            rect6,
            rect7,
            rect8,
            rect9,
            rect10,
            rect11,
            rect12,
            rect13,
            rect14,
            rect15,
            rect16,
            rect17,
            rect18,
            rect19,
            rect20,
            rect21,
            rect22,
            rect23,
            rect24,
            rect25,
            rect26,
            rect27,
            rect28,
            rect29,
            rect30,
        )

        def get_initials():
            initial = initials.start()
            return initial
        
        def newgame(PLAYER_SCORE,SPEED):
            t0 = time.time()
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            number_of_runs = 0
            pygame.mixer.init()
            music = pygame.mixer.music
            music.load("gamelvl1.mp3")
            music.set_volume(get_volume())
            music.play(-1)
            run = True
            while run:
                
                t1 = time.time()
                time0 = t1 - t0
                time1 = round(time0, 2)
                number_of_runs += 1
                screen.fill((0, 0, 0))
                
                pygame.draw.rect(screen, (0, 255, 0), player)
                for i in range(0, DIFFUCULTTY):
                    screen.blit(img,rect[i])
                    if number_of_runs == 1:
                        pygame.display.update()
                        time.sleep(0.1)

                for i in range(0, DIFFUCULTTY):
                    if pygame.Rect.colliderect(player, rect[i]):
                        PLAYER_SCORE += 1
                        rect[i].move_ip(10000, 10000)
                        pygame.display.update()
                        player.height += 8
                        player.width += 8
                        SPEED += 1.5
                        pass
                
                draw_text("SCORE: " + str(PLAYER_SCORE), text_font, (0, 255, 0), 22, 17)
                draw_text("TIME:" + str(time1), text_font, (0, 255, 0), 858, 17)

                key = pygame.key.get_pressed()
                
                delta = SPEED
                if key[pygame.K_LEFT] is True or key[pygame.K_a] is True:
                    if player.left > 2:
                        player.x -= delta
                    else:
                        pass
                if key[pygame.K_UP] is True or key[pygame.K_w] is True:
                    if player.top > 0:
                        player.y -= delta
                    else:
                        pass
                if key[pygame.K_DOWN] is True or key[pygame.K_s] is True:
                    if player.bottom < 799:
                        player.y += delta
                    else:
                        pass
                if key[pygame.K_RIGHT] is True or key[pygame.K_d] is True:
                    if player.right < 999:
                        player.x += delta
                    else:
                        pass
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.key.get_pressed() == pygame.K_p:
                        waiting = True
                        while waiting:
                            key = pygame.key.get_pressed()
                            if key[pygame.K_p]:
                                waiting = False

                if PLAYER_SCORE == DIFFUCULTTY:
                    screen.fill((0, 0, 0))
                    print("End")
                    draw_text(
                        "YOU WIN!",
                        pygame.font.SysFont("Trattatello", 200, bold=True),
                        (0, 255, 0),
                        40,
                        150,
                    )
                    draw_text(
                        "You finished in " + str(time1) + " seconds",
                        pygame.font.SysFont("Trattatello", 50, bold=False),
                        (0, 255, 0),
                        245,
                        420,
                    )
                    with open("/Users/nightacc/Documents/VSCode Projects/Python/pygameCHERRIES/saveFile.txt", "r") as scores:
                        string = scores.read()
                        if string != "":
                            split = string.split()
                            best_time = split[0]
                        if string == "" or float(best_time) > time1:
                            initial = get_initials()
                            
                            uppercase = initial.upper()
                            with open("/Users/nightacc/Documents/VSCode Projects/Python/pygameCHERRIES/saveFile.txt", "w") as scores1:
                                scores1.write(f"{str(time1)} {uppercase}")
                            draw_text(
                                "Thats a new highscore!",
                                pygame.font.SysFont("Trattatello", 50, bold=False),
                                (0, 255, 0),
                                300,
                                490,
                            )
                            draw_text(
                                "[game will turn off in five seconds]",
                                pygame.font.SysFont("Trattatello", 50, bold=False),
                                (0, 255, 0),
                                200,
                                560,
                            )
                        else:
                            with open("/Users/nightacc/Documents/VSCode Projects/Python/pygameCHERRIES/saveFile.txt", "r") as FILE:
                                high_score = FILE.read()
                                high_score_split = high_score.split()
                            draw_text(
                                f"The highscore is {high_score_split[0]} set by {high_score_split[1]}",
                                pygame.font.SysFont("Trattatello", 50, bold=False),
                                (0, 255, 0),
                                210,
                                490,
                            )
                            draw_text(
                                "[game will turn off in five seconds]",
                                pygame.font.SysFont("Trattatello", 50, bold=False),
                                (0, 255, 0),
                                185,
                                560,
                            )
                    pygame.display.update()
                    run = False
                pygame.display.update()
                clock.tick(FPS)
                if number_of_runs == 1:
                    t0 = t1
        newgame(PLAYER_SCORE=0,SPEED=10)
        sleep(2.5)
        pygame.quit()
        sleep(1)
        Start.begin()
    game()
        
if __name__ == "__main__":
    things()