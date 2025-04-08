class GameStats:
  """Track game statistics."""

  def __init__(self, ty_game):
    self.settings = ty_game.settings
    self.reset_stats()

  def reset_stats(self):
    self.health_left = self.settings.player_health