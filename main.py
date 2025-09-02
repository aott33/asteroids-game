# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from menu import MenuSystem

def reset_game():
    for group in [updatable, drawable, asteroids, shots]:
        group.empty()

    global asteroid_field, player
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    dt = 0

    menu_system = MenuSystem()
    
    game_state = MENU
    game_over_timer = 0.0
    score = 0

    global updatable, drawable, asteroids, shots, asteroid_field, player
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    asteroid_field = None
    player = None

    print("Starting Asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and game_state == PLAYING:
                    game_state = MENU
                    continue

            new_state = menu_system.handle_menu_input(event, game_state)

            if new_state == "QUIT":
                return
            elif new_state == PLAYING and game_state == MENU:
                reset_game()
                score = 0
            elif new_state == MENU and game_state == GAME_OVER:
                game_over_timer = 0.0

            if new_state != game_state:
                game_state = new_state


        if game_state == PLAYING:
            updatable.update(dt)

            for asteroid in asteroids:
                if player.collision(asteroid):
                    print("Game Over!")
                    game_state = GAME_OVER
                    game_over_timer = GAME_OVER_DISPLAY_TIME
                    break

                for shot in shots:
                    if asteroid.collision(shot):
                        asteroid.split()
                        shot.kill()
                        score += 100

        elif game_state == GAME_OVER:
            game_over_timer -= dt

            if game_over_timer <= 0:
                game_state = MENU

        if game_state == MENU:
            menu_system.draw_main_menu(screen)
        
        elif game_state == PLAYING:
            screen.fill("black")
            for thing in drawable:
                thing.draw(screen)
            
            font = pygame.font.Font(None,36)
            score_text = font.render(f"Score: {score}", True, "white")
            screen.blit(score_text, (10,10))

            escape_text = font.render("esc to quit", True, "white")
            screen.blit(escape_text, (SCREEN_WIDTH - 150, 10))
        
        elif game_state == GAME_OVER:
            menu_system.draw_game_over(screen, game_over_timer, score)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
