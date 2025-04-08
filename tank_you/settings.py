class Settings:
  """This class stores the settings for Tank You."""

  def __init__(self):
    self.screen_width = 1000
    self.screen_height = 800
    self.bg_color = (100, 230, 100)

    # Player tank speed.
    self.tank_speed = .3
    self.player_health = 3

    # Ammo settings.
    self.ammo_speed = 1.0
    self.ammo_width = 6
    self.ammo_height = 6
    self.ammo_color = (20, 20, 20)
    self.ammo_limit = 3

    # Enemy settings.
    self.enemy_speed = .3
    self.enemy_direction = 1 