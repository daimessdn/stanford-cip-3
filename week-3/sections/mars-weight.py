"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():
    # Fill this function out!
    earth_weight = input("Enter a weight on Earth: ")
    earth_weight = float(earth_weight)
    
    mars_weight = earth_weight * (37.8 / 100)
    mars_weight = str(round(mars_weight, 2))  
    
    print("The equivalent weight on Mars: " + mars_weight)

if __name__ == "__main__":
    main()