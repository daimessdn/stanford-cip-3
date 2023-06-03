"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""

"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

MERCURY_GRAVITY = 37.6
VENUS_GRAVITY = 89
MARS_GRAVITY = 37.8
JUPITER_GRAVITY = 236.0
SATURN_GRAVITY = 108.1
URANUS_GRAVITY = 82
NEPTUNE_GRAVITY = 114.0

def main():
    earth_weight = float(input("Enter a weight on Earth: "))
    
    planet = str(input("Enter a planet: "))
    
    planet_weight = get_planet_weight(earth_weight, planet)
    
    print("The equivalent weight on " + planet + ": " + planet_weight)
    
def get_percent_weight(gravity):
    return gravity / 100
    
def count_planet_weight(weight, gravity):
    planet_weight = weight * get_percent_weight(gravity)
    planet_weight = round(planet_weight, 2)
    
    planet_weight = str(planet_weight)
    
    return planet_weight
    
def get_planet_weight(weight, planet):
    if (planet == "Mercury"):
        return count_planet_weight(weight, MERCURY_GRAVITY)
    elif (planet == "Venus"):
        return count_planet_weight(weight, VENUS_GRAVITY)
    elif (planet == "Mars"):
        return count_planet_weight(weight, MARS_GRAVITY)
    elif (planet == "Jupiter"):
        return count_planet_weight(weight, JUPITER_GRAVITY)
    elif (planet == "Saturn"):
        return count_planet_weight(weight, SATURN_GRAVITY)
    elif (planet == "Uranus"):
        return count_planet_weight(weight, URANUS_GRAVITY)
    elif (planet == "Neptune"):
        return count_planet_weight(weight, NEPTUNE_GRAVITY)

if __name__ == "__main__":
    main()