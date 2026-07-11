import pygame

def level1():
    """
    First level of the game. The player must stay on the white path and avoid touching the brown areas.
    Returns:
        True if the player reaches the goal, False if the player loses.
    """
    # Initialize Pygame
    pygame.init()

    # Screen setup
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Level 1: Stay on the Path")

    # Load images
    map_image = pygame.image.load("map1.png").convert()
    player_image = pygame.image.load("ninja.png")
    guard_image = pygame.image.load("alien1.png")
    door_image = pygame.image.load("door.png")  # Load the crown image

    # Scale images
    map_image = pygame.transform.scale(map_image, (800, 600))
    player_image = pygame.transform.scale(player_image, (50, 50))
    guard_image = pygame.transform.scale(guard_image, (50, 50))
    crown_image = pygame.transform.scale(door_image, (100, 100))  # Scale the crown image to match the original end zone size

    # Set player position
    player_pos = [100, 380]
    player_rect = player_image.get_rect(topleft=player_pos)

    # Guard setup
    guard_pos = [400, 300]
    guard_rect = guard_image.get_rect(topleft=guard_pos)
    guard_dir = 1  # Moving direction

    # End zone position
    end_zone = pygame.Rect(700, 100, 50, 50)  # Use the Rect for collision detection

    # Clock for frame rate
    clock = pygame.time.Clock()

    # Game variables
    running = True
    level_active = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

            # Handle mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not level_active:
                    level_active = True
                    print("Level Activated!")

        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_pos[0] -= 5
        if keys[pygame.K_RIGHT]:
            player_pos[0] += 5
        if keys[pygame.K_UP]:
            player_pos[1] -= 5
        if keys[pygame.K_DOWN]:
            player_pos[1] += 5

        # Update player rectangle
        player_rect.topleft = player_pos

        # Check if the player is within the screen boundaries
        player_pos[0] = max(0, min(player_pos[0], 800 - player_rect.width))
        player_pos[1] = max(0, min(player_pos[1], 600 - player_rect.height))

        # Check the player's current pixel color
        player_color = map_image.get_at((player_pos[0] + player_rect.width // 2, player_pos[1] + player_rect.height // 2))

        # Collision detection
        if level_active:
            # Check if the player touches the brown areas (lose condition)
            if player_color == (206, 92, 0, 255):  # Adjust this to the exact RGB value of the brown color
                print("You touched the brown area!")
                pygame.quit()
                return False

            # Check if the player collides with the guard
            guard_pos[1] += guard_dir * 5
            if guard_pos[1] < 100 or guard_pos[1] > 500:
                guard_dir *= -1  # Reverse direction
            guard_rect.topleft = guard_pos
            if player_rect.colliderect(guard_rect):
                print("Caught by the guard!")
                pygame.quit()
                return False

            # Check if the player reaches the end zone
            if player_rect.colliderect(end_zone):
                print("Level Complete!")
                pygame.quit()
                return True

        # Draw everything
        screen.blit(map_image, (0, 0))  # Draw the map
        screen.blit(player_image, player_pos)  # Draw the player
        screen.blit(guard_image, guard_pos)  # Draw the guard
        screen.blit(crown_image, end_zone.topleft)  # Draw the crown image at the end zone

        # Instructions before activating the level
        if not level_active:
            font = pygame.font.Font(None, 36)
            text = font.render("Click to start the level", True, (255, 255, 255))
            screen.blit(text, (200, 550))

        pygame.display.flip()
        clock.tick(30)  # Limit to 30 FPS
