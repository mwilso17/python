# This program is created off of the Alien Invasion project in Eric Matthes's 2nd Edition Python Crash Course book.
# Changes to the base program (additions, new features, etc) will be added to the README file under "Changes from base code"

import sys

import pygame

from settings import Settings

class AlienInvasion:
  """Overall class to manage game assets and behavior."""

  def __init__(self):
    """Initialize game and create game resources"""
    pygame.init()
    self.settings = Settings()

    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Set background color.
    self.bg_color = (230, 230, 230)

  def run_game(self):
    """Start the main loop for the game"""
    while True:
      # Watch for keyboard and mouse events.
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()

      # Redraw screen during each pass through the loop.
      self.screen.fill(self.settings.bg_color)

      # Make the most recently drawn screen visible.
      pygame.display.flip()

if __name__ == "__main__":
  # Make a game instance and run the game.
  ai = AlienInvasion()
  ai.run_game()