import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
  """This class hosts the enemy tank."""

  def __init__(self, ty_game):
    """Initialize enemy tank and set its position."""
    super().__init__()
    self.screen = ty_game.screen
    self.screen_rect = ty_game.screen.get_rect()
    
    # Load enemy image and set its rect.
    self.image = pygame.image.load('tank_you\images\enemy_tank.bmp')
    self.rect = self.image.get_rect()

    # Start enemy tank in center right of screen.
    self.rect.midright = self.screen_rect.midright

    # Store enemy exact verticle position.
    self.y = float(self.rect.y)

