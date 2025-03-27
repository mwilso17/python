import pygame

class Tank:
  """Class manages player tank."""

  def __init__(self, ty_game):
    """Initialize tank and place it on the center left of the screen"""
    self.screen = ty_game.screen
    self.screen_rect = ty_game.screen.get_rect()

    self.image = pygame.image.load('tank_you\images\player_tank.bmp')
    self.rect = self.image.get_rect()

    self.rect.midleft = self.screen_rect.midleft

  def blitme(self):
    """Draw tank at current location."""
    self.screen.blit(self.image, self.rect)