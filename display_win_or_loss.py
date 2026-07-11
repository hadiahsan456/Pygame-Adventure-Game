import pygame

def display_loss_screen():
    """
    Displays a simple Game Over screen.
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Game Over")

    # Font and colors
    font = pygame.font.Font(None, 74)
    text = font.render("You Lost!", True, (255, 0, 0))
    restart_text = pygame.font.Font(None, 36).render("Press R to Restart", True, (255, 255, 255))

    # Display loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit"

            # Restart the game when 'R' is pressed
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                pygame.quit()
                return "restart"

        # Draw the background and text
        screen.fill((0, 0, 0))  # Black background
        screen.blit(text, (250, 200))  # Game Over text
        screen.blit(restart_text, (250, 300))  # Restart prompt

        pygame.display.flip()

def display_win_screen():
    """
    Displays a simple You Win screen.
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("You Win!")

    # Font and colors
    font = pygame.font.Font(None, 74)
    text = font.render("You Win!", True, (0, 255, 0))
    quit_text = pygame.font.Font(None, 36).render("Press Q to Quit", True, (255, 255, 255))

    # Display loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit"

            # Quit the game when 'Q' is pressed
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                return "quit"

        # Draw the background and text
        screen.fill((0, 0, 0))  # Black background
        screen.blit(text, (250, 200))  # You Win text
        screen.blit(quit_text, (250, 300))  # Quit prompt

        pygame.display.flip()
