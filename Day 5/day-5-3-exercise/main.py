#Write your code below this row 👇

#Initializes the variable for the total
total_even_numbers = 0

#Goes through all even numbers
for even_number in range(2, 101, 2):
  #Adds the current even number to the total
  total_even_numbers += even_number

#Prints the total of even numbers from 1 to 100
print(total_even_numbers)