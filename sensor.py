class Sensor():
    def __init__(self, sensor_type):
        self._sensor_type = sensor_type

    @property
    def sensor_type(self):
        """Get sensor readings."""
        return self.sensor_type

    @sensor_type.setter
    def sensor_type(self, value):
        """Set sensor readings.

        Args:
            value: New sensor readings (dict)
        """
        self._sensor_type = value

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
        if name in self._sensor_type:
            self._sensor_type[name] = value
        else:
            raise ValueError("Sensor not found")

        if value < 0:
            raise ValueError("Sensor reading cannot be negative")

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

#read_data()
#detect_obstacle()
#get_reading()