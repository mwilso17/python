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

    # Movement flag
    self.moving_up = False
    self.moving_down = False

  def update(self):
    """Update tank position based on movement flags."""
    if self.moving_up:
      self.rect.y -= 1
    if self.moving_down:
      self.rect.y += 1


  def blitme(self):
    """Draw tank at current location."""
    self.screen.blit(self.image, self.rect)