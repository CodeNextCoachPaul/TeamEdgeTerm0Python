# Coach Steph wrote it, not Paul

	# You've just learned about variables, conditionals, functions, and user input. 
	# You've also created a basic calculator in a previous project.
	
	# Now imagine you are going out to eat.
	# Are you at a restaurant for a meal? Are you grabbing boba? Or are you just going to an ice cream parlor?
	# At the end of the meal, you get the bill. 

	# How do you think restaurants automate that math?

					# Let's try it!

# -------------------------------------------- 

# Scenario Parameters: 

	# When you eat out, you have the option to order one or multiple items.
	# What kind of items are available to order? There's usually a menu.
	# Allow your user to order a drink, meal, and dessert.

	# At the end of the order, the receipt comes and you have to calculate the total cost:
	# Don't forget the tax and tip!

# After this program finishes running, it should output a receipt with:
  #1. the items you ordered and their cost 
	#2. a total for your order before tax
	#3. a total for your order after tax
	#4. the amount of your tip 
	#5. the total including tax and tip

# -------------------------------------------- 

drink_order = ''
drink_order_cost = 0
meal_order = ''
meal_order_cost = 0
dessert_order = ''
dessert_order_cost = 0
total = 0
TAX = .08875
tip = 0


# -------------------------------------------- 

# Part 1:
# Let's start by displaying the menu. Include the food item name and it's cost. 

# Write a function that will display the menu:
# - Print each item available and it's cost. You should have at least 3 items available (a drink, meal, and dessert item). 

# --------------------------------------------
def displayMenu():
  print('MENU \n')
  print('Drinks')
  print('------')
  print('1. Coke       $2.00 \n2. Sprite     $2.00')
  print('\nMeals')
  print('-----')
  print('3. Hot Dog    $3.00 \n4. Hamburger  $6.00\n5. Taco       $4.00')
  print('\nDesserts')
  print('--------')
  print('6. Apple Pie  $3.50 \n7. Flan       $4.00')





# -------------------------------------------- 

# Part 2:
# Let's take the order. What did the user order? What does it cost?

# Write a function that will take the order:
# - Prompt the user to enter a drink, dessert, and meal (Bonus: give them the option to not order an item)
# - Return the cost 

# Remember! Functions are meant to be reusable, so write a function that will work when called repeatedly!

# --------------------------------------------
def takeOrder():
  global drink_order
  global drink_order_cost
  global meal_order 
  global meal_order_cost
  global dessert_order 
  global dessert_order_cost 
  global total
  
  print('\n\nHi! Welcome to Stephanie\'s Snack Shack')
  order_input = input('What would you like to drink? (Enter 1 or 2):\n')
  if order_input == '1':
    drink_order = 'Coke'
    drink_order_cost = '2.00'
    total += 2 
  elif order_input == '2':
    drink_order = 'Sprite'
    drink_order_cost = '2.00'
    total += 2
  else:
    drink_order_cost = ''

  order_input = input('What would you like to eat? (Enter 3, 4, or 5):\n')
  if order_input == '3':
    meal_order = 'Hot Dog'
    meal_order_cost = '3.00'
    total += 3 
  elif order_input == '4':
    meal_order = 'Hamburger'
    meal_order_cost = '6.00'
    total += 6
  elif order_input == '5':
    meal_order = 'Taco'
    meal_order_cost = '4.00'
    total += 4
  else:
    meal_order_cost = ''


  order_input = input('What would you like for dessert? (Enter 6 or 7):\n')
  if order_input == '6':
    dessert_order = 'Apple Pie'
    dessert_order_cost = '3.50'
    total += 3.5 
  elif order_input == '7':
    dessert_order = 'Flan'
    dessert_order_cost = '4.00'
    total += 4
  else:
    dessert_order_cost = ''




# -------------------------------------------- 

# Part 3:
# Now that you have the costs of everything ordered, let's calculate the cost of the order(including tip and tax).

# Write a function that will calculate the cost of each person's order, including:
# - Cost of all of their ordered items
# - Tax (Look up the sales tax of your city)
# - Tip (Give the user the option to enter how much they want to tip)

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!

# -------------------------------------------- 
def calculateTotal():
  global tip 
  print(f'Your order total with tax is {"{:.2f}".format(total + total*TAX)}.')
  order_input = input('Would you like to leave a tip? (10% 15% 20% 22%): ')
  if order_input == '10%' or order_input == '10':
    tip = 0.1
  elif order_input == '15%' or order_input == '15':
    tip = .15
  elif order_input == '20%' or order_input == '20':
    tip = .2
  elif order_input == '22%' or order_input == '22':
    tip = .22
  else:
    tip = 0
  











# -------------------------------------------- 

# Part 4:
# Let's print out a receipt for each person.

# Write a function that will take the values of each person's order and total cost and print it out in an appealing way.

# The receipt should include:
# - Cost of each item
# - Total cost for the order

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!

# -------------------------------------------- 

def printReceipt():
  print('\n\nThanks! This is your receipt: \n')
  print(f'{drink_order}    {drink_order_cost}')
  print(f'{meal_order}    {meal_order_cost}')
  print(f'{dessert_order}    {dessert_order_cost}\n')
  print(f'Subtotal: {"{:.2f}".format(total)}')
  print(f'Tax: {"{:.2f}".format(total*TAX)}')
  print(f'Tip: {"{:.2f}".format(total*tip)}\n')
  print(f'Total: ${"{:.2f}".format(total+total*TAX+total*tip)}')

  print('\nCome again soon!')




# -------------------------------------------- 

# Part 6: Food Order Bot

# Call all of your functions to test your food order bot!

# --------------------------------------------
displayMenu()
takeOrder()
calculateTotal()
printReceipt()



# -------------------------------------------- 

# Part 7: Upchallenges!

# How many of these upchallenges can you implement?

# - Make sure the user is only entering valid values. If they enter an invalid value, prompt them to re-enter. 
# - The displayed prices should only have two decimal places.
# - Implement a rewards system (stamp cards, buy one get one, etc)

# --------------------------------------------
