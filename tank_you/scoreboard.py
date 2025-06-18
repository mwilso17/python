import pygame.font 
from pygame.sprite import Group

from tank import Tank

class Scoreboard:
  """Class reporting scoring info."""

  def __init__(self, ty_game):
    """Initialize score attributes."""
    self.ty_game = ty_game
    self.screen = ty_game.screen
    self.screen_rect = self.screen.get_rect()
    self.settings = ty_game.settings
    self.stats = ty_game.stats

    # Font settings for score info.
    self.text_color = (0, 0, 0)
    self.font = pygame.font.SysFont(None, 48)

    # Prepare score image.
    self.prep_score()

    # Prepare remaining player health
    self.prep_health()

    # Prepare version.
    self.prep_version()

  def prep_score(self):
    """Render score image."""
    score_str = "Tanks Destroyed " + str(self.stats.score)
    self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

    # Display score at top of screen
    self.score_rect = self.score_image.get_rect()
    self.score_rect.right = self.screen_rect.right - 20
    self.score_rect.top = 20

  def prep_health(self):
    """Show how much player health is left."""
    self.health = Group()
    for player_health in range(self.stats.health_left):
      health = Tank(self.ty_game)
      health.rect.x = 10 + player_health * health.rect.width
      health.rect.y = 10
      self.health.add(health)

  def prep_version(self):
    """Turn version into a rendered image."""
    version = "v1.1.0"
    self.version_image = self.font.render(version, True, self.text_color, self.settings.bg_color)

    # Center version at top middle of screen.
    self.version_rect = self.version_image.get_rect()
    self.version_rect.centerx = self.screen_rect.centerx
    self.version_rect.top = self.screen_rect.top


  def show_score(self):
    """Draw score, version, and health to screen."""
    self.screen.blit(self.score_image, self.score_rect)
    self.screen.blit(self.version_image, self.version_rect)
    self.health.draw(self.screen)