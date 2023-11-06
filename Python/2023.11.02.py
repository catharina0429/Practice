'''Leap Year'''
# def leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

print(leap_year(1996)) # TRUE
print(leap_year(2015)) # FALSE
print(leap_year(2000)) # TRUE
print(leap_year(1990)) # FALSE


'''Tryangle'''
def equilateral(sides):
    """all three sides the same length (정삼각형)"""
    if sides[0] == sides[1] == sides[2]:
        if sides[0] > 0 and sides[1] > 0 and sides[2]:
            return True
    return False

print(equilateral([0, 0, 0])) # FALSE
print(equilateral([4, 4, 4])) # TRUE

def isosceles(sides):
    """at least two sides the same length (이등변삼각형)"""
    if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
        if (sides[0] + sides[1] >= sides[2]) and (sides[0] + sides[2] >= sides[1]) and (sides[1] + sides[2] >= sides[0]):
            return True
    return False
print(isosceles([4,5,4]))  # TRUE   
print(isosceles([7,4,3]))  # FALSE

def scalene(sides):
    """all sides of different lengths (부등변삼각형)"""
    if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]:
        if (sides[0] + sides[1] >= sides[2]) and (sides[0] + sides[2] >= sides[1]) and (sides[1] + sides[2] >= sides[0]):
            return True
    return False

print(scalene([3,4,3]))
print(scalene([4,3,3])) # False
print(scalene([7,4,3]))