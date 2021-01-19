###114. Namespaces: Local vs. Global Scope###

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

##Local Scope

def drink_potion():
  potion_strength = 2
  print(potion_strength)

drink_potion()

#NameError -> the variable has been defined within the function drink_potion() so it can only be used inside the function
#print(potion_strength)

##Global Scope
player_health = 10

def drink_potion():
  potion_strength = 2

  #The variable has been defined at the global level so it can be used inside a function
  print(player_health)

drink_potion()

#The variable has been defined at the global level so it can be used anywhere
print(player_health)

###115. Does Python Have Block Scope?###

##There is no Block Scope

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

#Conditional and loop structures doesn't create a separated local scope
if game_level < 5:
  new_enemy = enemies[0]

#The variable has been created within an if statement and is still accessible from outside the structure
print(new_enemy)


###116. How to modify a Global Variable?###

enemies = 1

def increase_enemies():
  #Specify that the enemies variable used in this function is the global enemies variable
  #Not the best option
  global enemies
  enemies += 1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

##########

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  #Better option is to return the variable + 1
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")


###117. Python Constants and Global Scope###

#Convention is to write the name of constants in upper case and to create them in the global scope
PI = 3.14159