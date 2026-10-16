class Sensor():
    def __init__(self, sensor_type):
        self._sensor_type = sensor_type
        self._reading = "Clear"

    def read_data(self):
        """Read environmental data from sensors."""
        return {"Type": self._sensor_type, "Reading": self._reading}

    def detect_obstacle(self):
        """Detect if obstacle is present."""
        return self._reading == "Obstacle"

    def get_reading(self):
        """Get sensor reading value."""
        return self._reading


#read_data()
#detect_obstacle()
#get_reading()