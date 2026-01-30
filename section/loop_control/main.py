# List of country names
countries = ['Wales', 'Denmark', 'Belgium', 'Japan', 'South Korea', 'South Africa', 'Indonesia', 'Singapore', 'Australia', 'India', 'Saudi Arabia', 'Mexico', 'Turkey', 'Greece', 'Netherlands', 'Finland', 'Monako', 'United Arab Emirates', 'Egypt', 'Morocco', 'Brazil', 'Argentina', 'Ireland', 'Portugal', 'Chile', 'Spain', 'Czech Republic', 'Sweden', 'Switzerland', 'Thailand', 'Luxemburg', 'New Zealand', 'France', 'Italy', 'Germany', 'China', 'Canada', 'Hungary', 'Scotland', 'Norway', 'Austria', 'Ukraine', 'Poland']

# List to hold selected countries
selected = []

# Initialize the index
i = 0

# Iterate through the list
while i < len(countries):
    if countries[i][0] != "S":          # Countries to skip (no "S")
        i += 1
        continue
        
    selected.append(countries[i])      # Append valid countries

    if len(selected) == 3:             # Limit to first 3
        break

    i += 1

# Testing
print('First three countries starting with "S":', selected)