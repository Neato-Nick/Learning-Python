#defines the function titled cheese_and_crackers to contain cheese_count,
	#boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# %d is a variable reference to cheese_count or boxes_of_crackers
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	# /n breaks the lines
	print "Get a blanket. \n"

# straight up tells the function to run 20 and 30
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#uses the %d references for 10 and 50
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# instructions for amount_of_cheese, amonut_of_crackers to replace
	# cheese_count and boxes_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# feeds the function those two math operations directly
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# uses the %d references AND adds shit
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)