"""Project #2: Hangman Details:
Have you ever played hangman? It's a children's game, normally played by kids when they're supposed to be doing homework
 instead. If you've never played here are the rules:
https://www.youtube.com/watch?v=cGOeiQfjYPk and https://www.wikihow.com/Play-Hangman

For this assignment, we want to play hangman in 2-player mode. The game should start by prompting player 1 to pick a
word. Then the screen should clear itself so that player 2 can't see the word. hint: print(chr(27) + "[2J")

After the screen is clear, the "gallows" and the empty letter spaces should be drawn, and player 2 should be allowed to
guess letters until they either win, or lose.
As they choose correct letters, the letters should appear on the screen in place of the blank space (clear and redraw
the whole screen). As they choose wrong letters,
the "man" himself should come end up being drawn, piece by piece. How many guesses they get before losing is up to you
(depending on how complicated of a man you want to draw).

Important: If you'd rather not do "hangman" because of the violence aspect, that's fine! Please make "snowman" instead.
You can see an example in the wiki-how link above.
Extra Credit: Try finding a large list of dictionary words and embedding them in your application. When the game starts,
 instead of player 1 choosing the word to play with,
the computer should pick a random word from the dictionary. This will allow you to play against the computer instead of
only 2-player mode. When the game starts,
the user should be prompted to choose between 1-player or 2-player mode.
"""
# Imports
import pygame
import os
# Constants
CONST_WIDTH, CONST_HEIGHT, CONST_FPS = 800, 600, 12


class HangmanGame:
    def __init__(self):
        pygame.init()
        self.CurrentPlayer = 1
        self.Chances = 10
        self.LettersPlayed = {}
        self.CONST_HANGMAN_IMG = pygame.image.load(
            os.path.join("Assets", "hangman_" + str((self.Chances + 1)) + ".png"))
        self.WordToGuess = input("Player " + str(self.CurrentPlayer) + ", please enter a word for Player 2 to guess: ")
        self.PygameWindow = pygame.display.set_mode((CONST_WIDTH, CONST_HEIGHT))
        pygame.display.set_caption("Hangman")
        self.BG_COLOR_WHITE = (255, 255, 255)
        self.BG_COLOR_BLACK = (0, 0, 0)
        self.CONST_GAME_FONT = pygame.font.SysFont('Times New Roman', 32)
        self.TextSurface = self.CONST_GAME_FONT.render(str(self.WordToGuess), True, self.BG_COLOR_BLACK)

    def start_game(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(CONST_FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_x]:  # X to reduce chances...
                self.reduce_chances()
                self.set_hangman_img()
            self.draw_window()
        pygame.quit()

    def draw_window(self):
        self.PygameWindow.fill(self.BG_COLOR_WHITE)
        self.PygameWindow.blit(self.CONST_HANGMAN_IMG, (CONST_WIDTH - 300, 100))
        self.PygameWindow.blit(self.TextSurface, (100, 100))

        pygame.display.update()

    def reduce_chances(self):
        if self.Chances >= 0:
            self.Chances -= 1
        else:
            self.Chances = 10

    def set_hangman_img(self):
        self.CONST_HANGMAN_IMG = pygame.image.load(
            os.path.join("Assets", "hangman_" + str((self.Chances + 1)) + ".png"))


if __name__ == "__main__":
    Hangman = HangmanGame()
    Hangman.start_game()
    print(Hangman.WordToGuess)
