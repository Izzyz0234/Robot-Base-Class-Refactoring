class Sensor():
    def __init__(self, sensor_type):
        self._sensor_type = sensor_type

    # @property
    # def sensor_type(self):
    #     """Get sensor readings."""
    #     return self.sensor_type

    # @sensor_type.setter
    # def sensor_type(self, value):
    #     """Set sensor readings.

    #     Args:
    #         value: New sensor readings (dict)
    #     """
    #     self._sensor_type = value


    def read_data(self):
        """Read environmental data from sensors."""
        pass
    
    def detect_obstacle(self):
        """Detect if obstacle is present."""
        pass
    
    def get_reading(self):
        """Get sensor reading value."""
        pass


#read_data()
#detect_obstacle()
#get_reading()