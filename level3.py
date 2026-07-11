import pygame
import random

def level3():
    """
    Third level of the game. The player must stay on the white path, avoid guards, collect a key, and open the door.
    Returns:
        True if the player reaches the goal, False if the player loses.
    """
    # Initialize Pygame
    pygame.init()

    # Screen setup
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Level 3: Stay on the Path")

    # Load images
    map_image = pygame.image.load("Map3.png").convert()
    player_image = pygame.image.load("ninja.png")
    guard_image = pygame.image.load("alien1.png")
    key_image = pygame.image.load("key.png")
    door_image = pygame.image.load("door.png")
    cannon_image = pygame.image.load("canon1.png")
    fireball_image = pygame.image.load("fire.png")

    # Scale images
    map_image = pygame.transform.scale(map_image, (800, 600))
    player_image = pygame.transform.scale(player_image, (30, 30))
    guard_image = pygame.transform.scale(guard_image, (50, 50))
    key_image = pygame.transform.scale(key_image, (70, 70))
    door_image = pygame.transform.scale(door_image, (100, 100))
    cannon_image = pygame.transform.scale(cannon_image, (100, 100))
    fireball_image = pygame.transform.scale(fireball_image, (30, 30))

    # Set player position in the black area
    player_pos = [100, 170]
    player_rect = player_image.get_rect(topleft=player_pos)

    # Guard setup
    guards = [
        {"pos": [400, 200], "direction": 1},
        {"pos": [500, 250], "direction": -1},
    ]

    # Key setup
    key_rect = key_image.get_rect(center=(550, 400))
    key_collected = False

    # Door setup
    door_rect = door_image.get_rect(center=(700, 170))
    door_open = False

    # Cannon setup
    cannon_pos = [200, 500]
    cannon_rect = cannon_image.get_rect(topleft=cannon_pos)
    fireballs = []  # List to hold active fireballs
    fireball_speed = 7
    fireball_timer = 0

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

        if level_active:
            # Fireball mechanics
            fireball_timer += 1
            if fireball_timer > 60:  # Fire a fireball every second
                fireball_timer = 0
                fireball_start_pos = cannon_rect.midright
                fireball_direction = [player_pos[0] - fireball_start_pos[0], player_pos[1] - fireball_start_pos[1]]
                fireballs.append({"pos": list(fireball_start_pos), "direction": fireball_direction})

            # Update fireball positions
            for fireball in fireballs:
                direction = fireball["direction"]
                magnitude = (direction[0] ** 2 + direction[1] ** 2) ** 0.5
                fireball["pos"][0] += fireball_speed * (direction[0] / magnitude)
                fireball["pos"][1] += fireball_speed * (direction[1] / magnitude)

            # Remove fireballs that leave the screen
            fireballs = [f for f in fireballs if 0 <= f["pos"][0] <= 800 and 0 <= f["pos"][1] <= 600]

            # Check if any fireball hits the player
            for fireball in fireballs:
                fireball_rect = fireball_image.get_rect(center=fireball["pos"])
                if player_rect.colliderect(fireball_rect):
                    print("Hit by a fireball!")
                    pygame.quit()
                    return False

            # Update guards
            for guard in guards:
                guard["pos"][1] += guard["direction"] * 3  # Speed of guard
                if guard["pos"][1] < 100 or guard["pos"][1] > 500:
                    guard["direction"] *= -1  # Reverse direction

            # Check if the player collides with any guard
            for guard in guards:
                guard_rect = guard_image.get_rect(topleft=guard["pos"])
                if player_rect.colliderect(guard_rect):
                    print("Caught by a guard!")
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
        screen.blit(map_image, (0, 0))
        screen.blit(player_image, player_pos)

        for guard in guards:
            screen.blit(guard_image, guard["pos"])

        if not key_collected:
            screen.blit(key_image, key_rect)
        screen.blit(door_image, door_rect)
        screen.blit(cannon_image, cannon_pos)

        # Draw fireballs
        for fireball in fireballs:
            screen.blit(fireball_image, fireball["pos"])

        if not level_active:
            font = pygame.font.Font(None, 36)
            text = font.render("Click to start the level", True, (255, 255, 255))
            screen.blit(text, (200, 550))

        pygame.display.flip()
        clock.tick(30)
