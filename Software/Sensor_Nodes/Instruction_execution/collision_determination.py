# Imports

# This class checks for collisions using the robot's button sensor and updates the collision indicator.
class CollisionDetermination:
    def __init__(self):
        pass

    def update(self, robot):
        # If the button sensor is pressed, mark a collision
        if robot.senser_nodes.button_sensor:
            robot.collision_indicator = True
        else:
            robot.collision_indicator = False
