class Battery():
    def __init__(self, battery_level):
        self.battery_level = battery_level

    @property
    def battery_level(self):
        """Get battery level."""
        return self.battery_level

    @battery_level.setter
    def battery_level(self, value):
        """Set battery level with validation.

        Args:
            value: New battery level percentage (float, 0-100)
        Raises:
            ValueError: If battery level is not in valid range
        """
        if not (0 <= value <= 100):
            raise ValueError("Battery level must be between 0 and 100")
        self.battery_level = value
