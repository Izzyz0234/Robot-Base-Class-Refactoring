import random
from battery import Battery
from sensor import Sensor
from motor import Motor

class RobotBase:
    """A base class for a robot with basic functionalities."""

    def __init__(self, name):
        self._name = name
        self._battery = Battery(100)
        self._motor = Motor(True)
        self._sensor = Sensor(5)

    @property
    def name(self):
        """Get robot name."""
        return self._name


    def report_status(self):
        """Report the current status of the robot.
        
        Returns:
            A string containing robot name, battery level, moving status, and sensor readings.
        """
        return (f"Robot Name: {self._name}\n"
                f"Battery Level: {Battery}%\n"
                f"Is Moving: {Motor}\n"
                f"Sensor Readings: {Sensor}")


    def __str__(self):
        return f"RobotBase('{self._name}', {Battery}, {Motor}, {Sensor})"

    def __repr__(self):
        return (f"Robot Name: {self._name}\n"
                f"Battery Level: {Battery}%\n"
                f"Is Moving: {Motor}\n"
                f"Sensor Readings: {Sensor}")


print("Initial Robot Settings:")
robot = RobotBase("Bob")
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
