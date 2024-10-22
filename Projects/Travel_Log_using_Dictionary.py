# Travel Log using Dictionaries

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

def add_new_country(name, visit_count, cities_visited):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = visit_count
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country(name="Russia", cities_visited=["Moscow", "Saint Petersburg"], visit_count=2)

print(travel_log)
