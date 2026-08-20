class Battery():
    def __init__(self, capacity, current_level):
        self._capacity = capacity
        self._current_level = current_level

    @property
    def current_level(self):
        """Get battery level."""
        return self._current_level

    @current_level.setter
    def current_level(self, value):
        """Set battery level with validation.

        Args:
            value: New battery level percentage (float, 0-100)
        Raises:
            ValueError: If battery level is not in valid range
        """
        if not (0 <= value <= 100):
            raise ValueError("Battery level must be between 0 and 100")
        self._current_level = value

    def drain(self, amount):
        if self._current_level >= 0:
            self.current_level == self.current_level - amount

#drain(amount)
#charge()
#get_percentage()
#is_depleted()