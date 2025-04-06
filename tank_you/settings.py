class Settings:
  """This class stores the settings for Tank You."""

  def __init__(self):
    self.screen_width = 1000
    self.screen_height = 800
    self.bg_color = (100, 230, 100)

    # Player tank speed.
    self.tank_speed = .3