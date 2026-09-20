# This is a list of dictionaries. Each dictionary represents a log of countries visited, how many times they've been visited, and which cities were visited.
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# Define a function called add_new_country.
# This function takes in three arguments:
# 1. The name of the country.
# 2. The number of visits.
# 3. A list of cities visited in that country.


def add_new_country(country_name, number_of_visits, cities_visited):
    # Create a new dictionary with the provided data.
    new_country = {
        "country": country_name,
        "visits": number_of_visits,
        "cities": cities_visited
    }
    # Append the new country's dictionary to the travel_log list.
    travel_log.append(new_country)


# We call the function to add a new country "Russia" with the relevant details.
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

# Finally, we print the updated travel_log to see the newly added entry.
print(travel_log)
