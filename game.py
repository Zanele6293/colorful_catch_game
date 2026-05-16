import pygame
import argparse

# Color options
COLORS = {
    "BLACK": (0,0,0),
    "RED": (255,0,0),
    "GREEN": (0,255,0),
    "BLUE": (0,0,255),
    "PURPLE": (128,0,128),
    "WHITE": (255,255,255)
}

def main():
    parser = argparse.ArgumentParser(description="Let's catch the color")
    subparser = parser.add_subparsers(dest="command", required=True)

    play_game = subparser.add_parser("Play", help="Play the game")
    play_game.add_argument("--width", type=int, default=800, help="Window width")
    play_game.add_argument("--height", type=int, default=600, help="Window height")
    play_game.add_argument("--player_speed", type=int, default=5, help="Player speed")
    play_game.add_argument("--player_color", default="PURPLE",
                           choices=list(COLORS.keys()), help="Player color")

    return parser.parse_args()

pygame.init()

args = main()
WIDTH = args.width
HEIGHT = args.height
PLAYER_SPEED = args.player_speed
PLAYER_COLOR = COLORS[args.player_color]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Let's catch the Colors")

running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False

    screen.fill(COLORS["BLACK"])
    pygame.draw.rect(screen, PLAYER_COLOR, (WIDTH//2 - 50, HEIGHT - 60, 100, 50))
    pygame.display.flip()

pygame.quit()
