class GameStats:
  """Track game stats."""

  def __init__(self, ai_game):
    """Initialize stats."""
    self.settings = ai_game.settings
    self.reset_stats()

    # Start game in an active state.
    self.game_active = False

  def reset_stats(self):
    """Initialize stats that can chage in game."""
    self.ships_left = self.settings.ship_limit