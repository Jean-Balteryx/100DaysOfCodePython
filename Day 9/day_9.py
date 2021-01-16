###89. The Python Dictionary: Deep Dive###

#Creating a filled dictionary
#-> dictionary = {
      #key: value,
      #key: value
    #}
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again."
}

#Retrieving item from dictionary -> dictionary_name[key]
print(programming_dictionary["Bug"])

#KeyError
#print(programming_dictionary["Bog"])

#Adding new items to dictionary -> dictionary_name[key] = value
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

#Creating an empty dictionary -> dictionary_name = {}
empty_dictionary = {}

#Wiping an existing dictionary -> existing_dictionary = {}
programming_dictionary = {}

print(programming_dictionary)

#Editing an item of a dictionary -> dictionary_name[existing_key] = value
programming_dictionary["Bug"] = "A moth in your computer"

print(programming_dictionary)

#Looping through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])


###91. Nesting Lists and Dictionaries###

capitals = {
  "France": "Paris",
  "Germany": "Berlin"
}

#Nesting a List in a Dictionary
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

#Nesting a Dictionary in a Dictionary
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

#Nesting a Dictionary in a List
travel_log = [
  {
    "country_visited": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
  },
  {
    "country_visited": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
  }
]