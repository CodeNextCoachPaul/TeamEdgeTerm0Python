import random

# -------------------------------------------- 

	# You've just learned about variables, conditionals.
	# Just from knowing those two topics, you can do so much!
	
	# Let's try to make a simple program that responds to the user.
	# We're going to recreate the Magic 8 Ball!!!
			
			# Never heard of it? That's ok!

					# You got this!

  # -------------------------------------------- 

	# How a Magic 8 Ball Works:

	# The user asks a question and vigoriously shakes the ball. 
	# Then the ball will respond with one of twenty responses, chosen at random. 

	# That's pretty simple right?

 # -------------------------------------------- 

	# Part 1: 
	# Print instructions on the screen and 
	# prompt the user to ask a question

  # --------------------------------------------

print("How a Magic 8 Ball Works:\n\nThe user asks a question and vigoriously shakes the ball.\nThen the ball will respond with one of twenty responses, chosen at random. \n\nThat's pretty simple right?")	
question = input("Ask a question")

# -------------------------------------------- 

	# Part 2: Next, we need to randomly select a response from 20 options.

	# Randomly select a number from 0 - 19 
	# Use that to select from the following responses:
		# 0 - It is certain.
		# 1 - It is decidedly so.
		# 2 - Without a doubt.
		# 3 - Yes - definitely.
		# 4 - You may rely on it.
		# 5 - As I see it, yes.
		# 6 - Most likely.
		# 7 - Outlook good.
		# 8 - Yes.
		# 9 - Signs point to yes.
		# 10 - Reply hazy, try again.
		# 11 - Ask again later.
		# 12 - Better not tell you now.
		# 13 - Cannot predict now.
		# 14 - Concentrate and ask again.
		# 15 - Don't count on it.
		# 16 - My reply is no.
		# 17 - My sources say no.
		# 18 - Outlook not so good.
		# 19 - Very doubtful.

	# Look up random.rand_int to see how you can use it to select a random number.

  # -------------------------------------------- 

response = (random.randint(0, 19))
if response = 0:
	print(" It is certain.")
if response = 1:
	print("It is decidedly so.")
if response = 2:
	print("Without a doubt.")
if response = 3:
	print("Yes - definitely.")
if response = 4:
	print("You may rely on it.")
if response = 5:
	print("As I see it, yes.")
if response = 6:
	print("Most likely")
if response = 7:
	print("Outlook good")
if response = 8:
	print("Yes.")
if response = 9:
	print("Signs point to yes")
if response = 10:
	print("Reply hazy, try again")
if response = 11:
	print("Ask again later")
if response = 12:
	print("Better not tell you now.")
if response = 13:
	print("Cannot predict now")
if response = 14:
	print("Concentrate and ask again")
if response = 15:
	print("Don't count on it")
if response = 16:
	print("My reply is no")
if response = 17:
	print("My sources say no")
if response = 18:
	print("Outlook not so good")
if response = 19:
	print("Very doubtful")

# -------------------------------------------- 

	# Part 3: Customize it!

	# Select your own theme and use case and modify your code!
	
# -------------------------------------------- 
