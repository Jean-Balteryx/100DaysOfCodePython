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
#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

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

#🚨 Do NOT change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)















# Tests
import unittest
from unittest.mock import patch
from io import StringIO

class MyTest(unittest.TestCase):
    def test_1(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out:
          print(travel_log)
          expected_print = "[{'country': 'France', 'visits': 12, 'cities': ['Paris', 'Lille', 'Dijon']}, {'country': 'Germany', 'visits': 5, 'cities': ['Berlin', 'Hamburg', 'Stuttgart']}, {'country': 'Russia', 'visits': 2, 'cities': ['Moscow', 'Saint Petersburg']}]\n"
          self.assertEqual(fake_out.getvalue(), expected_print) 



print("\n")
print('Running some tests on your code:')
print(".\n.\n.\n.")
unittest.main(verbosity=1, exit=False)