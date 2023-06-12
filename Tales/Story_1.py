import pygame


def story():
    coins = 5
    print("Hello!")
    print("press 1 - to die and 2 - for continue")
    a = int(input())
    if a == 1:
        print("Okay you are dead :)")
        return
    elif a == 2:
        print("Ok let's play")
    else:
        print("You shall not pass through this test")
        return
    print("You enter the forest and look around")
    print(
        "Person that don't have to be in the story:HELLO WOULD YOU LIKE TO BUY NEW TOURCH? IT COSTS ONLY 5 COINS!")
    print(f"You looked in your bag and saw {coins} coins")
    print("What would you do?")
    print("1 - buy it and 2 - go away")
    a = int(input())
    if a == 1:
        print("You bought it and walk in the forest")
    elif a == 2:
        print("You didin't buy it and strange man hit you with the big stone of truth")
        print("END: STONE OF TRUTH")
        return
    else:
        print("hmmm")
        return


def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True

    clock = pygame.time.Clock()
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 170, 0))

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()