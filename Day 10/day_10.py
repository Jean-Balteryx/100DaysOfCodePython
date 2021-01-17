###97. Functions with Outputs###

#Defining a function that returns a result using the return keyword -> the return keyword ends a function
def format_name(f_name, l_name):
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()

  #Returning a formatted string
  return f"{formatted_f_name} {formatted_l_name}"

#Prints the result returned by the function format_name
print(format_name("JeAn-baptIstE", "piNEt"))


###98. Multiple return values###

def format_name(f_name, l_name):
  """Take a first and last name and format it
  to return the title case version of the name"""
  #Using an early return if inputs aren't valid
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."

  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()

  #Returning a formatted string when inputs are valid
  return f"{formatted_f_name} {formatted_l_name}"

#Prints the result returned by the function format_name
print(format_name(input("What is your first name? "), input("What is your last name? ")))