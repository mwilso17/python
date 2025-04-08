import pygame

class Tank:
  """Class manages player tank."""

  def __init__(self, ty_game):
    """Initialize tank and place it on the center left of the screen"""
    self.screen = ty_game.screen
    self.settings = ty_game.settings
    self.screen_rect = ty_game.screen.get_rect()

    self.image = pygame.image.load('tank_you\images\player_tank.bmp')
    self.rect = self.image.get_rect()

    self.rect.midleft = self.screen_rect.midleft

    # Store decimal value for vertical position.
    self.y = float(self.rect.y)

    # Movement flag
    self.moving_up = False
    self.moving_down = False

  def update(self):
    """Update tank position based on movement flags."""
    if self.moving_up and self.rect.y > 0:
      self.y -= self.settings.tank_speed
    if self.moving_down and (self.rect.y + 50) < self.screen_rect.bottom:
      self.y += self.settings.tank_speed

    # Update rect object from self.y.
    self.rect.y = self.y


  def blitme(self):
    """Draw tank at current location."""
    self.screen.blit(self.image, self.rect)

  def reset(self):
    """Center tank."""
    self.rect.midleft = self.screen_rect.midleft
    self.y = float(self.rect.y)