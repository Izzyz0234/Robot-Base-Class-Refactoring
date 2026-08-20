class Motor():
    def __init__(self, speed, is_running):
        self._speed = speed
        self._is_running = is_running

    @property
    def is_running(self):
        """Get moving status."""
        return self._is_running

    @is_running.setter
    def is_running(self, value):
        """Set moving status.

        Args:
            value: New moving status (bool)
        """

        self._is_running = value

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
            self._is_running = True
        if speed == 0:
            self._is_running = False
        if speed < 0:
            raise ValueError("Speed cannot be negative")

        

    def stop(self):
        """Stop the robot."""
        if self._is_running == False or self._battery_level <= 0:
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

#forward(distance)
#backward(distance)
#stop()
#set_speed(speed)