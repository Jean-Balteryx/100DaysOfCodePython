############DEBUGGING#####################

###121. Describe the Problem###
def my_function():
  #for i in range(1,20): -> it will never go to 20
  for i in range(1, 21):
    if i == 20:
      print("You got it")

my_function()

###122. Reproduce the Bug###
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(1, 6) -> lists are 0-index based so the value 6 will return an error as the maximum index in dice_imgs is 5. Also the first value will never be printed.
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

####123. Play Computer and Evaluate Each Line###
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
#elif year > 1994: -> if the user input 1994 it will print nothing as it's not handled
elif year >= 1994:
  print("You are a Gen Z.")

###124. Fixing Errors and Watching for Red Underlines###
#age = input("How old are you?") -> the input not being cast as int, it produces an error when comparing it with 18 in the if statement
age = int(input("How old are you?"))
if age > 18:
  print("You can drive at age {age}.")

###125. Squash bugs with a print() Statement###
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
#word_per_page == int(input("Number of words per page: ")) -> == tests the equality of both terms, it doesn't assign the user input to the variable
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

###126. Bringing out the BIG Gun: Using a Debugger###
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  #b_list.append(new_item) -> as it's outside the loop, the value is added after the loop has finished so it adds only one value
  print(b_list)

mutate([1,2,3,5,8,13])