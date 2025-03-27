import sys

import pygame

class TankYou:
  """Class to manage game."""

  def __init__(self):
    """Initialize game."""
    pygame.init()

    self.screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Tank You")

    self.bg_color = (200, 200, 200)

  def run_game(self):
    """Start game main loop."""
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()

      self.screen.fill(self.bg_color)

      # Makes current render visible.
      pygame.display.flip()

if __name__ == '__main__':
  ty = TankYou()
  ty.run_game()