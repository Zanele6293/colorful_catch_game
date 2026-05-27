import pygame
import argparse
import random
import sys
import time

# Color options
COLORS = {
    "BLACK": (0,0,0),
    "RED": (255,0,0),
    "GREEN": (0,255,0),
    "BLUE": (0,0,255),
    "PURPLE": (128,0,128),
    "WHITE": (255,255,255),
    "YELLOW": (255,255,0)
}

def get_args():
    parser = argparse.ArgumentParser(description="Catch the Colors Game")
    subparser = parser.add_subparsers(dest="command", required=True)

    play_game = subparser.add_parser("Play", help="Play the game")
    play_game.add_argument("--width", type=int, default=800, help="Window width")
    play_game.add_argument("--height", type=int, default=600, help="Window height")
    play_game.add_argument("--player_speed", type=int, default=5, help="Player speed")
    play_game.add_argument("--player_color", default="PURPLE",
                           choices=list(COLORS.keys()), help="Player color")

    try:
        args = parser.parse_args()
        return args
    except SystemExit:
        print("Invalid input: please use numbers for width, height, and speed.")
        sys.exit(1)

def clamp_position(x, width, screen_width):
    """Keep player inside the window."""
    if x < 0:
        return 0
    if x > screen_width - width:
        return screen_width - width
    return x

def main():
    args = get_args()
    WIDTH, HEIGHT = args.width, args.height
    PLAYER_SPEED = args.player_speed
    PLAYER_COLOR = COLORS[args.player_color]

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Catch the Colors")

    """Player setup"""
    player_width, player_height = 100, 50
    player_x = WIDTH // 2 - player_width // 2
    player_y = HEIGHT - player_height - 10

    """Falling object setup"""
    object_radius = 20
    object_x = random.randint(0, WIDTH - object_radius)
    object_y = -object_radius
    object_color = random.choice(list(COLORS.values()))
    object_speed = 5

    score = 0
    font = pygame.font.SysFont(None, 36)

    start_time = time.time()
    Game_Duration = 30

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        """ Handle keyboard input"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            player_x += PLAYER_SPEED

        """Restrict movement"""
        player_x = clamp_position(player_x, player_width, WIDTH)

        """ Move falling object"""
        object_y += object_speed

        """ Reset object if it falls off screen"""
        if object_y > HEIGHT:
            object_x = random.randint(0, WIDTH - object_radius)
            object_y = -object_radius
            object_color = random.choice(list(COLORS.values()))

      
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        object_rect = pygame.Rect(object_x - object_radius, object_y - object_radius,
                                  object_radius*2, object_radius*2)
        if player_rect.colliderect(object_rect):
            score += 1
            """ Respawn object"""
            object_x = random.randint(0, WIDTH - object_radius)
            object_y = -object_radius
            object_color = random.choice(list(COLORS.values()))

        """Check timer"""
        elapsed_time = time.time() - start_time
        if elapsed_time >= Game_Duration:
            running = False

        """ Draw everything"""
        screen.fill(COLORS["WHITE"])
        pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, player_width, player_height))
        pygame.draw.circle(screen, object_color, (object_x, object_y), object_radius)

        """Final score"""
        score_text = font.render(f"Score: {score}", True, COLORS["BLACK"])
        screen.blit(score_text, (10, 10))

        time_left = max(0, Game_Duration - int(elapsed_time))
        timer_text = font.render(f"Time: {time_left}", True, COLORS["PURPLE"])
        screen.blit(timer_text, (WIDTH - 150, 10))

        pygame.display.flip()

    font_big = pygame.font.SysFont(None, 72)
    screen.fill(COLORS["BLACK"])
    game_over_text = font_big.render("TIME UP!", True, COLORS["RED"])
    score_text = font.render(f"Final Score: {score}", True, COLORS["WHITE"])
    screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 100))
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2))
    pygame.display.flip()

    """It will wait until user closes window"""
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False

    pygame.quit()


if __name__ == "__main__":
    main()
