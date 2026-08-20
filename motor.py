class Motor():
    def __init__(self, is_moving):
        self.is_moving = is_moving

    @property
    def is_moving(self):
        """Get moving status."""
        return self.is_moving

    @is_moving.setter
    def is_moving(self, value):
        """Set moving status.

        Args:
            value: New moving status (bool)
        """

        self.is_moving = value

    def move_forward(self, speed):
        """Move the robot forward at a given speed.

        Args:
            speed: Speed at which to move forward (float)
        Raises:
            ValueError: If battery is out or speed is negative
        """
        if self._battery_level <= 0:
            raise ValueError("Out of battery")
        if speed >= 0:
            self._is_moving = True
        if speed == 0:
            self._is_moving = False
        if speed < 0:
            raise ValueError("Speed cannot be negative")

        

    def stop(self):
        """Stop the robot."""
        if self._is_moving == False or self._battery_level <= 0:
            self.stop

    def get_sensor_reading(self, name):
        """Get the reading of a specific sensor.

        Args:
            name: Name of the sensor (str)
        Raises:
            ValueError: If battery is out or sensor is negative
        """
        if self._battery_level <= 0:
            raise ValueError("Out of battery")
        if name in self._sensor_readings:
            return self._sensor_readings[name]
        else:
            raise ValueError("Sensor not found")
