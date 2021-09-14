# Miles to Meters
MI_TO_M = 1609.34

# This is the time constant
C = 120

# Initial Velocity
initialvelocity = float(input("What's your initial velocity? "))
# Time Elapsed
timeelapsed = float(input("How much time elapsed? "))
# Traveling Acceleration
acceleration = float(input("You were travelling at what acceleration? "))

# Converts initialvelocity from miles per second to meters per second
initialvelocity *= MI_TO_M

# Trips done in time
Trips = (C / timeelapsed) // 1

# timeremaining after compleating max number of trips
timeremaining = C - (timeelapsed * Trips)

# Gets finalvelocity
finalvelocity = initialvelocity + (acceleration * timeelapsed)

# Gets distancetraveled
distancetraveled = ((finalvelocity + initialvelocity) / 2) * timeelapsed

# Print Statements
print("Congratulations! You've done it!")
print("You made {0:.0f} trips.".format(Trips))
print("You had {0:.2f} seconds to spare.".format(timeremaining))
print("During each trip you travelled {0:.2f} meters.".format(distancetraveled))
print("Your final velocity was {0:.2f} m/s^2.".format(finalvelocity))
print("You're free to shout,", '"Hurray!"')
