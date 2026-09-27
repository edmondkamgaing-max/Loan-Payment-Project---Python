"""
    Edmond Kamgaing Kamdem
    Python
    Windows
    The coin class simulates the coin that can be flipped
"""

# Imports the random module, which allows us to generate random numbers
import random

# Defines a Coin class.
# The class represents a coin that has two possible sides: 
# Heads or Tails.
class Coin:

    # Constructor method.
    # It is automatically called when a new Coin object is created.
    def __init__(self):

        # Private attribute that stores the current side of the coin.
        # The coin starts with Heads facing up.
        self.__sideup = 'Heads'

    # Defines the toss method.
    # This method simulates flipping the coin.
    def toss(self):

        # random.randint(0, 1) randomly generates either 0 or 1.
        # If the result is 1, the coin shows Heads.
        if random.randint(0,1) == 1:
            self.__sideup = "Heads"

         # If the result is 0, the coin shows Heads.
        else:
            self.__sideup = "Trails"
            
    # Defines a method to retrieve the current side of the coin.
    def get_sideup(self):

        # Retuns the value stored in the private __sideup attribute.
        return self.__sideup

# Defines the main function of the program.
def main():

    # Creates a new coin object called my_coin.
    my_coin = Coin()
    
    # Displays the initial side of the coin.
    print ("This side is up", my_coin.get_sideup())
    
    # Displays the message indicating that the coin is being flipped.
    print("I am tossing the coin... ")

    # Calls the toss() method to randomly flip the coin.
    my_coin.toss()

    # Displays the side of the coin after the toss.
    print ("This side is up", my_coin.get_sideup())

# Checks whether this file is being executed directly
# If it is, the main() function is called.
if __name__ == '__main__':
    main()
