import pygame
from pygame.sprite import Sprite

class Alient(Sprite):
  """A class to represent one alien."""

  def __init__(self, ai_game):
    """Initialize the alien and set its start point."""
    super().__init__()
    self.screen = ai_game

    # Load alien image and set its rect attribute.
    self.image = pygame.image.load('alien_invasion\images\\alien.bmp')
    self.rect = self.image.get_rect()

    # Start each new alien in the top left corner.
    self.rect.x = self.rect.width
    self.rect.y = self.rect.height

    # Store alien's horizontal position.
    self.x = float(self.rect.x)