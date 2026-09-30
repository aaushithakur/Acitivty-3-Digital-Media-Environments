# Complete the TODOs using the Python concepts introduced in class.
# Run this file to check your result.  

# DG8002 - F26 - Activity 3
# Author Name: Aaushi Thakur 
# Date: 29th September 2026 

# SCENARIO
# A group of friends is planning a road trip and wants to estimate the
# driving time and fuel cost. Use these starting values:
# Distance: 650 km
# Average speed: 100 km/h
# Fuel efficiency: 8 L per 100 km
# Fuel price: $1.55 per litre
# Passengers: 3
# Assume constant average speed and fuel efficiency. Ignore stops,
# traffic, taxes, and other vehicle costs.

# TODO 1: Create five variables to store the trip information above.
# Give each variable a meaningful name.

# TODO 2: Calculate estimated driving time in HOURS.
# Hint: distance / average speed

# TODO 3: Calculate the total fuel needed in LITRES.
# Hint: fuel efficiency describes litres used for every 100 km.

# TODO 4: Calculate the total fuel cost.

# TODO 5: Use an if/else statement to check that passengers is greater
# than zero before calculating the fuel cost per passenger.
# If passengers is zero or less, print a helpful message instead.

# TODO 6: Print a readable trip summary showing:
#   - Estimated driving time (hours)
#   - Total fuel needed (litres)
#   - Total fuel cost (CAD)
#   - Fuel cost per passenger (CAD), when it can be calculated

# CHECK YOUR WORK
# With the starting values above, expect:
# Driving time: 6.5 hours
# Fuel needed: 52 litres
# Total fuel cost: $80.60
# Fuel cost per passenger: about $26.87
# Test again with zero passengers. Your program should not divide by zero.
# Example inputs, with units clearly identified.
distance_km = 650.0
average_speed_kmh = 100.0
fuel_consumption_l_per_100km = 8.0
fuel_price_per_litre = 1.55
number_of_passengers = 3

travel_time_hours = distance_km / average_speed_kmh
fuel_needed_litres = ( distance_km / 100) * fuel_consumption_l_per_100km
total_fuel_cost = fuel_needed_litres * fuel_price_per_litre
cost_per_passenger = total_fuel_cost / number_of_passengers

print(f"Trip distance: {distance_km:.1f} km")
print(f"Estimated travel time: {travel_time_hours:.2f} hours")
print(f"Estimated fuel consumption: {fuel_needed_litres:.2f} litres")
print(f"Estimated fuel cost: ${total_fuel_cost:.2f}")
print(f"Number of passengers sharing the cost: {number_of_passengers}")
print(f"Fuel cost per passenger: ${cost_per_passenger:.2f}")