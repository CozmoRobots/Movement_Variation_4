#import the cozmo and image libraries
import cozmo

#import libraries for movement 
from cozmo.util import degrees, distance_mm

#import random library for random number from range
from random import randrange

def getHawkID():
    hawkID = ["cjwallerich"]
    return hawkID

def driveStraight(robot: cozmo.robot.Robot):
    robot.drive_straight(cozmo.util.distance_mm(100), cozmo.util.speed_mmps(100)).wait_for_completed()
    return

def turnRight(robot: cozmo.robot.Robot):
    robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
    return

def turnLeft(robot: cozmo.robot.Robot):
    robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
    return

def cozmoIncrementalMovement(robot: cozmo.robot.Robot):
    
    #creates our random number of increments that cozmo will move in the desired range
    x = randrange(3,12,1)
    y = randrange(3,12,1)

    #requests variables for cozmo's current position
    currentX = input("where is Cozmo currently located on the x-axis? (input 0 for default): ")
    currentY = input("where is Cozmo currently located on the y-axis? (input 0 for default): ")
    
    #list of acceptable places for cozmo to be at
    goodValues = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    
    #checks if the user has inputted one of the acceptable numbers in string format
    if currentX not in goodValues:
        #cozmo expresses his confusion and exits the program if the number is not acceptable
        robot.say_text("Um, I don't know where that is").wait_for_completed()
        return
    elif currentY not in goodValues:
        robot.say_text("Um, I don't know where that is").wait_for_completed()
        return
    #if the still string-ed number is acceptable then it is cast as an integer and continues on
    else:
        currentX = int(currentX)
        currentY = int(currentY)
    
    #gets how many units cozmo will have to travel overall
    distance = x + y
    
    #cozmo announces what distances he will be traveling
    robot.say_text("I will drive " + str(x * 10 - (currentX * 10)) + "centimeters horizontally and " + str(y * 10 - (currentY * 10)) + "centimeters vertically").wait_for_completed()
    
    #orients cozmo horizontally to begin (assuming he beings facing vertically)
    turnRight(robot)
    
    #iterates through the number of units cozmo will have to travel
    for i in range(distance):
        #cozmo travels a unit horizontally and turns left in preparation to move vertically
        driveStraight(robot)
        turnLeft(robot)
        #updates cozmo's current position
        currentX += 1
        #enters an exception if cozmo has reached his desired destination horizontally
        if currentX == x:
            while currentY != y:
                driveStraight(robot)
                currentY += 1
            break
        #cozmo travels a unit vertically and turns right in preparation to move horizontally
        driveStraight(robot)
        turnRight(robot)
        #updates cozmo's current position
        currentY += 1
        #enters an exception if cozmo has reached his desired destination vertically
        if currentY == y:
            while currentX != x:
                driveStraight(robot)
                currentX += 1
            break

    #cozmo causes a ruckus upon completing his movement
    robot.play_anim(name="anim_petdetection_dog_02").wait_for_completed()
    return

cozmo.run_program(cozmoIncrementalMovement, use_viewer=False, force_viewer_on_top=False)