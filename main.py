import level1
import level2  # Import Level 2 module
import level3 #import level 3 module
import display_screen  # Import the display_screens file
import pygame
import sys

"""
This provides the overall structure of the game.

Edited for integration of start screen, multiple levels, and win/loss screens.
"""

def main():
    """
    Main game loop to call levels and handle win/loss screens.
    """
    pygame.init()

    # Show the start screen
    if not display_screen.display_start_screen():
        return  # Exit the game if the user closes the start screen

    # Loop for Level 1
    while True:
        passed_level1 = level1.level1()
        if not passed_level1:
            action = display_screen.display_game_over_screen()  # Show game over screen
            if action == "restart":
                continue  # Restart Level 1
            return  # Exit the game if the player chooses to quit

        print("Level 1 Complete!🎉🎉 Moving to Level 2...")
        break  # Exit Level 1 loop to proceed to Level 2

     #Loop for Level 2
    while True:
        passed_level2 = level2.level2()
        if not passed_level2:
            action = display_screen.display_game_over_screen()  # Show game over screen
            if action == "restart":
                continue  # Restart Level 2
            return  # Exit the game if the player chooses to quit

        print("Level 2 Complete! You Win!🎉🎉")
        break  # Exit Level 2 loop if the player completes it

        # Loop for Level 3
    while True:
            passed_level3 = level3.level3()  # Call the level3 function from level3.py

            if not passed_level3:  # If the player fails Level 3
                action = display_screen.display_game_over_screen()  # Show the game over screen

                if action == "restart":  # If the player chooses to restart
                    continue  # Restart Level 3
                return  # Exit the game if the player chooses to quit

            # If the player completes Level 3, break out of the loop
            print("Level 3 Complete! You Win!🎉🎉")
            break

#Display the win screen after all levels are completed

    # Display the win screen after both levels are completed
    action = display_screen.display_win_screen()
    if action == "quit":
        return  # Exit the game


if __name__ == "__main__":
    main()
