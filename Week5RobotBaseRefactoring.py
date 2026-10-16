from battery import Battery
from sensor import Sensor
from motor import Motor

class RobotBase:
    """A base class for a robot with basic functionalities."""

    def __init__(self, name):
        self._name = name
        self._battery = Battery(100, 50)
        self._motor = Motor(0, False)
        self._sensor = Sensor("object")

    @property
    def name(self):
        """Get robot name."""
        return self._name

    def move(self, distance):
        self.distance = distance

        if not isinstance(distance, int):
            raise TypeError("Distance must be an integer")

        if distance < 0:
            self._motor.backward(distance)
            self._motor = Motor(1, True)
        if distance == 0:
            self._motor = Motor(0, False)
        if distance > 0:
            self._motor.forward(distance)
            self._motor = Motor(1, True)
        

    def scan_environment(self):
        pass

    def get_battery_status(self):
        pass

    def stop(self):
        pass


    def report_status(self):
        """Report the current status of the robot.
        
        Returns:
            A string containing robot name, battery level, moving status, and sensor readings.
        """
        return (f"Robot Name: {self._name!r}\n"
                f"Battery Level: {self._battery.get_percentage()}\n"
                f"Is Moving: {self._motor.is_running()}\n"
                f"Sensor Readings: {self._sensor.get_reading()!r}")


    def __str__(self):
        return f"RobotBase('{self._name!r}', {self._battery.get_percentage()}, {self._battery.current_level()!r}, {self._motor.is_running()!r}, {self._sensor.get_reading()!r})"

    def __repr__(self):
        return (f"Robot Name: {self._name!r}\n"
                "Battery: \n"
                f"Battery Level: {self._battery.current_level}\n"                
                f"Battery Charge: {self._battery.charge()}\n"
                f"Battery Persentage: {self._battery.get_percentage()}\n"                
                f"Battery depleted: {self._battery.is_depleted()}\n"                

                "\nMotor: \n"
                f"Speed: {self._motor._speed!r}\n"
                f"Is Moving: {self._motor.is_running!r}\n"

                "\nSensor: \n"
                f"Sensor Read Data: {self._sensor.read_data()!r}\n"
                f"Sensor Detect Obstacle: {self._sensor.detect_obstacle()!r}\n"
                f"Sensor Get Reading: {self._sensor.get_reading()!r}\n")

print("Initial Robot Settings:")
robot = RobotBase("Bob")

# Battery
# robot._battery = Battery(100, 80)
# robot._battery.drain(50)

# Motor
robot.move(50)
# robot._motor = Motor(5, True)
# # robot._motor.forward(20)
# # robot._motor.stop()
# robot._motor.set_speed(50)

# Sensor
# robot._sensor = Sensor("object")

print(robot.report_status)

