import pygame.font 

class Scoreboard:
  """Class reporting scoring info."""

  def __init__(self, ty_game):
    """Initialize score attributes."""
    self.screen = ty_game.screen
    self.screen_rect = self.screen.get_rect()
    self.settings = ty_game.settings
    self.stats = ty_game.stats

    # Font settings for score info.
    self.text_color = (0, 0, 0)
    self.font = pygame.font.SysFont(None, 48)

    # Prepare score image.
    self.prep_score()

  def prep_score(self):
    """Render score image."""
    score_str = "Tanks Destroyed " + str(self.stats.score)
    self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

    # Display score at top of screen
    self.score_rect = self.score_image.get_rect()
    self.score_rect.right = self.screen_rect.right - 20
    self.score_rect.top = 20

  def show_score(self):
    """Draw score to screen."""
    self.screen.blit(self.score_image, self.score_rect)