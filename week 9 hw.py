#Hw week 9

#Problem 1

numbers = [1,2,3,4,5,6,7,8,9,10]
def square(x):
    return x*x

squared_numbers = map(square,numbers)
squared_numbers_list = list(squared_numbers)
even_numbers = [num for num in numbers if num%2==0]

#sort
sorted_numbers = sorted(numbers, reverse = True)

def remove_duplicates(seq):
    seen=set()
    return[x for x in seq if not (x in seen or seen.add((x)))]
unique_numbers = remove_duplicates(numbers)

print("origional list", numbers)
print("squared numbers", squared_numbers_list)
print("sorted numbers", sorted_numbers)
print("unique numbers", unique_numbers)

even_numbers2 = [2,4,5,8,10,12]
print("even numbers", even_numbers2)

#problem 2

red = (255, 0, 0)
blue = (342, 0, 0)
black = (0, 0, 0)
yellow = (623, 0, 0)


city_population = {"New York": 8419000,"Los Angeles" : 3980000, "Chicago": 2716000,
                   "Houston": 2328000, "Phoenix" : 1690000}

def add_city(city_dict, city_name, population):
    """Add a new city and its population to the dictionary."""
    city_dict[city_name] = population
    print(f"Added city: {city_name} with population: {population}")

def remove_city(city_dict, city_name):
    """Remove a city from the dictionary."""
    if city_name in city_dict:
        del city_dict[city_name]
        print(f"Removed city: {city_name}")
    else:
        print(f"City {city_name} not found.")

def update_population(city_dict, city_name, new_population):
    """Update the population of a specific city."""
    if city_name in city_dict:
        city_dict[city_name] = new_population
        print(f"Updated city: {city_name} to new population: {new_population}")
    else:
        print(f"City {city_name} not found.")

def filter_cities_by_population(city_dict, min_population):
    """Create a new dictionary with cities having a population greater than min_population."""
    return {city: pop for city, pop in city_dict.items() if pop > min_population}

# Example usage
if __name__ == "__main__":
    # Add a new city
    add_city(city_population, 'San Diego', 1420000)
    
    # Remove a city
    remove_city(city_population, 'Phoenix')
    
    # Update the population of a specific city
    update_population(city_population, 'Chicago', 2750000)
    
    # Filter cities with population greater than 1 million
    large_cities = filter_cities_by_population(city_population, 1000000)
    print("Cities with population greater than 1 million:")
    for city, pop in large_cities.items():
        print(f"{city}: {pop}")

set1 = {random.randint(1, 20) for _ in range(10)}
set2 = {random.randint(1, 20) for _ in range(10)}

# Display the sets
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Check if one set is a subset of the other
is_subset1 = set1.issubset(set2)
is_subset2 = set2.issubset(set1)
print(f"Set 1 is a subset of Set 2: {is_subset1}")
print(f"Set 2 is a subset of Set 1: {is_subset2}")

# Find the union of the two sets
union_set = set1.union(set2)
print(f"Union of Set 1 and Set 2: {union_set}")

# Calculate the intersection of the sets
intersection_set = set1.intersection(set2)
print(f"Intersection of Set 1 and Set 2: {intersection_set}")

# Determine the difference between the sets
difference_set1 = set1.difference(set2)
difference_set2 = set2.difference(set1)
print(f"Difference between Set 1 and Set 2: {difference_set1}")
print(f"Difference between Set 2 and Set 1: {difference_set2}")





