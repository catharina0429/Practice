print(True and True) # True
print(True and False) # False
print(False or False) # False
print(False and True)

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


