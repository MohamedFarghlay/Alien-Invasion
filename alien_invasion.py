import pygame
from game_functions import update_bullets
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(screen,ai_settings)
    
    # Make a group to store bullets in.
    bullets = Group()
    
    # Start the main loop for the game 
    while True:
        gf.check_events(ai_settings, screen, ship, bullets);
        ship.update()
        update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
        
        
        

def main():
    run_game()
    
if __name__ == '__main__':
    main()
    