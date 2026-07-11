import pygame

def display_start_screen():
    """
    Displays the start screen with instructions to start the game and an image.
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Start Screen")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    author_font = pygame.font.Font(None, 28)


    image = pygame.image.load("ninja.png")  # Replace with your image file name
    smaller_image = pygame.transform.scale(image, (200, 150))

    # Texts
    title_text = font.render("Welcome to PATH OF HEROES!", True, WHITE)
    instructions_text = small_font.render("Click anywhere to start.", True, WHITE)
    author_text = author_font.render("Game made by: HADI AHSAN and JEOVANA BOTROS", True, WHITE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:  # Start game on click
                return True

        # Draw background and text
        screen.fill(BLACK)  # Black background
        screen.blit(smaller_image, (300, 50))  # Position the smaller image at (300, 50)
        screen.blit(title_text, (30, 200))  # Draw the title text
        screen.blit(instructions_text, (250, 300))  # Draw the instructions text
        screen.blit(author_text, (10, 570))  # Draw the author text

        pygame.display.flip()

def display_game_over_screen():
    """
    Displays the Game Over screen with an option to restart or quit.
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Game Over")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)

    # Texts
    game_over_text = font.render("Game Over!", True, WHITE)
    restart_text = small_font.render("Press R to Restart or Q to Quit.", True, WHITE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart game
                    return "restart"
                if event.key == pygame.K_q:  # Quit game
                    return "quit"

        # Draw background and text
        screen.fill(BLACK)
        screen.blit(game_over_text, (250, 200))
        screen.blit(restart_text, (150, 300))

        pygame.display.flip()


def display_win_screen():
    """
    Displays the win screen with a congratulatory message.
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("You Win!")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)

    # Texts
    win_text = font.render("You Win!", True, WHITE)
    quit_text = small_font.render("Press Q to Quit.", True, WHITE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Quit game
                    return "quit"

        # Draw background and text
        screen.fill(BLACK)
        screen.blit(win_text, (300, 200))
        screen.blit(quit_text, (280, 300))

        pygame.display.flip()
