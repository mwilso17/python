import pygame

class Ship:
  """A class to manage the ship."""

  def __init__(self, ai_game):
    """Initialize the ship and set its start point."""
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()

    # Load ship image and get its rect.
    self.image = pygame.image.load('images/ship.bmp')
    self.rect = self.image.get_rect()

    # Start each new ship at bottom center of screen.
    self.rect.midbottom = self.screen_rect.midbottom

  def blitme(self):
    """Draw ship at its current location"""
    self.screen.blit(self.image, self.rect)