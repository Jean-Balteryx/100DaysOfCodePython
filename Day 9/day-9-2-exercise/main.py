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
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

#Defining a function adding a new country to the travel log
def add_new_country(country, visits, cities):
  #Creating a Dictionary for the country using arguments
  country = {
    "country": country,
    "visits": visits,
    "cities": cities
  }

  #Adding the country to the travel log
  travel_log.append(country)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



