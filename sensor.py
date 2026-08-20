class Sensor():
    def __init__(self, sensor_readings):
        self.sensor_readings = sensor_readings

    @property
    def sensor_readings(self):
        """Get sensor readings."""
        return self.sensor_readings

    @sensor_readings.setter
    def sensor_readings(self, value):
        """Set sensor readings.

        Args:
            value: New sensor readings (dict)
        """
        self.sensor_readings = value

    def set_sensor_reading(self, name, value):
        """Set the reading of a specific sensor.

        Args:
            name: Name of the sensor (str)
            value: New reading value (float)
        Raises:
            ValueError: If battery is out or sensor is negative
        """
        if self._battery_level <= 0:
            raise ValueError("Out of battery")
        if name in self._sensor_readings:
            self._sensor_readings[name] = value
        else:
            raise ValueError("Sensor not found")

        if value < 0:
            raise ValueError("Sensor reading cannot be negative")

