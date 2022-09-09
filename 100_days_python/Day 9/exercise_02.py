travel_log = [
{
"country": "France", 
"total_visits: 2"
"cities_visited":["Paris","Lille","Dijon"],
    
    },
{
"country": "Germany", 
"total_visits : 3"
"cities_visited": ["Berlin","Hamburg","stuttgart"],
    
    },
]
    
#TODO: write the function that will allow new country to be added to the travel_log 
def add_new_country( country_visited, time_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["total_visitis"]= time_visited
    new_country["cities_visited"]= cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow","Saint Petersbu"])
print(travel_log)