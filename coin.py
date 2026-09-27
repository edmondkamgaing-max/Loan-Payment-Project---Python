"""
    Edmond Kamgaing Kamdem
    CS115
    Windows
    The coin class simulates the coin that can be flipped
"""
import random

class Coin:
    def __init__(self):
        self.__sideup = 'Heads'

    def toss(self):
        if random.randint(0,1) == 1:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Trails"

    def get_sideup(self):
        return self.__sideup

def main():
    my_coin = Coin()

    print ("This side is up", my_coin.get_sideup())

    print("I am tossing the coin... ")
    my_coin.toss()

    print ("This side is up", my_coin.get_sideup())

if __name__ == '__main__':
    main()
