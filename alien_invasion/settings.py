class Settings:
  """A class to store all settings for Alien Invasion"""

  def __init__(self):
    """Initialize the game's static settings."""
    # Screen Settings
    self.screen_width = 1200
    self.screen_height = 800
    self.bg_color = (230, 230, 230)

    # Ship Settings
    self.ship_limit = 3

    # Bullet Settings
    self.bullet_width = 3
    self. bullet_height = 15
    self.bullet_color = (60, 60, 60)
    self.bullets_allowed = 3

    # Alien settings
    self.fleet_drop_speed = 10

    # Game speed scaling.
    self.speedup_scale = 1.2

    self.initialize_dynamic_settings()

  def initialize_dynamic_settings(self):
    """Initialize settings that change during game play."""
    self.ship_speed = 1.5
    self.bullet_speed = 3.0
    self.alien_speed = 1.0

    # fleet_direction of 1 represents right; -1 represents left.
    self.fleet_direction = 1

    # Scoring
    self.alien_points = 1

  def increase_speed(self):
    """Increase speed settings."""
    self.ship_speed *= self.speedup_scale
    self.bullet_speed *= self.speedup_scale
    self.alien_speed *= self.speedup_scale