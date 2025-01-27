# region imports
#This way of importing is saying from (the module) random, import (the function) random
#Other ways of importing might be:  import random
#             In the above case, we access the function random as random.random()
#Another way to import might be:  from random import random as rnd
#             In the above case, we use rnd() to produce a random number
from random import random
# endregion

# region functions
def rollFairDie():
    """
    This function simulates rolling a fair die such that the probability of each integer is 1/6.
    :return: an integer between 1 and 6 inclusive
    """
    from random import random
    x = random ()    # This calls random number from 0 to 1
    if x <= 1.0/6:      # This identifies what number was rolled
        return 1
    elif x<= 2.0/6:
        return 2
    elif x<= 3.0/6:
        return 3
    elif x<= 4.0/6:
        return 4
    elif x <= 5.0 / 6:
       return 5
    else:
        return 6



    #JES MISSING CODE

def rollUnFairDie():
    """
    This function simulates rolling an unfair die such that the probability of rolling a 1 is 0.2. with all other
    integers having equal probability.  Now, the probability of numbers 2-6 should be 0.8/5.
    :return: an integer between 1 and 6 inclusive
    """
    p=0.3
    x = random()  # This calls random number from 0 to 1
    if x <= 1.0 / 6:       # This identifies what number was rolled
        return 2
    elif x <= 2.0 / 6:
        return 2
    elif x <= 3.0 / 6:
        return 3
    elif x <= 4.0 / 6:
      return 4
    elif x <= 5.0 / 6:
       return 5
    else:
     return 6
# endregion

# The if statement below is known as: main guarding
if __name__ == "__main__":
    x = rollFairDie()
    print(x)