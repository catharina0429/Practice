print(True and True) # True
print(True and False) # False
print(False or False) # False

# Task 1: Define if Pac-Man eats a ghost
def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can the ghost be eaten?
    
    The function should return True only if 
    Pac-Man has a power pellet active and is touching a ghost.
    """
    if power_pellet_active == True and touching_ghost == True:
        return True
    else:
        return False

# Task 2: Define if Pac-Man scores
def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    :param touching_power_pellet: bool - is the player touching a power pellet?
    :param touching_dot: bool - is the player touching a dot?
    :return: bool - has the player scored or not?
    
     The function should return True if 
     Pac-Man is touching a power pellet or a dot.
    """
    if touching_power_pellet == True or touching_dot == True:
        return True
    else:
        return False

# Task 3: Define if Pac-Man loses
def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    
    The function should return True if 
    Pac-Man is touching a ghost and does not have a power pellet active.
    """
    if power_pellet_active == False and touching_ghost == True:
        return True
    else:
        return False
    
# Task 4: Define if Pac-Man wins
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    
    The function should return True if 
    Pac-Man has eaten all of the dots and 
    has not lost based on the parameters defined in task 3.
    """
    if has_eaten_all_dots == True and power_pellet_active == touching_ghost:
        return True
    else:
        return False

print(win(True, False, True)) # False
print(win(False, True, True)) # False
print(win(True, False, False)) # True
print(win(True, True, True)) # True
