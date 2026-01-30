# List of travel costs (each sublist represents a trip)
travel_costs = [
    [5, 15, 10, 8, 25, 30, 55, 68, 75, 5],                   # Trip 1
    [60, 20, 60, 70, 80, 80, 80, 90, 90, 90],                # Trip 2
    [100, 100, 100, 100, 50, 110, 110, 120, 120, 120, 130],  # Trip 3
    [130, 140, 39, 140, 150, 150, 150, 150, 160, 160],       # Trip 4
    [170, 180, 180, 190, 40, 190, 200],                      # Trip 5
    [200, 200, 200, 210, 11, 220, 220, 220, 250, 250, 250],  # Trip 6
    [280, 300, 300, 110, 300, 320, 350, 400, 400, 450],      # Trip 7
    [480, 500, 500, 90, 500, 550, 600, 700]                  # Trip 8
]

# List to store maximum costs per trip
max_costs = [] # Must append each individual max cost per trip

# Initialize i
i = 0

# Outer loop to iterate over trip expenses
while i < len(travel_costs):
    # Initialize inner loop variables
    current_max = travel_costs[i][0]
    j = 0
    # Inner loop
    while j < len(travel_costs[i]):
        if travel_costs[i][j] > current_max:
            current_max = travel_costs[i][j]
        j += 1
    # Store result
    max_costs.append(current_max)
    i += 1

# Testing
print('Maximum Travel Costs:', max_costs)