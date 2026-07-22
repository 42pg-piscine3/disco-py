class Robot:
    def mystr(self):  # Same name as class
        return "I am a robot!"

# BAD PRACTICE: Attempting to instantiate the class will now fail to call __init__ 
# and will return the Robot object itself in an uninitialized state.
#my_bot = Robot()
#print(my_bot.Robot())  # Outputs: I am a robot!
print(Robot())  # Outputs: I am a robot!
