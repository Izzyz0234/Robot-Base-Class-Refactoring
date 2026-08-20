import random
from battery import Battery
from line import LineSensor
from motor import Motor

class Robot:
    def __init__(self, name):
        self.name = name
        self.battery = Battery()
        self.motor = Motor()

class LineFolloweRobot(Robot):
    def __init__(self, name):
        super().__init__(name) # links to Robot name
        self.line_sensor = LineSensor()

line0 = LineFolloweRobot("Line Follower")

sam = Robot("Sam")

class RobotBase:
    """A base class for a robot with basic functionalities."""

    def __init__(self, robot_name, battery_level, is_moving, sensor_readings):
        """Initialize a robot.

        Args:
            robot_name: Name of the robot (str)
            battery_level: Battery level percentage (float, 0-100)
            is_moving: Whether the robot is currently moving (bool)
            sensor_readings: Dictionary of sensor readings (dict)
        """
        self._robot_name = robot_name
        self._battery_level = battery_level
        self._is_moving = is_moving
        self._sensor_readings = sensor_readings

    @property
    def robot_name(self):
        """Get robot name."""
        return self._robot_name

    @property
    def battery_level(self):
        """Get battery level."""
        return self._battery_level

    @property
    def is_moving(self):
        """Get moving status."""
        return self._is_moving

    @property
    def sensor_readings(self):
        """Get sensor readings."""
        return self._sensor_readings

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
        self._battery_level = value

    @is_moving.setter
    def is_moving(self, value):
        """Set moving status.

        Args:
            value: New moving status (bool)
        """

        self._is_moving = value


    @sensor_readings.setter
    def sensor_readings(self, value):
        """Set sensor readings.

        Args:
            value: New sensor readings (dict)
        """
        self._sensor_readings = value

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

    def report_status(self):
        """Report the current status of the robot.
        
        Returns:
            A string containing robot name, battery level, moving status, and sensor readings.
        """
        return (f"Robot Name: {self._robot_name}\n"
                f"Battery Level: {self._battery_level}%\n"
                f"Is Moving: {self._is_moving}\n"
                f"Sensor Readings: {self._sensor_readings}")

    def __str__(self):
        return f"RobotBase('{self._robot_name}', {self._battery_level}, {self._is_moving}, {self._sensor_readings})"

    def __repr__(self):
        return (f"Robot Name: {self._robot_name}\n"
                f"Battery Level: {self._battery_level}%\n"
                f"Is Moving: {self._is_moving}\n"
                f"Sensor Readings: {self._sensor_readings}")

print("Initial Robot Settings:")
robot = RobotBase("Bob", 85, False, {"temperature": 22.5, "proximity": 0.8})
print(robot.report_status)

print("\nStart Robot:")
# Updating status for movement and battery level
robot.move_forward(5)  # Move forward at speed 5
robot.battery_level = 82  # Set battery level to 82%

# Getting and setting sensor readings
proximity = robot.get_sensor_reading("proximity")
temperature = robot.get_sensor_reading("temperature")
robot.set_sensor_reading("proximity", 0.5)  # Update proximity sensor reading
robot.set_sensor_reading("temperature", 23.0)  # Update temperature sensor reading

print(robot.report_status)

print("\nStop Robot:")
# Updating status for movement and battery level
robot.move_forward(0)  # Move forward at speed 0
robot.battery_level = 80  # Set battery level to 80%
robot.stop

# Getting and setting sensor readings
robot.set_sensor_reading("proximity", 0.4)  # Update proximity sensor reading
robot.set_sensor_reading("temperature", 22.0)  # Update temperature sensor reading

print(robot.report_status)
