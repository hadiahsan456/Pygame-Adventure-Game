import pygame

def level2():
    """
    Second level of the game. The player must stay on the white path, avoid guards, collect a key, and open the door.
    Returns:
        True if the player reaches the goal, False if the player loses.
    """
    # Initialize Pygame
    pygame.init()

    # Screen setup
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Level 2: Stay on the Path")

    # Load images
    map_image = pygame.image.load("map2 2.png").convert()
    player_image = pygame.image.load("ninja.png")
    guard_image = pygame.image.load("alien1.png")
    key_image = pygame.image.load("key.png")  # Load the key image
    door_image = pygame.image.load("door.png")  # Load the door image

    # Scale images
    map_image = pygame.transform.scale(map_image, (980, 747))
    player_image = pygame.transform.scale(player_image, (50, 50))
    guard_image = pygame.transform.scale(guard_image, (50, 50))
    key_image = pygame.transform.scale(key_image, (70, 70))
    door_image = pygame.transform.scale(door_image, (100, 80))

    # Set player position in the black area
    player_pos = [100, 100]
    player_rect = player_image.get_rect(topleft=player_pos)

    # Guard setup
    guards = [
        {"pos": [400, 200], "direction": 1},
        {"pos": [500, 250], "direction": -1},
    ]
    guard_rects = [guard_image.get_rect(topleft=guard["pos"]) for guard in guards]

    # Key setup
    key_rect = key_image.get_rect(center=(550, 400))
    key_collected = False

    # Door setup
    door_rect = door_image.get_rect(center=(700, 170))
    door_open = False

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
            if event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse clicks
                if not level_active:
                    level_active = True  # Start the level when clicked
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

        # Collision detection
        if level_active:
            # Check if the player touches the brown areas (lose condition)
            player_color = map_image.get_at((player_pos[0] + player_rect.width // 2, player_pos[1] + player_rect.height // 2))
            if player_color == (206, 92, 0, 255):  # Adjust this to the exact RGB value of the brown color
                print("You touched the brown area!")
                pygame.quit()
                return False

            # Check if the player collides with any guard
            for i in range(len(guards)):
                guard = guards[i]  # Get the guard dictionary
                guard_rect = guard_rects[i]  # Get the corresponding Rect object

                # Update the guard's position
                guard["pos"][1] += guard["direction"] * 5  # Changed "dir" to "direction"
                if guard["pos"][1] < 100 or guard["pos"][1] > 500:
                    guard["direction"] *= -1  # Reverse direction

                # Update the guard's rectangle position
                guard_rect.topleft = guard["pos"]

                # Check for collision with the player
                if player_rect.colliderect(guard_rect):
                    print("Caught by the guard!")
                    pygame.quit()
                    return False

            # Check if the player collects the key
            if not key_collected and player_rect.colliderect(key_rect):
                key_collected = True
                print("Key Collected!")

            # Check if the player opens the door
            if key_collected and player_rect.colliderect(door_rect):
                door_open = True

            # Check if the player reaches the end zone
            if door_open and player_rect.colliderect(door_rect):
                print("Level Complete!")
                pygame.quit()
                return True

        # Draw everything
        screen.blit(map_image, (0, 0))  # Draw the map
        screen.blit(player_image, player_pos)  # Draw the player

        # Draw guards
        for guard_rect in guard_rects:
            screen.blit(guard_image, guard_rect.topleft)

        # Draw the key if it hasn't been collected
        if not key_collected:
            screen.blit(key_image, key_rect)

        # Draw the door
        screen.blit(door_image, door_rect)

        # Instructions before activating the level
        if not level_active:
            font = pygame.font.Font(None, 36)
            text = font.render("Click to start the level", True, (255, 255, 255))
            screen.blit(text, (200, 550))

        pygame.display.flip()
        clock.tick(30)  # Limit to 30 FPS
